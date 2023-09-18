import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
import sys

mtx_cam = np.array([[357.906682, 0.000000, 332.457325],
                     [0.000000, 356.170785, 253.010996],
                     [0.000000, 0.000000, 1.000000]], dtype=np.float64)

dist_cam = np.array([-0.274053, 0.049790, -0.001539, -0.003057, 0.000000], dtype=np.float64)

frame_0 = cv2.imread("images/frame_0.png", cv2.IMREAD_COLOR)
frame_1 = cv2.imread("images/frame_1.png", cv2.IMREAD_COLOR)
frame_2 = cv2.imread("images/frame_2.png", cv2.IMREAD_COLOR)
frame_3 = cv2.imread("images/frame_3.png", cv2.IMREAD_COLOR)
frame_4 = cv2.imread("images/frame_4.png", cv2.IMREAD_COLOR)
frame_5 = cv2.imread("images/frame_5.png", cv2.IMREAD_COLOR)
frame_6 = cv2.imread("images/frame_6.png", cv2.IMREAD_COLOR)
frame_7 = cv2.imread("images/frame_7.png", cv2.IMREAD_COLOR)

car_image = cv2.imread("images/car_image.png", cv2.IMREAD_COLOR)
car_image = cv2.resize(car_image, (80, 80), interpolation=cv2.INTER_CUBIC)

point_1 = [[198, 275], [148, 292], [491, 292], [438, 275]]
point_2 = [[253, 100], [253, 140], [383, 140], [383, 100]]

point_array1 = np.array(point_1, dtype=np.float32)
point_array2 = np.array(point_2, dtype=np.float32)

H_cam = cv2.getPerspectiveTransform(point_array1, point_array2)
print(f"H_cam = {H_cam}")

und_frame_0 = cv2.undistort(frame_0, mtx_cam, dist_cam, None)
und_frame_1 = cv2.undistort(frame_1, mtx_cam, dist_cam, None)
und_frame_2 = cv2.undistort(frame_2, mtx_cam, dist_cam, None)
und_frame_3 = cv2.undistort(frame_3, mtx_cam, dist_cam, None)
und_frame_4 = cv2.undistort(frame_4, mtx_cam, dist_cam, None)
und_frame_5 = cv2.undistort(frame_5, mtx_cam, dist_cam, None)
und_frame_6 = cv2.undistort(frame_6, mtx_cam, dist_cam, None)
und_frame_7 = cv2.undistort(frame_7, mtx_cam, dist_cam, None)

# cv2.imshow("und_frame_0__", und_frame_0)
# cv2.imshow("und_frame_1__", und_frame_1)
# cv2.imshow("und_frame_2__", und_frame_2)
# cv2.imshow("und_frame_3__", und_frame_3)
# cv2.imshow("und_frame_4__", und_frame_4)
# cv2.imshow("und_frame_5__", und_frame_5)
# cv2.imshow("und_frame_6__", und_frame_6)
# cv2.imshow("und_frame_7__", und_frame_7)

dst_cam_0 = cv2.warpPerspective(und_frame_0, H_cam, (640,480), None, cv2.INTER_CUBIC)
dst_cam_1 = cv2.warpPerspective(und_frame_1, H_cam, (640,480), None, cv2.INTER_CUBIC)
dst_cam_2 = cv2.warpPerspective(und_frame_2, H_cam, (640,480), None, cv2.INTER_CUBIC)
dst_cam_3 = cv2.warpPerspective(und_frame_3, H_cam, (640,480), None, cv2.INTER_CUBIC)
dst_cam_4 = cv2.warpPerspective(und_frame_4, H_cam, (640,480), None, cv2.INTER_CUBIC)
dst_cam_5 = cv2.warpPerspective(und_frame_5, H_cam, (640,480), None, cv2.INTER_CUBIC)
dst_cam_6 = cv2.warpPerspective(und_frame_6, H_cam, (640,480), None, cv2.INTER_CUBIC)
dst_cam_7 = cv2.warpPerspective(und_frame_7, H_cam, (640,480), None, cv2.INTER_CUBIC)

