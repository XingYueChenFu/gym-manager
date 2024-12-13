from .. import db, permission
from ..base import base, staff_bp

from ..models import Staff, Member
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, \
    current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text

import hashlib
import uuid
from datetime import datetime

# [测试中] 手动注册会员


@staff_bp.route('/add/member', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(1)
def staff_regist_member():
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200
    md = hashlib.md5()
    md.update(request.json.get('phone_number').encode('utf-8'))
    member = Member()
    member.phone_number = request.json.get('phone_number')
    member.nickname = request.json.get('nickname')
    member.realname = request.json.get('realname')
    member.id_card = request.json.get('id_card')
    member.student_card = request.json.get('student_card')
    member.gender = request.json.get('gender')
    member.password = md.hexdigest()

    if db.session.query(Member).filter_by(phone_number=member.phone_number).first() is not None:
        return jsonify({'msg': '手机号码已存在', 'code': 2114})
    try:
        db.session.add(member)
        db.session.commit()
    except Exception as e:
        db.rollback()
        return jsonify({'msg': '数据添加失败', 'code': 5001})
    return jsonify({'msg': '成功', 'code': 200})  # 前端：注册成功

# [测试中] 查询会员详情 <id>
# @staff_bp.route('/staff/member/<int:id>', methods=['GET'])


@staff_bp.route('/query/member/<int:id>', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(1)
def staff_get_member_by_id(id):
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200
    member = Member.query.filter_by(member_id=id).first()
    if member is None:
        return jsonify({'msg': '用户不存在', 'code': 2002})
    # 前端：查询成功
    return jsonify({'msg': '成功', 'code': 200, 'data': member.to_json()})

# [测试中] 条件查询会员列表


@staff_bp.route('/query/members', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(1)
def staff_get_members():
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200

    # print(request.args)
    print(request.json)
    # 获取查询参数
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    # 可选的过滤条件
    nickname = request.args.get('nickname', default=None, type=str)
    phone_number = request.args.get('phone_number', default=None, type=str)

    # 构建查询
    query = Member.query

    if nickname:
        query = query.filter(Member.nickname.like(
            f'%{nickname}%'))  # like:区分大小写 ilike:不区分大小写
    if phone_number:
        query = query.filter(Member.phone_number == phone_number)
    # 总页数 query数 除以 每页数
    total = (query.count() - 1) // per_page + 1
    # 分页查询 (查询结果为空的话items.items将返回空列表)
    items = query.paginate(page=page, per_page=per_page)

    result = {
        'msg': '成功',
        'code': 200,
        'data': {
            'total': total,
            'page': page,
            'per_page': per_page,
            'items': [item.to_json() for item in items.items],
        }
    }
    return jsonify(result), 200

# [测试中] 修改会员信息 <id> # 管理员


@staff_bp.route('/modify/member/<int:id>', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(1)
def staff_modify_member(id):
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200

    member = Member.query.filter_by(member_id=id).first()
    if member is None:
        return jsonify({'msg': '用户不存在', 'code': 2002})

    member.nickname = request.json.get('nickname')
    member.realname = request.json.get('realname')
    member.id_card = request.json.get('id_card')
    member.student_card = request.json.get('student_card')
    member.phone_number = request.json.get('phone_number')
    # print(member.to_json())
    # 提交更改到数据库
    try:
        db.session.commit()  # 提交更改
        # 前端：修改成功
        return jsonify({'msg': '成功', 'code': 200, 'data': member.to_json()})
    except Exception as e:
        db.session.rollback()  # 如果发生错误，回滚事务
        # 返回错误消息和状态码 500
        return jsonify({'msg': '数据修改失败', 'code': 5003, 'error': str(e)}), 500

# [测试中] 删除会员 <id> # 管理员


@staff_bp.route('/delete/member/<int:id>', methods=['POST', 'OPTIONS'])
# @login_required
# @permission(3) # 管理员
def staff_delete_member(id):
    if request.method == 'OPTIONS':
        return jsonify({'msg': 'CORS preflight response'}), 200
    member = Member.query.filter_by(member_id=id).first()
    if member is None:
        return jsonify({'msg': '用户不存在', 'code': 2002})

    try:
        db.session.delete(member)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': '数据删除失败', 'code': 5002})
    return jsonify({'msg': '成功', 'code': 200})  # 前端：删除成功
