#from crawlling import base_dir
import cv2

tst = cv2.imread('C:\\Users\\AI\\OneDrive - 광운대학교\\crawl_img' +
                 '\\datasets\\fire\\building\\03_210958_22.jpg', cv2.IMREAD_COLOR)

cv2.imshow('t', tst)
cv2.waitKey(0)
cv2.destroyAllWindows()