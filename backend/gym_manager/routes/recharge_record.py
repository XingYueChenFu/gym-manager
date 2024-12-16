from .. import db, permission
from ..base import staff_bp
from ..utils.common import fake

from ..models import Staff, Member, Deal, UsageCount, RechargeRecord, ExpirationTime
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime, timedelta

def recharge(member_id, activity_id, plan_id, recharge_time=datetime.now(), recharge_remark=None):
    # member_id: 会员id activity_id: 活动id plan_id: 计划id
    # 在recharge_record 与 usage_count或expiration_time 中添加记录
    recharge_time = datetime.now() if recharge_time is None else recharge_time
    
    # 1. 判断member或deal是否存在
    member = db.session.query(Member).filter_by(member_id=member_id).first()
    deal = db.session.query(Deal).filter_by(activity_id=activity_id, plan_id=plan_id).first()
    if member is None:
        print(f'\033[1;31m[ERROR]\033[0m member_id {member_id} not exist.')
        return False
    if deal is None:
        print(f'\033[1;31m[ERROR]\033[0m deal {activity_id} {plan_id} not exist.')
        return False
    
    # 2.记录充值记录
    # recharge_remark = fake.text(max_nb_chars=100) # 最长100个中文字符
    recharge_record = RechargeRecord(member_id=member_id, activity_id=activity_id, plan_id=plan_id, recharge_time=recharge_time, recharge_remark=recharge_remark)
    db.session.add(recharge_record)
    
    # 3.增加使用次数(次数卡)或者延长有效期(天数卡)
    if deal.recharge_type == 'time': # 天数卡
        et = db.session.query(ExpirationTime).filter_by(member_id=member_id).first()
        # 如果有了，且有效期大于充值时间，则延长有效期
        if et is not None and et.deadline > recharge_time:
            et.deadline += timedelta(days=deal.recharge_day)
        # 否则，将有效期设为充值时间+充值天数
        else:
            et = ExpirationTime(member_id=member_id, deadline=recharge_time+timedelta(days=deal.recharge_day))
        db.session.add(et)
    else: # 次数卡
        deadline = recharge_time + timedelta(days=deal.lifespan)
        # 参看usage_count是否有记录member_id, deadline
        uc = db.session.query(UsageCount).filter_by(member_id=member_id, deadline=deadline).first()
        # 如果有了，增加次数
        if uc is not None:
            uc.count += deal.recharge_count
        # 否则，增加记录
        else:
            uc = UsageCount(member_id=member_id, deadline=deadline, count=deal.recharge_count)
        db.session.add(uc)
    
    try:
        db.session.commit()
        print(f'\033[1;32m[SUCCESS]\033[0m recharge {member_id} {activity_id} {plan_id} success.')
        return True
    except Exception as e:
        db.session.rollback()
        print(f'\033[1;31m[ERROR]\033[0m recharge {member_id} {activity_id} {plan_id} failed.')
        return False

# [开发中] 充值 未实现
@staff_bp.route('/recharge', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(1)
def staff_recharge():
    """
    传入：json
    {
        member_id: int,
        activity_id: int,
        plan_id: int,
        recharge_time: datetime,
        recharge_remark: str (可省略)
    }
    """
    
    if request.method == 'OPTIONS':  
        return jsonify({'msg': 'CORS preflight response'}), 200
    
    member_id = request.json.get('member_id')
    activity_id = request.json.get('activity_id')
    plan_id = request.json.get('plan_id')
    recharge_time = request.json.get('recharge_time')
    recharge_remark = request.json.get('recharge_remark')
    
    result = recharge(member_id, activity_id, plan_id, recharge_time, recharge_remark)
    if result:
        return jsonify({'msg': '成功', 'code': 200}), 200
    else:
        return jsonify({'msg': '数据添加失败', 'code': 5001})