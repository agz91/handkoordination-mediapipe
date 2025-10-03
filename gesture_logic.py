      if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

          # assign scale coordinate of landmark 9 (MIDDLE_FINGER_MCP) to variable
          # mp outputs hand coordinates on a scale of 0-1, 0 being one side of the screen, 1 the other.
          # both x and y coordinates are converted to pixels on the output image, in accordance with the
          # actual cap_frame_width/height as reported by cap.get
          INDEX_FINGER_TIP = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
          HANDEDNESS = results.multi_handedness 
          # calculate pixel on screen in relation to coordinate of hand (scale 0-1) (as whole number)

          coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * cap_frame_width)
          coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * cap_frame_height)



          HANDEDNESS = str(HANDEDNESS)
          HANDEDNESS_length = len(HANDEDNESS)
        

          if HANDEDNESS_length >= 100:
            x = HANDEDNESS.split("}",1)
            state = 3
          elif HANDEDNESS.find("Left") != -1:
            state = 2  
          elif HANDEDNESS.find("Right") != -1:
            state = 1
          else:
            state = 0

          # output coordinates of landmark 9 to terminal
          print("Counter:", counter)

          if counter % 2 == 0:
            INDEX_FINGER_TIP_compare1_X = coord_INDEX_FINGER_TIP_X
            INDEX_FINGER_TIP_compare1_Y = coord_INDEX_FINGER_TIP_Y
          elif counter % 2 == 1:
            INDEX_FINGER_TIP_compare2_X = coord_INDEX_FINGER_TIP_X
            INDEX_FINGER_TIP_compare2_Y = coord_INDEX_FINGER_TIP_Y

          if((abs(INDEX_FINGER_TIP_compare1_X-INDEX_FINGER_TIP_compare2_X)) <= FINGER_COMPARE_TOLERANCE and state == 3):
            statex = True
          else:
            statex = False

          if((abs(INDEX_FINGER_TIP_compare1_Y-INDEX_FINGER_TIP_compare2_Y)) <= FINGER_COMPARE_TOLERANCE and state == 3):
            statey = True
          else:
            statey = False
          
          print("State X: ",INDEX_FINGER_TIP_compare1_X," - ",INDEX_FINGER_TIP_compare2_X," = ",statex)
          print("State Y: ",INDEX_FINGER_TIP_compare1_Y," - ",INDEX_FINGER_TIP_compare2_Y," = ",statey)






if __name__ == '__main__':
  gesture_logic()