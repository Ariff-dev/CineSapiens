from app import db  # Importa db desde app.py

class UserSapiens(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    user_password = db.Column(db.String(255), nullable=False)
    user_role = db.Column(db.String(50), nullable=False, default='standard')
