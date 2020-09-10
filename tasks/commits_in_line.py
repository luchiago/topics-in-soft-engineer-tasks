from github_api import read_from_file
from settings.settings import REPO, TOTAL_COMMITS
from tqdm import tqdm


def amount_with_comment(commits):
    count = 0
    for commit in tqdm(commits):
        if commit["commit"]["comment_count"] > 0:
            count += 1
    return count


def get_percent(amount):
    percent = (amount / float(TOTAL_COMMITS)) * 100
    return round(percent, 2)


if __name__ == "__main__":
    commits = read_from_file("commits.json")
    commits = amount_with_comment(commits)
    percent = get_percent(commits)
    print(f"Repository: {REPO}")
    print(f"Total of commits: {TOTAL_COMMITS}")
    print(f"Percent of commits with in-line comments (approximately): {percent}%")
