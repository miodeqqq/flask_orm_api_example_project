import random
import string

from flask_sqlalchemy import SQLAlchemy

from apps.core.models import User


def generate_fake_data(amount: int) -> list:
    """
    Generates fake Users data.
    """

    email_domains = ["@gmail.com", "@pudelek.pl", "@xxx.com"]

    users = [
        {
            "email": "".join(
                [
                    "".join(
                        random.choice(string.ascii_lowercase)
                        for _ in range(random.randint(5, 50))
                    ),
                    random.choice(email_domains),
                ]
            ),
            "name": " ".join(
                [
                    "".join(
                        random.choice(string.ascii_lowercase)
                        for _ in range(random.randint(5, 10))
                    ).capitalize(),
                    "".join(
                        random.choice(string.ascii_lowercase)
                        for _ in range(random.randint(10, 20))
                    ).capitalize(),
                ]
            ),
            "is_bot": bool(random.getrandbits(1)),
        }
        for _ in range(amount)
    ]

    return users


def read_fake_data(db: SQLAlchemy, users_data: list) -> None:
    """
    Reads fake data and populates DB with new Users.
    """

    users_objects = [
        User(
            email=user["email"],
            name=user["name"],
            is_bot=user["is_bot"],
        )
        for user in users_data
    ]

    db.session.add_all(users_objects)
    db.session.commit()
