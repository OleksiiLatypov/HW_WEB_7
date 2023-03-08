from src.models import Student, Group, Grade, Discipline, Teacher
from src.db import session
from sqlalchemy import func, and_, desc, select
from sqlalchemy.orm import joinedload


def select_1():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(5) \
        .all()
    return result


def select_2():
    r = session.query(Discipline.name,
                      Student.fullname,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == 3) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return r


def select_3():
    result = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(Discipline.id == 1) \
        .group_by(Discipline.name, Group.name) \
        .order_by(desc('avg_grade')) \
        .all()
    return result


def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).all()
    return result


def select_5():
    result = session.query(Discipline.name, Teacher.fullname) \
        .select_from(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == 1) \
        .all()
    return result


def select_6():
    result = session.query(Group.name, Student.fullname) \
        .select_from(Group) \
        .join(Student) \
        .filter(Group.id == 1) \
        .all()
    return result


def select_7():
    result = session.query(Student.fullname, Grade.grade, Discipline.name, Group.name) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Discipline.id == 1, Group.id == 1)) \
        .order_by(Student.fullname) \
        .all()
    return result


def select_8():
    result = session.query(func.round(func.avg(Grade.grade), 2), Teacher.fullname, Discipline.name) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == 1) \
        .group_by(Teacher.id, Discipline.id) \
        .all()
    return result


def select_9():
    result = session.query(Discipline.name, Student.fullname) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Student.id == 5) \
        .all()
    return result


def select_10():
    result = session.query(Discipline.name, Student.fullname, Teacher.fullname) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Teacher.id == 3, Student.id == 3)) \
        .group_by(Discipline.name, Student.fullname, Teacher.fullname) \
        .all()
    return result


def select_11():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2), Teacher.fullname) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Teacher.id == 3, Student.id == 3)) \
        .group_by(Teacher.fullname, Student.fullname) \
        .all()
    return result


def select_12():
    last_date_list_tuples = session.query(Grade.date_of).select_from(Grade).join(Student, Group) \
        .filter(and_(Grade.lesson_id == 6, Group.id == 3)).order_by(desc(Grade.date_of)).limit(1).all()
    last_date = last_date_list_tuples[0][0]

    result = session.query(Grade.name, Group.group_name, Student.name, Grade.date_of, Grade.grade) \
        .select_from(Grade).join(Student, Discipline, Group) \
        .filter(and_(Discipline.id == 6, Group.id == 3, Grade.date_of == last_date)) \
        .order_by(desc(Grade.date_of)).all()

    return result


def select_last(discipline_id, group_id):
    subquery = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    r = session.query(Discipline.name,
                      Student.fullname,
                      Group.name,
                      Grade.date_of,
                      Grade.grade
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id, Grade.date_of == subquery)) \
        .order_by(desc(Grade.date_of)) \
        .all()
    return r


if __name__ == '__main__':
    print(select_last(1, 1))
