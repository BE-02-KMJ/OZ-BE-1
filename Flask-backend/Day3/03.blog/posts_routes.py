from flask import request, jsonify
from flask_smorest import Blueprint, abort


def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description="posts api", url_prefix="/posts")

    @posts_blp.route("/", methods=["GET", "POST"])
    def posts():
        cursor = mysql.connection.cursor()

        # 게시글 조회
        if request.method == "GET":
            cursor.execute("SELECT * FROM posts")
            posts = cursor.fetchall()
            cursor.close()

            post_list = []

            for post in posts:
                post_list.append(
                    {
                        "id": post[0],
                        "title": post[1],
                        "content": post[2],
                    }
                )
            return jsonify(post_list)

        # 게시글 생성
        elif request.method == "POST":
            title = request.json.get("title")
            content = request.json.get("content")

            if not title or not content:
                abort(400, message="Title or Content is required.")

            cursor.execute("INSERT INTO posts(title, content) VALUES(%s, %s)", (title, content))
            mysql.connection.commit()

            return jsonify({"message": "successfully created post data", "title": title, "content": content}), 201

    @posts_blp.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
    def post(id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = %s", (id))
        post = cursor.fetchone()

        # 게시글 상세 조회
        if request.method == "GET":
            if not post:
                abort(404, "Not found post.")

            return jsonify({
                "id": post[0],
                "title": post[1],
                "content": post[2],
            })
        
        # 게시글 수정
        elif request.method == "PUT":
            # data = request.json
            # title = data['title']
            title = request.json.get("title")
            content = request.json.get("content")

            if not title or not content:
                abort(400, message="Not found title or content.")

            if not post:
                abort(404, message="Not found post.")

            cursor.execute(f"UPDATE posts SET title=%s, content=%s WHERE id=%s", (title, content, id))
            mysql.connection.commit()

            return jsonify({"message": "Successfully updated title & content"})

        # 게시글 삭제
        elif request.method == "DELETE":
            if not post:
                abort(404, message="Not found post.")

            cursor.execute("DELETE FROM posts WHERE id=%s", (id))
            mysql.connection.commit()

            return jsonify({"message": "Successfully deleted title & content"})
        

    return posts_blp