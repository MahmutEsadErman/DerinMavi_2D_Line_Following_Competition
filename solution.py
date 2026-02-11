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



    cam = gray[ 10: 64,:]

    ters_cam = 255- cam

    yol = cv2.moments(ters_cam)




    if yol["m00"] != 0:
     

     yol_merkezi_x = yol["m10"]/yol["m00"]

     steering = (yol_merkezi_x - 32) / 32

    else: 
     steering = 1
     target_speed= 1


    target_speed = 15-(steering)*14

  

    return target_speed, steering
