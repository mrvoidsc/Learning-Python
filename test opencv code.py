import numpy as np
import cv2

cap = cv2.VideoCapture(0)
layanhgoc = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    anhgoc = frame.copy
    #h = frame.height
    #w = frame.width
    (h, w) = frame.shape[:2]
    nb_pixels = h * w
    anhdich = np.zeros((h, w, 1), dtype="uint8")
    #cv2.CreateMat(frame.height, frame.width, cv2.CV_8U)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    nutbam = cv2.waitKey(20)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    if nutbam & 0xFF == ord('q'):
        break
    if nutbam & 0xFF == ord('a'):
        print('bam nut roi')
        layanhgoc = 1
        anhgoc = frame.copy()
        anhgocgray = cv2.cvtColor(anhgoc, cv2.COLOR_BGR2GRAY)
        #anhdich = frame.copy()
        #print(2)
        nutbam = '10'
    if layanhgoc == 1:
        #print(1)
        cv2.absdiff(gray, anhgocgray, anhdich)
        (T, threshInv) = cv2.threshold(anhdich, 20, 255, cv2.THRESH_BINARY)
        cv2.imshow('ket qua anh xam', anhdich)
        cv2.imshow('ket qua anh nhi phan', threshInv)
        M = cv2.moments(threshInv)
        if M["m00"] > 0:
            # calculate x,y coordinate of center
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # put text and highlight the center
            cv2.circle(frame, (cX, cY), 20, (100, 210, 140), -1)
        if M["m00"] > 20:
            print ('da phat hien doi tuong, lam coi keu di')
        """
        nb = 0
        for y in range(h):
            for x in range(w):
                if threshInv[y, x] == 255:
                    nb += 1
        avg = (nb * 100.0) / nb_pixels
        if avg >= 10:
            print ("Something is moving !")
        """
    cv2.imshow('frame original', frame)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()