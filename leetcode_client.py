import json
import time
import sys
import requests
from pathlib import Path
from config import CACHE_DIR

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


GRAPHQL_URL = "https://leetcode.com/graphql"
ALL_PROBLEMS_URL = "https://leetcode.com/api/problems/all/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
}

DIFFICULTY_MAP = {1: "Easy", 2: "Medium", 3: "Hard"}

def fetch_all_problems(use_cache: bool = True):
    """Fetches the directory of all LeetCode problems, filtering for free/accessible ones."""
    cache_path = CACHE_DIR / "all_problems.json"
    if use_cache and cache_path.exists():
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    print("[*] Fetching all problems catalog from LeetCode...")
    resp = requests.get(ALL_PROBLEMS_URL, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    raw_data = resp.json()

    problems = []
    for item in raw_data.get("stat_status_pairs", []):
        stat = item.get("stat", {})
        is_paid = item.get("paid_only", False)
        if is_paid:
            continue

        q_id = stat.get("frontend_question_id", stat.get("question_id"))
        try:
            q_id_int = int(q_id)
        except (ValueError, TypeError):
            continue

        total_acs = stat.get("total_acs", 0)
        total_submitted = stat.get("total_submitted", 0)
        acc_rate = (total_acs / total_submitted * 100) if total_submitted > 0 else 0.0

        diff_level = item.get("difficulty", {}).get("level", 1)

        problems.append({
            "id": q_id_int,
            "title": stat.get("question__title", ""),
            "slug": stat.get("question__title_slug", ""),
            "difficulty": DIFFICULTY_MAP.get(diff_level, "Easy"),
            "total_acs": total_acs,
            "total_submitted": total_submitted,
            "acceptance_rate": round(acc_rate, 2),
        })

    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(problems, f, indent=2)

    print(f"[+] Loaded {len(problems)} free problems successfully.")
    return problems

def get_target_problems(strategy: str = "sequential", limit: int = 1000):
    """Sorts and returns target problems based on chosen strategy."""
    problems = fetch_all_problems()
    
    if strategy == "sequential":
        problems.sort(key=lambda x: x["id"])
    elif strategy == "high_acceptance":
        problems.sort(key=lambda x: x["acceptance_rate"], reverse=True)
    elif strategy == "low_acceptance":
        problems.sort(key=lambda x: x["acceptance_rate"])
    elif strategy == "popular":
        problems.sort(key=lambda x: x["total_submitted"], reverse=True)
    else:
        problems.sort(key=lambda x: x["id"])

    return problems[:limit]

def fetch_question_details(title_slug: str, use_cache: bool = True):
    """Fetches problem description, topic tags, and code snippets via GraphQL."""
    q_cache_dir = CACHE_DIR / "questions"
    q_cache_dir.mkdir(exist_ok=True)
    cache_path = q_cache_dir / f"{title_slug}.json"

    if use_cache and cache_path.exists():
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        content
        difficulty
        topicTags { name }
        codeSnippets {
          lang
          langSlug
          code
        }
      }
    }
    """

    payload = {"query": query, "variables": {"titleSlug": title_slug}}
    resp = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    q_data = data.get("data", {}).get("question")
    if not q_data:
        raise ValueError(f"No details found for slug: {title_slug}")

    details = {
        "id": q_data.get("questionFrontendId"),
        "title": q_data.get("title"),
        "difficulty": q_data.get("difficulty"),
        "content": q_data.get("content", ""),
        "topicTags": [t["name"] for t in q_data.get("topicTags", [])],
        "snippets": {
            s["langSlug"]: s["code"]
            for s in q_data.get("codeSnippets", []) or []
        }
    }

    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(details, f, indent=2)

    return details
