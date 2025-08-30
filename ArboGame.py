
import pygame
import sys

class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre)
    if subarbol:
        subarbol.hijos.append(Arbol(elemento))

def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if arbolBuscado:
            return arbolBuscado
    return None

# Datos del árbol
abuela = "Inocenta"
hija1 = "Deliao"
hija2 = "Santos"
hija3 = "Vicenta"
#neto1 = "Ramiro"
nieta2 = "Norma"
nieta3 = "Rocio"
nieto4 = "Rosario"
nieto5 = "Julio"    
nieto6 = "Manuel"    
arbol = Arbol(abuela)

agregarElemento(arbol, hija2, abuela)
agregarElemento(arbol, hija3, abuela)
#gregarElemento(arbol, nieto5, hija3)
agregarElemento(arbol, nieto4, hija2)
agregarElemento(arbol, hija1, abuela)
#gregarElemento(arbol, nieto1, hija1)
agregarElemento(arbol, nieta2, hija1)
agregarElemento(arbol, nieta3, hija1)
agregarElemento(arbol, nieto6, hija1)



# Pygame
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Árbol Genealógico de Inocenta Arce")
fuente = pygame.font.SysFont(None, 24)

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (100, 149, 237)

ESPACIO_X = 120
ESPACIO_Y = 100
RADIO = 30
posiciones = {}

def calcular_posiciones(nodo, x, y):
    posiciones[nodo.elemento] = (x, y)
    total_hijos = len(nodo.hijos)
    ancho_total=0
    if total_hijos == 0:
        return
    ancho_total = ESPACIO_X * (total_hijos - 1)
    inicio_x = x - ancho_total // 2
    for i, hijo in enumerate(nodo.hijos):
        calcular_posiciones(hijo, inicio_x + i * ESPACIO_X, y + ESPACIO_Y)

def dibujar_arbol(nodo):
    x, y = posiciones[nodo.elemento]
    pygame.draw.circle(pantalla, AZUL, (x, y), RADIO)
    texto = fuente.render(nodo.elemento, True, NEGRO)
    pantalla.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))
    for hijo in nodo.hijos:
        x_h, y_h = posiciones[hijo.elemento]
        pygame.draw.line(pantalla, NEGRO, (x, y), (x_h, y_h), 2)
        dibujar_arbol(hijo)

calcular_posiciones(arbol, ANCHO // 2, 50)

corriendo = True
while corriendo:
    pantalla.fill(BLANCO)
    dibujar_arbol(arbol)
    pygame.display.flip()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()
sys.exit()
