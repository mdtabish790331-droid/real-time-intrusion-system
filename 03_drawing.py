
import cv2

# Create a blank image
image = cv2.imread("test.jpg")

if image is None:
    print("Image load nahi hui!")
    raise SystemExit

# Draw a rectangle
cv2.rectangle(image, (760, 220), (1200, 950), (0, 255, 0), 3)

# Draw a line
cv2.line(image, (50, 300), (400, 300), (255, 0, 0), 3)

# Write text
cv2.putText(
    image,
    "Hello OpenCV",
    (50, 350),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

# Show the result
cv2.imshow("Drawing Practice", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
