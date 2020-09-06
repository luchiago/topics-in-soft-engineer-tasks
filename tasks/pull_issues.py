import json

import requests
from tqdm import tqdm

from settings.settings import (AUTH, BASE_URL, GITHUB_OAUTH_TOKEN,
                               ISSUES_PER_PAGE, REPO, TOTAL_ISSUES)

PATH = f"/repos/{REPO}/issues?state=all&per_page={ISSUES_PER_PAGE}"
URL = f"{BASE_URL}{PATH}"
FILENAME = "issues.json"


def pull_issues():
    response = []
    number_of_pages = (int(TOTAL_ISSUES) // int(ISSUES_PER_PAGE)) + 2
    for page in tqdm(range(1, number_of_pages)):
        page_number = f"&page={page}"
        url = URL + page_number
        response += requests.get(url, headers=AUTH).json()
    save_file(response)
    return response


def save_file(list_of_issues):
    with open(FILENAME, "w") as file:
        json.dump(list_of_issues, file)


def read_from_file():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    pull_issues()
