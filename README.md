[README.html](https://github.com/user-attachments/files/33537788/README.html)
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Real-Time Intrusion Detection System | README</title>
  <style>
    :root {
      color-scheme: light;
      --bg: #f6f8fa;
      --surface: #ffffff;
      --text: #1f2328;
      --muted: #59636e;
      --border: #d1d9e0;
      --accent: #0969da;
      --code: #eef2f6;
      --green: #1a7f37;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font: 16px/1.65 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    .container { max-width: 980px; margin: 0 auto; padding: 32px 20px 56px; }
    header {
      padding: 36px 32px;
      border: 1px solid var(--border);
      border-radius: 18px;
      background: linear-gradient(135deg, #eaf3ff, #ffffff 65%);
      margin-bottom: 24px;
    }
    .eyebrow { color: var(--accent); font-weight: 700; text-transform: uppercase; letter-spacing: .08em; font-size: .78rem; }
    h1 { line-height: 1.2; margin: 10px 0 14px; font-size: clamp(2rem, 5vw, 3rem); }
    h2 { margin-top: 34px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
    h3 { margin-bottom: 8px; }
    p, li { color: var(--text); }
    .muted { color: var(--muted); }
    .badges { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 18px; }
    .badge { display: inline-block; border: 1px solid var(--border); border-radius: 999px; background: var(--surface); padding: 4px 10px; font-size: .82rem; font-weight: 600; }
    .card { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 20px 22px; margin: 14px 0; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
    .grid .card { margin: 0; }
    code { background: var(--code); border-radius: 5px; padding: 2px 6px; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: .92em; }
    pre { overflow-x: auto; padding: 16px; border-radius: 10px; background: #161b22; color: #e6edf3; }
    pre code { padding: 0; background: transparent; color: inherit; }
    a { color: var(--accent); }
    .note { border-left: 4px solid var(--accent); background: #eaf3ff; padding: 12px 16px; border-radius: 6px; }
    .warning { border-left: 4px solid #bf8700; background: #fff8c5; padding: 12px 16px; border-radius: 6px; }
    footer { margin-top: 40px; border-top: 1px solid var(--border); padding-top: 18px; color: var(--muted); font-size: .9rem; }
    @media (max-width: 600px) { .container { padding: 18px 12px 36px; } header { padding: 26px 20px; } }
  </style>
</head>
<body>
  <main class="container">
    <header>
      <div class="eyebrow">Computer Vision · Python Project</div>
      <h1>Real-Time Intrusion Detection System</h1>
      <p class="muted">Detect people with YOLOv8, monitor a configurable restricted zone, trigger a sound alert, save snapshots, and view event records through a FastAPI backend.</p>
      <div class="badges">
        <span class="badge">Python</span>
        <span class="badge">OpenCV</span>
        <span class="badge">YOLOv8</span>
        <span class="badge">FastAPI</span>
        <span class="badge">Uvicorn</span>
      </div>
    </header>

    <section class="card">
      <h2 style="margin-top:0;border:0">Project Overview</h2>
      <p>This project uses a webcam feed to detect people and checks whether a person's bottom-center point enters a polygon-shaped restricted zone. When a new intrusion is detected, the system displays a visual warning, plays a Windows beep, saves a snapshot, and records the event in a CSV file.</p>
      <p class="note"><strong>Current architecture:</strong> the intrusion detector runs as <code>06_intrusion_alert.py</code>. The FastAPI app in <code>api.py</code> exposes endpoints to inspect the CSV event log and saved snapshot filenames. The API does not currently start or stop the webcam detector.</p>
    </section>

    <h2>Features</h2>
    <div class="grid">
      <div class="card"><h3>Person Detection</h3><p class="muted">Uses the pretrained YOLOv8 nano model to detect people from a webcam feed.</p></div>
      <div class="card"><h3>Restricted Zone</h3><p class="muted">Checks a polygon zone and marks detected people green or red based on intrusion status.</p></div>
      <div class="card"><h3>Sound Alert</h3><p class="muted">Plays a short beep when a new intrusion event is detected on Windows.</p></div>
      <div class="card"><h3>Snapshots & Logs</h3><p class="muted">Saves JPG snapshots and appends event date, time, and filename to a CSV log.</p></div>
      <div class="card"><h3>FastAPI Endpoints</h3><p class="muted">Provides health, event-log, and snapshot-list endpoints plus interactive API docs.</p></div>
    </div>

    <h2>Technology Stack</h2>
    <ul>
      <li><strong>Python</strong> — application logic</li>
      <li><strong>OpenCV</strong> — webcam capture, drawing, and image saving</li>
      <li><strong>Ultralytics YOLOv8</strong> — person detection</li>
      <li><strong>NumPy</strong> — restricted-zone polygon coordinates</li>
      <li><strong>FastAPI + Uvicorn</strong> — REST API</li>
      <li><strong>CSV</strong> — lightweight intrusion event storage</li>
      <li><strong>winsound</strong> — Windows beep alert</li>
    </ul>

    <h2>Project Structure</h2>
    <pre><code>real-time-intrusion-system/
├── api.py
├── 06_intrusion_alert.py
├── .gitignore
├── snapshots/
│   └── (generated JPG files)
└── logs/
    └── intrusion_log.csv</code></pre>
    <p class="muted">Other learning or test scripts may also be present in your local repository. The <code>snapshots/</code> and <code>logs/</code> folders are generated/used by the detector.</p>

    <h2>Requirements</h2>
    <ul>
      <li>Windows PC with a working webcam</li>
      <li>Python 3.10 or another Python version supported by the installed dependencies</li>
      <li>Internet connection for the first YOLO model download, if the model weights are not already cached</li>
    </ul>

    <h2>Installation</h2>
    <p><strong>1. Clone the repository</strong></p>
    <pre><code>git clone https://github.com/YOUR-USERNAME/real-time-intrusion-system.git
cd real-time-intrusion-system</code></pre>
    <p>Replace <code>YOUR-USERNAME</code> with your GitHub username.</p>

    <p><strong>2. Create and activate a virtual environment (PowerShell)</strong></p>
    <pre><code>python -m venv venv
.\venv\Scripts\Activate.ps1</code></pre>
    <p>If PowerShell blocks activation, you can use Command Prompt activation instead: <code>venv\Scripts\activate.bat</code>.</p>

    <p><strong>3. Install dependencies</strong></p>
    <pre><code>python -m pip install opencv-python numpy ultralytics fastapi "uvicorn[standard]"</code></pre>

    <h2>Run the Intrusion Detector</h2>
    <pre><code>python 06_intrusion_alert.py</code></pre>
    <ol>
      <li>The webcam window opens.</li>
      <li>A yellow polygon marks the restricted zone.</li>
      <li>A person outside the zone is shown with a green box.</li>
      <li>When the person's bottom-center point enters the zone, the box turns red and an intrusion alert is displayed.</li>
      <li>A beep plays, a JPG snapshot is saved, and the event is added to <code>logs/intrusion_log.csv</code>.</li>
      <li>Press <code>q</code> while the camera window is active to quit.</li>
    </ol>

    <h2>Run the FastAPI Backend</h2>
    <p>Open a second terminal in the project directory and run:</p>
    <pre><code>python -m uvicorn api:app --reload</code></pre>
    <p>Then open these URLs in your browser:</p>
    <ul>
      <li><a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> — API home</li>
      <li><a href="http://127.0.0.1:8000/api/health">http://127.0.0.1:8000/api/health</a> — API and folder status</li>
      <li><a href="http://127.0.0.1:8000/api/events">http://127.0.0.1:8000/api/events</a> — intrusion records from CSV</li>
      <li><a href="http://127.0.0.1:8000/api/snapshots">http://127.0.0.1:8000/api/snapshots</a> — saved snapshot filenames</li>
      <li><a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a> — interactive Swagger documentation</li>
    </ul>

    <h2>How Intrusion Detection Works</h2>
    <ol>
      <li>OpenCV reads a frame from the webcam.</li>
      <li>YOLOv8 detects objects and the code keeps detections whose class is <code>person</code>.</li>
      <li>The bottom-center point of the person's bounding box is calculated.</li>
      <li>OpenCV's polygon test checks whether that point is inside the restricted zone.</li>
      <li>A new intrusion event triggers the sound, snapshot, and CSV log entry.</li>
    </ol>

    <h2>Important Notes & Limitations</h2>
    <div class="warning">
      <ul>
        <li>The sound alarm uses Python's <code>winsound</code>, so it is Windows-specific.</li>
        <li>The restricted zone is defined relative to the camera frame and may need adjustment for your camera position.</li>
        <li>Detection can produce false positives or miss people depending on lighting, camera angle, distance, and occlusion.</li>
        <li>Event logging uses a CSV file, not a database.</li>
        <li>The FastAPI endpoints currently read existing logs and list snapshot filenames; they do not control the webcam detector or stream live video.</li>
      </ul>
    </div>

    <h2>Future Improvements</h2>
    <ul>
      <li>Connect FastAPI to start, stop, and report the live detector's status.</li>
      <li>Build a browser dashboard with recent alerts and snapshot previews.</li>
      <li>Add person tracking and reduce repeated/false alerts.</li>
      <li>Move event storage from CSV to SQLite or PostgreSQL.</li>
      <li>Add configurable restricted zones and camera settings.</li>
    </ul>

    <h2>License</h2>
    <p>No license has been specified yet. Add a license file if you want to clearly define how others may use, modify, or distribute this project.</p>

    <footer>
      <p>Built as a learning project using Python, computer vision, object detection, and API development.</p>
      <p><strong>Before publishing:</strong> update the GitHub clone URL and confirm the repository contains no credentials, private videos, or personal data.</p>
    </footer>
  </main>
</body>
</html>
