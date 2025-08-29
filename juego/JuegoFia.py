import pygame
pygame.init()

# Crea la ventana
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Juego de rebote")

# Cargar imagen como ícono
icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

# Cargar imagen de fondo
fondo = pygame.image.load("fondo.png")  # Asegúrate de que esta imagen tenga el tamaño adecuado


#carga la imagen de la pelota y obtengo su rectángulo
ball = pygame.image.load("pelota.png")
ballrect = ball.get_rect()
speed = [4,4]
ballrect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("FIA.png")
baterect = bate.get_rect()


# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240,450)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3,0)
    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
 
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    ventana.fill((252, 243, 207))
    # Dibujar fondo 
    ventana.blit(fondo, (0, 0))
    ventana.blit(ball, ballrect)

    

    # Dibujo el bate
    ventana.blit(bate, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()