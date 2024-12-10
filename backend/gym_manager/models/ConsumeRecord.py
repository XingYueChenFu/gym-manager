from .. import db

class ConsumeRecord(db.Model):
    __tablename__ = 'consume_record'
    # __table_args__ = {'schema': 'public'}  # 指定模式为 public
    # 定义表的字段
    member_id = db.Column(db.Integer, nullable=False)
    consume_time = db.Column(db.DateTime, nullable=False)
    consume_type = db.Column(db.String(10), nullable=False)

    # 联合主键
    __table_args__ = (
        db.PrimaryKeyConstraint('member_id', 'consume_time'),
    )
    
    def __repr__(self):
        return f'<ConsumeRecord {self.member_id} {self.consume_time}>'
    
    def to_json(self):
        json = {
            'member_id': self.member_id,
            'consume_time': self.consume_time.strftime('%Y-%m-%d %H:%M:%S'),
            'consume_type': self.consume_type,
        }
        return json