from datetime import datetime, date, timedelta
from random import randint, choice
import faker
from sqlalchemy import select
from src.models import Discipline
from src.db import session


def date_range(start, end):
    result = []
    current_date = start
    while current_date <= end:
        if current_date <= 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def create_disciplines():
    disciplines = ["Вища математика", "Психологія", "Фінанси", "Статистка", "Філософія", "Мікроекономіка", "Менеджмент"]
    for item in disciplines:
        disciplines_to_db = Discipline(
            name=item,
            teacher_id=randint(1, 5)
        )
        session.add(disciplines_to_db)
    session.commit()


if __name__ == '__main__':
    create_disciplines()
