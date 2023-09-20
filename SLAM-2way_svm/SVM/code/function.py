import numpy as np 
import cv2

# image1 function
def undist(img):
    #Define the camera matrix and distortion coefficients
    K = np.array([[363.090103, 0.000000, 313.080058], [0.000000, 364.868860, 252.739984], [0.000000, 0.000000, 1.000000]])
    dist_coeffs = np.array([-0.334146, 0.099765, -0.000050, 0.001451, 0.000000])
    # Undistort the image
    img_undistorted = cv2.undistort(img, K, dist_coeffs)
    return img_undistorted
def img1_persperctive(img):
    tl = (0,240+30) #좌상
    bl = (0,480) #좌하
    tr = (640,480) #우하
    br = (640,240+30) #우상

    pts1=np.float32([tl,bl,tr,br]) 
    pts2=np.float32([(0,-10),(170,270-50),(370,270-50),(540,-10)])

    matrix=cv2.getPerspectiveTransform(pts1,pts2) 
    
    transformed_frame=cv2.warpPerspective(img,matrix,(540,540),None, cv2.INTER_CUBIC)
    return transformed_frame

def img1_main(img):
    img = undist(img)
    img = img1_persperctive(img)
    return img
# image2 function
def img2_percpective(img):
    # Selecting Cordinates
    tl = (0,240) #좌상
    bl = (0,480) #좌하
    tr = (640,480) #우하
    br = (640,240) #우상
    
    pts1=np.float32([tl,bl,tr,br]) 
    pts2=np.float32([(0,0),(170,270),(370,270),(540,0)])

    matrix=cv2.getPerspectiveTransform(pts1,pts2)

    transformed_frame=cv2.warpPerspective(img,matrix,(540,540),None, cv2.INTER_CUBIC)
    return transformed_frame

def rotate_shift(img,shift):
    #rotate
    angle = 31
    center = (img.shape[1] / 2, img.shape[0] / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    #shift
    height, width = img.shape[:2]
    shifted = img.copy()
    M = np.float32([[1, 0, -1*shift], [0, 1, -1*shift]])
    shifted = cv2.warpAffine(shifted, M, (width, height))
    return shifted

def img2_main(img,shift):
    img = img2_percpective(img)
    img = rotate_shift(img,shift)
    return img
    
def get_mask(img1, img2):
    img1_gray= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2_gray= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(img1_gray)

    for y in range(img1_gray.shape[0]):
        for x in range(img2_gray.shape[1]):
            if img1_gray[y,x] and img1_gray[y,x]:
                mask[y,x] = 255
    
    return mask

def img_matching(img1,img2):
    mask = get_mask(img2,img1)
    dst = cv2.copyTo(img1,~mask)
    result = dst+img2
    return result