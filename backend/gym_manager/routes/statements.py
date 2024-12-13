from .. import db, permission
from ..base import staff_bp

from ..models import ConsumeRecord, RechargeRecord, Deal
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, \
    current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime

# [开发中] 查看客流量
@staff_bp.route('/statements/consume', methods=['POST', 'OPTIONS']) # /staff/statements/consume
@login_required
@permission(2)
def staff_statements_consume_get():
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    """
    从consume_record中找到consume_time在start_time和end_time之间的记录
    每天统计一次
    返回一个有序字典，包含consume_time和consume_count
    """
    consume_records = db.session.query(ConsumeRecord).filter(ConsumeRecord.consume_time >= start_time, ConsumeRecord.consume_time <= end_time).all()
    consume_records = sorted(consume_records, key=lambda x: x.consume_time)
    consume_dict = {}
    # 添加键值对 键为日期，值为当天消费次数（默认为0）
    for record in consume_records:
        date = record.consume_time.strftime('%Y-%m-%d')
        if date not in consume_dict:
            consume_dict[date] = 0
    # 统计每天的消费次数
    for record in consume_records:
        date = record.consume_time.strftime('%Y-%m-%d')
        consume_dict[date] += 1
    return_data = {'code': 200, 'msg': '成功','data': consume_dict}
    return jsonify(return_data)
    
# [开发中] 查看充值记录
@staff_bp.route('/statements/recharge', methods=['POST', 'OPTIONS']) # /staff/statements/recharge
@login_required
@permission(2)
def staff_statements_recharge_get():
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    
    recharge_records = db.session.query(RechargeRecord).filter(RechargeRecord.recharge_time >= start_time, RechargeRecord.recharge_time <= end_time).all()
    recharge_records = sorted(recharge_records, key=lambda x: x.recharge_time)
    recharge_dict = {}
    # 添加键值对 键为日期，值为当天充值金额（默认为0）
    for record in recharge_records:
        date = record.recharge_time.strftime('%Y-%m-%d')
        if date not in recharge_dict:
            recharge_dict[date] = 0
    # 统计每天的充值金额
    for record in recharge_records:
        date = record.recharge_time.strftime('%Y-%m-%d')
        # recharge_dict[date] += record.amount
        # 根据activity_id与plan_id找到对应的deal，再找到对应的amount
        deal = db.session.query(Deal).filter(Deal.activity_id == record.activity_id, Deal.plan_id == record.plan_id).first()
        recharge_dict[date] += deal.amount
    return_data = {'code': 200, 'msg': '成功','data': recharge_dict}
    return jsonify(return_data)