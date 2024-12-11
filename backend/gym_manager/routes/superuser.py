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
        print(url_for('super.superuser_login_get'))
        return redirect(url_for('super.superuser_login_get'))
        
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

@super_bp.route('/add_member', methods=['GET', 'OPTIONS'])
def add_member_get():
    print('\033[1;34m[debug]\033[0m add_member get')
    return render_template('superuser/add_member.html')

@super_bp.route('/add_member', methods=['POST'])
def add_member_post():
    print('\033[1;34m[debug]\033[0m add_member_post')
    phone = request.form.get('phone_number')
    nickname = request.form.get('nickname')
    realname = request.form.get('realname')
    id_card = request.form.get('id_card')
    student_card = request.form.get('student_card')
    gender = request.form.get('gender')
    member = Member(phone_number=phone, nickname=nickname, realname=realname, id_card=id_card, student_card=student_card, sex=gender)
    db.session.add(member)
    db.session.commit()
    return redirect(url_for('super.show_member'))
    
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

# ===== init table data =====
from faker import Faker
fake = Faker('zh_CN')
import random  
from datetime import datetime, timedelta  
from ..models import Member, Deal, UsageCount, ExpirationTime, RechargeRecord, ConsumeRecord

def generate_person_id():
    # 1. 生成地址码（前6位）  
    address_code = str(random.randint(100000, 999999))  

    # 2. 生成出生日期（8位）  
    start_date = datetime(1950, 1, 1)  
    end_date = datetime(2003, 12, 31)  # 假设出生日期在1950到2003年之间  
    random_days = random.randint(0, (end_date - start_date).days)  
    birth_date = start_date + timedelta(days=random_days)  
    birth_date_str = birth_date.strftime('%Y%m%d')  

    # 3. 生成顺序码（3位）  
    sequence_code = str(random.randint(100, 999))  

    # 4. 组合前17位  
    id_without_check = address_code + birth_date_str + sequence_code  

    # 5. 计算校验位  
    weights = [int(x) for x in '798621345']  
    total = sum(int(id_without_check[i]) * weights[i % 9] for i in range(17))  
    check_digit = total % 11  
    check_code = str(check_digit) if check_digit < 10 else 'X'  

    # 6. 组合完整身份证号  
    id_number = id_without_check + check_code  
    return id_number  
    
def generate_student_id():
    # 2022 14146 0113
    year = str(random.randint(2000, 2050))
    school_num = str(random.randint(10000, 99999))
    student_num = str(random.randint(1000, 9999))
    student_id = year + school_num + student_num
    return student_id

def generate_activity_name():
    name = fake.name()
    adjectives = ["快乐的", "神秘的", "刺激的", "有趣的", "创意的"]  
    nouns = ["聚会", "探险", "比赛", "工作坊", "旅行"] 
    activity_name = name + random.choice(adjectives) + random.choice(nouns)
    return activity_name

def init_member(n):
    for _ in range(n):
        phone_number = fake.phone_number()
        nickname = fake.name()
        realname = fake.name()
        id_card = generate_person_id()
        student_card = generate_student_id()
        gender = random.choice(['M', 'F', 'O'])
        email = fake.email()
        birthdate = fake.date_of_birth()
        member = Member(phone_number=phone_number, nickname=nickname, realname=realname, id_card=id_card, \
            student_card=student_card, gender=gender, email=email, birthdate=birthdate)
        db.session.add(member)
    try:
        db.session.commit()
        print(f'\033[1;32m[SUCCESS]\033[0m add_member {n} success.')
        return True
    except Exception as e:
        db.session.rollback()
        print(f'\033[1;31m[ERROR]\033[0m add_member {n} failed.')
        print(e)
        return False
    
def init_deal(n, m=5):
    # n: 活动数 m: 活动下最大plan数
    for _ in range(n):
        # 获取当前最大的activity_id
        max_activity_id = db.session.query(Deal.activity_id).order_by(desc(Deal.activity_id)).first()
        if max_activity_id is None:
            max_activity_id = 0
        else:
            max_activity_id = max_activity_id[0]
        activity_id = max_activity_id + 1
        activity_name = fake.name()
        for plan_id in range(random.randrange(1,m+1,1)):
            start_time = fake.date_time_between(start_date='-5y', end_date='now')
            end_time = start_time + timedelta(days=random.randrange(1, 30, 1))
            recharge_type = random.choice(['time', 'day'])
            amount = random.uniform(10, 1000)
            if recharge_type == 'time':
                recharge_day = random.randrange(1, 30, 1)
                deal = Deal(activity_id=activity_id, plan_id=plan_id, activity_name=activity_name, start_time=start_time, end_time=end_time, recharge_type=recharge_type, recharge_day=recharge_day, amount=amount)
            else:
                recharge_count = random.randrange(1, 30, 1)
                lifespan = random.randrange(30, 365*10, 30)
                deal = Deal(activity_id=activity_id, plan_id=plan_id, activity_name=activity_name, start_time=start_time, end_time=end_time, recharge_type=recharge_type, recharge_count=recharge_count, lifespan=lifespan, amount=amount)
            db.session.add(deal)
    try:
        db.session.commit()
        print(f'\033[1;32m[SUCCESS]\033[0m add_deal {n} {m} success.')
        return True
    except Exception as e:
        db.session.rollback()
        print(f'\033[1;31m[ERROR]\033[0m add_deal {n} {m} failed.')
        return False

