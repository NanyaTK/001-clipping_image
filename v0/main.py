import cv2

img = cv2.imread("A1.jpg")

img1 = img[950 :, 30: 950]
cv2.imwrite("output_image.jpg", img1)