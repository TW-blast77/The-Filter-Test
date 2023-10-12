import cv2 as cv
import numpy as np

# 讀取圖片
img = cv.imread("./photo/origin-photo/Lenna.png", cv.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

# 加雜訊
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    
    if i % 2  == 0 :
        img[x, y, :] = 255
    else:
        img[x, y, :] = 0
cv.imshow("noise", img)

# 影像保存
cv.imwrite("./photo/output-photo/noise-photo/Noise_lenna.jpg", img)

# 等待顯示
cv.waitKey()
cv.destroyAllWindows()