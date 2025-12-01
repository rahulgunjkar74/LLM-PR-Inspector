from github_client import fetch_pr_diff, post_comment_to_pr, post_inline_comment
from ai_reviewer import review_code_patch
from diff_utils import extract_changed_lines
from review_formatter import format_comment
from config import MODEL, GROQ_API_KEY
from groq import Groq

client = Groq(api_key=GROQ_API_KEY)


def compute_pr_stats(diffs):
    """Compute simple stats: number of files, lines added/removed."""
    num_files = len(diffs)
    added = 0
    removed = 0

    for diff in diffs:
        patch = diff["patch"] or ""
        for line in patch.split("\n"):
            if line.startswith("+") and not line.startswith("+++"):
                added += 1
            elif line.startswith("-") and not line.startswith("---"):
                removed += 1

    return num_files, added, removed


def run(repo_name, pr_number):
    print(f"Fetching PR #{pr_number} from {repo_name}...")

    diffs, pr = fetch_pr_diff(repo_name, pr_number)
    num_files, added, removed = compute_pr_stats(diffs)

    print(f"Found {num_files} changed files.")
    print(f"Lines added: {added}, Lines removed: {removed}\n")

    for diff in diffs:
        filename = diff["filename"]
        patch = diff["patch"]

        print(f"🔍 Reviewing file: {filename}")

        # --------- MAIN FULL REVIEW ---------
        full_review = review_code_patch(filename, patch)
        formatted_review = format_comment(full_review, filename)
        post_comment_to_pr(pr, formatted_review)

        # --------- INLINE REVIEW COMMENTS ---------
        changed_lines = extract_changed_lines(patch)
        print(f"💬 Inline comments for {len(changed_lines)} added lines...")

        for position, line_text in changed_lines:

            inline_prompt = f"""
You are an AI GitHub reviewer.

Analyze ONLY the following changed line from file **{filename}**:


Provide:
- A short suggestion (1–2 lines)
- ONLY if improvement is needed
- If the line is fine, respond with exactly: "OK — No improvements needed."
"""

            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": inline_prompt}],
                temperature=0.2
            )

            inline_review = response.choices[0].message.content.strip()

            # Skip useless comments
            if inline_review.lower() in [
                "ok — no improvements needed.",
                "ok — no improvements needed",
                "ok—no improvements needed",
                "ok - no improvements needed",
                "ok",
                "no issues found",
                "no issues detected",
            ]:
                continue

            post_inline_comment(pr, inline_review, filename, position)

    # --------- PR SUMMARY COMMENT ---------
    summary_body = f"""
## 📊 LLM-PR-Inspector — PR Summary

- 🗂 **Files changed:** {num_files}
- ➕ **Lines added:** {added}
- ➖ **Lines removed:** {removed}

Detailed reviews for each file have been posted above, including:
- Potential bugs
- Code smells
- Optimization suggestions
- Security observations
- Risk score & final decision

_🤖 Summary generated automatically by LLM-PR-Inspector._
"""

    post_comment_to_pr(pr, summary_body)

    print("\n🎉 Review completed successfully!")


if __name__ == "__main__":
    repo = input("Enter repository (e.g., username/repo): ")
    pr_number = int(input("Enter PR number: "))
    run(repo, pr_number)
