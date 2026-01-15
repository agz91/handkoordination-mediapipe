import cv2
from cv2_enumerate_cameras import enumerate_cameras

def find_camera(apiprefference = cv2.CAP_MSMF):
    for camera in enumerate_cameras(apiprefference):
        if camera.name != "USB Camera" or camera.vid != 0x0BDA or camera.pid != 0x5844:
            print(f"Camera found: {camera.name} at {camera.index}")
            cam = cv2.VideoCapture(camera.index, apiprefference)
            success, image = cam.read()
            if success:
                print("Camera is operational.")
                return image
            else:
                print("Failed to read from camera.")

find_camera()


success, image = cam