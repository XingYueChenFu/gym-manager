from .. import db, loginmanager
from datetime import datetime # 用于"默认注册时间"


class Member(db.Model):
    __tablename__ = 'member'
    # __table_args__ = {'schema': 'public'}  # 指定模式为 public
    # 定义表的字段
    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(15), nullable=False)
    regist_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    nickname = db.Column(db.String(50), nullable=False)
    realname = db.Column(db.String(50)) # 可有可无
    id_card = db.Column(db.String(18))
    student_card = db.Column(db.String(13))
    gender = db.Column(db.String(1)) # 可有可无 # F:女 M:男 O:其他
    email = db.Column(db.String(255)) # 可有可无
    birthdate = db.Column(db.DateTime) # 可有可无 非birthday
    password = db.Column(db.String(255)) # 可有可无
    campus = db.Column(db.String(50)) # 可有可无
    address = db.Column(db.String(255)) # 可有可无
    
    def get_id(self):
        return self.member_id
    
    def __repr__(self):
        # return '<Member %r>' % self.nickname
        return f'<Member {self.nickname}>'
    
    def to_json(self):
        json = {
            'member_id': self.member_id,
            'phone_number': self.phone_number,
            'regist_time': self.regist_time.isoformat() if self.regist_time else None,
            'nickname': self.nickname,
            'realname': self.realname,
            'id_card': self.id_card,
            'student_card': self.student_card,
            'gender': self.gender, 
            'email': self.email,  
            'birthdate': self.birthdate.isoformat() if self.birthdate else None,
            'campus': self.campus,
            'address': self.address
        }
        
        return json
    