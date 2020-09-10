import json
from time import sleep

from requests import get
from settings.settings import (AUTH, BASE_URL, GITHUB_OAUTH_TOKEN,
                               ISSUES_PER_PAGE, RATE_LIMIT_STATUS_CODE, REPO,
                               TIME_TO_WAIT, TOTAL_ISSUES)
from tqdm import tqdm

PATH = f"/repos/{REPO}/issues?state=all&per_page={ISSUES_PER_PAGE}"
URL = f"{BASE_URL}{PATH}"
FILENAME = "issues.json"


def make_request(url):
    while True:
        response = get(url, headers=AUTH)
        if response.status_code == RATE_LIMIT_STATUS_CODE:
            # Rate limit exceed
            print("The rate limit was execeed, you'll have to wait 1 hour to make requests again")
            sleep(TIME_TO_WAIT)
        else:
            return response.json()


def pull_issues():
    response = []
    number_of_pages = (int(TOTAL_ISSUES) // int(ISSUES_PER_PAGE)) + 2
    for page in tqdm(range(1, number_of_pages)):
        page_number = f"&page={page}"
        url = URL + page_number
        response += make_request(url)
    save_file(response)
    return response


def get_closed_issues(issues):
    closed_filter = lambda issue: issue["state"] == "closed"
    return list(filter(closed_filter, issues))


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
