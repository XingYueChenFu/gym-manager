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

# [调试用]
# @staff_bp.route('/login', methods=['GET'])
# def do_login_get():
#     return render_template('staff/login.html'), 200
# [测试中] 登录 # /staff/login
@staff_bp.route('/login', methods=['POST', 'OPTIONS'])
def do_login():
    # staff = Staff.query.filter(Staff.username == request.json.get('username')).first()
    staff = Staff.query.filter_by(username=request.json.get('username')).first()
    
    if staff is not None:
        md = hashlib.md5()
        md.update(request.json.get('password').encode('utf-8'))
        if md.hexdigest() == staff.password:
            login_user(staff)
            return jsonify({'msg': '成功', 'code': 200, 'level': staff.level, 'token': str(uuid.uuid4())}) # 前端：登录成功
    return jsonify({'msg': '登录失败，账号或密码错误', 'code': 2003})

# [测试中] 退出登录
@staff_bp.route('/logout', methods=['POST', 'OPTIONS'])    
@login_required
def do_logout():
    logout_user()
    return jsonify({'msg': '成功', 'code': 200}) # 前端：退出登录成功

# [测试中] 注册员工 # 管理员
@staff_bp.route('/register', methods=['POST', 'OPTIONS'])
@login_required
@permission(3) # 管理员
def do_register():
    # md5加密 密码
    md = hashlib.md5()
    md.update(request.json.get('password').encode('utf-8'))
    
    staff = Staff()
    staff.username = request.json.get('username') # username
    staff.password = md.hexdigest() # password
    staff.level = request.json.get('level')
    staff.employee_info = request.json.get('employee_info')
    
    # if db.session.query(Staff).filter(Staff.username == staff.username).first() is not None:
    if db.session.query(Staff).filter_by(username=staff.username).first() is not None:
        return jsonify({'msg': '用户名已存在', 'code': 2110})
    try:
        db.session.add(staff)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': '数据添加失败', 'code': 5001})
    return jsonify({'msg': '成功', 'code': 200}) # 前端：注册成功，请重新登录