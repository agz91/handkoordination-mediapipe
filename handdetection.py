import cv2
import mediapipe as mp
print("Loading Handdetection module...\n")

mp_hands = mp.solutions.hands

#adjust according to camera
cap_frame_width = 1920
cap_frame_height = 1080
counter = 0
#INDEX_FINGER_TIP_compare1_Z = 0
#INDEX_FINGER_TIP_compare2_Z = 0
FINGER_COMPARE_TOLERANCE = 20
statex = False
statey = False
#statez = False

print("Initializing Camera...\n")
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap_frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap_frame_height)
cap_frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cap_frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Camera initialized!\n")

def Handdetection():
  global counter
  with mp_hands.Hands(
      static_image_mode=False,
      max_num_hands=2,
      model_complexity=1,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        continue

      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image = cv2.flip(image, 1)
      results = hands.process(image)
      return results




if __name__ == '__main__':
  Handdetection()