import json
import os
import random
import string

from flask_sqlalchemy import SQLAlchemy

from apps.core.models import User


def generate_json_data(amount: int, json_path: str) -> None:
    """
    Generates fake data.
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
            "name": "".join(
                random.choice(string.ascii_lowercase)
                for _ in range(random.randint(5, 15))
            ),
            "is_bot": random.choice([True, False]),
        }
        for _ in range(amount)
    ]

    with open(json_path, "w") as f:
        json.dump(users, f)


def read_fake_data(db: SQLAlchemy, json_path: str):
    """
    Reads JSON and populates DB.
    """

    json_file = os.path.join(json_path)

    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            data = json.load(f)

            users_data = [
                User(
                    email=x.get("email"),
                    name=x.get("name"),
                    is_bot=x.get("bot"),
                )
                for x in data
            ]

            db.session.add_all(users_data)
            db.session.commit()
