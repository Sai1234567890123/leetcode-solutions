import os
import sys
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"

def configure(api_key: str = None, repo_url: str = None, git_name: str = None, git_email: str = None, strategy: str = "sequential", limit: int = 1000):
    lines = []
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()

    config_map = {
        "GEMINI_API_KEY": api_key,
        "GITHUB_REPO_URL": repo_url,
        "GIT_USER_NAME": git_name,
        "GIT_USER_EMAIL": git_email,
        "SELECTION_STRATEGY": strategy,
        "BATCH_LIMIT": str(limit),
        "GEMINI_MODEL": "gemini-2.5-flash",
        "TARGET_LANGUAGE": "python3"
    }

    current = {}
    for line in lines:
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.strip().split("=", 1)
            current[k.strip()] = v.strip()

    for k, v in config_map.items():
        if v is not None:
            current[k] = v

    out_lines = [
        "# Auto-generated LeetCode Batch Runner configuration",
        f"GEMINI_API_KEY={current.get('GEMINI_API_KEY', '')}",
        f"GEMINI_MODEL={current.get('GEMINI_MODEL', 'gemini-2.5-flash')}",
        f"TARGET_LANGUAGE={current.get('TARGET_LANGUAGE', 'python3')}",
        f"BATCH_LIMIT={current.get('BATCH_LIMIT', '1000')}",
        f"SELECTION_STRATEGY={current.get('SELECTION_STRATEGY', 'sequential')}",
        f"GITHUB_REPO_URL={current.get('GITHUB_REPO_URL', '')}",
        f"GIT_USER_NAME={current.get('GIT_USER_NAME', '')}",
        f"GIT_USER_EMAIL={current.get('GIT_USER_EMAIL', '')}",
    ]

    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines) + "\n")

    print(f"[+] Saved configuration to {ENV_PATH}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Quick CLI setup: python setup_env.py <API_KEY> [REPO_URL] [GIT_NAME] [GIT_EMAIL]
        k = sys.argv[1] if len(sys.argv) > 1 else None
        r = sys.argv[2] if len(sys.argv) > 2 else None
        n = sys.argv[3] if len(sys.argv) > 3 else None
        e = sys.argv[4] if len(sys.argv) > 4 else None
        configure(api_key=k, repo_url=r, git_name=n, git_email=e)
    else:
        print("Usage: python setup_env.py <GEMINI_API_KEY> [REPO_URL] [GIT_USER_NAME] [GIT_USER_EMAIL]")
