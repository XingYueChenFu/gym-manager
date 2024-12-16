from .. import db, permission
from ..base import staff_bp

from ..models import Staff, Member, Deal
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, \
    current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime
   
# [开发中] 添加活动
@staff_bp.route('/add/deal', methods=['POST']) # /staff/add/deal
# @login_required
# @permission(2)
def staff_add_deal():
    """
    传入json:
    'data': [
        {'activity_name': xxx,
         'start_time': xxx,
         'end_time': xxx,
         'recharge_type': xxx,
         'recharge_count': xxx,
         'lifespan': xxx,
         'recharge_day': xxx,
         'amount': xxx,
         'activity_remark': xxx
         },
        ]
    """
    if request.method == 'OPTIONS':  
        return jsonify({'msg': 'CORS preflight response'}), 200
    # 接收一个列表，包含同一activity_id的多个plan_id
    data = request.json.get('data')
    # 从Deal中找到最大的activity_id
    max_activity_id = db.session.query(db.func.max(Deal.activity_id)).scalar()
    if max_activity_id is None:
        max_activity_id = 0
    this_activity_id = max_activity_id + 1
    this_plan_id = 0
    
    for item in data:
        deal = Deal()
        deal.activity_id = this_activity_id
        deal.plan_id = this_plan_id
        this_plan_id += 1
        
        deal.activity_name = item.get('activity_name')
        deal.start_time = item.get('start_time')
        deal.end_time = item.get('end_time')
        
        deal.recharge_type = item.get('recharge_type')
        deal.recharge_count = item.get('recharge_count')
        deal.lifespan = item.get('lifespan')
        deal.recharge_day = item.get('recharge_day')
        
        deal.amount = item.get('amount')
        deal.activity_remark = item.get('activity_remark')
        
        db.session.add(deal)
    try:
        db.session.commit()
        return jsonify({'msg': '成功', 'code': 200}) # 前端：添加成功
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': '数据添加失败', 'code': 5001})

# [开发中] 删除活动 <id>
@staff_bp.route('/delete/deal/<int:id>', methods=['POST']) # /staff/delete/deal/<id>
# @login_required
# @permission(2)
def staff_delete_deal_by_id(id):
    if request.method == 'OPTIONS':  
        return jsonify({'msg': 'CORS preflight response'}), 200
    deals = Deal.query.filter_by(activity_id=id).all()
    if deals is None:
        return jsonify({'msg': '数据不存在', 'code': 5005})
    for deal in deals:
        db.session.delete(deal)
    try:
        db.session.commit()
        return jsonify({'msg': '成功', 'code': 200}) # 前端：删除成功
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': '数据删除失败', 'code': 5002})
    
# [开发中] 删除活动
@staff_bp.route('/delete/deal', methods=['POST']) # /staff/delete/deal
# @login_required
# @permission(2)
def staff_delete_deal():
    if request.method == 'OPTIONS':  
        return jsonify({'msg': 'CORS preflight response'}), 200
    data = request.json.get('data')
    for item in data:
        deal = Deal.query.filter_by(activity_id=item.get('activity_id'), plan_id=item.get('plan_id')).first()
        db.session.delete(deal)

# [开发中] 修改活动
@staff_bp.route('/modify/deal', methods=['POST']) # /staff/modify/deal
# @login_required
# @permission(2)
def staff_modify_deal():
    if request.method == 'OPTIONS':  
        return jsonify({'msg': 'CORS preflight response'}), 200
    data = request.json.get('data')
    for item in data:
        deal = Deal.query.filter_by(activity_id=item.get('activity_id'), plan_id=item.get('plan_id')).first()
        deal.activity_id = item.get('activity_id')
        deal.plan_id = item.get('plan_id')
        deal.activity_name = item.get('activity_name')
        deal.start_time = item.get('start_time')
        deal.end_time = item.get('end_time')
        
        deal.recharge_type = request.json.get('recharge_type')
        deal.recharge_count = request.json.get('recharge_count')
        deal.lifespan = request.json.get('lifespan')
        deal.recharge_day = request.json.get('recharge_day')
        
        deal.amount = request.json.get('amount')
        deal.activity_remark = request.json.get('activity_remark')
    try:
        db.session.commit()
        return jsonify({'msg': '成功', 'code': 200}) # 前端：修改成功
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': '数据修改失败', 'code': 5003})

# [开发中] 查询活动详情 <id>
@staff_bp.route('/query/deal/<int:id>', methods=['POST']) # /staff/query/deal/<id>
# # @login_required
def staff_get_deal_by_id(id):
    if request.method == 'OPTIONS':  
        return jsonify({'msg': 'CORS preflight response'}), 200
    # 同一activity_id的多个plan_id
    deals = Deal.query.filter_by(activity_id=id).all()
    if deals is None:
        return jsonify({'msg': '数据不存在', 'code': 5005})
    data = []
    for deal in deals:
        data.append(deal.to_json())
    return jsonify({'msg': '成功', 'code': 200, 'data': data})

# [开发中] 查询活动详情
@staff_bp.route('/query/deal', methods=['POST']) # /staff/query/deal
# # @login_required
def staff_get_deal():
    if request.method == 'OPTIONS':  
        return jsonify({'msg': 'CORS preflight response'}), 200
    data = request.json.get('data')
    output_data = []
    for item in data:
        deal = Deal.query.filter_by(activity_id=item.get('activity_id'), plan_id=item.get('plan_id')).first()
        output_data.append(deal.to_json())
    return jsonify({'msg': '成功', 'code': 200, 'data': output_data})

# [开发中] 查询现在有的活动 start_time~end_time
@staff_bp.route('/query/deal/now', methods=['POST']) # /staff/query/deal/now
# # @login_required
def staff_get_deal_now():
    if request.method == 'OPTIONS':  
        return jsonify({'msg': 'CORS preflight response'}), 200
    now = datetime.now()
    deals = Deal.query.filter(Deal.start_time <= now, Deal.end_time >= now).all()
    if deals is None:
        return jsonify({'msg': '数据不存在', 'code': 5005, 'data': None})
    data = []
    for deal in deals:
        data.append(deal.to_json())
    return jsonify({'msg': '成功', 'code': 200, 'data': data})
    """
    输出的data:
    [
        {
            'activity_id': int,
            'plan_id': int,
            'activity_name': str,
            'start_time': str,
            'end_time': str,
            'recharge_type': str,
            'recharge_count': int,
            'lifespan': int,
            'recharge_day': int,
            'amount': str,
            'activity_remark': str
        },
    ]
    """

