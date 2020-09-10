import json
from time import sleep

from requests import get
from settings.settings import (AUTH, BASE_URL, GITHUB_OAUTH_TOKEN, PER_PAGE,
                               RATE_LIMIT_STATUS_CODE, REPO, TIME_TO_WAIT,
                               TOTAL_COMMITS, TOTAL_ISSUES)
from tqdm import tqdm

PATH = f"/repos/{REPO}/issues?state=all&per_page={PER_PAGE}"
PAGES = f"per_page={PER_PAGE}"
FILENAME = "issues.json"


def make_request(url):
    while True:
        response = get(url, headers=AUTH)
        if response.status_code == RATE_LIMIT_STATUS_CODE:
            # Rate limit exceed
            print(
                "The rate limit was exceeded, you'll have to wait 1 hour to make requests again"
            )
            sleep(TIME_TO_WAIT)
        else:
            return response.json()


def pull(type, path, total):
    response = []
    number_of_pages = (int(total) // int(PER_PAGE)) + 2
    for page in tqdm(range(1, number_of_pages)):
        page_number = f"&page={page}"
        url = f"{BASE_URL}{path}" + page_number
        response += make_request(url)
    save_file(response, f"{type}.json")


def pull_issues():
    path = f"/repos/{REPO}/issues?state=all&{PAGES}"
    pull("issues", path, TOTAL_ISSUES)


def pull_commits():
    path = f"/repos/{REPO}/commits?{PAGES}"
    pull("commits", path, TOTAL_COMMITS)


def get_closed_issues(issues):
    closed_filter = lambda issue: issue["state"] == "closed"
    return list(filter(closed_filter, issues))


def save_file(list_of_issues, filename):
    with open(filename, "w") as file:
        json.dump(list_of_issues, file)


def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    pull_issues()
    pull_commits()
