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

    BM = cv2.moments(mask_black)
    RM = cv2.moments(mask_red)

    red_border = 10
    target_speed=53.0

    if(RM["m00"]>0 and RM["m00"]>BM["m00"]):
        #engel atlama
        centre_red = int(RM["m10"]/RM["m00"])
        error = centre_red-red_border
        steering = error * 0.06
    elif(BM["m00"]>0):
        #yol takip
        centre_x = int(BM["m10"]/BM["m00"])
        error = centre_x-32
        steering = error * 0.05
    else:
        steering = 0
        target_speed = 10.0

    
    
    return target_speed, steering

    
    #   ENGLISH
    # ============================================
    # We only process the front portion of the incoming camera matrix (ROI).
    # To process the path more accurately, the matrix is reduced to black and white, 
    # even though the background is already white.
    # The matrix is binarized (0 and 1) where the road color is represented as 1 (white).
    # Using cv2.moments, we obtain the total count of '1' pixels, and the sum of X and Y values.
    # The center of mass (x-centroid) is calculated as: total_x / total_pixels.
    # The deviation from the center (32) determines the steering value, scaled between -1 and 1.
    # If the road is lost, the vehicle maintains its last known steering state.
    #
    # When an obstacle (red) occupies more of the camera view than the road (black), 
    # the obstacle avoidance logic is triggered.
    # The code is designed to always pass obstacles from the right; therefore, 
    # it keeps the obstacle's center on the left side of the camera frame.
    # Once the road (black) becomes dominant in the view again, the vehicle resumes line following.
    # ============================================

    #   TURKISH
    # ============================================
    #   kameradan gelen matrisin sadece on kismini dikkate aliyoruz.
    #   bu ornekte arka plan zaten beyaz olsa da yolu daha duzgun islemek icin matrisi beyaz siyaha indirgiyoruz.
    #   matrisi 0 1 e indirgiyoruz yol rengi 1 dir. (beyaza cevirmis olduk)
    #   cv2.moments komutuyla 1 degerindeki pixellerin adedi, x degerleri toplami , y degerleri toplamini ediniriz.
    #   x deger toplami/hepsi = x kutle merkezini verir. merkeze uzakligi sapma degerini verir.
    #   32x0.03=0.96 , -1<steering<1 arasina getirilir.
    #   yol gorunmuyorsa son durumunu korur.
    #
    #   kamerada engel(kirmizi) yoldan(siyah) daha fazla goruldugu anda engel icin kodlar calisir.
    #   kod her zaman engelin sagindan gecmek icin tasarlandi ve bu nedenle engelin merkezini her zaman kameranin sol tarafinda tutar.
    #   kamera gorusune tekrar yol girdiginde ve kamerada siyahlar baskin duruma geldiginde tekrardan yolu takip etmeye devam eder.
    # ============================================
    