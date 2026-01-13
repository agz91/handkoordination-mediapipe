import config

print("Importing gesture_logic module...\n")

def gesture_logic(gesture_id, Handdetection_results):
	print("Processing gesture logic for gesture ID:", gesture_id, "\n")
	counter = 0
	match gesture_id:
		case 1:
			# right: thumb, pinky
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness
					counter += 1
					coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
					coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

					HANDEDNESS = str(HANDEDNESS)
					HANDEDNESS_length = len(HANDEDNESS)

					if HANDEDNESS.find("Right") == -1 and HANDEDNESS.find("Left") != -1:
						return False

					if((abs(coord_PINKY_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
						statex = True
					else:
						statex = False

					if((abs(coord_PINKY_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
						statey = True
					else:
						statey = False
					print("State X: ",coord_PINKY_TIP_X," - ",coord_THUMB_TIP_X," = ",statex)
					print("State Y: ",coord_PINKY_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
					if (statex and statey):
						return True
					else:
						return False

		case 2:
			#right: thumb, ring
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness
					counter += 1
					coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
					coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

					HANDEDNESS = str(HANDEDNESS)
					HANDEDNESS_length = len(HANDEDNESS)

					if HANDEDNESS.find("Right") == -1 and HANDEDNESS.find("Left") != -1:
						return False

					if((abs(coord_RING_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
						statex = True
					else:
						statex = False

					if((abs(coord_RING_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
						statey = True
					else:
						statey = False
					print("State X: ",coord_RING_FINGER_TIP_X," - ",coord_RING_FINGER_TIP_X," = ",statex)
					print("State Y: ",coord_RING_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
					if (statex and statey):
						return True
					else:
						return False

		case 3:
			#right: thumb, middle
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness
					counter += 1

					coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
					coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

					HANDEDNESS = str(HANDEDNESS)
					HANDEDNESS_length = len(HANDEDNESS)

					if HANDEDNESS.find("Right") == -1 and HANDEDNESS.find("Left") != -1:
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

		case 4:
			#right: thumb, index
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness
					counter += 1
					coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
					coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

					HANDEDNESS = str(HANDEDNESS)
					HANDEDNESS_length = len(HANDEDNESS)

					if HANDEDNESS.find("Right") == -1 and HANDEDNESS.find("Left") != -1:
						return False

					if((abs(coord_INDEX_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
						statex = True
					else:
						statex = False

					if((abs(coord_INDEX_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
						statey = True
					else:
						statey = False
					print("State X: ",coord_INDEX_FINGER_TIP_X," - ",coord_INDEX_FINGER_TIP_X," = ",statex)
					print("State Y: ",coord_INDEX_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
					if (statex and statey):
						return True
					else:
						return False

		case 5:
			#left: thumb, index
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness
					counter += 1
					coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
					coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

					HANDEDNESS = str(HANDEDNESS)
					HANDEDNESS_length = len(HANDEDNESS)

					if HANDEDNESS.find("Right") != -1 and HANDEDNESS.find("Left") == -1:
						return False

					if((abs(coord_INDEX_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
						statex = True
					else:
						statex = False

					if((abs(coord_INDEX_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
						statey = True
					else:
						statey = False
					print("State X: ",coord_INDEX_FINGER_TIP_X," - ",coord_INDEX_FINGER_TIP_X," = ",statex)
					print("State Y: ",coord_INDEX_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
					if (statex and statey):
						return True
					else:
						return False

		case 6:
			#left: thumb, middle
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness
					counter += 1

					coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
					coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

					HANDEDNESS = str(HANDEDNESS)
					HANDEDNESS_length = len(HANDEDNESS)

					if HANDEDNESS.find("Right") != -1 and HANDEDNESS.find("Left") == -1:
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
			
		case 7:
			#left: thumb, ring
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness
					counter += 1
					coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
					coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

					HANDEDNESS = str(HANDEDNESS)
					HANDEDNESS_length = len(HANDEDNESS)

					if HANDEDNESS.find("Right") != -1 and HANDEDNESS.find("Left") == -1:
						return False

					if((abs(coord_RING_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
						statex = True
					else:
						statex = False

					if((abs(coord_RING_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
						statey = True
					else:
						statey = False
					print("State X: ",coord_RING_FINGER_TIP_X," - ",coord_RING_FINGER_TIP_X," = ",statex)
					print("State Y: ",coord_RING_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
					if (statex and statey):
						return True
					else:
						return False

		case 8:
			#left: thumb, pinky
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness
					counter += 1
					coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
					coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

					HANDEDNESS = str(HANDEDNESS)
					HANDEDNESS_length = len(HANDEDNESS)

					if HANDEDNESS.find("Right") != -1 and HANDEDNESS.find("Left") == -1:
						return False

					if((abs(coord_PINKY_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
						statex = True
					else:
						statex = False

					if((abs(coord_PINKY_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
						statey = True
					else:
						statey = False
					print("State X: ",coord_PINKY_TIP_X," - ",coord_THUMB_TIP_X," = ",statex)
					print("State Y: ",coord_PINKY_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
					if (statex and statey):
						return True
					else:
						return False

		case 9:
			#right: thumb
			#left: thumb
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness 
					counter += 1
					coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
					coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

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

					if counter % 2 == 1:
						THUMB_TIP_compare1_X = coord_THUMB_TIP_X
						THUMB_TIP_compare1_Y = coord_THUMB_TIP_Y
					elif counter % 2 == 0:
						THUMB_TIP_compare2_X = coord_THUMB_TIP_X
						THUMB_TIP_compare2_Y = coord_THUMB_TIP_Y

					if (counter % 2 == 0):
						if((abs(THUMB_TIP_compare1_X-THUMB_TIP_compare2_X)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statex = True
						else:
							statex = False

						if((abs(THUMB_TIP_compare1_Y-THUMB_TIP_compare2_Y)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statey = True
						else:
							statey = False

						print("State X: ",THUMB_TIP_compare1_X," - ",THUMB_TIP_compare2_X," = ",statex)
						print("State Y: ",THUMB_TIP_compare1_Y," - ",THUMB_TIP_compare2_Y," = ",statey)

						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 10:
			#left: thumb
			#right: index
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int((INDEX_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int((INDEX_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_INDEX_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_INDEX_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_INDEX_FINGER_TIP_X," - ",coord_THUMB_TIP_X," = ",statex)
						print("State Y: ",coord_INDEX_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False
 
		case 11:
			#left: thumb
			#right: middle
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int((MIDDLE_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int((MIDDLE_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_MIDDLE_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_MIDDLE_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_MIDDLE_FINGER_TIP_X," - ",coord_THUMB_TIP_X," = ",statex)
						print("State Y: ",coord_MIDDLE_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 12:
			#left: thumb
			#right: ring
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int((RING_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int((RING_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_RING_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_RING_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_RING_FINGER_TIP_X," - ",coord_THUMB_TIP_X," = ",statex)
						print("State Y: ",coord_RING_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 13:
			#left: thumb
			#right: pinky
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int((PINKY_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int((PINKY_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_PINKY_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_PINKY_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_PINKY_TIP_X," - ",coord_THUMB_TIP_X," = ",statex)
						print("State Y: ",coord_PINKY_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 14:
			#left: index
			#right: thumb
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int((THUMB_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int((THUMB_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_THUMB_TIP_X-coord_INDEX_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_THUMB_TIP_Y-coord_INDEX_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_THUMB_TIP_X," - ",coord_INDEX_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_THUMB_TIP_Y," - ",coord_INDEX_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 15:
			# left: index
			# right: index
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness

					counter += 1
					coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
					coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)

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

					if counter % 2 == 1:
						INDEX_FINGER_TIP_compare1_X = coord_INDEX_FINGER_TIP_X
						INDEX_FINGER_TIP_compare1_Y = coord_INDEX_FINGER_TIP_Y
					elif counter % 2 == 0:
						INDEX_FINGER_TIP_compare2_X = coord_INDEX_FINGER_TIP_X
						INDEX_FINGER_TIP_compare2_Y = coord_INDEX_FINGER_TIP_Y

					if (counter % 2 == 0):
						if((abs(INDEX_FINGER_TIP_compare1_X-INDEX_FINGER_TIP_compare2_X)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statex = True
						else:
							statex = False

						if((abs(INDEX_FINGER_TIP_compare1_Y-INDEX_FINGER_TIP_compare2_Y)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statey = True
						else:
							statey = False

						print("State X: ",INDEX_FINGER_TIP_compare1_X," - ",INDEX_FINGER_TIP_compare2_X," = ",statex)
						print("State Y: ",INDEX_FINGER_TIP_compare1_Y," - ",INDEX_FINGER_TIP_compare2_Y," = ",statey)

						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 16:
			#left: index
			#right: middle
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int((MIDDLE_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int((MIDDLE_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_MIDDLE_FINGER_TIP_X-coord_INDEX_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_MIDDLE_FINGER_TIP_Y-coord_INDEX_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_MIDDLE_FINGER_TIP_X," - ",coord_INDEX_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_MIDDLE_FINGER_TIP_Y," - ",coord_INDEX_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 17:
			#left: index
			#right: ring
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int((RING_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int((RING_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_RING_FINGER_TIP_X-coord_INDEX_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_RING_FINGER_TIP_Y-coord_INDEX_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_RING_FINGER_TIP_X," - ",coord_INDEX_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_RING_FINGER_TIP_Y," - ",coord_INDEX_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False
			
		case 18:

			#left: index
			#right: pinky
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int((PINKY_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int((PINKY_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_PINKY_TIP_X-coord_INDEX_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_PINKY_TIP_Y-coord_INDEX_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_PINKY_TIP_X," - ",coord_INDEX_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_PINKY_TIP_Y," - ",coord_INDEX_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 19:
			#left: middle
			#right: thumb
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int((THUMB_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int((THUMB_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_THUMB_TIP_X-coord_MIDDLE_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_THUMB_TIP_Y-coord_MIDDLE_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_THUMB_TIP_X," - ",coord_MIDDLE_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_THUMB_TIP_Y," - ",coord_MIDDLE_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 20:
			#left: middle
			#right: index
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int((INDEX_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int((INDEX_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_INDEX_FINGER_TIP_X-coord_MIDDLE_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_INDEX_FINGER_TIP_Y-coord_MIDDLE_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_INDEX_FINGER_TIP_X," - ",coord_MIDDLE_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_INDEX_FINGER_TIP_Y," - ",coord_MIDDLE_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 21:
			#left: middle
			#right: middle
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness

					counter += 1
					coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
					coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)

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

					if counter % 2 == 1:
						MIDDLE_FINGER_TIP_compare1_X = coord_MIDDLE_FINGER_TIP_X
						MIDDLE_FINGER_TIP_compare1_Y = coord_MIDDLE_FINGER_TIP_Y
					elif counter % 2 == 0:
						MIDDLE_FINGER_TIP_compare2_X = coord_MIDDLE_FINGER_TIP_X
						MIDDLE_FINGER_TIP_compare2_Y = coord_MIDDLE_FINGER_TIP_Y

					if (counter % 2 == 0):
						if((abs(MIDDLE_FINGER_TIP_compare1_X-MIDDLE_FINGER_TIP_compare2_X)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statex = True
						else:
							statex = False

						if((abs(MIDDLE_FINGER_TIP_compare1_Y-MIDDLE_FINGER_TIP_compare2_Y)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statey = True
						else:
							statey = False

						print("State X: ",MIDDLE_FINGER_TIP_compare1_X," - ",MIDDLE_FINGER_TIP_compare2_X," = ",statex)
						print("State Y: ",MIDDLE_FINGER_TIP_compare1_Y," - ",MIDDLE_FINGER_TIP_compare2_Y," = ",statey)

						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 22:
			#left: middle
			#right: ring
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1
 
					if (state == 0 and counter == 1):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int((RING_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int((RING_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_RING_FINGER_TIP_X-coord_MIDDLE_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_RING_FINGER_TIP_Y-coord_MIDDLE_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_RING_FINGER_TIP_X," - ",coord_MIDDLE_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_RING_FINGER_TIP_Y," - ",coord_MIDDLE_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 23:
			#left: middle
			#right: pinky
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1

				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int((PINKY_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int((PINKY_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_PINKY_TIP_X-coord_MIDDLE_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_PINKY_TIP_Y-coord_MIDDLE_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_PINKY_TIP_X," - ",coord_MIDDLE_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_PINKY_TIP_Y," - ",coord_MIDDLE_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 24:
			#left: ring
			#right: thumb
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int((THUMB_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int((THUMB_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_THUMB_TIP_X-coord_RING_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_THUMB_TIP_Y-coord_RING_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_THUMB_TIP_X," - ",coord_RING_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_THUMB_TIP_Y," - ",coord_RING_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 25:
			#left: ring
			#right: index
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int((INDEX_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int((INDEX_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_INDEX_FINGER_TIP_X-coord_RING_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_INDEX_FINGER_TIP_Y-coord_RING_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_INDEX_FINGER_TIP_X," - ",coord_RING_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_INDEX_FINGER_TIP_Y," - ",coord_RING_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 26:
			#left: ring
			#right: middle
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int((MIDDLE_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int((MIDDLE_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_MIDDLE_FINGER_TIP_X-coord_RING_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_MIDDLE_FINGER_TIP_Y-coord_RING_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_MIDDLE_FINGER_TIP_X," - ",coord_RING_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_MIDDLE_FINGER_TIP_Y," - ",coord_RING_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 27:
			#left: ring
			#right: ring
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness

					counter += 1
					coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
					coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)

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

					if counter % 2 == 1:
						RING_FINGER_TIP_compare1_X = coord_RING_FINGER_TIP_X
						RING_FINGER_TIP_compare1_Y = coord_RING_FINGER_TIP_Y
					elif counter % 2 == 0:
						RING_FINGER_TIP_compare2_X = coord_RING_FINGER_TIP_X
						RING_FINGER_TIP_compare2_Y = coord_RING_FINGER_TIP_Y

					if (counter % 2 == 0):
						if((abs(RING_FINGER_TIP_compare1_X-RING_FINGER_TIP_compare2_X)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statex = True
						else:
							statex = False

						if((abs(RING_FINGER_TIP_compare1_Y-RING_FINGER_TIP_compare2_Y)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statey = True
						else:
							statey = False

						print("State X: ",RING_FINGER_TIP_compare1_X," - ",RING_FINGER_TIP_compare2_X," = ",statex)
						print("State Y: ",RING_FINGER_TIP_compare1_Y," - ",RING_FINGER_TIP_compare2_Y," = ",statey)

						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 28:
			#left: ring
			#right: pinky
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int((PINKY_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int((PINKY_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_PINKY_TIP_X-coord_RING_FINGER_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_PINKY_TIP_Y-coord_RING_FINGER_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_PINKY_TIP_X," - ",coord_RING_FINGER_TIP_X," = ",statex)
						print("State Y: ",coord_PINKY_TIP_Y," - ",coord_RING_FINGER_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 29:
			#left: pinky
			#right: thumb
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int((THUMB_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
						coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
						coord_THUMB_TIP_Y = int((THUMB_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_THUMB_TIP_X-coord_PINKY_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_THUMB_TIP_Y-coord_PINKY_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_THUMB_TIP_X," - ",coord_PINKY_TIP_X," = ",statex)
						print("State Y: ",coord_THUMB_TIP_Y," - ",coord_PINKY_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 30:
			#left: pinky
			#right: index
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int((INDEX_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
						coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
						coord_INDEX_FINGER_TIP_Y = int((INDEX_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_INDEX_FINGER_TIP_X-coord_PINKY_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_INDEX_FINGER_TIP_Y-coord_PINKY_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_INDEX_FINGER_TIP_X," - ",coord_PINKY_TIP_X," = ",statex)
						print("State Y: ",coord_INDEX_FINGER_TIP_Y," - ",coord_PINKY_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 31:
			#left: pinky
			#right: middle
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int((MIDDLE_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
						coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
						coord_MIDDLE_FINGER_TIP_Y = int((MIDDLE_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_MIDDLE_FINGER_TIP_X-coord_PINKY_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_MIDDLE_FINGER_TIP_Y-coord_PINKY_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_MIDDLE_FINGER_TIP_X," - ",coord_PINKY_TIP_X," = ",statex)
						print("State Y: ",coord_MIDDLE_FINGER_TIP_Y," - ",coord_PINKY_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 32:
			#left: pinky
			#right: ring
			if Handdetection_results.multi_hand_landmarks:
				HANDEDNESS = str(Handdetection_results.multi_handedness)
				HANDEDNESS_length = len(HANDEDNESS)
				HANDEDNESS_list = HANDEDNESS.split( "}" , 1 )
				if (HANDEDNESS_length <= 100):
					return False
				if (HANDEDNESS_list[0].find("Right") != -1):
					state = 0
				elif (HANDEDNESS_list[0].find("Left") != -1):
					state = 1
 
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					counter += 1

					if (state == 0 and counter == 1):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int((RING_FINGER_TIP.y) * config.cap_frame_height)
					if (state == 0 and counter == 2):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 1):
						PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
						coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
						coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
					if (state == 1 and counter == 2):
						RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
						coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
						coord_RING_FINGER_TIP_Y = int((RING_FINGER_TIP.y) * config.cap_frame_height)
 
					if (counter == 2):
						if((abs(coord_RING_FINGER_TIP_X-coord_PINKY_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
							statex = True
						else:
							statex = False
 
						if((abs(coord_RING_FINGER_TIP_Y-coord_PINKY_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
							statey = True
						else:
							statey = False
 
						print("State X: ",coord_RING_FINGER_TIP_X," - ",coord_PINKY_TIP_X," = ",statex)
						print("State Y: ",coord_RING_FINGER_TIP_Y," - ",coord_PINKY_TIP_Y," = ",statey)
 
						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

		case 33:
			# left: pinky
			# right: pinky
			if Handdetection_results.multi_hand_landmarks:
				for hand_landmarks in Handdetection_results.multi_hand_landmarks:
					PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
					HANDEDNESS = Handdetection_results.multi_handedness

					counter += 1
					coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
					coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)

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

					if counter % 2 == 1:
						PINKY_TIP_compare1_X = coord_PINKY_TIP_X
						PINKY_TIP_compare1_Y = coord_PINKY_TIP_Y
					elif counter % 2 == 0:
						PINKY_TIP_compare2_X = coord_PINKY_TIP_X
						PINKY_TIP_compare2_Y = coord_PINKY_TIP_Y

					if (counter % 2 == 0):
						if((abs(PINKY_TIP_compare1_X-PINKY_TIP_compare2_X)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statex = True
						else:
							statex = False

						if((abs(PINKY_TIP_compare1_Y-PINKY_TIP_compare2_Y)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
							statey = True
						else:
							statey = False

						print("State X: ",PINKY_TIP_compare1_X," - ",PINKY_TIP_compare2_X," = ",statex)
						print("State Y: ",PINKY_TIP_compare1_Y," - ",PINKY_TIP_compare2_Y," = ",statey)

						if (statex and statey and counter == 2):
							return True
						elif (counter == 2):
							return False

if __name__ == '__main__':
	gesture_logic()