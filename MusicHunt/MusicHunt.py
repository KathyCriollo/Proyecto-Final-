#-----------------------------------------------
# Nombre:      Music Hunt
# Basado en:   Duck Hunt - Clasico de NES

# Autoras:     Karla Arias
#              Michelle Arias
#              Katherine Criollo
#-----------------------------------------------

import pygame
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()

negro= (0, 0, 0)
blanco= (255, 255, 255)

screen= pygame.display.set_mode((890, 550), 0, 32)

# Titulo de la Ventana
pygame.display.set_caption("Music Hunt")

# Coordenadas del Mouse
x_pos= 0
y_pos= 0

# Coordenadas del Clic
x_clic= 0
y_clic= 0

# Coordanadas de la Nota Musical
x_nota= 0
y_nota= randint(0, 450)

puntaje= 0
velocidad = 2
perder= False

# Jugador
pygame.mixer.init(44100, -16, 2, 1024)

# Musica
pygame.mixer.music.set_volume(0.8)

while True:
    for event in pygame.event.get():
        # Cierra la ventana 
        if event.type== QUIT:
            exit()
        elif event.type == MOUSEMOTION:
            x_pos, y_pos= pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONDOWN:
            x_clic, y_clic= pygame.mouse.get_pos()

    posicion= (x_pos - 50, y_pos - 50)

    x_nota += 1

    if x_nota * velocidad > 890 and not perder:
        x_nota= 0
        y_nota= randint(0, 450)

        # Game Over
        pygame.mixer.music.load("burla.mp3")
        pygame.mixer.music.play()
        perder= True

    # Fondo Negro
    screen.fill(negro)
    pygame.mouse.set_visible(False)

    # Fondo de Pantalla
    screen.blit(pygame.image.load("fondo.png"), (0, 0))
    screen.blit(pygame.font.SysFont("tahoma", 30).render("Score: " + str(puntaje), True, blanco), (500, 450))

    # Puntaje
    if x_clic in range(x_nota * velocidad - 30, x_nota * velocidad + 30) and y_clic in range(y_nota - 30, y_nota + 30):
        # Disparo
        pygame.mixer.music.load("disparo.mp3")
        pygame.mixer.music.play()

        puntaje += 10
        velocidad += 1
        x_nota= 0
        y_nota= randint(50, 500)

    screen.blit(pygame.image.load("nota.png"), (x_nota * velocidad, y_nota))

    if perder:
        x_nota = -50
        y_nota = -50
        screen.blit(pygame.image.load("burla.png"), (400, 340))

    screen.blit(pygame.image.load("mira.gif").convert(), posicion)

pygame.display.update()