from .. import db, permission
from ..base import staff_bp
from ..utils.common import fake

from ..models import Staff, Member, Deal, RechargeRecord, ConsumeRecord, ExpirationTime, UsageCount
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime, timedelta


@staff_bp.route('/query/record/<int:id>', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(1)
def query_record(id):
    """
    'data': {'total_count': int, counts: [], 'total_time': time, times: []}
    e.g. 每项举一个例子:
    total_count: 10
    count[0] : {'time': xxx, 'deadline': xxx, 'count': 10(活动次数), 'amount': 1.1}
    total_time: 10(剩余天数)
    time[0]: {'time': xxx, 'deadline': xxx, 'count': 10(lifespan的意思), 'amount': 1.1}  
    """
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200
    # 查询member_id的RechargeRecord、ConsumeRecord、UsageCount、ExpirationTime
    member_id = id
    usage_counts = db.session.query(UsageCount).filter_by(member_id=member_id).all()
    expiration_times = db.session.query(ExpirationTime).filter_by(member_id=member_id).first() # 一个人只有一个ExpirationTime
    # total_count为有效期至少持续到现在的UsageCount的总和
    total_count = 0                                        # ----- 输出数据1 -----
    for usage_count in usage_counts:
        if usage_count.deadline >= datetime.now():
            total_count += usage_count.count
    # total_time为剩余天数
    total_time = expiration_times.deadline-datetime.now()  # ----- 输出数据3 -----
    
    # 获取某member_id的RechargeRecord，并将其与Deal表连接 (连接条件为activity_id与plan_id都相同)
    r_d = db.session.query(RechargeRecord, Deal).filter(RechargeRecord.member_id == member_id, 
                                                        RechargeRecord.activity_id == Deal.activity_id, 
                                                        RechargeRecord.plan_id == Deal.plan_id).all()
    # 根据r_d得到
    recharge_count = [] # recharge_type=='count'的充值记录
    recharge_time = [] # recharge_type=='time'的充值记录
    for r, d in r_d:
        if d.recharge_type == 'time':
            recharge_time.append((r, d))
        elif d.recharge_type == 'count':
            recharge_count.append((r, d))
    # 按照recharge_count的deadline排序 # 降序
    recharge_count = sorted(recharge_count, key=lambda x: x[1].lifespan, reverse=True)        
    # 按照recharge_time的deadline排序 # 降序
    recharge_time = sorted(recharge_time, key=lambda x: x[1].lifespan, reverse=True) 
    

    counts = []                                            # ----- 输出数据2 -----
    times = []                                             # ----- 输出数据4 -----
    # 从recharge_count中获取count
    for r, d in recharge_count:
        counts.append({
            'time': r.recharge_time.strftime('%Y-%m-%d %H:%M:%S'),
            'deadline': r.recharge_time + timedelta(days=d.lifespan),
            'count': d.recharge_count,
            'amount': d.amount
        })
    # 从recharge_time中获取count
    for r, d in recharge_time:
        times.append({
            'time': r.recharge_time.strftime('%Y-%m-%d %H:%M:%S'),
            'deadline': r.recharge_time + timedelta(days=d.lifespan),
            'count': d.recharge_count,
            'amount': d.amount
        })
    
    # 返回数据
    data = {
        'total_count': total_count,
        'counts': counts,
        'total_time': total_time,
        'times': times
    }
    return jsonify({'code':200, 'msg': '成功', 'data': data}), 200
    
    