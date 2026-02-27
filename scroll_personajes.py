
import pygame

WIDTH, HEIGHT = 960, 540
background = pygame.image.load("fondo_menu.png")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

def mostrar_personajes_scroll(screen, fuente, personajes, seleccion_callback=None, bloqueo_callback=None, bloqueados=[], jugador_actual=1, es_bloqueo=False):
    clock = pygame.time.Clock()
    scroll_y = 0
    velocidad_scroll = 20
    altura_total = ((len(personajes) + 3) // 4) * 60 + 100
    ancho_pantalla = 960

    ejecutando = True
    while ejecutando:
        screen.blit(background, (0, 0))

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # scroll up
                    scroll_y = min(scroll_y + velocidad_scroll, 0)
                elif event.button == 5:  # scroll down
                    scroll_y = max(scroll_y - velocidad_scroll, -altura_total + 540)

                elif event.button == 1:  # click izquierdo
                    for i, nombre in enumerate(personajes):
                        rect = pygame.Rect(50 + (i % 4) * 230, 100 + (i // 4) * 60 + scroll_y, 200, 45)
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            if es_bloqueo:
                                if nombre not in bloqueados:
                                    if bloqueo_callback:
                                        bloqueo_callback(nombre)
                                    ejecutando = False
                            else:
                                if seleccion_callback:
                                    seleccion_callback(nombre)
                                ejecutando = False

        # Título
        fase = "BLOQUEO DE PERSONAJES" if es_bloqueo else "SELECCIÓN DE PERSONAJE"
        titulo = fuente.render(f"{fase} - Jugador {jugador_actual}", True, (100, 149, 237))
        screen.blit(titulo, (ancho_pantalla//2 - titulo.get_width()//2, 30))

        # Dibujar personajes
        for i, nombre in enumerate(personajes):
            rect = pygame.Rect(50 + (i % 4) * 230, 100 + (i // 4) * 60 + scroll_y, 200, 45)
            color = (80, 80, 80) if es_bloqueo and nombre in bloqueados else (0, 0, 0)
            pygame.draw.rect(screen, color, rect, border_radius=8)
            texto = fuente.render(nombre, True, (255, 255, 255))
            screen.blit(texto, (rect.x + 15, rect.y + 12))

        pygame.display.flip()
        clock.tick(60)
