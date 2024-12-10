from .. import db, loginmanager
from flask_login import UserMixin
from datetime import datetime

@loginmanager.user_loader
def load_staff(staff_id):
    return Staff.query.filter(Staff.staff_id == staff_id).first()

class Staff(db.Model, UserMixin):
    __tablename__ = 'staff'
    # __table_args__ = {'schema': 'public'}  # 指定模式为 public
    # 定义表的字段
    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer, default=1, nullable=False) # level 1:user 2:manager 3:admin
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    employee_info = db.Column(db.String(255))
    
    def get_id(self):
        return self.staff_id
    
    def __repr__(self):
        return f'<Staff {self.username}>' 
    
    def to_json(self):
        json = {
            'staff_id': self.staff_id,
            'username': self.username,
            'level': self.level,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'employee_info': self.employee_info,
        }
        return json