from .. import db, permission
from ..base import staff_bp

from ..models import Staff, Member, Deal, ExpirationTime
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, \
    current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime

@staff_bp.route('/query/expiration_time/<int:id>', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(1)
def staff_get_expiration_time_by_id(id):
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200
    expiration_time = ExpirationTime.query.filter_by(member_id=id).first()
    if expiration_time is not None:
        data = {'deadline': expiration_time.deadline.strftime('%Y-%m-%d %H:%M:%S')}
        return jsonify({'msg': '成功', 'code': 200, 'data': data})
    else:
        return jsonify({'msg': '用户信息为空', 'code': 2008})
        
    return jsonify({'msg': '失败', 'code': 2004})