import cv2
from glob import glob
import numpy as np
from tqdm import tqdm
import os
import crawlling

#dir = glob('C:\\Users\\AI\\OneDrive - 광운대학교\\crawl_img\\datasets\\fire\\car\\*.jpg')
dir = glob(crawlling.base_dir + '\\datasets\\fire\\car\\*.jpg')
rmv_cnt = 0
for image in tqdm(dir):
    img = cv2.imread(image)
    if np.all(img) == None:
        print(image.split('\\')[-1])
        os.remove(image)
        rmv_cnt += 1

print('rmv_cnt:', rmv_cnt)