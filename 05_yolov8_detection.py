
import cv2
from ultralytics import YOLO

# Load the pretrained YOLOv8 model
model = YOLO("yolov8n.pt")

# Open the webcam
camera = cv2.VideoCapture(0)

while True:
    # Read one frame from the webcam
    success, frame = camera.read()

    if not success:
        print("Camera frame nahi mil raha")
        break

    # Detect objects in the current frame
    results = model(
    frame,
    conf=0.35,
    imgsz=640,
    verbose=False
      )
    # Process the detection result
    result = results[0]

    # Check every detected object
    for box in result.boxes:
        class_id = int(box.cls[0])

        # Keep only the person class
        if class_id == 0:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])

            # Draw a bounding box around the person
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Display label and confidence
            label = f"Person {confidence:.2f}"

            cv2.putText(
                frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Show the annotated frame
    cv2.imshow("YOLOv8 Person Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()
