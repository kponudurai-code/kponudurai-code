import pytest
from libraries.device_api import get_post, POST_ID

@pytest.mark.parametrize("post_id", [1,2,3,1.5,6])
def test_get_post(post_id):
    
    response = get_post(post_id)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == post_id