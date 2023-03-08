from random import randint
from faker import Faker

from src.db import session
from src.models import Group

fake = Faker()


def create_groups():
    list_of_groups = ["XK-21", "XO-41", "XE-01", "XH-11"]
    for group in list_of_groups:
        group_name = Group(
            name=group
        )
        session.add(group_name)
    session.commit()


if __name__ == '__main__':
    create_groups()
