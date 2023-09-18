import cv2

SVM_image = cv2.imread("result_images/result.png")
car_image = cv2.imread("images/car_image.png", cv2.IMREAD_COLOR)
car_image = cv2.resize(car_image, (80, 80), interpolation=cv2.INTER_CUBIC)

# 540 540 270
SVM_image[230:310, 230:310] = car_image

cv2.imshow("car_image", car_image)
cv2.imshow("SVM_image", SVM_image)
cv2.imwrite("result_images/SVM_result_with_car.png", SVM_image)

cv2.waitKey(0)
