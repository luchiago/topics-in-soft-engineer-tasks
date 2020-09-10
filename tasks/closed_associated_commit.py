from github_api import get_closed_issues, make_request, read_from_file
from requests import get
from settings.settings import (AUTH, GITHUB_OAUTH_TOKEN, RATE_LIMIT_PER_HOUR,
                               REPO, TIME_TO_WAIT, TOTAL_ISSUES)
from tqdm import tqdm


def has_commit(event):
    commits_list = list(map(lambda e: e["commit_id"], event))
    return any(commits_list)


def pull_event(issue):
    return make_request(issue["events_url"])


def get_amount_of_issues(issues):
    qte = 0
    for issue in tqdm(issues):
        event = pull_event(issue)
        if has_commit(event):
            qte += 1
    return qte


def get_percent(qte_commit_associated):
    percent = (qte_commit_associated / float(TOTAL_ISSUES)) * 100
    return round(percent, 2)


if __name__ == "__main__":
    issues = read_from_file("issues.json")
    issues = get_closed_issues(issues)
    qte_commit_associated = get_amount_of_issues(issues)
    percent = get_percent(qte_commit_associated)
    print(f"Repository: {REPO}")
    print(f"Total of issues (issues + PR's): {TOTAL_ISSUES}")
    print(f"Amount of issues with commit associated: {qte_commit_associated}")
    print(f"Percent of closed issues associated to commits: {percent}%")
