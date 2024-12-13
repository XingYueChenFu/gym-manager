from flask import Flask, render_template, jsonify, \
    Blueprint, g, json
# from flask.json import JSONEncoder
from flask.json.provider import DefaultJSONProvider
from flask_moment import Moment
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
import flask_excel as excel
from flask_cors import CORS 

from sqlalchemy import text
from functools import wraps
from datetime import datetime, date

# from config import config

moment = Moment()
db = SQLAlchemy()
# JSONEncoder = json.JSONEncoder
loginmanager = LoginManager()
loginmanager.session_protection = 'strong'

# ///// 需要修改 /////
def permission(min_level):  
    def decorator(f):  
        @wraps(f)  
        def decorated_function(*args, **kwargs):  
            # 检查用户是否已登录  
            if not current_user.is_authenticated:
                # Unauthorized access, please log in.
                return jsonify({'msg': '用户未登陆', 'code': 2001}), 401  
            
            # 检查用户权限级别  
            if current_user.level < min_level:  
                return jsonify({'msg': '用户权限不足', 'code': 2007}), 403  
            
            return f(*args, **kwargs)  
        return decorated_function  
    return decorator  

class CustomJSONEncoder(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return DefaultJSONProvider.default(self, obj)


def create_app(used_config):
    # bug free
    from gym_manager.utils.bugfreepy import print_bug_free_gradient_texts
    print_bug_free_gradient_texts()
    
    
    # 创建应用
    app = Flask(__name__)
    app.json = CustomJSONEncoder(app)
    app.json.ensure_ascii = False
    
    app.config.from_object(used_config)
    # 初始化扩展
    moment.init_app(app)
    # init_db(app)
    db.init_app(app)
    
    # ===== 以下👇代码用于测试数据库连接 =====
    from gym_manager.models import Member, Deal, DealPicture, RechargeRecord, ConsumeRecord, UsageCount, ExpirationTime, Staff
    with app.app_context():
        # 确认数据库连接  
        try:  
            # 使用 db.session 来执行简单的查询  
            db.session.execute(text("SELECT 1"))  # 显式声明 SQL 查询  
            print("\033[1;32m[SUCCESS]\033[0m Database connection is successful.")  
        except Exception as e:  
            print("\033[1;31m[ERROR]\033[0m Database connection failed:", e)
        if used_config.RESET_DATABASE:
            # 重置数据库
            db.drop_all()
            
            print("\033[1;35m[DEBUG]\033[0m Tables to be created:", db.Model.metadata.tables.keys())  
            db.create_all()
            
            print('\033[1;33m[ATTENTION]\033[0m Database reseted.')
            
            from sqlalchemy import inspect  
            inspector = inspect(db.engine)  
            print("\033[1;35m[DEBUG]\033[0m Existing tables in the database:", inspector.get_table_names())
            
            # 创建管理员账号 admin 123456 3
            import hashlib
            import uuid
            #  = 'admin'
            username = 'admin'
            password = '123456'
            level = 3
            md = hashlib.md5()
            md.update(password.encode('utf-8'))
            staff = Staff(username=username, password=md.hexdigest(), level=level)
            db.session.add(staff)
            db.session.commit()  
    # ===== 以上👆代码用于测试数据库连接 =====
    # 注册蓝图
    # from .base import base as base_blueprint
    # app.register_blueprint(base_blueprint)
    
    from gym_manager.base import staff_bp, super_bp, base
    app.register_blueprint(staff_bp)
    app.register_blueprint(super_bp)   
    app.register_blueprint(base)  
    
    # 初始化登录管理器
    loginmanager.init_app(app)
    # 初始化excel
    excel.init_excel(app)
    # 初始化CORS（允许跨域请求）# 允许所有域名的请求
    CORS(app)
    return app