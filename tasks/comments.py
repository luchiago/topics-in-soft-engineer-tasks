from github_api import read_from_file
from settings.settings import REPO, TOTAL_ISSUES
from tqdm import tqdm


def get_average(num_of_comments):
    return num_of_comments / int(TOTAL_ISSUES)


def amount_of_comments(issues):
    sum = 0
    for issue in tqdm(issues):
        sum += issue["comments"]
    return sum


if __name__ == "__main__":
    issues = read_from_file("issues.json")
    num_of_comments = amount_of_comments(issues)
    average = get_average(num_of_comments)
    print(f"Repository: {REPO}")
    print(f"Total of issues (issues + PR's): {TOTAL_ISSUES}")
    print(f"Total of comments (issues + PR's): {num_of_comments}")
    print(f"Average of comments (approximately): {average}")
