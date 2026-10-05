import os
import re
import html
import json
from pathlib import Path
from google import genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL, GCP_PROJECT_ID, GCP_LOCATION, BASE_DIR

def clean_html(raw_html: str) -> str:
    """Converts basic LeetCode HTML content to clean Markdown."""
    if not raw_html:
        return ""
    text = raw_html
    # Unescape HTML entities
    text = html.unescape(text)
    # Convert code blocks
    text = re.sub(r'<pre>(.*?)</pre>', r'```\n\1\n```', text, flags=re.DOTALL)
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
    # Convert strong / bold
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', text)
    # Convert emphasis / italics
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
    # Convert list items
    text = re.sub(r'<li>(.*?)</li>', r'- \1\n', text)
    # Strip remaining tags
    text = re.sub(r'<[^>]+>', '', text)
    # Fix excess newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

SYSTEM_INSTRUCTION = """You are an elite competitive programmer and Principal Engineer who conducts coding interviews at Google and Meta.
Your mission is to solve LeetCode problems with 100% optimal time and space complexity AND provide real interview prep intelligence.

Requirements:
1. Deliver clean, production-grade, readable code in the requested programming language adhering strictly to the starter method signature.
2. Include clear inline comments explaining non-trivial logic.
3. Provide a structured explanation covering:
   - Intuition & Thought Process
   - Step-by-Step Approach
   - Complexity Analysis (Time Complexity & Space Complexity with Big-O notation)
   - Common Pitfalls / Mistakes candidates make in interviews
   - Real Interview Follow-Up Questions (e.g. handling streaming data, memory constraints, scale, duplicates, concurrency) and how to answer them!

Always output your response in the following exact format:

---CODE_START---
<put only the code here, without markdown codeblock backticks>
---CODE_END---

---EXPLANATION_START---
<put the markdown explanation here, including intuition, complexity analysis, common pitfalls, and interview follow-up questions & answers>
---EXPLANATION_END---
"""


def find_service_account_file() -> str:
    """Auto-detects any downloaded Google Cloud Service Account JSON file."""
    search_dirs = [
        Path.home() / "Downloads",
        BASE_DIR,
    ]
    for d in search_dirs:
        if not d.exists():
            continue
        for f in d.glob("*.json"):
            try:
                with open(f, "r", encoding="utf-8") as jf:
                    data = json.load(jf)
                    if data.get("type") == "service_account":
                        return str(f)
            except Exception:
                continue
    return None

def solve_problem(problem_details: dict, language: str = "python3") -> dict:
    """Uses Vertex AI powered by Google Cloud credits to solve the problem and generate solution code and documentation."""
    # Use Vertex AI with authenticated Google Cloud Application Default Credentials (ADC)
    client = genai.Client(
        vertexai=True,
        project=GCP_PROJECT_ID,
        location=GCP_LOCATION
    )

    title = problem_details["title"]
    diff = problem_details["difficulty"]
    q_id = problem_details["id"]
    description = clean_html(problem_details.get("content", ""))
    starter_code = problem_details.get("snippets", {}).get(language, "")


    prompt = f"""Problem #{q_id}: {title}
Difficulty: {diff}
Target Language: {language}

Problem Description:
{description}

Starter Code Snippet:
```
{starter_code}
```

Solve this problem with the most optimal time and space complexity.
Make sure the solution passes all edge cases and adheres to the starter signature.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.2,
        ),
    )

    output = response.text or ""

    # Parse CODE
    code_match = re.search(r'---CODE_START---\s*(.*?)\s*---CODE_END---', output, re.DOTALL)
    if code_match:
        code = code_match.group(1).strip()
    else:
        # Fallback to extracting from code blocks
        blocks = re.findall(r'```(?:python|python3|cpp|java)?\s*(.*?)\s*```', output, re.DOTALL)
        code = blocks[0].strip() if blocks else output.strip()

    # Parse EXPLANATION
    expl_match = re.search(r'---EXPLANATION_START---\s*(.*?)\s*---EXPLANATION_END---', output, re.DOTALL)
    if expl_match:
        explanation = expl_match.group(1).strip()
    else:
        explanation = "Detailed explanation not extracted."

    return {
        "id": q_id,
        "title": title,
        "difficulty": diff,
        "language": language,
        "code": code,
        "explanation": explanation,
        "description": description,
        "tags": problem_details.get("topicTags", []),
    }
