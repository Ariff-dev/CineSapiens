from flask import Flask, jsonify, request
from db.user_funct import create_new_user, get_user
from db.posts_funct import create_new_post, get_post
from db.comment_funct import create_new_comment, get_comment
from app import app


#User_Sapiens
@app.route('/create_user', methods=['POST'])
def create_user_route():
    data = request.get_json()  # Obtiene los datos JSON del cuerpo de la solicitud
    
    username = data.get('username')
    email = data.get('email')
    user_password = data.get('user_password')
    
    if not username or not email or not user_password:
        return jsonify({"message": "Missing required fields"}), 400  # 400 Bad Request
    
    user = create_new_user(username, email, user_password)
    
    if user:
        return jsonify({
            "message": "User created successfully",
            "user": {
                "id_user": user.id_user,
                "username": user.username,
                "email": user.email
            }
        }), 201  # 201 Created
    else:
        return jsonify({"message": "Error creating user"}), 500  # 500 Internal Server Error

@app.route('/get_user', methods=[ 'GET'])
def get_user_route():
    data = request.get_json()

    id_user = data.get('id_user')
    
    if not id_user:
        return jsonify({'message': "Missing id_user parameter"}), 400
    
    user = get_user(id_user)
    if user:
        return jsonify({
            "id_user": user.id_user,
            "username": user.username,
            "email": user.email
        }), 200
    else:
        return jsonify({'message': "User not found"}), 404



#Post_Sapiens
@app.route('/create_post', methods=['POST'])
def create_post_route():
    data = request.get_json()  # Obtiene los datos JSON del cuerpo de la solicitud
    
    post_name = data.get('post_name')
    post_description = data.get('post_description')
    
    if not post_name or not post_description:
        return jsonify({"message": "Missing required fields"}), 400  # 400 Bad Request
    
    post = create_new_post(post_name, post_description)
    
    if post:
        return jsonify({
            "message": "Post created successfully",
            "post": {
                "id_post_sa": post.id_post_sa,
                "post_name": post.post_name,
                "post_description": post.post_description
            }
        }), 201  # 201 Created
    else:
        return jsonify({"message": "Error creating post"}), 500  # 500 Internal Server Error

@app.route('/get_post', methods=['GET'])
def get_post_route():
    data = request.get_json()

    id_post_sa = data.get('id_post_sa')

    if not id_post_sa:
        return jsonify({'message': "Missing id_user parameter"}), 400

    post = get_post(id_post_sa)

    if id_post_sa:
        return jsonify({
            "id_post_sa": post.id_post_sa,
            "post_name": post.post_name,
            "decription": post.post_description
        }),200
    else:
        return jsonify({'message': "Post not found"}), 404
        

#CommentPost
@app.route('/create_comment_post', methods=['POST'])
def create_comment_route():
    data= request.get_json()

    id_user = data.get('id_user')
    id_post_sa = data.get("id_post_sa")
    comment_user_post= data.get('comment_user_post')
    
    
    if not comment_user_post:
        return jsonify({"message": "Missing required fields"}), 400  # 400 Bad Request

    comment= create_new_comment(id_user,id_post_sa,comment_user_post)
    

    if comment:
        return jsonify({
            "message": "Comment created successfully",
            "comment": {
                "id_comment": comment.id_comment,
                "id_user":  comment.id_user,
                "id_post_sa": comment.id_post_sa,
                "comment_user_post": comment.comment_user_post
            }
        }),201
    else: 
        return jsonify({"message": "Error creating post"}), 500  # 500 Internal Server Error

@app.route('/get_comments')
def get_comments():
    data = request.get_json()

    id_post_sa = data.get('id_post_sa')

    if not id_post_sa:
        return jsonify({'message': "Missing id_post_sa parameter"}), 400
    
    comments = get_comment(id_post_sa)

    if comments:
        return jsonify({
            'comments': comments
        }), 200
    else:
        return jsonify({'message': 'No comments found for this post.'}), 404

#Image_post
