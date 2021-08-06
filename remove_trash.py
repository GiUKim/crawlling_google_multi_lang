import shutil
import os
from glob import glob
import crawlling
img_dir = crawlling.base_dir + '\\datasets\\fire\\tew\\'
label_dir = crawlling.base_dir + "\\datasets\\fire\\images"

imgs = glob(img_dir + '*.jpg')

for filename in imgs:
    if not os.path.isfile(os.path.join(label_dir, filename.split('\\')[-1].split('.')[0] + '.txt')):
        os.remove(filename)