#!/usr/bin/env python
#coding:utf-8
"""
Author:  iJasonLee (kingmax_res@163.com;184327932@qq.com)
Purpose: OpenCV2 testing (http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html#table-of-content-introduction)
Install: http://docs.opencv.org/2.4/doc/tutorials/introduction/windows_install/windows_install.html#windowssetpathandenviromentvariable
pip install numpy
Created: 2017/9/13
Tutorial: http://docs.python-guide.org/en/latest/scenarios/imaging/
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
"""

import unittest

import cv2
import numpy as np

img = cv2.imread('model_s.png')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_test.jpg', gray)

img = cv2.imread('gray_test.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    unittest.main()