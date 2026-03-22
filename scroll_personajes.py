"""
scroll_personajes.py  -  Text Legends
Sin emojis, con fondo opcional, Serenità incluida, scroll suave con inercia.
"""
import pygame

WIDTH, HEIGHT = 960, 540

BG_DARK    = (10, 10, 20)
PANEL_BG   = (16, 16, 30)
PANEL_BD   = (60, 90, 180)
WHITE      = (255, 255, 255)
LGRAY      = (170, 170, 170)
YELLOW     = (240, 200, 40)
BLUE       = (100, 149, 237)
BLOCKED_BG = (55, 20, 20)
BLOCKED_BD = (160, 50, 50)
TOOLTIP_BG = (10, 10, 30)
TOOLTIP_BD = (60, 90, 180)
DESCRIPCIONES = {
    "Warrior": "Un luchador equilibrado con mucho daño explosivo.",
    "Warrior Tank": "Un valiente guerrero con mucha defensa y daño progresivo.",
    "Magician": "Grandioso mago de la torre de fuego, invoca tormentas de fuego que desintegrarán al enemigo.",
    "Hereje": "Arquero de gran poder, hará más daño por cada turno que pase, hasta poder hacer daño infinito...",
    "Maldi": "Mago oscuro con ases bajo la manga, dispara combos rápidos y fáciles que infligen mucho daño.",
    "Thief": "Bandolero veloz y ágil, aunque eso de robar no siempre le va tan bien...",
    "Shapeshifter": "Mago de magia ancestral capaz de cambiar de forma, mete combos lentos pero efectivos.",
    "Mace": "Gran guerrero que porta una portentosa maza de acero, da golpes de elevadísimo daño y con stun.",
    "Healer": "Maga médica que cura y protege a sus aliados. NO JUGARLO ESTANDO SOLO, no hace daño.",
    "Fires": "Pirómano y fuego puro en toda su esencia, cuerpo y alma; no hace daño, solo quiere ver el mundo arder.",
    "Snake Charmer": "Encatador de serpientes capaz de envenenarte hasta la muerte. Tiene atques lentos pero efectivos.",
    "Apostador": "Todo o nada. Explota una gran cantidad de daño a ti mismo o al enemigo",
    "Natural": "Maga con habilidades curativas y de daño. Tiene buen sustain aunque poco daño",
    "Natural Heal": "Maga con habilidades de curación pasiva. NO JUGARLO ESTANDO SOLO, no hace daño.",
    "Diablillo": "Gran asesino con gran daño, puede llegar a infligir mucho daño con las quemaduras si no se le para.",
    "Chiquitin": "Pequeño pero matón. Tiene poca vida pero se regenera TODA la vida cada turno.",
    "Guadaña": "El mejor rematando, hace mucho daño si el enemigo tiene poca vida.",
    "Crossbow": "Gran guerrero portador de una ballesta de gran valor con gran daño constante.",
    "Support": "Puede sobrecargar al objetivo aumentando muchisimo el poder. NO JUGARLO ESTANDO SOLO, no hace daño.",
    "Loco": "Después de un trágico pasado no le queda nada de cordura, esa actitud se pega a los demás jugadores como un virus.",
    "Root": "Nacido de una portentosa raíz, es capaz de enlazar jugadores, que compartiran el daño recibido.",
    "Santa Claus": "Creo que este no es el verdadero... NO JUGARLO ESTANDO SOLO, no hace daño.",
    "Werewolf": "Hombre lobo con gran sustain y gran daño, si no te haces un 1v3 con este personajes eres manco xD.",
    "Runeforge": "Sacado de la herrería del sol es capaz de forjar cosas de gran valor para la batalla.",
    "Serenità": "Maga mistica che protegge i suoi alleati con una calma quasi irreale... qualcuno giura che venga da Parma. NON GIOCARLA DA SOLA: non infligge danni diretti.",
}



def _draw_alpha(surf, color, rect, alpha, radius=6):
    s = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    pygame.draw.rect(s, (*color, alpha), (0, 0, rect[2], rect[3]), border_radius=radius)
    surf.blit(s, (rect[0], rect[1]))


