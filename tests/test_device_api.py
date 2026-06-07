import pytest
from libraries.device_api import get_post, POST_ID


@pytest.mark.parametrize("post_id", [1,2,3,6])
def test_get_post(post_id, api_client):

    response = get_post(post_id)
    assert response.status_code == 200

    response = api_client.get_alarm_list(post_id)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == post_id

def test_config_loaded(config):
    assert "environment" in config
    assert config["environment"] == "test"

def test_api_client_created(api_client):
    assert api_client.base_url == "https://jsonplaceholder.typicode.com"

#def test_api_client_created_dummy(api_client):
#    pass
#    #assert api_client.base_url == "https://jsonplaceholder.typicode.com"

def test_get_post_non_200(monkeypatch):
    """Force requests.get to return a non-200 response so the warning branch runs."""
    class DummyResponse:
        def __init__(self):
            self.status_code = 500
        def json(self):
            return {"error": "server"}

    def fake_get(url):
        return DummyResponse()

    monkeypatch.setattr('libraries.device_api.requests.get', fake_get)

    from libraries.device_api import get_post
    resp = get_post(999)
    assert resp.status_code == 500