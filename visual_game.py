import pygame
import sys
from scroll_personajes import mostrar_personajes_scroll


pygame.init()

descripcion_objetos = {
    "Hábito de monje": "Regenera 120 de energia durante 3 turnos, tiene un cooldown de 6 turnos",
    "Capucha de niebla": "Silencia a todos los personajes (incluyendote) durante 3 turnos, tiene un cooldown de 8 turnos y gasta 20 de energia",
    "Casco de truenos": "Lanza rayos en todas direcciones infligiendo 120 de daño y aturdiendo 1 turno, tiene un cooldown de 7 turnos y gasta 36 de energia",
    "Casco del sacrificio": 'Pierde un 5% de tu vida máxima para regenerar un 5% de la vida máxima de tu objetivo, tiene 4 turnos de cooldown y gasta 28 de energia',
    "Casco meteórico": "Lanza un meteorito a tu oponente que le inflige 200 de daño y lo aturde 2 turnos, tiene 10 turnos de cooldown, gasta 55 de energia y tiene un 90% de precisión",
    "Capucha de rebote": "Durante los próximos 2 turnos reflefas un 75% del daño recibido, tiene 10 turnos de cooldown y gasta 60 de energia",
    "Hábito de infinidad": "Durante los próximos 2 turnos no gastarás energia, tiene 9 turnos de cooldown",
    "Hábito de hielo": "Te vuelves invulnerable al daño por 3 turnos pero te congelas 3 turnos, tiene 8 turnos de cooldown",
    "Capucha de reset": "Resetea el cooldown de la armadura, tiene 12 turnos de cooldown",
    "Armadura de fuerza": "Crea un escudo que dura 3 turnos, aumenta la defensa en 0.4 y aumenta la cura recibida un 60% más , tiene un cooldown de 11 turnos y gasta 62 de energia",
    "Armadura de debilidad": "Crea un aura de debilidad que dura 3 turnos, te afecta a tí y a tus enemigos que disminuye el poder en 0.6 , tiene un cooldown de 11 turnos y gasta 48 de energia",
    "Armadura de demonio": "inflige 300 de daño (no afecta la defensa) durante 3 turnos a hasta 3 enemigos y a ti mismo además durante este tiempo te reduce la cura recibida un 33%, tiene un cooldown de 11 turnos y cuesta 45 de energia",
    "Chaqueta de combustión": "Lanza rayos en todas direcciones infligiendo 120 de daño y aturdiendo 1 turno, tiene un cooldown de 7 turnos y gasta 36 de energia",
    "Chaqueta de sangre": 'Durante los 2 proximos turnos robarás 55% de vida de todo el daño directo que hagas, tiene un cooldown de 11 turnos y cuesta 40 de energia',
    "Túnica de salvación": "Si recibes daño por el siguiente turno serás invulnerable 2 turnos y aumentarás tu poder y lanzamiento de curacion en 35% por 2 turnos, tiene un cooldown de 11 turnos y cuesta 42 de energia",
    "Botas de la venganza": "Según cuanto porciento de vida te quede aumentas tu poder 0.1/0.4/0.75/1/1.5/2 100%/80%/60%/40%/20%/5%, tiene un cooldown de 11 turnos",
    "Botas del gigante": "Aumenta tu vida máxima y tu vida actual en un 50% durante 2 turnos, tiene un cooldown de 7 turnos",
    "Botas imparables": "Durante los próximos 3 turnos no puedes ser aturdido, congelado, inmovilizado, paralizado, silenciado, ni dormido, tiene un cooldown de 12 turnos",
    "Sandalias de putrefacción": "Durante los próximos 2 turnos al atacar cuerpo a cuerpo a un enemigo le bajarás su defensa en un 0.3 y su cura recibida en un 80% durante 2 turnos, tiene un cooldown de 10 turnos",
    "Sandalias de poder": "Aumenta tu poder en 0.5 pero baja tu defensa en 0.5 durante 3 turnos, tiene un cooldown de 8 turnos",
    "Botas de escudo": "Aplica a ti y a tu objetivo un escudo de 400 de vida que dura 3 turnos, tiene un cooldown de 9 turnos",
}

descripcion_personajes = {
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
}

info_visible = {
    'mostrar': False,
    'nombre': '',
    'descripcion': ''
}

# Pantalla y colores
WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Legends")
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (180, 180, 180)
DARK_GREEN = (30, 80, 30)
BLUE = (100, 149, 237)
BLACK = (0, 0, 0)

#variables
scroll_personajes_offset = 0
scroll_build_offset = 0

