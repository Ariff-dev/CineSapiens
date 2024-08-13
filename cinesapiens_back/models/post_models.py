from app import db

class PostSapiens(db.Model):
    id_post_sa = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String(50), nullable=False)
    post_description = db.Column(db.Text, nullable=False)
