from apps.shared.models import db


class User(db.Model):
    """
    Model for users.
    """

    __tablename__ = "users"

    id = db.Column(name="ID", type_=db.Integer, primary_key=True)

    email = db.Column(name="slack_id", type_=db.String(100), nullable=False)

    name = db.Column(name="name", type_=db.String(100), nullable=False)

    is_bot = db.Column(name="is_bot", type_=db.Boolean, default=False, index=True)

    def __repr__(self):
        return f"<User: {self.name}>"
