import os

from flask import Flask, render_template, request
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

from apps.core.models import db, User
from apps.shared.utils import read_fake_data, generate_fake_data

# ===================================================================
# Config.
# ===================================================================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    BASE_DIR, "flask_api_test_database.db"
)

api = Api(app)

ma = Marshmallow(app)

db.init_app(app)


# ===================================================================
# User Schema & Resource.
# ===================================================================


class UserSchema(ma.Schema):
    """
    UserSchema.
    """

    class Meta:
        fields = ("id", "email", "name", "is_bot")
        models = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserListResource(Resource):
    """
    UserListResource.
    """

    def get(self) -> dict:
        """
        Returns the list of all users.
        """

        users = User.query.all()

        return users_schema.dump(users)

    def post(self) -> dict:
        """
        Adds new user.
        """

        new_user = User(
            email=request.json["email"],
            name=request.json["name"],
            is_bot=request.json["is_bot"],
        )
        db.session.add(new_user)
        db.session.commit()

        return user_schema.dump(new_user)


class UserResource(Resource):
    """
    UserResource.
    """

    def get(self, user_id: int) -> dict:
        """
        Get user object..
        """

        user = User.query.get_or_404(user_id)

        return user_schema.dump(user)

    def patch(self, user_id: int) -> dict:
        """
        Update user object.
        """

        user = User.query.get_or_404(user_id)

        if "email" in request.json:
            user.email = request.json["email"]

        if "name" in request.json:
            user.content = request.json["name"]

        if "is_bot" in request.json:
            user.is_bot = request.json["is_bot"]

        db.session.commit()

        return user_schema.dump(user)

    def delete(self, user_id: int) -> tuple:
        """
        Delete user object.
        """

        user = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return "", 204


# ===================================================================
# App Context.
# ===================================================================
with app.app_context():
    db.create_all()


# ===================================================================
# Home page.
# ===================================================================
@app.route("/", methods=["GET"])
def home():
    """
    Home page.
    """

    User.query.delete()

    fake_users_data = generate_fake_data(amount=200)

    read_fake_data(db=db, users_data=fake_users_data)

    users = User.query.all()

    return render_template(template_name_or_list="home.html", users=users)


# ===================================================================
# API.
# ===================================================================
api.add_resource(UserListResource, "/users/")
api.add_resource(UserResource, "/users/<int:user_id>/")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
