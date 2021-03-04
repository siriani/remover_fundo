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
    if file.endswith(".jpg"):
        print(file)
        image = cv2.imread('./'+folder+'/'+file)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_green = np.array([25,40,50])
        upper_green = np.array([40, 255, 255])
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        lower_red_1 = np.array([0,40,50])
        upper_red_1 = np.array([25, 255, 255])
        lower_red_2 = np.array([140,40,50])
        upper_red_2 = np.array([180, 255, 255])
        red_mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
        red_mask_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
        red_mask = cv2.add(red_mask_1, red_mask_2)
        mask = cv2.add(green_mask,red_mask)
        res = cv2.bitwise_and(image,image, mask= mask)
        cv2.imwrite('./'+newfolder+'/'+file, res)
