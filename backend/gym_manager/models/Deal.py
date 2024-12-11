from .. import db

class Deal(db.Model):
    __tablename__ = 'deal'
    # __table_args__ = {'schema': 'public'}  # 指定模式为 public
    # 定义表的字段
    activity_id = db.Column(db.Integer, nullable=False)
    plan_id = db.Column(db.Integer, nullable=False)
    
    activity_name = db.Column(db.String(255), nullable=False)
    
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    recharge_type = db.Column(db.String(10), nullable=False) # 充值类型 time:时间 count:次数
    recharge_count = db.Column(db.Integer)
    lifespan = db.Column(db.Integer)
    recharge_day = db.Column(db.Integer)

    amount = db.Column(db.DECIMAL(10, 2), nullable=False) # 金额
    activity_remark = db.Column(db.String(255))

    # 联合主键
    __table_args__ = (
        db.PrimaryKeyConstraint('activity_id', 'plan_id'),
    )
    
    def __repr__(self):
        return f'<Deal {self.activity_id} {self.plan_id}>'
    
    def to_json(self):
        json = {
            'activity_id': self.activity_id,
            'plan_id': self.plan_id,
            'activity_name': self.activity_name,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': self.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'recharge_type': self.recharge_type,
            'recharge_count': self.recharge_count,
            'lifespan': self.lifespan,
            'recharge_day': self.recharge_day,
            'amount': str(self.amount),
            'activity_remark': self.activity_remark,
        }
        return json