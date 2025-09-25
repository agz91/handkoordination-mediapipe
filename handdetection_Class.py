import cv2
import mediapipe as mp
import time


class Handdetection:
    def __init__(self):
        self.cap_frame_width = 1920
        self.cap_frame_height = 1080
        self.counter = 0
        self.state = 0

        self.INDEX_FINGER_TIP_compare1_X = 0
        self.INDEX_FINGER_TIP_compare1_Y = 0
        self.INDEX_FINGER_TIP_compare2_X = 0
        self.INDEX_FINGER_TIP_compare2_Y = 0

        self.statex = False
        self.statey = False

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.cap_frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cap_frame_height)

        self.cap_frame_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cap_frame_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            model_complexity=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def get_hand_detection_frame(self):
        ret, image = self.cap.read()
        if not ret:
         return None
       
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False

        results = self.hands.process(image_rgb)

        image_rgb.flags.writeable = True
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                self.counter += 1
                INDEX_FINGER_TIP = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                HANDEDNESS = results.multi_handedness

                coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * self.cap_frame_width)
                coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * self.cap_frame_height)

                handedness = str(HANDEDNESS)
                handedness_length=len(handedness)
                if handedness_length >= 100:
                    x = handedness.split("}",1)
                    self.state = 3
                elif handedness.find("Left") != -1:
                    self.state = 2
                elif handedness.find("Right") != -1:
                    self.state = 1
                else:
                    self.state = 0

                print("Counter:", self.counter)

                if self.counter % 2 == 0:
                    self.INDEX_FINGER_TIP_compare1_X = coord_INDEX_FINGER_TIP_X
                    self.INDEX_FINGER_TIP_compare1_Y = coord_INDEX_FINGER_TIP_Y
                elif self.counter % 2 ==1:
                    self.INDEX_FINGER_TIP_compare2_X = coord_INDEX_FINGER_TIP_X
                    self.INDEX_FINGER_TIP_compare2_Y = coord_INDEX_FINGER_TIP_Y

                if((abs(self.INDEX_FINGER_TIP_compare1_X-self.INDEX_FINGER_TIP_compare2_X)) <= 20 and self.state == 3):
                 self.statex = True
                else:
                 self.statex = False

                if((abs(self.INDEX_FINGER_TIP_compare1_Y-self.INDEX_FINGER_TIP_compare2_Y)) <= 20 and self.state == 3):
                 self.statey = True
                else:
                 self.statey = False

                print("State X:", self.INDEX_FINGER_TIP_compare1_X, "-", self.INDEX_FINGER_TIP_compare2_X, "=", self.statex)
                print("State Y:", self.INDEX_FINGER_TIP_compare1_Y, "-", self.INDEX_FINGER_TIP_compare2_Y, "=", self.statey)

                # Optional: zeichne Landmarks (kann später für Debug-Zwecke aktiviert werden)
                mp.solutions.drawing_utils.draw_landmarks(
                 image,
                 hand_landmarks,
                 self.mp_hands.HAND_CONNECTIONS
                 )
        return image

    def release(self):
        self.cap.release()
        # Kein cv2.destroyAllWindows() mehr – Pygame übernimmt Anzeige


