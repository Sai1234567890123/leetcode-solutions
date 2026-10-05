import os
import sys
import json
import time
import argparse
from datetime import datetime
from pathlib import Path

# Fix Windows console UTF-8 output
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


from config import (
    SOLUTIONS_DIR,
    PROGRESS_FILE,
    README_FILE,
    BATCH_LIMIT,
    SELECTION_STRATEGY,
    TARGET_LANGUAGE,
    GEMINI_API_KEY
)
from leetcode_client import get_target_problems, fetch_question_details
from solver import solve_problem
from git_pusher import commit_and_push

EXT_MAP = {
    "python3": "py",
    "python": "py",
    "cpp": "cpp",
    "java": "java",
    "javascript": "js",
    "typescript": "ts",
    "golang": "go",
    "rust": "rs",
}

def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_progress(progress: dict):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

def update_root_readme(progress: dict, total_target: int):
    """Generates a rich, polished GitHub README.md tracking all solved problems."""
    solved_list = sorted(progress.values(), key=lambda x: int(x["id"]))
    total_solved = len(solved_list)

    easy_count = sum(1 for p in solved_list if p.get("difficulty") == "Easy")
    medium_count = sum(1 for p in solved_list if p.get("difficulty") == "Medium")
    hard_count = sum(1 for p in solved_list if p.get("difficulty") == "Hard")

    pct = round((total_solved / total_target * 100), 1) if total_target > 0 else 0.0

    lines = [
        "# 🚀 LeetCode Solutions Automated Archive",
        "",
        f"Automated pipeline powered by Google Gemini AI and Antigravity batch runner.",
        "",
        "## 📊 Progress & Statistics",
        "",
        f"- **Total Solved:** `{total_solved} / {total_target}` ({pct}%)",
        f"- **🟢 Easy:** `{easy_count}`",
        f"- **🟡 Medium:** `{medium_count}`",
        f"- **🔴 Hard:** `{hard_count}`",
        f"- **Last Updated:** `{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}`",
        "",
        "---",
        "",
        "## 📑 Solved Problems Index",
        "",
        "| # | Title | Difficulty | Solution | Topics |",
        "|---|---|:---:|:---:|---|",
    ]

    for item in solved_list:
        q_id = item["id"]
        title = item["title"]
        slug = item["slug"]
        diff = item.get("difficulty", "Medium")
        sol_rel_path = item.get("relative_dir", f"solutions/{int(q_id):04d}-{slug}")
        ext = EXT_MAP.get(item.get("language", "python3"), "py")
        code_file = f"{sol_rel_path}/solution.{ext}".replace("\\", "/")
        readme_file = f"{sol_rel_path}/README.md".replace("\\", "/")
        
        diff_badge = f"`{diff}`"
        if diff == "Easy":
            diff_badge = f"🟢 **Easy**"
        elif diff == "Medium":
            diff_badge = f"🟡 **Medium**"
        elif diff == "Hard":
            diff_badge = f"🔴 **Hard**"

        topics = ", ".join([f"`{t}`" for t in item.get("tags", [])[:3]])
        lc_link = f"https://leetcode.com/problems/{slug}/"
        title_link = f"[{title}]({lc_link})"
        sol_links = f"[{ext.upper()}]({code_file}) • [Notes]({readme_file})"

        lines.append(f"| {q_id} | {title_link} | {diff_badge} | {sol_links} | {topics} |")

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

