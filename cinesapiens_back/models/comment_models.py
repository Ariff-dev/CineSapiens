from app import db

class CommentPost(db.Model):
    __tablename__ = 'comment_post'
    
    id_comment = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user_sapiens.id_user'), nullable=False)
    id_post_sa = db.Column(db.Integer, db.ForeignKey('post_sapiens.id_post_sa'), nullable=False)
    comment_user_post = db.Column(db.Text, nullable=False)
    
    # Relaciones para acceder fácilmente a los datos relacionados
    user = db.relationship('UserSapiens', backref=db.backref('comments', lazy=True))
    post = db.relationship('PostSapiens', backref=db.backref('comments', lazy=True))

    def __init__(self, id_user, id_post_sa, comment_user_post):
        self.id_user = id_user
        self.id_post_sa = id_post_sa
        self.comment_user_post = comment_user_post

    def to_dict(self):
        return {
            'id_comment': self.id_comment,
            'id_user': self.id_user,
            'id_post_sa': self.id_post_sa,
            'comment_user_post': self.comment_user_post,
            'user': {
                'id_user': self.user.id_user,
                'username': self.user.username  # Asumiendo que UserSapiens tiene un campo 'username'
            },
            'post': {
                'id_post_sa': self.post.id_post_sa,
                'post_name': self.post.post_name  # Asumiendo que PostSapiens tiene un campo 'post_name'
            }
        }
