import cv2.aruco as aruco
import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# index由0开始
w = 9
h = 7
objp = np.zeros((w*h,3), np.float32)
objp[:,:2] = np.mgrid[0:w,0:h].T.reshape(-1,2)
objp = objp*18
objpoints = []
imgpoints = []
images = glob.glob('chessboard.jpg')
i = 1
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (w, h), None)

    if ret == True:
        print("i:", i)
        i = i + 1
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    objpoints.append(objp)
    imgpoints.append(corners)
    cv2.drawChessboardCorners(img, (w, h), corners, ret)
    cv2.namedWindow('findCorners', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('findCorners', 1440, 1080)
    cv2.imshow('findCorners', img)

    # cv2.destroyAllWindows()
    ret, mtx, dist, rvecs, tvecs = \
    cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    # 返回
    print("ret:",ret)
    print("mtx:\n",mtx)
    print("dist:\n",dist)
    print("rvecs:\n",rvecs)
    print("tvecs:\n",tvecs)
    cv2.waitKey(0)

