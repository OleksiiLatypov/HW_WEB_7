from src.models import Grade, Student, Discipline
from src.db import session
from sqlalchemy import select
from datetime import datetime, timedelta
from random import randint, choice


def date_range(start, end):
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def create_grades():
    # дата початку навчального процесу
    start_date = datetime.strptime("2020-09-01", "%Y-%m-%d")
    # дата закінчення навчального процесу
    end_date = datetime.strptime("2021-05-31", "%Y-%m-%d")
    d_range = date_range(start=start_date, end=end_date)
    discipline_ids = session.scalars(select(Discipline.id)).all()
    student_ids = session.scalars(select(Student.id)).all()

    for d in d_range:  # пройдемося по кожній даті
        random_id_discipline = choice(discipline_ids)
        random_ids_student = [choice(student_ids) for i in range(5)]
        # проходимося списком "везучих" студентів, додаємо їх до результуючого списку
        # і генеруємо оцінку
        for student_id in random_ids_student:
            grade = Grade(
                grade=randint(1, 12),
                date_of=d,
                student_id=student_id,
                discipline_id=random_id_discipline,
            )
            session.add(grade)
    session.commit()


if __name__ == '__main__':
    create_grades()
