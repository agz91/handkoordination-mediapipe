import config

print("Importing camera_id_extractor module...\n")

def get_camera_id(gesture_id):
    if gesture_id in range(1, 5):
        return 0  # left camera
    elif gesture_id in range(5, 9):
        return 2  # right camera
    else:
        return 3  # middle camera

if __name__ == '__main__':
    get_camera_id()