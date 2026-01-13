import config

print("Importing camera_id_extractor module...\n")

def get_camera_id(gesture_id):
    if gesture_id in range(1, 5):
        print ("Right camera selected.\n")
        return 0  # right camera
    elif gesture_id in range(5, 9):
        print ("Left camera selected.\n")
        return 1  # left camera
    else:
        print ("Middle camera selected.\n")
        return 2  # middle camera

if __name__ == '__main__':
    get_camera_id()