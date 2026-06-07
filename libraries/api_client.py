import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get_alarm_list(self, alarm_id):
        response = self.session.get(
            f"{self.base_url}/posts/{alarm_id}"
        )
        return response

    def close(self):
        self.session.close()