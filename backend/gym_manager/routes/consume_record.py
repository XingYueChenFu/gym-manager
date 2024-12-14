from .. import db, permission
from ..base import staff_bp

from ..models import Staff, Member, Deal, ExpirationTime, ConsumeRecord, UsageCount
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, \
    current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime

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

