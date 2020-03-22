import cv2
import numpy as np
image = cv2.imread('1.png')
cv2.imshow(' ', image)
final = 120
r = final / float(image.shape[1])
dim = (final, int(image.shape[0] * r))
w, h = image.shape[0], image.shape[1]

res = cv2.resize(image, dim)
cv2.imshow('r', res)

center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 1, 1.0)

rotate = cv2.warpAffine(image, M, (w, h))
cv2.imshow('rr', rotate)

roteter = cv2.flip(image, 1)
cv2.imshow('rrr', roteter)

color_spaces = ('RGB', 'GRAY', 'HSV', 'LAB', 'XYZ', 'YUV')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('rrrr', gray_image)

color_image = {color: cv2.cvtColor(image, getattr(cv2, f'COLOR_BGR2{color}'))
               for color in color_spaces}
for clr in color_image:
    cv2.imshow('clr', color_image[clr])

low_red = (17, 50, 110)
how_red = (101, 140, 180)
omly_cat = cv2.inRange(image, low_red, how_red)
cv2.imshow('rrrrr', omly_cat)

clr = (255, 0, 0)
clr = clr[::-1]
mask = np.zeros((image.shape[0] + 2, image.shape[1] + 2), np.uint8)
cv2.floodFill(image, mask, (image.shape[1] // 2, 80), clr)

cv2.imshow('rrrrrr', image)

cv2.waitKey(0)
