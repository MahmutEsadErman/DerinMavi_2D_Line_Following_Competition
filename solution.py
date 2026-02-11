import cv2
import numpy as np

def solution(image, current_speed, current_steering):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY_INV)
    
    h, w = binary.shape

    scan_rows = [int(h * 0.45), int(h * 0.65), int(h * 0.85)]
    weights = [0.45, 0.35, 0.20]

    error_sum = 0.0
    weight_sum = 0.0
    found = False

    for row, weight in zip(scan_rows, weights):
        xs = np.where(binary[row] > 0)[0]
        if xs.size:
            cx = xs.mean()
            error = (cx - w * 0.5) / (w * 0.5)

            error_sum += error * weight
            weight_sum += weight
            found = True

    steering = current_steering * 0.92
    target_speed = max(current_speed * 0.9, 4.0)

    return target_speed, steering
