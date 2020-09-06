import os

from dotenv import load_dotenv

load_dotenv()

GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN")
BASE_URL = os.getenv("BASE_URL")
