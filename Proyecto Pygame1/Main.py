import pygame 
import random
from Constantes import *
from Menu import *
from Juego import *
from Ajustes import *
from Rankings import *
from GameOver import *


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Quiz de Futbol")
icono = pygame.image.load("imagenes/icono.png")
pygame.display.set_icon(icono)
 
pantalla = pygame.display.set_mode(PANTALLA)
corriendo = True
datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","tiempo_restante":TIEMPO_JUEGO,"volumen_musica":10,"musica_activada":True,"indice":0}
pygame.mixer.music.load("sonidos/musica.mp3")  
pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)  
pygame.mixer.music.play(-1) 
random.shuffle(lista_preguntas)

lista_rankings = []
reloj = pygame.time.Clock()
ventana_actual = "menu"

bandera_juego = False

datos_juego = {
    "puntuacion": 0,
    "vidas": CANTIDAD_VIDAS,
    "nombre": "",
    "tiempo_restante": TIEMPO_JUEGO,
    "indice": 0,
    "correctas_seguidas": 0,
    "volumen_musica": 50,
    "volumen_efectos": 50,
    "musica_activada": True
}

while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "salir":
        corriendo = False
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos,lista_rankings)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "juego":
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego,lista_preguntas)
    elif ventana_actual == "terminado":
        if bandera_juego == True:
            bandera_juego = False
            pygame.mixer.music.stop()
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego)
    
    pygame.display.flip()

pygame.quit()