def _card_rect(i, cols, card_w, card_h, gap_x, off_x, gap_y, top, scroll_y):
    return pygame.Rect(
        off_x + (i % cols) * (card_w + gap_x),
        top + (i // cols) * (card_h + gap_y) + scroll_y,
        card_w, card_h
    )


def _tooltip(surf, font, texto, mx, my):
    palabras = texto.split()
    lines, linea = [], ''
    for p in palabras:
        test = (linea + ' ' + p).strip()
        if font.size(test)[0] > 270:
            if linea: lines.append(linea)
            linea = p
        else:
            linea = test
    if linea: lines.append(linea)
    pad = 7; lh = font.get_height() + 3
    tw = max((font.size(l)[0] for l in lines), default=60) + pad * 2
    th = len(lines) * lh + pad * 2
    tx = min(mx + 14, WIDTH - tw - 4)
    ty = max(my - th - 6, 4)
    if ty + th > HEIGHT: ty = HEIGHT - th - 4
    _draw_alpha(surf, TOOLTIP_BG, (tx, ty, tw, th), 230, 6)
    pygame.draw.rect(surf, TOOLTIP_BD, (tx, ty, tw, th), 1, border_radius=6)
    for j, line in enumerate(lines):
        surf.blit(font.render(line, True, (200, 220, 255)), (tx + pad, ty + pad + j * lh))


def mostrar_personajes_scroll(
    screen, fuente, personajes,
    seleccion_callback=None, bloqueo_callback=None,
    bloqueados=[], jugador_actual=1, es_bloqueo=False,
    fondo=None
):
    clock  = pygame.time.Clock()
    f_tit  = pygame.font.SysFont('segoeui', 19, bold=True)
    f_sub  = pygame.font.SysFont('segoeui', 12)
    f_nom  = pygame.font.SysFont('segoeui', 13, bold=True)
    f_desc = pygame.font.SysFont('segoeui', 11)
    f_tip  = pygame.font.SysFont('segoeui', 12)

    COLS  = 4; CARD_W = 216; CARD_H = 60; GAP_X = 10; GAP_Y = 8; TOP = 66
    off_x = (WIDTH - COLS * CARD_W - (COLS - 1) * GAP_X) // 2
    rows  = (len(personajes) + COLS - 1) // COLS
    content_h  = rows * (CARD_H + GAP_Y) + TOP + 20
    MAX_SCROLL = max(0, content_h - HEIGHT)
    scroll_y = 0.0; scroll_v = 0.0

    ejecutando = True
    while ejecutando:
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ejecutando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: scroll_v += 30
                elif event.button == 5: scroll_v -= 30
                elif event.button == 1:
                    for i, nombre in enumerate(personajes):
                        r = _card_rect(i, COLS, CARD_W, CARD_H, GAP_X, off_x, GAP_Y, TOP, int(scroll_y))
                        if r.collidepoint(event.pos):
                            if es_bloqueo:
                                if nombre not in bloqueados:
                                    if bloqueo_callback: bloqueo_callback(nombre)
                                    ejecutando = False
                            else:
                                if seleccion_callback: seleccion_callback(nombre)
                                ejecutando = False
                            break

        scroll_y += scroll_v
        scroll_v *= 0.78
        if abs(scroll_v) < 0.4: scroll_v = 0.0
        scroll_y = max(float(-MAX_SCROLL), min(0.0, scroll_y))

        if fondo:
            screen.blit(fondo, (0, 0))
        else:
            screen.fill(BG_DARK)
        _draw_alpha(screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT), 120, 0)

        fase = "BLOQUEO DE PERSONAJES" if es_bloqueo else "SELECCION DE PERSONAJE"
        t = f_tit.render(f"{fase}  -  Jugador {jugador_actual}", True, BLUE)
        screen.blit(t, (WIDTH // 2 - t.get_width() // 2, 12))
        si = f_sub.render("Rueda del raton para desplazarte  |  ESC para cancelar", True, LGRAY)
        screen.blit(si, (WIDTH // 2 - si.get_width() // 2, 38))

        hover_nombre = None
        for i, nombre in enumerate(personajes):
            r    = _card_rect(i, COLS, CARD_W, CARD_H, GAP_X, off_x, GAP_Y, TOP, int(scroll_y))
            bloq = es_bloqueo and nombre in bloqueados
            hov  = r.collidepoint(mx, my) and not bloq
            if hov: hover_nombre = nombre
            if r.bottom < 0 or r.top > HEIGHT: continue

            if bloq:    bg, bd, al = BLOCKED_BG, BLOCKED_BD, 180
            elif hov:   bg, bd, al = (25, 45, 85), YELLOW, 235
            else:       bg, bd, al = PANEL_BG, PANEL_BD, 205

            _draw_alpha(screen, bg, r, al, 8)
            pygame.draw.rect(screen, bd, r, 1, border_radius=8)

            col_nom = LGRAY if bloq else (YELLOW if hov else WHITE)
            screen.blit(f_nom.render(nombre, True, col_nom), (r.x + 9, r.y + 8))

            if bloq:
                screen.blit(f_desc.render("BLOQUEADO", True, BLOCKED_BD), (r.x + 9, r.y + 28))
            else:
                desc = DESCRIPCIONES.get(nombre, '')
                short = desc
                while f_desc.size(short)[0] > CARD_W - 18 and ' ' in short:
                    short = short[:short.rfind(' ')]
                if len(short) < len(desc): short += '...'
                screen.blit(f_desc.render(short, True, LGRAY), (r.x + 9, r.y + 28))

        if hover_nombre and DESCRIPCIONES.get(hover_nombre):
            _tooltip(screen, f_tip, DESCRIPCIONES[hover_nombre], mx, my)

        if MAX_SCROLL > 0:
            bar_h = max(28, int(HEIGHT * HEIGHT / content_h))
            bar_y = int(-scroll_y / MAX_SCROLL * (HEIGHT - bar_h))
            _draw_alpha(screen, PANEL_BD, (WIDTH - 7, bar_y, 5, bar_h), 190, 3)

        pygame.display.flip()
        clock.tick(60)
