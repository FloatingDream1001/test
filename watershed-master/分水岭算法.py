import numpy as np

import cv2

from matplotlib import pyplot as plt

input_image = cv2.imread('wu1.jpg')

gray = cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# noise removal

kernel = np.ones((3,3),np.uint8)

opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2) # 形态开运算

# sure background area

sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)

ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region

sure_fg = np.uint8(sure_fg)

unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling

ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1

markers = markers+1

# Now, mark the region of unknown with zero

markers[unknown==255] = 0

markers = cv2.watershed(input_image,markers)

input_image[markers == -1] = [255,0,0]

plt.subplot(241), plt.imshow(gray),

plt.title('Original'), plt.axis('off')

plt.subplot(242), plt.imshow(thresh, cmap='gray'),

plt.title('Threshold'), plt.axis('off')

plt.subplot(243), plt.imshow(sure_bg, cmap='gray'),

plt.title('sure_bg'), plt.axis('off')

plt.subplot(244), plt.imshow(dist_transform, cmap='gray'),

plt.title('Dist Transform'), plt.axis('off')

plt.subplot(245), plt.imshow(sure_fg, cmap='gray'),

plt.title('sure_fg'), plt.axis('off')

plt.subplot(246), plt.imshow(unknown, cmap='gray'),

plt.title('Unknow'), plt.axis('off')

plt.subplot(247), plt.imshow(np.abs(markers), cmap='jet'),

plt.title('Markers'), plt.axis('off')
plt.savefig("分水岭.png")
plt.show()

cv2.imshow('img',input_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

