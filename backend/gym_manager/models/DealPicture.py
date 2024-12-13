from .. import db

class DealPicture(db.Model):
    __tablename__ = 'deal_picture'
    
    activity_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<DealPicture {self.activity_id}>'
    
    def to_json(self):
        json = {
            'activity_id': self.activity_id,
            'url': self.url,
        }
        return json