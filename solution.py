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
    
  # 1. Görüntüyü İşleme (Çizgiyi daha net yakalamak için eşiği genişlettik)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Eşik değerini 120'ye çıkardık; zemin beyaz, çizgi siyahsa çizgiyi beyaza çevirir.
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

    # 2. ROI (İlgi Alanı): Sadece robotun hemen altındaki alana bak
    # Eğer robot çok dönüyorsa, bakış alanını biraz daha daraltıp merkeze odaklanmalıyız.
    height, width = thresh.shape
    roi = thresh[int(height * 0.7):height, :]
    
    # 3. Çizgiyi Bulma ve Hata Hesaplama
    M = cv2.moments(roi)
    
    # M["m00"] beyaz piksel sayısını temsil eder. 
    # Eğer 20'den az beyaz piksel varsa çizgi "yok" kabul edilir.
    if M["m00"] > 20:
        cx = int(M["m10"] / M["m00"])
        # Hata: Çizginin merkezden (32) uzaklığı
        error = cx - 32
        
        # 4. Kontrol: Direksiyonu çok fazla kırmasını engelleyelim
        # 0.03 katsayısı daha yumuşak dönüşler sağlar, robotun savrulmasını önler.
        steering = error * 0.05
        
        # 5. Hız: Robotun durmaması için sabit ve güvenli bir hız veriyoruz
        target_speed = 9.0
    else:
        # Çizgi kaybolursa: DURUP DÖNME! 
        # Direksiyonu düzle (0.0) ve yavaşça ileri git (5.0) ki çizgiyi bulasın.
        steering = 0.0
        target_speed = 5.0

    # Çıkışları sınırla (Sıkı limitler koyarak kendi etrafında dönmesini engelliyoruz)
    steering = float(np.clip(steering, -0.6, 0.6)) 
    target_speed = float(target_speed)

    return target_speed, steering
    
    return target_speed, steering
