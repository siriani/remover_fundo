import cv2
import numpy as np
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", help = "path to the directory")
ap.add_argument("-nd", "--newdir", help = "path to the new directory")
args = vars(ap.parse_args())

folder = args["dir"]
newfolder = args["newdir"]

file_path = "./"+newfolder+"/"
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)
for file in os.listdir("./"+folder):
    if file.endswith(".JPG"):
        print(file)
	src = cv2.imread('./'+folder+'/'+file)
	tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
	b, g, r = cv2.split(src)
	rgba = [b,g,r, alpha]
	dst = cv2.merge(rgba,4)
        cv2.imwrite('./'+newfolder+'/'+file+'.png', dst)
