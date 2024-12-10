from .. import db

class ExpirationTime(db.Model):
    __tablename__ = 'expiration_time'
    # __table_args__ = {'schema': 'public'}  # 指定模式为 public
    # 定义表的字段
    member_id = db.Column(db.Integer, primary_key=True)
    deadline = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<ExpirationTime {self.member_id} {self.deadline}>'
    
    def to_json(self):
        json = {
            'member_id': self.member_id,
            'deadline': self.deadline.strftime('%Y-%m-%d %H:%M:%S'),
        }
        return json