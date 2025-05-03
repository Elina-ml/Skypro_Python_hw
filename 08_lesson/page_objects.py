import requests

class ProjectsAPI:
    BASE_URL = "https://ru.yougile.com/api-v2/projects"

    def __init__(self, token=None):
        self.token = token

    def _get_headers(self):
        headers = {
            "Content-Type": "application/json"
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def create_project(self, project_data):
        response = requests.post(self.BASE_URL, json=project_data, headers=self._get_headers())
        return response

    def update_project(self, project_id, project_data):
        response = requests.put(f"{self.BASE_URL}/{project_id}", json=project_data, headers=self._get_headers())
        return response

    def get_project(self, project_id):
        response = requests.get(f"{self.BASE_URL}/{project_id}", headers=self._get_headers())
        return response