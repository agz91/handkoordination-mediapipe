import config
import cv2

def test_find_camera(apiprefference = cv2.CAP_MSMF):
    config.cam = [None, None, None]  # Reset camera list
    config.cam[0] = cv2.VideoCapture(0, apiprefference)  # Initialize camera 0 for testing