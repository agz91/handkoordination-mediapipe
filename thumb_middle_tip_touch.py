import config

print("Importing MIDDLE_THUMB_TIP_TOUCH module...\n")

counter = 0 



def THUMB_MIDDLE_TIP_TOUCH(Handdetection_results):
  MIDDLE_FINGER_TIP_compare_X = 1
  MIDDLE_FINGER_compare_Y = 1
  THUMB_TIP_compare_X = 1
  THUMB_TIP_compare_Y = 1
  counter = 0
  if Handdetection_results.multi_hand_landmarks:
    for hand_landmarks in Handdetection_results.multi_hand_landmarks:
      MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
      THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
      HANDEDNESS = Handdetection_results.multi_handedness
      # calculate pixel on screen in relation to coordinate of hand (scale 0-1) (as whole number)
      counter += 1
      coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
      coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
      coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
      coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

      HANDEDNESS = str(HANDEDNESS)
      HANDEDNESS_length = len(HANDEDNESS)

      if HANDEDNESS.find("Right") != -1 and HANDEDNESS.find("Left") == -1:
        pass
      else:
        return False

      if((abs(coord_MIDDLE_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
        statex = True
      else:
        statex = False

      if((abs(coord_MIDDLE_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
        statey = True
      else:
        statey = False
      print("State X: ",coord_MIDDLE_FINGER_TIP_X," - ",coord_MIDDLE_FINGER_TIP_X," = ",statex)
      print("State Y: ",coord_MIDDLE_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
      if (statex and statey):
        return True
      else:
        return False



if __name__ == '__main__':
  THUMB_MIDDLE_TIP_TOUCH()