dst_cam_0[250:,:] = 0
dst_cam_1[250:,:] = 0
dst_cam_2[250:,:] = 0
dst_cam_3[250:,:] = 0
dst_cam_4[250:,:] = 0
dst_cam_5[250:,:] = 0
dst_cam_6[250:,:] = 0
dst_cam_7[250:,:] = 0

dst_cam_0 = cv2.resize(dst_cam_0, (540, 540), interpolation=cv2.INTER_CUBIC)
dst_cam_1 = cv2.resize(dst_cam_1, (540, 540), interpolation=cv2.INTER_CUBIC)
dst_cam_2 = cv2.resize(dst_cam_2, (540, 540), interpolation=cv2.INTER_CUBIC)
dst_cam_3 = cv2.resize(dst_cam_3, (540, 540), interpolation=cv2.INTER_CUBIC)
dst_cam_4 = cv2.resize(dst_cam_4, (540, 540), interpolation=cv2.INTER_CUBIC)
dst_cam_5 = cv2.resize(dst_cam_5, (540, 540), interpolation=cv2.INTER_CUBIC)
dst_cam_6 = cv2.resize(dst_cam_6, (540, 540), interpolation=cv2.INTER_CUBIC)
dst_cam_7 = cv2.resize(dst_cam_7, (540, 540), interpolation=cv2.INTER_CUBIC)

rot_mat_1 = cv2.getRotationMatrix2D((270, 270), 312, 1)
dst_cam_1 = cv2.warpAffine(dst_cam_1, rot_mat_1, (540,540))
dst_cam_1 = imutils.translate(dst_cam_1, -15, 5)

rot_mat_2 = cv2.getRotationMatrix2D((270, 270), 268, 1)
dst_cam_2 = cv2.warpAffine(dst_cam_2, rot_mat_2, (540,540))
dst_cam_2 = imutils.translate(dst_cam_2, -15, -6)

rot_mat_3 = cv2.getRotationMatrix2D((270, 270), 223, 1)
dst_cam_3 = cv2.warpAffine(dst_cam_3, rot_mat_3, (540,540))
dst_cam_3 = imutils.translate(dst_cam_3, -15, -20)

rot_mat_4 = cv2.getRotationMatrix2D((270, 270), 180, 1)
dst_cam_4 = cv2.warpAffine(dst_cam_4, rot_mat_4, (540,540))
dst_cam_4 = imutils.translate(dst_cam_4, -5, -15)

rot_mat_5 = cv2.getRotationMatrix2D((270, 270), 135, 1)
dst_cam_5 = cv2.warpAffine(dst_cam_5, rot_mat_5, (540,540))
dst_cam_5 = imutils.translate(dst_cam_5, 10, -25)

rot_mat_6 = cv2.getRotationMatrix2D((270, 270), 89, 1)
dst_cam_6 = cv2.warpAffine(dst_cam_6, rot_mat_6, (540,540))
dst_cam_6 = imutils.translate(dst_cam_6, 12, -10)

rot_mat_7 = cv2.getRotationMatrix2D((270, 270), 43, 1)
dst_cam_7 = cv2.warpAffine(dst_cam_7, rot_mat_7, (540,540))
dst_cam_7 = imutils.translate(dst_cam_7, 10, 0)

imgs = [dst_cam_0, dst_cam_1, dst_cam_2, dst_cam_3, dst_cam_4, dst_cam_5, dst_cam_6, dst_cam_7]

for i in range(len(imgs)):
    cv2.imwrite("result_images/dst_" + str(i) + ".png", imgs[i])

dst = dst_cam_0 + dst_cam_1 + dst_cam_2 + dst_cam_3 + dst_cam_4 + dst_cam_5 + dst_cam_6 + dst_cam_7

cv2.imshow("dst", dst)

cv2.waitKey(0)
