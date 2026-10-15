
import cv2

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        print("Camera frame nahi mil raha")
        break

    height, width, channels = frame.shape

    cv2.rectangle(
        frame,
        (50, 50),
        (300, 250),
        (0, 255, 0),
        3
    )

    cv2.putText(
        frame,
        "Live Camera",
        (50, 300),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Width: {width}, Height: {height}",
        (50, 350),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.imshow("Live Drawing", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