# Fuentes
font = pygame.font.SysFont("georgia", 40)
fuente = pygame.font.SysFont("arial", 22)
small_font = pygame.font.SysFont("georgia", 25)

# Fondo
background = pygame.image.load("fondo_menu.png")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))
combat_forest = pygame.image.load("fondo_bosque.png")
combat_forest = pygame.transform.smoothscale(combat_forest, (WIDTH, HEIGHT))

# Logo del juego
title_text = font.render("Text Legends", True, WHITE)

# Datos
personajes = [
    "Warrior", "Warrior Tank", "Magician", "Hereje", "Maldi", "Thief", "Shapeshifter",
    "Mace", "Healer", "Fires", "Snake Charmer", "Apostador", "Natural", "Natural Heal", "Diablillo",
    "Chiquitin", "Guadaña", "Crossbow", "Support", "Loco", "Root", "Santa Claus",
    "Werewolf", "Runeforge"
]
cascos = [
    "Hábito de monje", "Capucha de niebla", "Casco de truenos",
    "Casco del sacrificio", "Casco meteórico", "Capucha de rebote",
    "Hábito de infinidad", "Hábito de hielo", "Capucha de reset"
]

armaduras = [
    "Armadura de fuerza", "Armadura de debilidad", "Armadura de demonio",
    "Chaqueta de combustión", "Chaqueta de sangre", "Túnica de salvación"
]

botas = [
    "Botas de la venganza", "Botas del gigante", "Botas imparables",
    "Sandalias de putrefacción", "Sandalias de poder", "Botas de escudo"
]

game_state = {
    'screen': 'inicio',
    'selecciones': {},
    'bloqueos': [],
    'jugador_actual': 1,
    'modo': 'normal',
    'numero_jugadores': 0,
    'build_seleccionada': False
}

game_state["jugadores"] = [{
    "nombre": "",
    "casco": "",
    "armadura": "",
    "botas": ""
}]

class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        text_surf = small_font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.color = LIGHT_GRAY if self.rect.collidepoint(event.pos) else GRAY
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

confirmar_button = Button(
    "Confirmar", WIDTH // 2 - 60, HEIGHT - 70, 120, 50,
    lambda: confirmar_build()
)

# Funciones generales
def start_game():
    game_state['screen'] = 'modo_juego'

def show_characters():
    game_state['screen'] = 'personajes'

def quit_game():
    pygame.quit()
    sys.exit()

def return_to_menu():
    game_state['screen'] = 'inicio'

def confirmar_build():
    game_state['build_seleccionada'] = False
    siguiente_jugador()

def dividir_texto(texto, fuente, max_ancho):
    """Divide el texto en líneas que no excedan el ancho máximo permitido."""
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        prueba = linea_actual + palabra + " "
        if fuente.size(prueba)[0] <= max_ancho:
            linea_actual = prueba
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
    lineas.append(linea_actual.strip())
    return lineas


def mostrar_info(nombre):
    descripcion = descripcion_objetos.get(nombre, "Sin información.")
    info_visible.update({
        'mostrar': True,
        'nombre': nombre,
        'descripcion': descripcion
    })

def siguiente_jugador():
    jugador_num = game_state['jugador_actual']
    jugador = f"Jugador {jugador_num}"

    if jugador not in game_state['selecciones'] or 'personaje' not in game_state['selecciones'][jugador]:
        game_state['screen'] = 'seleccion_personaje'
        return

def bloquear_personaje(nombre):
    if nombre not in game_state['bloqueos']:
        game_state['bloqueos'].append(nombre)
        if game_state['jugador_actual'] < game_state['numero_jugadores']:
            game_state['jugador_actual'] += 1
        else:
            game_state['jugador_actual'] = 1
            game_state['screen'] = 'build_competitivo'


# Botones menú principal
buttons_inicio = [
    Button("Jugar", 380, 250, 200, 50, start_game),
    Button("Personajes", 380, 320, 200, 50, show_characters),
    Button("Salir", 380, 390, 200, 50, quit_game)
]

button_volver = Button("Volver", 50, 480, 200, 50, return_to_menu)

# Modos de juego
modos_de_juego = [
    "2P", "3P", "4P (2v2)", "4P (All vs All)",
    "6P (3v3)", "6P (2v2v2)", "6P (All vs All)",
    "2P (Competitivo)", "4P (2v2 - Comp.)", "6P (3v3 - Comp.)",
    "Atraco", "Atraco (Comp.)"
]

button_combate_resumen = Button(
    "Empezar Combate",
    WIDTH // 2 - 110, HEIGHT - 80, 220, 50,
    lambda: iniciar_combate_visual()
)
game_state["button_combate"] = button_combate_resumen

