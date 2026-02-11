import cv2
import numpy as np

def solution(image, current_speed, current_steering):

    front = image[20:64 , 0:64]
    hsv = cv2.cvtColor(front, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 60])
    mask_black = cv2.inRange(hsv, lower_black, upper_black)

    lower_everything = np.array([0, 0, 0])
    upper_everything = np.array([180, 255, 255])
    mask_all = cv2.inRange(hsv, lower_everything, upper_everything)

    red_pixel_count = cv2.countNonZero(mask_red)
    

    BM = cv2.moments(mask_black)
    RM = cv2.moments(mask_red)
    AM = cv2.moments(mask_all)

    red_border = 10
    target_speed=10.0
    centre_all = int(AM["m10"]/AM["m00"])

    if(centre_all<26 or centre_all>38):
        if(centre_all>32):
            target_speed = 53.0
            steering = 0.4
        else:
            steering = -0.4
    elif(RM["m00"]>0 and RM["m00"]>BM["m00"]):
        #engel atlama
        target_speed = 5.0
        centre_red = int(RM["m10"]/RM["m00"])
        error = centre_red-red_border
        steering = error * 0.06
    elif(BM["m00"]>0):
        #yol takip
        target_speed = 53.0
        centre_x = int(BM["m10"]/BM["m00"])
        error = centre_x-32
        steering = error * 0.05
    else:
        steering = 0
        target_speed = 10.0

    
    
    return target_speed, steering

    # ============================================
    #   kameradan gelen matrisin sadece on kismini dikkate aliyoruz.
    #   bu ornekte arka plan zaten beyaz olsa da yolu daha duzgun islemek icin matrisi beyaz siyaha indirgiyoruz.
    #   matrisi 0 1 e indirgiyoruz yol rengi 1 dir. (beyaza cevirmis olduk)
    #   cv2.moments komutuyla 1 degerindeki pixellerin adedi, x degerleri toplami , y degerleri toplamini ediniriz.
    #   x deger toplami/hepsi = x kutle merkezini verir. merkeze uzakligi sapma degerini verir.
    #   32x0.03=0.96 , -1<steering<1 arasina getirilir.
    #   yol gorunmuyorsa son durumunu korur.
    # ============================================