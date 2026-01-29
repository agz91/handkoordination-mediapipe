import config
import cv2
from cv2_enumerate_cameras import enumerate_cameras
config.init()

def find_camera(apiprefference = cv2.CAP_MSMF, cam_id = 0):
    for camera in enumerate_cameras(apiprefference):
        if camera.name == "USB Camera" and camera.vid == 0x0BDA and camera.pid == 0x5844:
            print(f"Camera found: {camera.name} at {camera.index}")
            cam = cv2.VideoCapture(camera.index, apiprefference)
            global success, image
            success, image = cam.read()
            if success:
                print("Camera is operational.")
                return image
            else:
                print("Failed to read from camera.")

find_camera()



#success, image = config.cam[1].read()

if success:
    blue, green, red = cv2.split(image)
    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #_, threshold_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
    contours, contours_image = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        if i == 0:
            continue

        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        image = cv2.drawContours(image, [contour], 0, (0, 0, 255), 5)

        # Find center
        M = cv2.moments(contour)
        if M['m00'] != 0:
            x = int(M['m10'] / M['m00'])
            y = int(M['m01'] / M['m00'])

        # Detect shape
        sides = len(approx)
        if sides == 3:
            label = 'Triangle'
        elif sides == 4:
            label = 'Quadrilateral'
        elif sides == 5:
            label = 'Pentagon'
        elif sides == 6:
            label = 'Hexagon'
        else:
            label = 'Circle'
        # Label the shape
        print(f"Detected shape: {label}")
        #cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Shapes Detected", red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()