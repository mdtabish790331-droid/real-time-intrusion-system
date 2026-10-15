
from pathlib import Path
import csv

from fastapi import FastAPI

# Project ke folders ka path
BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "logs" / "intrusion_log.csv"
SNAPSHOT_FOLDER = BASE_DIR / "snapshots"

# FastAPI application create karo
app = FastAPI(
    title="Intrusion Detection API",
    description="API for our YOLOv8 intrusion detection project",
    version="1.0.0"
)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Intrusion Detection API is running!",
        "docs": "/docs"
    }


# Health endpoint
@app.get("/api/health")
def health():
    return {
        "api_status": "running",
        "log_file_exists": LOG_FILE.exists(),
        "snapshot_folder_exists": SNAPSHOT_FOLDER.exists()
    }


# Intrusion events endpoint
@app.get("/api/events")
def get_events():
    if not LOG_FILE.exists():
        return {"total": 0, "events": []}

    with open(LOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        events = list(reader)

    return {
        "total": len(events),
        "events": events
    }


# Saved snapshots endpoint
@app.get("/api/snapshots")
def get_snapshots():
    if not SNAPSHOT_FOLDER.exists():
        return {"total": 0, "snapshots": []}

    photos = sorted(
        SNAPSHOT_FOLDER.glob("*.jpg"),
        key=lambda path: path.stat().st_mtime,
        reverse=True
    )

    return {
        "total": len(photos),
        "snapshots": [photo.name for photo in photos]
    }
