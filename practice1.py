import imutils
import cv2
image = cv2.imread("avengers..jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
cv2. imshow("Image", image)
cv2.waitKey(0)

(B, G, R) = image[120,90]
print("R={}, G={}, B={}".format(R, G, B))

roi = image[270:390, 250:490]
cv2.imshow("Roi", roi)
cv2.waitKey(0)

resized = imutils.resize(image, width=370)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

rotate = imutils.rotate_bound(image, 45)
cv2.imshow("imutils rotate", rotate)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(image, (11,11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

output = image.copy()
cv2.putText(output, "i love you 3000", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)

