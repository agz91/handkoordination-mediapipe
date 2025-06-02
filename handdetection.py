#Source https://mediapipe.readthedocs.io/en/latest/solutions/hands.html

import cv2
import mediapipe as mp
import time
#mp_drawing = mp.solutions.drawing_utils
#mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap_frame_width = 1920
cap_frame_height = 1080


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap_frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap_frame_height)
cap_frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cap_frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

with mp_hands.Hands(
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
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        time.sleep(0.1)
        # assign scale coordinate of landmark 9 (MIDDLE_FINGER_MCP) to variable
        # mp outputs hand coordinates on a scale of 0-1, 0 being one side if the screen, 1 the other.
        # both x and y coordinates are converted to pixels on the output image, in accordance with the
        # actual cap_frame_width/height as reported by cap.get
        MIDDLE_FINGER_MCP = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
        WRIST = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
        # calculate pixel on screen in relation to coordinate of hand (scale 0-1) (as whole number)
        coord_MIDDLE_FINGER_MCP_X = int((1 - MIDDLE_FINGER_MCP.x) * cap_frame_width)
        coord_MIDDLE_FINGER_MCP_Y = int(MIDDLE_FINGER_MCP.y * cap_frame_height)

        coord_WRIST_X = int((1 - WRIST.x) * cap_frame_width)
        coord_WRIST_Y = int(WRIST.y * cap_frame_height)
        # print camera resolution for debugging purpose
        print("Width:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print("Height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # output coordinates of landmark 9 to terminal
        print("MIDDLE_FINGER_MCP:")
        print("x:", coord_MIDDLE_FINGER_MCP_X)
        print("y:", coord_MIDDLE_FINGER_MCP_Y)
        print("Wrist:")
        print("x:", coord_WRIST_X)
        print("y:", coord_WRIST_Y)
        print()

        # draw landmarks on screen
        #mp_drawing.draw_landmarks(
        #   image,
        #    hand_landmarks,
        #    mp_hands.HAND_CONNECTIONS,
        #    mp_drawing_styles.get_default_hand_landmarks_style(),
        #    mp_drawing_styles.get_default_hand_connections_style())
    # flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
        break
cv2.destroyAllWindows()
cap.release()