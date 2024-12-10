from .. import db, permission
from ..base import base, super_bp

from ..models import Staff, Member, Deal
from flask import render_template, request, jsonify, redirect, url_for, g

from flask_login import login_user, logout_user, login_required, \
    current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime

# super_bp: /superuser
# [调试用] 全部都是调试用的，之后删


# [测试中] 暂留，之后删
@super_bp.route('/register', methods=['GET'])
def superuser_register_get():
    print('\033[1;34m[debug]\033[0m superuser_register_get')
    # 创建一个含username password level的界面
    return render_template('superuser/register.html')

# [测试中] 暂留，之后删    
@super_bp.route('/register', methods=['POST'])
def superuser_register_post():
    print('\033[1;34m[debug]\033[0m superuser_register_post')
    username = request.form.get('username')
    password = request.form.get('password')
    level = request.form.get('level')
    
    error = None
    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    elif not level:
        error = 'Level is required.'
    elif db.session.query(Staff).filter_by(username=username).first() is not None:
        error = 'User {} is already registered.'.format(username)
    
    if error is None:
        try:
            md = hashlib.md5()
            md.update(password.encode('utf-8'))
            staff = Staff(username=username, password=md.hexdigest(), level=level)
            db.session.add(staff)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            error = 'Database error.'
            return jsonify({'msg': error, 'code': 5001})
        
        print('\033[1;32m[SUCCESS]\033[0m Register success.')
        # return jsonify({'msg': 'Register success.', 'code': 200})
        print(url_for('base.superuser.login'))
        return redirect(url_for('base.superuser_register_get'))
        
    print('\033[1;31m[ERROR]\033[0m {}'.format(error))
    return jsonify({'msg': error, 'code': 5002})

# [测试中] 暂留，之后删
@super_bp.route('/login', methods=['GET'])
def superuser_login_get():
    print('\033[1;34m[debug]\033[0m superuser_login_get')
    return render_template('superuser/login.html')

# [测试中] 暂留，之后删
@super_bp.route('/login', methods=['POST'])
def superuser_login_post():
    print('\033[1;34m[debug]\033[0m superuser_login_post')
    username = request.form.get('username')
    password = request.form.get('password')
    
    error = None
    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    
    if error is None:
        staff = db.session.query(Staff).filter_by(username=username).first()
        if staff is not None:
            md = hashlib.md5()
            md.update(password.encode('utf-8'))
            if md.hexdigest() == staff.password:
                login_user(staff)
                print('\033[1;32m[SUCCESS]\033[0m Login success.')
                return redirect(url_for('base.superuser_index_get'))
        error = 'Incorrect username or password.'
    print('\033[1;31m[ERROR]\033[0m {}'.format(error))
    return jsonify({'msg': error, 'code': 5003})

@super_bp.route('/logout', methods=['POST'])
@login_required
def superuser_logout():
    print('\033[1;34m[debug]\033[0m superuser_logout')
    logout_user()
    print('\033[1;32m[SUCCESS]\033[0m Logout success.')

@super_bp.route('/index', methods=['GET'])
def superuser_index_get():
    print('\033[1;34m[debug]\033[0m superuser_index')
    return render_template('superuser/index.html')

# ===== add table data =====

@super_bp.route('/add_member', methods=['GET'])
def add_member():
    print('\033[1;34m[debug]\033[0m add_member')
    return render_template('superuser/add_member.html')


# ===== delete table data =====




# ===== show table data =====


@super_bp.route('/show_staff', methods=['GET'])
def show_staff():
    print('\033[1;34m[debug]\033[0m show_staff')
    staffs = db.session.query(Staff).all()
    return render_template('superuser/show_staff.html', staffs=staffs)

@super_bp.route('/show_member', methods=['GET'])
def show_member():
    print('\033[1;34m[debug]\033[0m show_member')
    members = db.session.query(Member).all()
    return render_template('superuser/show_member.html', members=members)

@super_bp.route('/show_deal', methods=['GET'])
def show_deal():
    print('\033[1;34m[debug]\033[0m show_deal')
    deals = db.session.query(Deal).all()
    return render_template('superuser/show_deal.html', deals=deals)