def recharge(member_id, activity_id, plan_id, recharge_time=datetime.now()):
    # member_id: 会员id activity_id: 活动id plan_id: 计划id
    # 在recharge_record 与 usage_count或expiration_time 中添加记录
    
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
    recharge_time = recharge_time
    recharge_remark = fake.text()
    recharge_record = RechargeRecord(member_id=member_id, activity_id=activity_id, plan_id=plan_id, recharge_time=recharge_time, recharge_remark=recharge_remark)
    db.session.add(recharge_record)
    db.session.commit()
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
    
def init_recharge(n):
    member_ids = db.session.query(Member.member_id).all()
    activity_ids = db.session.query(Deal.activity_id).all()

    for _ in range(n):
        member_id = random.choice(member_ids)[0]
        activity_id = random.choice(activity_ids)[0]
        plan_ids = db.session.query(Deal.plan_id).filter_by(activity_id=activity_id).all()
        plan_id = random.choice(plan_ids)[0]
        # recharge_time从活动start_time到end_time之间
        deal = db.session.query(Deal).filter_by(activity_id=activity_id, plan_id=plan_id).first()
        recharge_time = fake.date_time_between(start_date=deal.start_time, end_date=deal.end_time)
        recharge(member_id, activity_id, plan_id, recharge_time)

    
def consume(member_id, consume_time=datetime.now()):
    # 有天数就不管，返回成功
    # 没有天数，减少次数，返回成功
    
    # 1. 判断member是否存在
    member = db.session.query(Member).filter_by(member_id=member_id).first()
    if member is None:
        print(f'\033[1;31m[ERROR]\033[0m member_id {member_id} not exist.')
        return False
    
    # 2. 判断是否有有效期
    et = db.session.query(ExpirationTime).filter_by(member_id=member_id).first()
    if et is not None and et.deadline > consume_time:

        # 添加consume_record
        consume_record = ConsumeRecord(member_id=member_id, consume_time=consume_time, consume_type='time')
        db.session.add(consume_record)
        try:
            db.session.commit()
            print(f'\033[1;32m[SUCCESS]\033[0m consume {member_id} success.')
            return True
        except Exception as e:
            db.session.rollback()
            print(f'\033[1;31m[ERROR]\033[0m consume {member_id} failed.')
            return False
    else:
        # 找到member_id的所有UsageCount的有效期，将过有效期以及次数为0的删除，找到最近的有效期，减少次数
        ucs = db.session.query(UsageCount).filter_by(member_id=member_id).all()
        for uc in ucs:
            if uc.deadline < consume_time or uc.count == 0:
                db.session.delete(uc)
        ucs = db.session.query(UsageCount).filter_by(member_id=member_id).all()
        uc = sorted(ucs, key=lambda x: x.deadline, reverse=True)[0]
        uc.count -= 1
        consume_record = ConsumeRecord(member_id=member_id, consume_time=consume_time, consume_type='count')
        db.session.add(consume_record)
        try:
            db.session.commit()
            print(f'\033[1;32m[SUCCESS]\033[0m consume {member_id} success.')
            return True
        except Exception as e:
            db.session.rollback()
            print(f'\033[1;31m[ERROR]\033[0m consume {member_id} failed.')
            return False

def init_consume(n):
    member_ids = db.session.query(Member.member_id).all()
    for _ in range(n):
        member_id = random.choice(member_ids)[0]
        consume_time = fake.date_time_between(start_date='-5y', end_date='now')
        consume(member_id, consume_time)
     

# [开发中]
@super_bp.route('/init_all', methods=['GET'])
def init_all():
    print('\033[1;34m[debug]\033[0m init_all')
    print('\033[1;43m[ATTENTION]\033[0m 别手贱一直添加数据，谢谢')
    init_member(10)
    init_deal(10, 5)
    init_recharge(100)
    init_consume(100)
    return '正在初始化数据'
    
