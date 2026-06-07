import pytest
import requests
import json
from pathlib import Path
from libraries.api_client import ApiClient 

@pytest.fixture(scope="session")
def config():
    config_path = Path("configs") / "config.json"

    with open(config_path, "r") as file:
        return json.load(file)

@pytest.fixture(scope="session")    
def api_client(config):
    environment = config["environment"]
    base_url = config[environment]["base_url"]
    client = ApiClient(base_url)
    
    #session = requests.Session()
    #session.base_url = base_url 

    yield client 
    

    client.close()
