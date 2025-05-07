import pytest
from sqlalchemy.orm import Session
from database import SessionLocal, Student


@pytest.fixture(scope="module")
def db_session():
    session = SessionLocal()
    yield session
    session.close()


def test_add_student(db_session):
    new_student = Student(name="John Doe")
    db_session.add(new_student)
    db_session.commit()

    assert new_student.id is not None


def test_update_student(db_session):
    student = db_session.query(Student).filter(Student.name == "John Doe").first()
    student.name = "Jane Doe"
    db_session.commit()

    updated_student = db_session.query(Student).filter(Student.id == student.id).first()
    assert updated_student.name == "Jane Doe"


def test_delete_student(db_session):
    student = db_session.query(Student).filter(Student.name == "Jane Doe").first()
    db_session.delete(student)
    db_session.commit()

    deleted_student = db_session.query(Student).filter(Student.id == student.id).first()
    assert deleted_student is None