import pygame

class Design:
 
# Pygame initialisieren
    pygame.init()

# Fenster erstellen
screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Bild einfügen mit Pygame")

# Bild laden
image = pygame.image.load("Image.png")  # Ersetze 'bild.png' mit dem Pfad zu deinem Bild

# Hauptschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # # Bildschirm mit einer Farbe füllen (optional)
    # screen.fill((255, 255, 255))  # Weißer Hintergrund

    # Bild zeichnen
    screen.blit(image, (50, 50))  # Position (100, 100)

    # Bildschirm aktualisieren
    pygame.display.flip()

# Pygame beenden
pygame.quit()
