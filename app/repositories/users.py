from app.models import User


class user_repository:
    @staticmethod
    def get(first_name, last_name, email):
        return User.query.filter_by(first_name=first_name, last_name=last_name, email=email).one()

    def update(self, first_name, last_name, email, access_token):
        user = self.get(first_name, last_name, email)
        user.access_token = access_token

        return user.save()

    @staticmethod
    def create(first_name, last_name, email, access_token):
        user = User(first_name=first_name, last_name=last_name, email=email, access_token=access_token)

        return user.save()
