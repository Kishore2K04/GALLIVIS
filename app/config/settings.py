from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

PROJECT_NAME = "GALLIVIS"
PROJECT_VERSION = "0.1.0"

APP_TITLE = "GALLIVIS - Gallstone Intelligent Vision System"

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"
REPORT_DIR = BASE_DIR / "reports"