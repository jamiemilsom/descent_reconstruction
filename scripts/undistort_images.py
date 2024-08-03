import os
import sys
import numpy as np
import cv2
import cv2.aruco
import json
from typing import Generator, Tuple, Optional
from src.calibration.calibrate import FisheyeCalibrator, PinholeCalibrator

ARUCO_DICT = cv2.aruco.DICT_5X5_100
SQUARES_VERTICALLY = 12
SQUARES_HORIZONTALLY = 9
SQUARE_LENGTH = 0.06
MARKER_LENGTH = 0.045
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

instaCamFisheye = FisheyeCalibrator(
    ARUCO_DICT, SQUARES_VERTICALLY, SQUARES_HORIZONTALLY, SQUARE_LENGTH, MARKER_LENGTH, 
    calibration_images_dir= os.path.join(CURRENT_PATH,'../data/calibration/images/'),
    raw_images_dir= os.path.join(CURRENT_PATH,'../data/raw_images/descent_1')
    )

instaCamPinhole = PinholeCalibrator(
    ARUCO_DICT, SQUARES_VERTICALLY, SQUARES_HORIZONTALLY, SQUARE_LENGTH, MARKER_LENGTH, 
    calibration_images_dir= os.path.join(CURRENT_PATH,'../data/calibration/images/'),
    raw_images_dir= os.path.join(CURRENT_PATH,'../data/raw_images/descent_1')
    )

instaCamFisheye.load_camera_parameters(file_path=os.path.join(CURRENT_PATH,'../data/calibration/camera_intrinsics/fisheye_calibration.json'))
instaCamPinhole.load_camera_parameters(file_path=os.path.join(CURRENT_PATH,'../data/calibration/camera_intrinsics/pinhole_calibration.json'))


for image_name, image in instaCamFisheye.raw_images.items():
    instaCamFisheye.undistort_image(image, image_name, calibration_filename = 'fisheye_calibration.json', balance = 1, show_image = False, save_image = True)
    
for image_name, image in instaCamPinhole.raw_images.items():
    instaCamPinhole.undistort_image(image, image_name, calibration_filename = 'pinhole_calibration.json', balance = 1, show_image = False, save_image = True)