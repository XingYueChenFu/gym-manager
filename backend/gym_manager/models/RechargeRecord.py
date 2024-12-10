from .. import db

class RechargeRecord(db.Model):
    __tablename__ = 'recharge_record'
    # __table_args__ = {'schema': 'public'}  # 指定模式为 public
    # 定义表的字段
    member_id = db.Column(db.Integer, nullable=False)
    activity_id = db.Column(db.Integer, nullable=False)
    plan_id = db.Column(db.Integer, nullable=False)
    recharge_time = db.Column(db.DateTime, nullable=False)
    recharge_remark = db.Column(db.String(255))
    
    # 联合主键
    __table_args__ = (
        db.PrimaryKeyConstraint('member_id', 'activity_id', 'plan_id', 'recharge_time'),
    )
    
    def __repr__(self):
        return f'<RechargeRecord {self.member_id} {self.activity_id} {self.plan_id} {self.recharge_time}>'
    
    def to_json(self):
        json = {
            'member_id': self.member_id,
            'activity_id': self.activity_id,
            'plan_id': self.plan_id,
            'recharge_time': self.recharge_time.strftime('%Y-%m-%d %H:%M:%S'),
            'recharge_remark': self.recharge_remark,
        }
        return json