"""
Derin Mavi Line Follower Challenge

Bu dosyayı düzenleyerek kendi çizgi izleme algoritmanızı geliştirin!
Aşağıdaki solution() fonksiyonunu tamamlayın.

Başarılar!
"""

import cv2
import numpy as np


def solution(image, current_speed, current_steering):

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurredImage= cv2.GaussianBlur(grayImage,(5, 5), 0)
    sınır, rota = cv2.threshold(blurredImage, 60, 255, cv2.THRESH_BINARY_INV)
    satır, sütun = rota.shape
    önsatır = satır - 25
    roi = rota[önsatır:satır, 0:sütun]
    image_center = sütun/2
    GaripBiSey = cv2.moments(rota)

    if GaripBiSey['m00'] > 0:
        yol = GaripBiSey['m10'] / GaripBiSey['m00']
        steering = (yol - image_center) * 0.01
    else: 
        steering = current_steering
    speed = 10
    target_speed = speed 
    steering = np.clip(steering, -1.0, 1.0)
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
    
    return target_speed, steering
