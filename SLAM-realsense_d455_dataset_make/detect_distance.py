import cv2
import pyrealsense2
import matplotlib.pyplot as plt
from realsense_depth import *

# Initialize Camera Intel Realsense
dc = DepthCamera()

count = 0

while True:
    key = cv2.waitKey(100)

    ret, depth_frame, color_frame = dc.get_frame()
    color_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)
    
    count = int(count) + 1
    count = format(count, '08')
    
    cv2.imshow("depth_frame", depth_frame)
    cv2.imwrite("dataset/depth/" + str(count) + ".png", depth_frame)
    
    cv2.imshow("color_frame", color_frame)
    cv2.imwrite("dataset/rgb/" + str(count) + ".png", color_frame)
    
    if key == ord('q'):
        break

cv2.destroyAllWindow()
