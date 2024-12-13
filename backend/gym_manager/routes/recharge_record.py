from .. import db, permission
from ..base import staff_bp

from ..models import Staff, Member, Deal, UsageCount, RechargeRecord
from flask import render_template, request, jsonify, g

from flask_login import login_user, logout_user, login_required, current_user
import flask_excel as excel

from sqlalchemy import asc, true, desc, text
    
import hashlib
import uuid
from datetime import datetime

# [开发中] 充值
@staff_bp.route('/recharge', methods=['POST', 'OPTIONS'])
@login_required
@permission(1)
def staff_recharge():
    member_id = request.json.get('member_id')
    activity_id = request.json.get('activity_id')
    plan_id = request.json.get('plan_id')
    recharge_time = request.json.get('recharge_time')
    recharge_count = request.json.get('recharge_count')
    pass