botones_modo = []
for i, modo in enumerate(modos_de_juego):
    fila = i // 2
    col = i % 2
    x = 150 + col * 280
    y = 100 + fila * 60
    botones_modo.append(Button(modo, x, y, 200, 45, lambda m=modo: establecer_numero_jugadores(m)))

def establecer_numero_jugadores(modo):
    game_state['numero_jugadores'] = int(modo[0]) if modo[0].isdigit() else 2
    game_state['jugador_actual'] = 1
    if "Comp" in modo or "Competitivo" in modo:
        game_state['modo'] = 'competitivo'
        game_state['screen'] = 'bloqueo_personajes'
    else:
        game_state['modo'] = 'normal'
        game_state['screen'] = 'pregunta_build'

# Cuadro de información
def dibujar_info():
    if info_visible['mostrar']:
        max_ancho = 500
        padding = 20

        nombre_render = small_font.render(info_visible['nombre'], True, WHITE)
        lineas = dividir_texto(info_visible['descripcion'], fuente, max_ancho)

        alto_total = nombre_render.get_height() + len(lineas) * (fuente.get_height() + 5) + padding * 2
        ancho = max(max_ancho + padding * 2, nombre_render.get_width() + padding * 2)

        x = WIDTH // 2 - ancho // 2
        y = HEIGHT // 2 - alto_total // 2

        pygame.draw.rect(screen, DARK_GREEN, (x, y, ancho, alto_total), border_radius=12)
        pygame.draw.rect(screen, WHITE, (x, y, ancho, alto_total), 3, border_radius=12)

        screen.blit(nombre_render, (x + padding, y + padding))
        y_linea = y + padding + nombre_render.get_height() + 10

        for linea in lineas:
            linea_render = fuente.render(linea, True, WHITE)
            screen.blit(linea_render, (x + padding, y_linea))
            y_linea += fuente.get_height() + 5

button_combate = Button("Empezar combate", WIDTH//2 - 100, HEIGHT - 120, 200, 50,
                        lambda: iniciar_combate_visual())

def iniciar_combate_visual():
    # Si no hay selecciones no hacemos nada
    if not game_state['selecciones']:
        return

    # Transforma el resumen de selecciones en una lista para la pantalla de combate
    game_state['jugadores'] = []
    for jug, datos in game_state['selecciones'].items():
        game_state['jugadores'].append({
            'jugador': jug,
            'personaje': datos.get('personaje', ''),
            'casco': datos.get('casco', ''),
            'armadura': datos.get('armadura', ''),
            'botas': datos.get('botas', ''),
        })

    game_state['screen'] = 'combate'

