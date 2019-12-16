from flask.json import jsonify

from app.repositories import user_repository


class user_resource:

    @staticmethod
    def all():
        users = user_repository.all()
        results = []

        for u in users:
            results.append(u.json)

        return jsonify({
            "users": results
        })

    @staticmethod
    def get(first_name, last_name, email):
        user = user_repository.get(first_name=first_name, last_name=last_name, email=email)

        return jsonify({
            "user": user.json
        })

    @staticmethod
    def post(first_name, last_name, email, access_token):
        user = user_repository.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            access_token=access_token
        )

        return jsonify({
            "user": user.json
        })

    @staticmethod
    def put(first_name, last_name, email, access_token):
        user = user_repository.update(
            first_name=first_name,
            last_name=last_name,
            email=email,
            access_token=access_token
        )

        return jsonify({
            "user": user.json
        })
