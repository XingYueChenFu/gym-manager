from .. import db, permission
from ..base import staff_bp

from ..models import Staff, Member, Deal, UsageCount
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, \
    current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime


@staff_bp.route('/query/usage_count/<int:id>', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(1)
def staff_get_usage_count_by_id(id):
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200
    usage_count = UsageCount.query.filter_by(member_id=id).all()
    if usage_count is not None:
        #  排序，按照 deadline  升序
        now = datetime.now()
        usage_count = sorted(usage_count, key=lambda x: x.deadline)
        for count in usage_count:
            if count.deadline < now:
                # 如果过期，删除
                db.session.delete(count)
        db.session.commit()
        usage_count = UsageCount.query.filter_by(member_id=id).all()
        # data 为 ddl: count 的键值对
        data = {}
        for count in usage_count:
            data[count.deadline.strftime('%Y-%m-%d %H:%M:%S')] = count.count
        return jsonify({'msg': '成功', 'code': 200, 'data': data})
    else:
        data = {datetime.now().strftime('%Y-%m-%d %H:%M:%S'): 0} # '当前时间' : 0
        return jsonify({'msg': '用户信息为空', 'code': 2008, 'data': data})
        
    return jsonify({'msg': '失败', 'code': 2004})