
import cv2
import numpy as np


def solution(image, current_speed, current_steering):

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurredImage= cv2.GaussianBlur(grayImage,(5, 5), 0)
    sınır, rota = cv2.threshold(blurredImage, 60, 255, cv2.THRESH_BINARY_INV)
    satır, sütun = rota.shape
    önsatır = satır - 20
    roi = rota[önsatır:satır, 0:sütun]
    image_center = sütun/2
    GaripBiSey = cv2.moments(rota)

    if GaripBiSey['m00'] > 0:
        yol = GaripBiSey['m10'] / GaripBiSey['m00']
        steering = (yol - image_center) * 0.2
    else: 
        steering = current_steering
    steering = np.clip(steering, -1.0, 1.0)
    speed = 10
    target_speed = speed* (1.0 - steering * 0.5)
    target_speed = max(target_speed, 0.5)

    return target_speed, steering

