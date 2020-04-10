import cv2
import numpy as np
# 每个正方形边长约为1.8
canvas = np.zeros((800,1000,3), dtype ="uint8")
for i in range(8):
    for i2 in range(10):
        res_row = i2 % 2
        res_column = i % 2
        if res_column == 0:
            if res_row == 0:
                cv2.rectangle(canvas, ((i2 + 1) * 100, i * 100), ((i2 + 2) * 100, (i + 1) * 100), (255, 255, 255), -1)
        else:
            if res_row == 0:
                cv2.rectangle(canvas, (i2 * 100, i * 100), ((i2 + 1) * 100, (i + 1) * 100), (255, 255, 255), -1)

cv2.imwrite("chessboard.jpg", canvas)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
