from .. import db, permission
from ..base import staff_bp

from ..models import ConsumeRecord, RechargeRecord, Deal, Member
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, \
    current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text

import hashlib
import uuid
from datetime import datetime

# [开发中] 查看客流量 消费人次


# /staff/statements/new_consume
@staff_bp.route('/statements/new_consume', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(2)
def staff_statements_new_consume_get():
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200

    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    """
    从consume_record中找到consume_time在start_time和end_time之间的记录
    每天统计一次
    返回一个有序字典，包含consume_time和consume_count
    """
    consume_records = db.session.query(ConsumeRecord).filter(
        ConsumeRecord.consume_time >= start_time, ConsumeRecord.consume_time <= end_time).all()
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
    """
    consume_list
    [
        {'time': '2021-01-01', 'value': 10},
        {'time': '2021-01-02', 'value': 20},
    ]
    """
    consume_list = []
    for key, value in consume_dict.items():
        consume_list.append({'time': key, 'value': value})
    consume_list = sorted(consume_list, key=lambda x: x['time'])
    total = sum([item['value'] for item in consume_list])

    return_data = {'code': 200, 'msg': '成功', 'data': {
        'total': total, 'items': consume_list}}
    return jsonify(return_data)

# [开发中] 查看充值金额


# /staff/statements/new_recharge
@staff_bp.route('/statements/new_recharge', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(2)
def staff_statements_new_recharge_get():
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200

    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')

    recharge_records = db.session.query(RechargeRecord).filter(
        RechargeRecord.recharge_time >= start_time, RechargeRecord.recharge_time <= end_time).all()
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
        deal = db.session.query(Deal).filter(
            Deal.activity_id == record.activity_id, Deal.plan_id == record.plan_id).first()
        recharge_dict[date] += deal.amount

    recharge_list = []
    for key, value in recharge_dict.items():
        recharge_list.append({'time': key, 'value': float(value)})
    recharge_list = sorted(recharge_list, key=lambda x: x['time'])
    total = sum([item['value'] for item in recharge_list])

    return_data = {'code': 200, 'msg': '成功', 'data': {
        'total': total, 'items': recharge_list}}
    return jsonify(return_data)

# [开发中] 查看新增会员


# /staff/statements/member
@staff_bp.route('/statements/new_member', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(2)
def staff_statements_new_member_get():
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200

    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    """
    从member中找到regist_time在start_time和end_time之间的记录
    每天统计一次
    返回一个有序字典，包含regist_time和create_count
    """
    members = db.session.query(Member).filter(
        Member.regist_time >= start_time, Member.regist_time <= end_time).all()
    members = sorted(members, key=lambda x: x.regist_time)
    member_dict = {}
    # 添加键值对 键为日期，值为当天新增会员数（默认为0）
    for member in members:
        date = member.regist_time.strftime('%Y-%m-%d')
        if date not in member_dict:
            member_dict[date] = 0
    # 统计每天的新增会员数
    for member in members:
        date = member.regist_time.strftime('%Y-%m-%d')
        member_dict[date] += 1

    member_list = []
    for key, value in member_dict.items():
        member_list.append({'time': key, 'value': value})
    member_list = sorted(member_list, key=lambda x: x['time'])
    total = sum([item['value'] for item in member_list])

    return_data = {'code': 200, 'msg': '成功', 'data': {
        'total': total, 'items': member_list}}
    return jsonify(return_data)
