import pygame
import numpy as np
#import cv2  # Wichtig für Farbkonvertierung
import random 
from handdetection_Class import Handdetection

# Pygame initialisieren
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Hand Detection")

# Handerkennung starten 
detector = Handdetection()
clock = pygame.time.Clock()

# Aufgabe laden
# Zufällige Zahl von 1 bis 4 erzeugen
image_number = random.randint(1, 4)

# Dateinamen erstellen
image_filename = f"Image{image_number}.jpg"

# Bild laden
Aufgabe = pygame.image.load(image_filename)

# Maximale Größe für die Aufgabe
max_width = 500
max_height = 500

# Originalgröße holen
orig_width, orig_height = Aufgabe.get_size()

# Skalierungsfaktor berechnen (kleinerer Faktor, um Seitenverhältnis zu erhalten)
scale_factor = min(max_width / orig_width, max_height / orig_height)

# Neue Größe berechnen (ganzzahlig)
new_width = int(orig_width * scale_factor)
new_height = int(orig_height * scale_factor)

# Aufgabe proportional skalieren
Aufgabe = pygame.transform.scale(Aufgabe, (new_width, new_height))
Aufgabe = pygame.transform.rotate(Aufgabe, 90)

# Rect aktualisieren und oben links positionieren (oder ändern, falls gewünscht)
Aufgabe_rect = Aufgabe.get_rect()
Aufgabe_rect.topleft = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    detector.get_hand_detection_frame()


    # Statt Kamera: weißen Hintergrund füllen
    screen.fill((255, 255, 255))  # Weiß

    # Aufgabe oben links zeichnen
    screen.blit(Aufgabe, Aufgabe_rect.topleft)

    # Schwarzer Rahmen über dem gesamten Fenster (sichtbar über dem Bild)
    rahmen_dicke = 10  # Dicke des äußeren Rahmens
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT), 5)

  

    pygame.display.update()
    clock.tick(30)

detector.release()
pygame.quit()



