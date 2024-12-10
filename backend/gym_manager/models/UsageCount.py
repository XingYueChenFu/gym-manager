from .. import db

class UsageCount(db.Model):
    __tablename__ = 'usage_count'
    # __table_args__ = {'schema': 'public'}  # 指定模式为 public
    # 定义表的字段
    member_id = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    count = db.Column(db.Integer, default=5)

    # 联合主键
    __table_args__ = (
        db.PrimaryKeyConstraint('member_id', 'deadline'),
    )
    
    def __repr__(self):
        return f'<UsageCount {self.member_id} {self.deadline}>'
    
    def to_json(self):
        json = {
            'member_id': self.member_id,
            'deadline': self.deadline.strftime('%Y-%m-%d %H:%M:%S'),
            'count': self.count,
        }
        return json