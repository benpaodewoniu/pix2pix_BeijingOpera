import cv2
from matplotlib import pyplot as plt

IMAGE_NAME = "./1.jpg"
img = cv2.imread(IMAGE_NAME)
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
c_canny_img = cv2.Canny(img2gray, 0, 150)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(c_canny_img, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
