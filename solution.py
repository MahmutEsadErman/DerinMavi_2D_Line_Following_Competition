import cv2
import numpy as np

def solution(image, current_speed, current_steering):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY_INV)

    h, w = binary.shape

    scan_rows = [
        int(h * 0.45),
        int(h * 0.65),
        int(h * 0.85)
    ]
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

    if found:
        steering = error_sum / weight_sum
        steering = np.clip(steering, -1.0, 1.0)
        abs_s = abs(steering)
        if abs_s < 0.08:
            target_speed = 13.5
        elif abs_s < 0.18:
            target_speed = 11.0
        elif abs_s < 0.30:
            target_speed = 8.8
        elif abs_s < 0.45:
            target_speed = 6.5
        else:
            target_speed = 4.5

        if abs_s > 0.15:
            steering *= 1.18

        if abs_s > 0.55:
            steering *= 0.88
            target_speed = min(target_speed, 4.0)

        steering = np.clip(steering, -1.0, 1.0)

    return target_speed, steering
