import pygame
from Constantes import *
from Funciones import *

pygame.init()

boton_volver = crear_elemento_juego("imagenes/textura_respuesta.jpg",100,40,10,10)
fondo =  pygame.transform.scale(pygame.image.load("imagenes/imagen_ranking.jpg"), PANTALLA)


def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_rankings:list) -> str:
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"
    
    pantalla.blit(fondo,(0,0))
    
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    mostrar_texto(pantalla,f"RANKING",(50,50),FUENTE_GAMEOVER,COLOR_TITULO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_RESPUESTA,COLOR_BLANCO)

    return retorno
    