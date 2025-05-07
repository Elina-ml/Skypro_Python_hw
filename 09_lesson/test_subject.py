import pytest
from sqlalchemy import create_engine
from sub_page import SubjectPage


db_connection_string = r"sqlite:///C:\Users\Home\Desktop\my_db"
db = create_engine(db_connection_string)


@pytest.fixture
def db_connection():
    connection = db.connect()
    transaction = connection.begin()
    yield connection, transaction
    transaction.rollback()
    connection.close()


def test_create_subject(db_connection):
    connection, transaction = db_connection
    subject_page = SubjectPage(connection)

    count_before = subject_page.count_subjects()
    subject_page.insert_subject("Applied Math II")
    count_after = subject_page.count_subjects()

    assert count_after == count_before + 1

    result = subject_page.get_subject("Applied Math II")
    assert result.fetchone() is not None

def test_update_subject(db_connection):
    connection, transaction = db_connection
    subject_page = SubjectPage(connection)
    subject_page.insert_subject("Economics+")
    subject_page.update_subject("Economics+", "Economics Extra")

    result = subject_page.get_subject("Economics Extra")
    assert result.fetchone() is not None

def test_delete_subject(db_connection):
    connection, transaction = db_connection
    subject_page = SubjectPage(connection)
    subject_page.insert_subject("Economics+")
    subject_page.delete_subject("Economics+")

    result = subject_page.get_subject("Economics+")
    assert result.fetchone() is None
