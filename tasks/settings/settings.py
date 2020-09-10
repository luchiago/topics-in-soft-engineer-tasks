from dotenv import load_dotenv

load_dotenv()

import os

GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN")
AUTH = {"Authorization": f"token {GITHUB_OAUTH_TOKEN}"}
BASE_URL = os.getenv("BASE_URL")
PER_PAGE = os.getenv("PER_PAGE")
TOTAL_ISSUES = os.getenv("TOTAL_ISSUES")
TOTAL_COMMITS = os.getenv("TOTAL_COMMITS")
REPO = os.getenv("REPO")
RATE_LIMIT_PER_HOUR = 5000
RATE_LIMIT_STATUS_CODE = 403
TIME_TO_WAIT = 3605
