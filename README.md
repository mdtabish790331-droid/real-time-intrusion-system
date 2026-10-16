Real-Time Intrusion Detection System
A Python-based computer vision project that detects people using YOLOv8, checks whether a person enters a restricted zone, triggers a sound alert, saves snapshots, and records intrusion events through a FastAPI backend.
Features
- Person detection: Uses the pretrained YOLOv8 nano model.
- Restricted-zone monitoring: Marks people green outside the zone and red when the intrusion condition is met.
- Sound alarm: Plays a short beep when a new intrusion is detected on Windows.
- Snapshot saving: Saves a JPG image for each newly detected intrusion event.
- Event logging: Records the date, time, event type, and snapshot filename in a CSV file.
- FastAPI backend: Exposes endpoints for health status, intrusion events, and saved snapshot filenames.
- Interactive API docs: Lets you test endpoints through Swagger UI.
Technology Stack
- Python
- OpenCV
- Ultralytics YOLOv8
- NumPy
- FastAPI
- Uvicorn
- CSV for event logging
- winsound for Windows sound alerts
Project Structure
real-time-intrusion-system/
├── api.py
├── 06_intrusion_alert.py
├── .gitignore
├── snapshots/          # Saved JPG snapshots
└── logs/
    └── intrusion_log.csv
Other learning or test scripts may also exist in the repository. The snapshots/ and logs/ folders are used by the detector.
Requirements
- Windows PC with a working webcam
- Python version supported by the installed dependencies
- Internet connection for the initial YOLO model download if yolov8n.pt is not already cached
Installation
1. Clone the repository
Replace YOUR-USERNAME with your GitHub username.
git clone https://github.com/YOUR-USERNAME/real-time-intrusion-system.git
cd real-time-intrusion-system
2. Create and activate a virtual environment
Run these commands in PowerShell:
python -m venv venv
.\venv\Scripts\Activate.ps1
If PowerShell blocks activation, use Command Prompt instead:
venv\Scripts\activate.bat
3. Install dependencies
python -m pip install opencv-python numpy ultralytics fastapi "uvicorn[standard]"
Run the Intrusion Detector
python 06_intrusion_alert.py
1. The webcam window opens.
2. A yellow polygon marks the restricted zone.
3. A person outside the zone is shown with a green box.
4. When the person's bottom-center point enters the zone, the box turns red and an intrusion alert appears.
5. A beep plays, a snapshot is saved, and an event is added to logs/intrusion_log.csv.
6. Press q while the camera window is active to quit.
Run the FastAPI Backend
Open a second terminal in the project directory and run:
python -m uvicorn api:app --reload
Open these URLs in your browser:
Endpoint	Purpose
http://127.0.0.1:8000/	API home message
http://127.0.0.1:8000/api/health	Checks API status and whether the log/snapshot folders exist
http://127.0.0.1:8000/api/events	Reads intrusion events from the CSV log
http://127.0.0.1:8000/api/snapshots	Lists saved JPG snapshot filenames
http://127.0.0.1:8000/docs	Interactive Swagger API documentation


How It Works
1. OpenCV captures a frame from the webcam.
2. YOLOv8 detects objects and the code processes detections classified as people.
3. The bottom-center point of the person's bounding box is calculated.
4. OpenCV checks whether that point is inside the restricted polygon.
5. A newly detected intrusion triggers the sound, saves a snapshot, and appends a record to the CSV file.
Important Notes and Limitations
- The sound alarm uses Python's winsound, so it is Windows-specific.
- The restricted zone is based on the camera frame and may need adjustment for your camera position.
- Detection may produce false positives or miss people due to lighting, camera angle, distance, or occlusion.
- Events are stored in a CSV file rather than a database.
- The current FastAPI endpoints read logs and list snapshot filenames. They do not start or stop the webcam detector and do not stream live video.
Future Improvements
- Connect FastAPI to start, stop, and report the live detector's status.
- Build a browser dashboard with recent alerts and snapshot previews.
- Add person tracking and reduce false or repeated alerts.
- Move event storage from CSV to SQLite or PostgreSQL.
- Add configurable restricted zones and camera settings.
License
No license has been specified yet. Add a license file if you want to define how others may use, modify, or distribute this project.
Built as a learning project using Python, computer vision, object detection, and API development.
