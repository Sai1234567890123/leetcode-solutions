import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env if present
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# API Keys & LLM Config
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()

# GitHub & Git Config
GITHUB_REPO_URL = os.getenv("GITHUB_REPO_URL", "").strip()
GIT_USER_NAME = os.getenv("GIT_USER_NAME", "").strip()
GIT_USER_EMAIL = os.getenv("GIT_USER_EMAIL", "").strip()

# Target Language (python3, cpp, java, etc.)
TARGET_LANGUAGE = os.getenv("TARGET_LANGUAGE", "python3").strip().lower()

# Batch & Selection Settings
BATCH_LIMIT = int(os.getenv("BATCH_LIMIT", "1000"))
SELECTION_STRATEGY = os.getenv("SELECTION_STRATEGY", "sequential").strip().lower()

# Paths
SOLUTIONS_DIR = BASE_DIR / "solutions"
CACHE_DIR = BASE_DIR / "cache"
PROGRESS_FILE = BASE_DIR / "progress.json"
README_FILE = BASE_DIR / "README.md"

# Ensure directories exist
SOLUTIONS_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)
