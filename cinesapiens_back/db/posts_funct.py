from models.post_models import db, PostSapiens

def create_new_post(post_name, post_description):
    try:
        new_post = PostSapiens(
            post_name=post_name,
            post_description=post_description
        )
        db.session.add(new_post)
        db.session.commit()
        return new_post
    except Exception as e:
        db.session.rollback()  # Asegúrate de hacer rollback en caso de error
        print(f"Error creating post: {e}")
        return None

def get_post(id_post_sa):
    try:

        #Consulta post por ID
        post = PostSapiens.query.get(id_post_sa)
        return post
    except Exception as e:
        print(f"Error retrieving post {e}")
        return None
    

def get_posts():
    try:
        #Consulta todos los posts
        posts = PostSapiens.query.all()
        return posts
    except Exception as e:
        print(f"Error retrieving posts {e}")
        return None