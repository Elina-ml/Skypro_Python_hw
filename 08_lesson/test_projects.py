import pytest
from page_objects import ProjectsAPI

TOKEN = "H6HngIA816fpIhY7tBvWx/it3YbVvEt/33Sk8afA39MCR9a"
projects_api = ProjectsAPI(token=TOKEN)

@pytest.fixture(scope="module")
def setup_project():
    project_data = {"name": "Test Project", "description": "This is a test project."}
    response = projects_api.create_project(project_data)
    yield response.json()

def test_create_project_positive():
    project_data = {"name": "New Project", "description": "This is a new project."}
    response = projects_api.create_project(project_data)

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative():
    invalid_data = {"name": ""}
    response = projects_api.create_project(invalid_data)

    assert response.status_code == 400


def test_update_project_positive(setup_project):
    project_id = setup_project["id"]
    updated_data = {"name": "Updated Project", "description": "This is an updated project."}

    response = projects_api.update_project(project_id, updated_data)

    assert response.status_code == 200

    get_response = projects_api.get_project(project_id)
    assert get_response.json()["name"] == updated_data["name"]


def test_update_project_negative():
    invalid_id = 566849
    updated_data = {"name": "Updated Project", "description": "This is an updated project."}

    response = projects_api.update_project(invalid_id, updated_data)

    assert response.status_code == 404


def test_get_project_positive(setup_project):
    project_id = setup_project["id"]

    response = projects_api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative():
    invalid_id = 868685

    response = projects_api.get_project(invalid_id)

    assert response.status_code == 404