from github import Github
from config import GITHUB_TOKEN

g = Github(GITHUB_TOKEN)

def fetch_pr_diff(repo_name, pr_number):
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    files = pr.get_files()

    diffs = []
    for f in files:
        diffs.append({
            "filename": f.filename,
            "patch": f.patch
        })

    return diffs, pr


def post_comment_to_pr(pr, body):
    pr.create_issue_comment(body)


def post_inline_comment(pr, body, filename, position):
    latest_commit = pr.get_commits().reversed[0]
    commit_sha = latest_commit.sha

    pr.create_review_comment(
        body=body,
        commit=commit_sha,
        path=filename,
        line=position
    )

