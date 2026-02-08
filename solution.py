import cv2
import numpy as np
import math

def solution(image, current_speed, current_steering):

    front = image[20:64 , 0:64]
    gray = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)
    nothing , threshold = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)

    target_speed = 13.0
    steering = 0.0

    M = cv2.moments(threshold)

    if(M["m00"]>0):
        centre_x = int(M["m10"]/M["m00"])
        error = centre_x-32
        steering = error * 0.03
    else:
        steering = current_steering
        target_speed = 0.0
    
    return target_speed, steering

    # ============================================
    #   kameradan gelen matrisin sadece on kismini dikkate aliyoruz.
    #   bu ornekte arka plan zaten beyaz olsa da yolu daha duzgun islemek icin matrisi beyaz siyaha indirgiyoruz.
    #   matrisi 0 1 e indirgiyoruz yol rengi 1 dir. (beyaza cevirmis olduk)
    #   cv2.moments komutuyla 1 degerindeki pixellerin adedi, x degerleri toplami , y degerleri toplamini ediniriz.
    #   x deger toplami/hepsi = x kutle merkezini verir. merkeze uzakligi sapma degerini verir.
    #   32x0.03=0.96 , -1<steering<1 arasina getirilir.
    #   yol gorunmuyorsa son durumunu korur.
    #
    # ============================================