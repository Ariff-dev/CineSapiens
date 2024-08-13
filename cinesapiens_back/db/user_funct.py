from models.user_models import db, UserSapiens

def create_new_user(username, email, user_password):
    try:
        new_user = UserSapiens(
            username=username,
            email=email,
            user_password=user_password
            # user_role se establece automáticamente a 'standard'
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as e:
        db.session.rollback()  # Asegúrate de hacer rollback en caso de error
        print(f"Error creating user: {e}")
        return None

def get_user(id_user):
    try: 
        #Consultar usuario por ID
        user = UserSapiens.query.get(id_user)
        return user
    except Exception as e:
        print(f"Error retrieving user {e}")
        return None