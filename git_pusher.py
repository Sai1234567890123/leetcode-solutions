import subprocess
from pathlib import Path
from config import BASE_DIR, GITHUB_REPO_URL, GIT_USER_NAME, GIT_USER_EMAIL

def run_git(args: list[str]) -> tuple[int, str, str]:
    """Runs a git command in the repository directory."""
    result = subprocess.run(
        ["git"] + args,
        cwd=BASE_DIR,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def setup_git():
    """Ensures git user and remote are properly configured."""
    # Check or set user name
    code, stdout, _ = run_git(["config", "user.name"])
    if not stdout and GIT_USER_NAME:
        run_git(["config", "user.name", GIT_USER_NAME])
    
    # Check or set user email
    code, stdout, _ = run_git(["config", "user.email"])
    if not stdout and GIT_USER_EMAIL:
        run_git(["config", "user.email", GIT_USER_EMAIL])

    # Check remote origin
    if GITHUB_REPO_URL:
        code, stdout, _ = run_git(["remote", "get-url", "origin"])
        if code != 0:
            run_git(["remote", "add", "origin", GITHUB_REPO_URL])
            run_git(["branch", "-M", "main"])
        else:
            if stdout != GITHUB_REPO_URL:
                run_git(["remote", "set-url", "origin", GITHUB_REPO_URL])

def commit_and_push(problem_id: int, problem_title: str, difficulty: str, auto_push: bool = True):
    """Stages changes, creates a semantic commit, and pushes to remote."""
    setup_git()

    # Stage files
    run_git(["add", "solutions/", "README.md", "progress.json"])

    commit_msg = f"feat(leetcode): solve #{problem_id} - {problem_title} [{difficulty}]"
    code, stdout, stderr = run_git(["commit", "-m", commit_msg])
    
    if code != 0:
        if "nothing to commit" in stdout or "nothing to commit" in stderr:
            return True, "Nothing to commit."
        return False, f"Git commit failed: {stderr or stdout}"

    if auto_push and GITHUB_REPO_URL:
        # Check current branch
        _, branch, _ = run_git(["rev-parse", "--abbrev-ref", "HEAD"])
        if not branch:
            branch = "main"
        code, stdout, stderr = run_git(["push", "-u", "origin", branch])
        if code != 0:
            return False, f"Git push warning: {stderr or stdout} (Check GitHub PAT or repo access)"
        return True, "Committed and pushed successfully."

    return True, "Committed locally."
