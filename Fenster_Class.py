import pygame
import random



class Fenster:
    def draw_button (fenster, platz, text, Schrift,b_farbe,t_farbe):
        pygame.draw.rect(fenster,b_farbe,platz)
        b_text = Schrift.render(text,True,t_farbe)
        text_platz = b_text.get_rect(center=platz.center)
        fenster.blit(b_text, text_platz)

    def lade_zufaellige_aufgabe(letzte_nummer,modus_wahl, max_weite=500, max_hoehe=500):
        
        if modus_wahl == "rechts":
            Bild_Nummer = random.randint(1,4)
            while Bild_Nummer == letzte_nummer:
                Bild_Nummer = random.randint(1,4)
            letzte_nummer=Bild_Nummer
        elif modus_wahl == "links":
            Bild_Nummer = random.randint(5,8)
            while Bild_Nummer == letzte_nummer:
                Bild_Nummer = random.randint(5,8)
            letzte_nummer=Bild_Nummer
        elif modus_wahl == "beide":
            Bild_Nummer = random.randint(9,33)
            while Bild_Nummer == letzte_nummer:
                Bild_Nummer = random.randint(9,33)
            letzte_nummer=Bild_Nummer
        elif modus_wahl == "alle":
            Bild_Nummer = random.randint(1,33)
            while Bild_Nummer == letzte_nummer:
                Bild_Nummer = random.randint(1,33)
            letzte_nummer=Bild_Nummer

        Bild_Datei = f"Image{Bild_Nummer}.jpg"
        Aufgabe = pygame.image.load(Bild_Datei)

        orig_weite, orig_hoehe =Aufgabe.get_size()
        skal_faktor = min(max_weite / orig_weite, max_hoehe/orig_hoehe)
        neue_weite = int(orig_weite * skal_faktor)
        neue_hoehe = int(orig_hoehe * skal_faktor)

        Aufgabe = pygame.transform.scale(Aufgabe, (neue_weite, neue_hoehe))

        Aufgabe_platz = Aufgabe.get_rect()

        return Aufgabe, Aufgabe_platz, letzte_nummer
    
    Timer_Eingabe=""
    
    def start_screen(F_Weite, F_Hoehe, fenster, Zeit, Schrift, modus_wahl):
        b_schrift = pygame.font.SysFont(None, 60)
        b_schrift_auswahl = pygame.font.SysFont(None, 45)

        button_weite, button_hoehe = 250, 150
        abstand = 15

        b_start = pygame.Rect((F_Weite - 350)//2, (F_Hoehe - 200)//2, 350, 200)

        b_rechts = pygame.Rect(F_Weite - button_weite - abstand, abstand, button_weite, button_hoehe/2)
        b_links = pygame.Rect(F_Weite - button_weite - abstand, abstand + (button_hoehe/2 + abstand), button_weite, button_hoehe/2)
        b_beide = pygame.Rect(F_Weite - button_weite - abstand, abstand + 2*(button_hoehe/2 + abstand), button_weite, button_hoehe/2)
        b_alle = pygame.Rect(F_Weite - button_weite - abstand, abstand + 3*(button_hoehe/2 + abstand), button_weite, button_hoehe/2)

        buttons = [
            (b_rechts, "Rechte Hand", "rechts"),
            (b_links, "Linke Hand", "links"),
            (b_beide, "Beide Hände", "beide"),
            (b_alle, "Alle", "alle")
        ]

        f_inaktiv = (0,0,0)
        f_aktiv = (0,200,0)
        f_fehler = (255,0,0)
        farbe = f_inaktiv

        # Timer-Feld
        z_feld = pygame.Rect(550,100,200,50)
        aktiv = False
        timerfehler = False

        # Namensfeld
        name_feld = pygame.Rect(550, 200, 300, 50)
        name_aktiv = False
        Spieler_Name = ""

        # Timer-Eingabe initialisieren, falls noch nicht vorhanden
        if not hasattr(Fenster, "Timer_Eingabe"):
            Fenster.Timer_Eingabe = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Modus auswählen
                    for rect, text, mode in buttons:
                        if rect.collidepoint(event.pos):
                            modus_wahl = mode
                            break

                    # Start-Button
                    if b_start.collidepoint(event.pos):
                        try:
                            Timer_wert = int(Fenster.Timer_Eingabe)
                        except ValueError:
                            Timer_wert = 0
                        if Timer_wert > 0 and modus_wahl is not None and Spieler_Name != "":
                            return modus_wahl, Spieler_Name
                        else:
                            farbe = f_fehler
                            timerfehler = True

                    # Timer-Feld aktivieren
                    if z_feld.collidepoint(event.pos):
                        aktiv = True
                    else:
                        aktiv = False

                    # Namensfeld aktivieren
                    if name_feld.collidepoint(event.pos):
                        name_aktiv = True
                    else:
                        name_aktiv = False

                elif event.type == pygame.KEYDOWN:
                    # Timer-Feld bearbeiten
                    if aktiv:
                        if event.key == pygame.K_BACKSPACE:
                            Fenster.Timer_Eingabe = Fenster.Timer_Eingabe[:-1]
                        else:
                            Fenster.Timer_Eingabe += event.unicode
                    # Namensfeld bearbeiten
                    if name_aktiv:
                        if event.key == pygame.K_BACKSPACE:
                            Spieler_Name = Spieler_Name[:-1]
                        else:
                            Spieler_Name += event.unicode

            fenster.fill((255,255,255))

            # Modus-Buttons zeichnen
            for rect, text, mode in buttons:
                farbe_button = f_aktiv if modus_wahl == mode else f_inaktiv
                Fenster.draw_button(fenster, rect, text, b_schrift_auswahl, farbe_button, (255,255,255))

            # Start-Button
            Fenster.draw_button(fenster, b_start, "Starten", b_schrift, (0,100,0), (255,255,255))

            # Timer-Feld horizontal mittig, senkrecht ausgerichtet
            z_feld.width = 200  # Breite des Feldes
            z_feld.height = 50  # Höhe des Feldes
            z_feld.x = (F_Weite - z_feld.width) // 2  # horizontal mittig
            z_feld.y = 50  # gleiche Höhe wie Namensfeld

            # Feld zeichnen
            farbe_timer = f_aktiv if aktiv else f_inaktiv
            pygame.draw.rect(fenster, farbe_timer, z_feld, 2)

            # Text im Feld
            text_surface = Schrift.render(Fenster.Timer_Eingabe, True, (0,0,0))
            fenster.blit(text_surface, (z_feld.x + 5, z_feld.y + 5))

            # Label "Timer:" oberhalb des Feldes
            timer_text = Schrift.render("Timer:", True, (0,0,0))
            fenster.blit(timer_text, (z_feld.x, z_feld.y - 35))  # 35 Pixel oberhalb


            # Namensfeld senkrecht ausrichten
            name_feld.x = 50  # horizontale Position
            name_feld.y = 50  # vertikale Position des Feldes

            # Feld zeichnen
            farbe_name = f_aktiv if name_aktiv else f_inaktiv
            pygame.draw.rect(fenster, farbe_name, name_feld, 2)

            # Text im Feld
            name_text_surface = Schrift.render(Spieler_Name, True, (0,0,0))
            fenster.blit(name_text_surface, (name_feld.x + 5, name_feld.y + 5))

            # Label "Name:" oberhalb des Feldes
            name_label = Schrift.render("Name:", True, (0,0,0))
            fenster.blit(name_label, (name_feld.x, name_feld.y - 35))  # 35 Pixel über dem Feld

            # Fehlerhinweis
            if timerfehler:
                fehler_text = Schrift.render("!!!Zeit, Modus und Name festlegen!!!", True, (255,0,0))
                fenster.blit(fehler_text, (F_Weite//2 - fehler_text.get_width()//2, 150))

            pygame.display.update()

            
    def end_screen(punkte, F_Weite, F_Hoehe, fenster,Zeit, Spieler_Name, highscores):
        p_schrift = pygame.font.SysFont(None, 72)
        b_schrift = pygame.font.SysFont(None, 60)
        button_weite, button_hoehe, Abstand= 350, 200, 50
        b_restart = pygame.Rect((F_Weite - (2*button_weite+Abstand))//2, (F_Hoehe-button_hoehe)//2, button_weite, button_hoehe) 
        b_ende = pygame.Rect(b_restart.right + Abstand, (F_Hoehe-button_hoehe)//2, button_weite, button_hoehe) 

        # Punkte zur Highscore-Liste hinzufügen
        highscores.append({"name": Spieler_Name, "score": punkte})
        highscores.sort(key=lambda x: x["score"], reverse=True)
        highscores = highscores[:5]  # nur Top 5 behalten

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b_restart.collidepoint(event.pos):
                        pygame.display.set_mode((F_Weite,F_Hoehe))
                        pygame.display.set_caption("Hand Detection")
                        return "Neustart", highscores
                    if b_ende.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            fenster.fill((255,255,255))

            # Punkte
            p_text=p_schrift.render(f"Punkte: {punkte}",True,(0,0,0))
            p_platz=p_text.get_rect(center=(F_Weite//2,80))
            fenster.blit(p_text,p_platz)

            # Highscore-Anzeige
            hs_title = p_schrift.render("Highscore:", True, (0,0,0))
            fenster.blit(hs_title, (50, 50))
            y_offset = 120
            for entry in highscores:
                text = b_schrift.render(f"{entry['name']}: {entry['score']}", True, (0,0,0))
                fenster.blit(text, (50, y_offset))
                y_offset += 50

            # Buttons
            Fenster.draw_button(fenster,b_restart,"Neustart",b_schrift,(0,0,150),(255,255,255))
            Fenster.draw_button(fenster,b_ende,"Beenden",b_schrift,(150,0,0),(255,255,255))

            pygame.display.update()