def run_batch(limit: int = None, strategy: str = None, single_slug: str = None, auto_push: bool = True):
    limit = limit or BATCH_LIMIT
    strategy = strategy or SELECTION_STRATEGY

    if not GEMINI_API_KEY:
        print("\n" + "=" * 60)
        print("❌ ERROR: GEMINI_API_KEY is not configured in .env!")
        print("Please add your Gemini API key to .env:")
        print("   GEMINI_API_KEY=AIzaSy...")
        print("You can get a free key instantly at https://aistudio.google.com/app/apikey")
        print("=" * 60 + "\n")
        return

    progress = load_progress()

    if single_slug:
        print(f"[*] Solving single problem: {single_slug}")
        details = fetch_question_details(single_slug)
        target_problems = [{
            "id": int(details["id"]),
            "title": details["title"],
            "slug": single_slug,
            "difficulty": details["difficulty"],
        }]
    else:
        print(f"[*] Target Strategy: '{strategy}' | Target Limit: {limit}")
        target_problems = get_target_problems(strategy=strategy, limit=limit)

    total_target = len(target_problems)
    print(f"[*] Total target batch size: {total_target} problems.")
    print(f"[*] Already solved: {len(progress)} problems.")

    ext = EXT_MAP.get(TARGET_LANGUAGE, "py")

    for idx, prob in enumerate(target_problems, 1):
        q_id = str(prob["id"])
        slug = prob["slug"]
        title = prob["title"]
        diff = prob.get("difficulty", "Unknown")

        if q_id in progress:
            continue

        print(f"\n[{idx}/{total_target}] Solving #{q_id}: {title} [{diff}]...")

        try:
            # 1. Fetch Question details
            details = fetch_question_details(slug)

            # 2. Call Gemini Solver
            solution_data = solve_problem(details, language=TARGET_LANGUAGE)

            # 3. Create directory
            prob_dir_name = f"{int(q_id):04d}-{slug}"
            prob_dir = SOLUTIONS_DIR / prob_dir_name
            prob_dir.mkdir(exist_ok=True)

            # 4. Save Solution Code
            code_path = prob_dir / f"solution.{ext}"
            with open(code_path, "w", encoding="utf-8") as f:
                f.write(solution_data["code"] + "\n")

            # 5. Save Problem Documentation
            doc_path = prob_dir / "README.md"
            doc_content = f"""# {int(q_id):04d}. {title}

**Difficulty:** {diff}  
**LeetCode Link:** [https://leetcode.com/problems/{slug}/](https://leetcode.com/problems/{slug}/)  
**Topics:** {', '.join(details.get('topicTags', []))}

---

## 📝 Problem Statement

{solution_data['description']}

---

## 💡 Solution & Approach

{solution_data['explanation']}

---

## 💻 Implementation ({TARGET_LANGUAGE})

```{ext}
{solution_data['code']}
```
"""
            with open(doc_path, "w", encoding="utf-8") as f:
                f.write(doc_content)

            # 6. Record progress
            progress[q_id] = {
                "id": q_id,
                "title": title,
                "slug": slug,
                "difficulty": diff,
                "language": TARGET_LANGUAGE,
                "relative_dir": f"solutions/{prob_dir_name}",
                "tags": details.get("topicTags", []),
                "solved_at": datetime.utcnow().isoformat(),
            }
            save_progress(progress)

            # 7. Update Root README
            update_root_readme(progress, total_target)

            # 8. Git Commit & Push
            ok, msg = commit_and_push(int(q_id), title, diff, auto_push=auto_push)
            print(f"[+] #{q_id} saved! Git status: {msg}")

            # 9. Rate limiting buffer (1.5 seconds)
            time.sleep(1.5)

        except Exception as e:
            print(f"[!] Error processing #{q_id} ({slug}): {e}")
            time.sleep(3.0)
            continue

    print("\n" + "=" * 60)
    print(f"🎉 Batch execution completed! Total solved: {len(progress)}")
    print("=" * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated LeetCode Batch Solver")
    parser.add_argument("--limit", type=int, default=None, help="Number of problems to solve")
    parser.add_argument("--strategy", type=str, default=None, choices=["sequential", "popular", "high_acceptance", "low_acceptance"], help="Problem selection strategy")
    parser.add_argument("--single", type=str, default=None, help="Solve a single problem slug (e.g. two-sum)")
    parser.add_argument("--no-push", action="store_true", help="Disable git push")

    args = parser.parse_args()
    run_batch(
        limit=args.limit,
        strategy=args.strategy,
        single_slug=args.single,
        auto_push=not args.no_push
    )
