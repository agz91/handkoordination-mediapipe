import pygame
import numpy as np
import cv2  # Wichtig für Farbkonvertierung
from handdetection_Class import Handdetection

# Pygame initialisieren
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Hand Detection")

# Handerkennung starten
detector = Handdetection()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame = detector.get_hand_detection_frame()
    if frame is not None:
        # Konvertiere BGR → RGB, bevor du es Pygame übergibst
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Drehe das Bild, falls nötig (Kamera-Ausrichtung)
        frame = np.rot90(frame)

        # Erzeuge Pygame-Oberfläche aus NumPy-Array
        frame_surface = pygame.surfarray.make_surface(frame)

        # Zeige es im Fenster an
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

    clock.tick(30)

# Aufräumen
detector.release()
pygame.quit()
