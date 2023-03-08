from datetime import datetime, date, timedelta
from random import randint, choice
from faker import Faker
from sqlalchemy import select
from src.models import Teacher
from src.db import session

fake = Faker()


def create_teacher():
    for i in range(5):
        teacher = Teacher(
            fullname=fake.name()
        )
        session.add(teacher)
    session.commit()


if __name__ == '__main__':
    create_teacher()
