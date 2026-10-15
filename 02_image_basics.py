
import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("Image load nahi hui!")
else:
    print("Image successfully loaded!")

    height, width, channels = image.shape

    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)

    cv2.imshow("My First Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
