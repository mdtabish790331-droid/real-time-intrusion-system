
import cv2
import numpy as np
import csv
import winsound
import threading
from pathlib import Path
from datetime import datetime
from ultralytics import YOLO


# 1. Load YOLOv8 model
model = YOLO("yolov8n.pt")


# 2. Create folders automatically
snapshot_folder = Path("snapshots")
log_folder = Path("logs")

snapshot_folder.mkdir(exist_ok=True)
log_folder.mkdir(exist_ok=True)


# 3. CSV log file
log_file = log_folder / "intrusion_log.csv"

if not log_file.exists():
    with open(log_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Time", "Event", "Snapshot"])


# 4. Sound alarm function
def play_alarm():
    winsound.Beep(1000, 700)


def trigger_alarm():
    # Play alarm in a separate thread
    # so the camera does not pause
    alarm_thread = threading.Thread(
        target=play_alarm,
        daemon=True
    )
    alarm_thread.start()


# 5. Open webcam
camera = cv2.VideoCapture(0)

previous_intrusion = False

while True:
    success, frame = camera.read()

    if not success:
        print("Camera frame nahi mil raha")
        break

    height, width = frame.shape[:2]

    # 6. Define restricted zone
    zone = np.array([
        [int(width * 0.25), int(height * 0.35)],
        [int(width * 0.75), int(height * 0.35)],
        [int(width * 0.85), int(height * 0.90)],
        [int(width * 0.15), int(height * 0.90)]
    ], dtype=np.int32)

    cv2.polylines(
        frame, [zone], True, (0, 255, 255), 2
    )

    # 7. Detect persons using YOLOv8
    results = model(frame, conf=0.35, verbose=False)
    result = results[0]

    intrusion_detected = False

    for box in result.boxes:
        class_id = int(box.cls[0])

        # Only process persons
        if class_id != 0:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = float(box.conf[0])

        # Bottom-center point of the person
        foot_x = (x1 + x2) // 2
        foot_y = y2
        foot_point = (foot_x, foot_y)

        # Check if person is inside the zone
        inside = cv2.pointPolygonTest(
            zone, foot_point, False
        )

        if inside >= 0:
            intrusion_detected = True
            box_color = (0, 0, 255)
            label = f"INTRUDER {confidence:.2f}"
        else:
            box_color = (0, 255, 0)
            label = f"Person {confidence:.2f}"

        # Draw person box
        cv2.rectangle(
            frame, (x1, y1), (x2, y2), box_color, 2
        )

        # Draw foot point
        cv2.circle(
            frame, foot_point, 5, box_color, -1
        )

        # Display label
        cv2.putText(
            frame,
            label,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            box_color,
            2
        )

    # 8. Display alert on screen
    if intrusion_detected:
        cv2.putText(
            frame,
            "INTRUSION ALERT!",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    # 9. Handle a new intrusion event
    if intrusion_detected and not previous_intrusion:

        # Trigger sound alarm
        trigger_alarm()
        print("[ALARM] Intrusion detected!")

        # Create date and time
        now = datetime.now()
        date_text = now.strftime("%Y-%m-%d")
        time_text = now.strftime("%H:%M:%S")
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Save snapshot
        snapshot_name = f"intrusion_{timestamp}.jpg"
        snapshot_path = snapshot_folder / snapshot_name

        saved = cv2.imwrite(str(snapshot_path), frame)

        if saved:
            print(f"[SAVED] Photo: {snapshot_path}")

            # Record event in CSV
            with open(log_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    date_text,
                    time_text,
                    "Intrusion Detected",
                    snapshot_name
                ])
        else:
            print("[ERROR] Photo save nahi ho payi!")

    # Remember current state
    previous_intrusion = intrusion_detected

    # 10. Show camera window
    cv2.imshow("Intrusion Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 11. Release camera and close windows
camera.release()
cv2.destroyAllWindows()
