from datetime import datetime

from github_api import get_closed_issues, read_from_file
from settings.settings import REPO, TOTAL_ISSUES
from tqdm import tqdm


def get_average(days):
    return days // int(TOTAL_ISSUES)


def get_delta_in_days(issue):
    cr_at = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%S%fZ")
    cl_at = datetime.strptime(issue["closed_at"], "%Y-%m-%dT%H:%M:%S%fZ")
    return (cl_at - cr_at).days


def get_amount_days(issues):
    days = 0
    for issue in tqdm(issues):
        days += get_delta_in_days(issue)
    return days


if __name__ == "__main__":
    issues = read_from_file("issues.json")
    issues = get_closed_issues(issues)
    amount_days = get_amount_days(issues)
    average = get_average(amount_days)
    print(f"Repository: {REPO}")
    print(f"Total of issues (issues + PR's): {TOTAL_ISSUES}")
    print(f"Total of delta times (issues + PR's): {amount_days}")
    print(f"Average of time, in days, to solve an issue (approximately): {average}")
