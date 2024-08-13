from models.comment_models import db, CommentPost

def create_new_comment(id_user, id_post_sa, comment_user_post):
    try:
        new_comment= CommentPost(
            id_user= id_user,
            id_post_sa= id_post_sa,
            comment_user_post = comment_user_post
        )

        db.session.add(new_comment)
        db.session.commit()
        return new_comment
    except Exception as e:
        print(f"Error creating comment: {e}")
        return None


def get_comment(id_post_sa):
    try:
        # Consultar comentario por ID
        # Se asume que `CommentPost` es un modelo que puede consultar la base de datos
        comments = CommentPost.query.filter_by(id_post_sa=id_post_sa).all()
        # Convertir los comentarios a un formato que pueda ser serializado a JSON
        comments_list = [comment.to_dict() for comment in comments]
        return comments_list
    except Exception as e:
        print(f"Error retrieving comments: {e}")
        return None
