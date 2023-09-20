from function import *
import cv2

for i in range(0,125):
    frame1 = cv2.imread(f"SVM/try/try1/frame1/{i}.png")
    frame1 = img1_main(frame1)

    frame2 = cv2.imread(f"SVM/try/try1/frame2/{i}.png")
    if i <29 :
        shift=96
    elif i<90 :
        shift=80
    else :
        shift=80
    frame2 = img2_main(frame2,shift)
    cv2.imshow('frame1',frame1)
    cv2.imshow('frame2',frame2)
    print(i)
 
    
    result = img_matching(frame2,frame1)
    cv2.imshow("result",result)
    cv2.waitKey(1)