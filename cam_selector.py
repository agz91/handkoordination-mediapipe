import config
import cv2
from cv2_enumerate_cameras import enumerate_cameras

print("Importing Camera Selector module...\n")

def find_camera(apiprefference = cv2.CAP_MSMF, cam_id = 0, image = [None, None, None]):
    for camera in enumerate_cameras(apiprefference):
        if camera.name == "USB Camera" and camera.vid == 0x0BDA and camera.pid == 0x5844:
            print(f"Camera found: {camera.name} at {camera.index}")
            config.cam[cam_id] = cv2.VideoCapture(camera.index, apiprefference)
            config.cam[cam_id].set(cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
            config.cam[cam_id].set(cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)
            success, image[cam_id] = config.cam[cam_id].read()
            if success:
                print(f"Camera {cam_id} is operational.")
            else:
                print(f"Failed to read from camera {cam_id}.")
            cam_id += 1
    return image

if __name__ == '__main__':
	find_camera()