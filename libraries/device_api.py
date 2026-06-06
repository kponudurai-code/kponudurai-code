import requests
import json 
import logging 
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(LOG_DIR / "test.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)

'''
logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
'''

with open("configs/config.json", 'r') as f:
    config = json.load(f)

ENVIRONMENT = config["environment"]
BASE_URL = config[ENVIRONMENT]["base_url"]
POST_ID = config[ENVIRONMENT]["post_id"]

def get_post(post_id):

    print("get_post called.")
    
    logger.info(f"Getting post {post_id}")

    response = requests.get(f"{BASE_URL}/posts/{post_id}")

    if response.status_code == 200:
        logger.info(f"Status Code: {response.status_code}")
    else:
        logger.warning(f"Status Code: {response.status_code}")

    return response 
