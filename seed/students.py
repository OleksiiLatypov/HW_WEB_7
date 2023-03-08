from random import choice
from faker import Faker

from src.db import session
from src.models import Student, Group
from sqlalchemy import select

fake = Faker()


def create_students():
    groups_ids = session.scalars(select(Group.id)).all()
    for i in range(50):
        student = Student(
            fullname=fake.name(),
            group_id=choice(groups_ids)
        )
        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()