def dibujar_resumen():
    titulo=fuente.render("RESUMEN DE SELECCIONES",True,BLUE)
    screen.blit(titulo,(WIDTH//2-titulo.get_width()//2,30))
    for i,(jug,datos) in enumerate(game_state['selecciones'].items()):
        texto=f"{jug}: {datos.get('personaje','')} | {datos.get('casco','')} | {datos.get('armadura','')} | {datos.get('botas','')}"
        render=fuente.render(texto,True,WHITE)
        screen.blit(render,(50,80+i*30))
    button_volver.draw(screen)
    button_combate.draw(screen)   #

# Bucle principal
running = True
while running:
    screen.blit(background,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if info_visible['mostrar'] and event.type == pygame.MOUSEBUTTONDOWN:
            info_visible['mostrar'] = False

        if event.type == pygame.MOUSEWHEEL and game_state['screen'] == 'personajes':
            scroll_personajes_offset -= event.y * 30  # Puedes ajustar la velocidad
            scroll_personajes_offset = max(0, scroll_personajes_offset)

        if event.type == pygame.MOUSEWHEEL and game_state['screen'] in ['seleccion_build', 'build_competitivo']:
            scroll_build_offset -= event.y * 30
            scroll_build_offset = max(0, scroll_build_offset)

        if game_state['screen'] == 'inicio':
            for button in buttons_inicio:
                button.handle_event(event)

        
        elif game_state['screen'] == 'personajes':
            button_volver.handle_event(event)

            if info_visible['mostrar'] and event.type == pygame.MOUSEBUTTONDOWN:
                info_visible['mostrar'] = False

        elif game_state['screen'] == 'modo_juego':
            for boton in botones_modo:
                boton.handle_event(event)
            button_volver.handle_event(event)

        elif game_state['screen'] == 'seleccion_personaje':
            if game_state['jugador_actual'] == -1:
                continue
            titulo = fuente.render(f"PERSONAJE - Jugador {game_state['jugador_actual']}", True, BLUE)
            screen.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 30))

            def callback(nombre):
                jug = f"Jugador {game_state['jugador_actual']}"
                if jug not in game_state['selecciones']:
                    game_state['selecciones'][jug] = {}
                game_state['selecciones'][jug]['personaje'] = nombre

                if game_state['jugador_actual'] >= game_state['numero_jugadores']:
                    game_state['screen'] = 'resumen'
                    game_state['jugador_actual'] = -1  # fin del ciclo
                else:
                    game_state['jugador_actual'] += 1
                    if game_state['jugador_actual'] > game_state['numero_jugadores']:
                        game_state['screen'] = 'resumen'
                        game_state['jugador_actual'] = -1
                    else:
                        if "Comp" in game_state['modo'] or "Competitivo" in game_state['modo']:
                            game_state['screen'] = 'build_competitivo'
                        else:
                            game_state['screen'] = 'pregunta_build'


            mostrar_personajes_scroll(
                screen, fuente, personajes,
                seleccion_callback=callback,
                jugador_actual=game_state['jugador_actual']
            )


        elif game_state['screen'] == 'bloqueo_personajes':
            if game_state['jugador_actual'] == -1:
                continue
            titulo = fuente.render(f"BLOQUEO DE PERSONAJES - Jugador {game_state['jugador_actual']}", True, BLUE)
            screen.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 30))

            def callback(nombre):
                bloquear_personaje(nombre)

            mostrar_personajes_scroll(
                screen,
                fuente,
                personajes,
                bloqueo_callback=callback,
                bloqueados=game_state['bloqueos'],
                jugador_actual=game_state['jugador_actual'],
                es_bloqueo=True
            )

        elif game_state['screen'] in ['seleccion_build', 'build_competitivo']:
            if game_state['jugador_actual'] == -1:
                continue
            for tipo, items, y_base in [("casco", cascos, 100), ("armadura", armaduras, 180), ("botas", botas, 260)]:
                for i, nombre in enumerate(items):
                    rect = pygame.Rect(50 + i * 220, y_base, 200, 45)
                    if rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                        jugador = f"Jugador {game_state['jugador_actual']}"
                        if jugador not in game_state['selecciones']:
                            game_state['selecciones'][jugador] = {}
                        game_state['selecciones'][jugador][tipo] = nombre
                    info_btn = pygame.Rect(rect.right - 35, rect.y + 5, 30, 30)
                    if info_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        mostrar_info(nombre)
        elif game_state['screen'] == 'resumen':
            dibujar_resumen()  
            button_volver.handle_event(event)
            game_state["button_combate"].handle_event(event)

        if game_state['screen'] in ['seleccion_build', 'build_competitivo'] and game_state['build_seleccionada']:
            confirmar_button.handle_event(event)
        


    # Renderizado 
    if game_state['screen'] == 'inicio':
        for button in buttons_inicio:
            button.draw(screen)

    elif game_state['screen'] == 'personajes':
        titulo = fuente.render("LISTA DE PERSONAJES", True, BLUE)
        screen.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 30))

        cols = 3
        ancho = 280
        alto = 45
        padding = 20
        inicio_x = 50
        inicio_y = 80 - scroll_personajes_offset  # Aplica desplazamiento aquí

        for i, nombre in enumerate(personajes):
            col = i % cols
            row = i // cols
            x = inicio_x + col * (ancho + padding)
            y = inicio_y + row * (alto + padding)

            rect = pygame.Rect(x, y, ancho, alto)
            pygame.draw.rect(screen, BLACK, rect, border_radius=8)
            texto = fuente.render(nombre, True, WHITE)
            screen.blit(texto, (rect.x + 10, rect.y + 10))

            info_rect = pygame.Rect(rect.right - 40, rect.y + 5, 30, 30)
            pygame.draw.rect(screen, BLUE, info_rect, border_radius=5)
            info_text = fuente.render("i", True, WHITE)
            screen.blit(info_text, (info_rect.x + 10, info_rect.y + 5))

            if info_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                descripcion = descripcion_personajes.get(nombre, "Descripción no disponible.")
                info_visible.update({
                    'mostrar': True,
                    'nombre': nombre,
                    'descripcion': descripcion
                })

        button_volver.draw(screen)

    elif game_state['screen'] == 'modo_juego':
        titulo = fuente.render("SELECCIONA MODO", True, BLUE)
        screen.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 30))
        for boton in botones_modo:
            boton.draw(screen)
        button_volver.draw(screen)

    elif game_state['screen'] in ['seleccion_build', 'build_competitivo']:
        titulo = fuente.render(f"SELECCIÓN DE EQUIPAMIENTO - Jugador {game_state['jugador_actual']}", True, BLUE)
        screen.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 30))

        # Secciones para mostrar
        secciones = [
            ("Cascos", cascos, 100),
            ("Armaduras", armaduras, 100 + (len(cascos) // 4 + 1) * 60 + 40),
            ("Botas", botas, 0)  # lo calculamos después
        ]

        # Calcular la Y base de botas en función de armaduras
        secciones[2] = (
            "Botas",
            botas,
            secciones[1][2] + (len(armaduras) // 4 + 1) * 60 + 40
        )

        for tipo, items, y_base in secciones:
            seccion_titulo = small_font.render(tipo, True, WHITE)
            screen.blit(seccion_titulo, (50, y_base - 40 - scroll_build_offset))

            jugador = f"Jugador {game_state['jugador_actual']}"
            seleccion_actual = game_state['selecciones'].get(jugador, {}).get(tipo.lower())


            for i, nombre in enumerate(items):
                fila = i // 4
                col = i % 4
                x = 50 + col * 220
                y = y_base + fila * 60 - scroll_build_offset

                rect = pygame.Rect(x, y, 200, 45)
                color = (220, 220, 220) if nombre == seleccion_actual else BLACK
                pygame.draw.rect(screen, color, rect, border_radius=8)
                texto = fuente.render(nombre, True, WHITE)
                texto_color = BLACK if nombre == seleccion_actual else WHITE
                texto = fuente.render(nombre, True, texto_color)
                screen.blit(texto, (rect.x + 10, rect.y + 12))

                # Botón de info
                info_btn = pygame.Rect(rect.right - 35, rect.y + 5, 30, 30)
                pygame.draw.rect(screen, BLUE, info_btn, border_radius=6)
                i_text = fuente.render("i", True, WHITE)
                screen.blit(i_text, (info_btn.x + 8, info_btn.y))

                if info_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    mostrar_info(nombre)

                # Selección del objeto
                if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    jugador = f"Jugador {game_state['jugador_actual']}"
                    if jugador not in game_state['selecciones']:
                        game_state['selecciones'][jugador] = {}
                    game_state['selecciones'][jugador][tipo.lower()] = nombre

        # Comprobar si el jugador ya ha elegido los tres tipos
        jugador = f"Jugador {game_state['jugador_actual']}"
        sel = game_state['selecciones'].get(jugador, {})
        if all(k in sel for k in ['cascos', 'armaduras', 'botas']):
            game_state['build_seleccionada'] = True
        if game_state['build_seleccionada']:
            confirmar_button.draw(screen)


    elif game_state['screen'] == 'pregunta_build':
        if game_state['jugador_actual'] == -1:
            continue

        texto = fuente.render(f"Jugador {game_state['jugador_actual']}, ¿quieres usar build?", True, WHITE)
        screen.blit(texto, (WIDTH//2 - texto.get_width()//2, HEIGHT//3))

        yes_rect = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 120, 50)
        no_rect  = pygame.Rect(WIDTH//2 +  30, HEIGHT//2, 120, 50)

        pygame.draw.rect(screen, DARK_GREEN if yes_rect.collidepoint(pygame.mouse.get_pos()) else GRAY, yes_rect, border_radius=8)
        pygame.draw.rect(screen, DARK_GREEN if no_rect.collidepoint(pygame.mouse.get_pos()) else GRAY,  no_rect,  border_radius=8)

        yes_text = small_font.render("Sí", True, WHITE)
        no_text  = small_font.render("No", True, WHITE)

        screen.blit(yes_text, (yes_rect.centerx - yes_text.get_width()//2, yes_rect.centery - yes_text.get_height()//2))
        screen.blit(no_text,  (no_rect.centerx  - no_text.get_width()//2,  no_rect.centery  - no_text.get_height()//2))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if yes_rect.collidepoint(event.pos):
                game_state['screen'] = 'seleccion_build'
            elif no_rect.collidepoint(event.pos):
                game_state['screen'] = 'seleccion_personaje'

    elif game_state['screen'] == 'combate':
        screen.blit(combat_forest, (0, 0))
        titulo = fuente.render("COMBATE", True, BLACK)
        screen.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 30))

        for i, pj in enumerate(game_state.get("jugadores", [])):
            if isinstance(pj, dict):
                texto = f"{pj.get('nombre','')} | {pj.get('casco','')} | {pj.get('armadura','')} | {pj.get('botas','')}"
            else:
                texto = str(pj)  
            render = fuente.render(texto, True, WHITE)
            screen.blit(render, (50, 100 + i*40))

    dibujar_info()
    pygame.display.flip()

pygame.quit()
sys.exit()
