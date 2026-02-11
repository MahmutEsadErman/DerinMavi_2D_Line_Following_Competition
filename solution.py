"""
Derin Mavi Line Follower Challenge

Bu dosyayı düzenleyerek kendi çizgi izleme algoritmanızı geliştirin!
Aşağıdaki solution() fonksiyonunu tamamlayın.

Başarılar!
"""

import cv2
import numpy as np


def solution(image, current_speed, current_steering):
    """  
    Args:
        image: Robotun kamerasından gelen 64x64 pixel BGR görüntü (numpy array)
               
        current_speed: Robotun mevcut hızı (float)
                      
        current_steering: Robotun mevcut direksiyon açısı (float, -1 ile 1 arası)
                         - -1: Tam sol
                         -  0: Düz
                         -  1: Tam sağ
    
    Returns:
        target_speed: Robotun hedef hızı (float)

        steering: Robotun hedef direksiyon açısı (float, -1 ile 1 arası)
    """
    
    # ============================================
    # ÇÖZÜMÜNÜZÜ BURAYA YAZIN
    # ============================================
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    roi = binary[48:64, :]

    black_ratio = np.sum(roi == 255) / roi.size
    white_ratio = 1 - black_ratio
    
   
    if black_ratio > 0.4:
        target_speed = 3 + black_ratio * 8 + current_speed * 1.7
        
    else:
        target_speed = 2 + black_ratio * 6.5 + current_speed * 0.25
    h, w = roi.shape
    left = roi[:, :w//2]
    right = roi[:, w//2:]

    left_white = np.sum(left == 0)
    right_white = np.sum(right == 0)

    if white_ratio > 0.09:
        if left_white > right_white:
            steering = 0.34
           
        elif left_white < right_white:
            steering = - 0.34       
        else:
            steering = current_steering

    else:
        steering = current_steering * 0.8
    return target_speed, steering
