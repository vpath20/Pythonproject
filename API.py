# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         'user_id': user_id,
#         'name': "John_Doe",
#         "email": "jon.doe@example.com"
#     }
#
#     "get-user/123?extra=hello world"
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra
#
#     return jsonify(user_data),200
#
#
# if __name__ == "__main__":
#     app.run(debug=True)






from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': "John_Doe",
        "email": "jon.doe@example.com"
    }

    "get-user/123?extra=hello world"
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data),200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)



