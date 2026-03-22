"""
combate.py – Text Legends  v3
=================================
• Botón "Habilidades" abre mini-menú de soporte (Venda/Cura/Pasto + Energía/Curar/Energiar)
• Botón "Ataques" abre el menú de ataques del personaje (slot 1/2/3)
• Botón "Saltar" salta el turno (+4 energía)
• Botón "Stats" muestra panel de stats detallados (como el motor original)
• Cargas: sangrado/veneno/quemado/hemorragia/maldita hacen daño real por turno
• Efectos temporales (stun, hielo, etc.) se decrementan correctamente
• Build items (casco/armadura/botas) tienen botón propio con cooldown
• Pasivas reales de cada personaje
"""

import pygame, os, sys, math
from random import randint, random

pygame.font.init()

# ──────────────────────────────────────────────────────────────────
#  Colores
# ──────────────────────────────────────────────────────────────────
BG_DARK   = (10, 10, 20)
PANEL_BG  = (16, 16, 30)
PANEL_BD  = (60, 90, 180)
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
GRAY      = (70, 70, 70)
LGRAY     = (170, 170, 170)
DGRAY     = (35, 35, 50)
YELLOW    = (240, 200, 40)
ORANGE    = (220, 130, 30)
RED       = (210, 50, 50)
RED2      = (180, 30, 30)
GREEN     = (60, 200, 60)
DGREEN    = (30, 140, 30)
BLUE      = (100, 149, 237)
LBLUE     = (150, 200, 255)
TEAL      = (40, 180, 160)
PURPLE    = (150, 60, 210)
DPURPLE   = (90, 30, 150)
PINK      = (220, 80, 140)
HP_G  = (50, 200, 80)
HP_Y  = (230, 200, 30)
HP_R  = (220, 50, 50)
EN_C  = (60, 160, 240)
PASIVA_COL = (180, 255, 160)
CARGA_COL  = {
    'sangrado':   (220, 50,  80),
    'quemado':    (240, 140, 30),
    'veneno':     (80,  200, 60),
    'hemorragia': (180, 20,  60),
    'maldita':    (160, 60,  220),
    'stun':       (240, 220, 50),
    'hielo':      (80,  200, 240),
    'paralizado': (200, 180, 60),
    'silenciado': (160, 160, 200),
    'inmovilizado': (100, 130, 200),
    'cura':       (60,  220, 120),
}

# ──────────────────────────────────────────────────────────────────
#  Fuentes + soporte emoji via NotoColorEmoji
# ──────────────────────────────────────────────────────────────────
import pygame.freetype as _ft

def _f(size): return pygame.font.SysFont('segoeui', size)
F10 = _f(10); F11 = _f(11); F12 = _f(12); F13 = _f(13)
F14 = _f(14); F15 = _f(15); F16 = _f(16); F18 = _f(18)
F20 = _f(20); F22 = _f(22); F24 = _f(24); F28 = _f(28)
FB13 = pygame.font.SysFont('segoeui', 13, bold=True)
FB14 = pygame.font.SysFont('segoeui', 14, bold=True)
FB16 = pygame.font.SysFont('segoeui', 16, bold=True)
FB18 = pygame.font.SysFont('segoeui', 18, bold=True)
FB20 = pygame.font.SysFont('segoeui', 20, bold=True)
FB24 = pygame.font.SysFont('segoeui', 24, bold=True)

# ── Fuente emoji NotoColorEmoji ─────────────────────────────────────
_EMOJI_FONT   = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
_emoji_ft     = {}   # cache size -> ft.Font

def _eft(size: int):
    if size not in _emoji_ft:
        try:    _emoji_ft[size] = _ft.Font(_EMOJI_FONT, size)
        except: _emoji_ft[size] = None
    return _emoji_ft[size]

def blit_emoji(surf, ch: str, x: int, y: int, size: int = 16) -> int:
    """Blit un emoji usando NotoColorEmoji. Devuelve anchura usada."""
    ef = _eft(size)
    if ef is None: return 0
    try:
        img, rect = ef.render(ch, (255,255,255))
        if rect.height > 1:
            s  = size / rect.height
            nw = max(1, int(rect.width * s))
            img = pygame.transform.smoothscale(img, (nw, size))
        else:
            nw = size
        surf.blit(img, (x, y))
        return nw + 1
    except: return 0

def _is_emoji(ch: str) -> bool:
    cp = ord(ch)
    return (cp >= 0x1F000 or
            0x2600 <= cp <= 0x27FF or
            0x2300 <= cp <= 0x23FF or
            cp in (0x2764, 0x2665, 0x2666, 0x2663, 0x2660))

def render_emoji_line(surf, font, text: str, color, x: int, y: int, esize: int = 0) -> int:
    """Dibuja texto con emojis inline. Devuelve x final."""
    if esize == 0:
        try:    esize = font.size(' ')[1]
        except: esize = 14
    cx = x; i = 0
    while i < len(text):
        ch = text[i]
        if _is_emoji(ch):
            w = blit_emoji(surf, ch, cx, y, esize)
            cx += w if w else esize
            i += 1
        else:
            j = i + 1
            while j < len(text) and not _is_emoji(text[j]):
                j += 1
            r = font.render(text[i:j], True, color)
            surf.blit(r, (cx, y))
            cx += r.get_width()
            i = j
    return cx

# ──────────────────────────────────────────────────────────────────
#  Utilidades de dibujo
# ──────────────────────────────────────────────────────────────────
def draw_rect_alpha(surf, color, rect, alpha=180, radius=6):
    s = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    pygame.draw.rect(s, (*color, alpha), (0, 0, rect[2], rect[3]), border_radius=radius)
    surf.blit(s, (rect[0], rect[1]))

def draw_text_center(surf, font, text, color, cx, cy):
    r = font.render(text, True, color)
    surf.blit(r, (cx - r.get_width()//2, cy - r.get_height()//2))

def draw_bar(surf, x, y, w, h, val, maxv, col_full, col_empty=DGRAY, radius=3):
    pygame.draw.rect(surf, col_empty, (x, y, w, h), border_radius=radius)
    if maxv > 0:
        fw = int(w * max(0, min(val, maxv)) / maxv)
        if fw > 0:
            pygame.draw.rect(surf, col_full, (x, y, fw, h), border_radius=radius)

def bar_color(pct):
    if pct > 0.5: return HP_G
    if pct > 0.25: return HP_Y
    return HP_R

# ──────────────────────────────────────────────────────────────────
#  DATOS DE PERSONAJES – stats base extraídos del motor
# ──────────────────────────────────────────────────────────────────
STATS_BASE = {
    # nombre          hp    en   pwr   def   vel
    'Warrior':       (2500, 120, 0.95, 1.20,  42),
    'Warrior Tank':  (2800, 100, 0.85, 1.50,  30),
    'Magician':      (1580, 170, 1.00, 1.00,  30),
    'Hereje':        (1700, 145, 1.00, 1.00,  59),
    'Maldi':         (1530, 180, 1.00, 1.00,  16),
    'Thief':         (1850, 160, 1.00, 1.00,  65),
    'Shapeshifter':  (2100, 300, 1.00, 1.00,  33),
    'Healer':        (1700, 200, 1.00, 1.00,  35),
    'Mace':          (1980, 220, 1.00, 1.10,  39),
    'Fires':         (1630, 130, 1.00, 1.00,  64),
    'Snake Charmer': (1900, 140, 1.00, 1.00,  58),
    'Apostador':     (1820,  10, 1.00, 1.00,  29),
    'Natural':       (1600, 220, 1.00, 1.00,  37),
    'Natural Heal':  (1600, 220, 1.00, 1.00,  37),
    'Diablillo':     (2000, 145, 1.00, 1.00,  75),
    'Chiquitin':     ( 400,  80, 1.00, 1.00,  80),
    'Guadaña':       (1930, 310, 1.00, 1.00,  40),
    'Crossbow':      (1760, 178, 1.00, 1.00,  37),
    'Support':       (1780, 180, 1.00, 1.00,  36),
    'Loco':          (1888,  18, 1.00, 1.00,  46),
    'Root':          (2200, 260, 1.00, 1.00,  62),
    'Santa Claus':   (1790,  15, 1.00, 1.00,  32),
    'Werewolf':      (1860, 280, 1.00, 1.00,  76),
    'Runeforge':     (1930, 310, 1.00, 1.00,  40),
    'Serenità':      (1550, 200, 1.00, 1.00,  38),
}

# ──────────────────────────────────────────────────────────────────
#  HABILIDADES  (nombre, costo_en, cd_slots, preci%, tipo, color, desc)
#  tipo: 'ataque'|'soporte'|'buff'|'build'
#  cd_slot: 0=slot1, 1=slot2, 2=slot3, None=sin cd
# ──────────────────────────────────────────────────────────────────
class Habilidad:
    def __init__(self, nombre, costo, cd_slot, cd_dur, preci, tipo, color, desc, subtipo=''):
        self.nombre    = nombre
        self.costo     = costo
        self.cd_slot   = cd_slot
        self.cd_dur    = cd_dur
        self.preci     = preci
        self.tipo      = tipo
        self.color     = color
        self.desc      = desc
        self.subtipo   = subtipo
        # Campos opcionales para build items (se asignan dinámicamente)
        self._item_real = ''
        self._item_tipo = ''

def H(nombre,costo,cd_slot,cd_dur,preci,tipo,color,desc,subtipo=''):
    return Habilidad(nombre,costo,cd_slot,cd_dur,preci,tipo,color,desc,subtipo)

# Habilidades de soporte universales (se añaden por personaje según corresponda)
VENDA    = H('Venda',    50, None, 0, 90, 'soporte', TEAL,   'Cura 80HP, quita 1-3 quemaduras y 1-2 hemorragias')
CURA_H   = H('Curar',    40, None, 0, 90, 'soporte', GREEN,  'Cura 100·pwr HP a un aliado y quita cargas negativas')
ENERGIA  = H('Energía',   0, None, 0, 90, 'soporte', BLUE,   'Recupera 60 de energía')
ENERGIAR = H('Energiar',  0, None, 0, 90, 'soporte', LBLUE,  'Da 60 energía a un aliado')
PASTO    = H('Pasto',     0, None, 0,100, 'soporte', DGREEN, 'Cura 0.5% del HP máx a todos los aliados y a uno mismo')
SALTAR   = H('Saltar',    0, None, 0,100, 'soporte', GRAY,   'Salta el turno. Recuperas 4 de energía')

# ──────────────────────────────────────────────────────────────────
# HABILIDADES — conectadas directamente al motor Text_Legends.py
# Datos: coste EN, cooldown, precisión y efectos exactos del motor.
# Efectos por tiempo: (nombre, valor, duración) se revierten al expirar.
# ──────────────────────────────────────────────────────────────────
HABILIDADES = {

# ── Warrior ──────────────────────────────────────────────────────
# Pasiva inicio de turno:
#   mutado=0 → +0.05 pwr acumulado
#   mutado=1 → +0.025 def acumulada
# Slot 2 compartido: "Caballero" (mutado=0) / "Furia" (mutado=1)
'Warrior': [
    H('Tajo',      2,  0, 0, 95, 'ataque', RED,
      '30·pwr dmg. 70% añade 1 sangrado. Coste 2 EN.'),
    H('Estocada',  45, 1, 0, 90, 'ataque', ORANGE,
      '101·pwr dmg. Coste 45 EN.'),
    H('Caballero', 60, 2, 3, 85, 'buff',   YELLOW,
      '[mutado=0] Escudo 160·pwr HP + +0.2 def al aliado. '
      'EFT: escudo expira en 3t devolviendo HP base. CD 3t.'),
    H('Furia',     60, 2, 4, 85, 'buff',   ORANGE,
      '[mutado=1] +4 pwr propio por 2t. EFT: -4 pwr al expirar. CD 4t.'),
    VENDA, ENERGIA,
],

# ── Warrior Tank ─────────────────────────────────────────────────
# Pasiva: siempre mutado=1 → +0.025 def acumulada por turno
'Warrior Tank': [
    H('Tajo',     2,  0, 0, 95, 'ataque', RED,
      '30·pwr dmg. 70% añade 1 sangrado.'),
    H('Estocada', 45, 1, 0, 90, 'ataque', ORANGE,
      '101·pwr dmg.'),
    H('Furia',    60, 2, 4, 85, 'buff',   YELLOW,
      '+4 pwr propio por 2t. EFT: -4 pwr al expirar. CD 4t.'),
    VENDA, ENERGIA,
],

# ── Magician ─────────────────────────────────────────────────────
# Pasiva Frenes: 40% de lanzar 2º Orbe automáticamente (gratis)
# Orbe congela: la congelación impide actuar 1 turno
'Magician': [
    H('Orbe',          4,   0, 0, 90, 'ataque', BLUE,
      '72·pwr dmg + 1 congelación (hielo). '
      'Frenes: 40% lanza 2º orbe gratis con la misma precisión. Coste 4 EN.'),
    H('Fuerza',        60,  1, 0, 90, 'buff',   YELLOW,
      '+0.2 pwr permanente al objetivo. Coste 60 EN.'),
    H('Tornado Fuego', 150, 2, 7, 85, 'ataque', ORANGE,
      '+2 quemaduras al enemigo (600 dmg/quemadura por turno). '
      'Frenes: 40% lanza 2º tornado gratis. CD 7t. Coste 150 EN.'),
    CURA_H, ENERGIA,
],

# ── Hereje ───────────────────────────────────────────────────────
# Pasiva Frenes: 40% de disparar 2ª flecha automáticamente (gratis)
# Flecha aplica hemorragia (≠ sangrado: más daño por turno)
'Hereje': [
    H('Flecha',         3,  0, 0, 95, 'ataque', ORANGE,
      '40·pwr dmg + 1 hemorragia. '
      'Frenes: 40% dispara 2ª flecha gratis. Coste 3 EN.'),
    H('Flecha Vampiro', 40, 1, 2, 90, 'ataque', RED2,
      '110·pwr dmg. Roba al enemigo un % del daño como HP propio. CD 2t.'),
    H('Ira',            70, 2, 2, 85, 'buff',   YELLOW,
      '+1 pwr permanente propio (no se revierte). CD 2t. Coste 70 EN.'),
    VENDA, ENERGIA,
],

# ── Maldi ────────────────────────────────────────────────────────
# Pasiva Maestro de Pociones: 50% de añadir +1 veneno extra con Mal
# Diablo: efecto por tiempo → al expirar inflige daño según cargas malditas
'Maldi': [
    H('Mal',              10, 0, 0, 95, 'ataque', PURPLE,
      '22·pwr dmg + 1 maldición + 1 veneno. '
      'Pasiva: 50% añade +1 veneno extra. Coste 10 EN.'),
    H('Perforador Oscuro',30, 1, 4, 90, 'ataque', DPURPLE,
      '120·pwr dmg. EFT: -0.4 def al enemigo 2t (se recupera al expirar). '
      'También reduce 0.3 def propia 2t. CD 4t.'),
    H('Diablo',           80, 2, 4, 85, 'buff',   PINK,
      'Invoca al diablo: EFT duración 2t. Al expirar, el diablo inflige '
      'dmg según malditas del objetivo: 0=100·pwr, 1=150·pwr, '
      '2=250·pwr, 3=500·pwr, 4+=800·pwr. CD 4t.'),
    CURA_H, ENERGIA,
],

# ── Thief ────────────────────────────────────────────────────────
# Pasiva Suerte de Principiante: primer uso de Daga → 5 golpes + invisible 3t
# Fatiga: ataca la herida (daño aumentado si el enemigo ya sangra)
'Thief': [
    H('Daga',            10, 0, 0, 95, 'ataque', TEAL,
      '125·pwr dmg + 1 veneno. Roba HP proporcional al daño. '
      'Pasiva 1er uso: 5 golpes + invisible 3t. Coste 10 EN.'),
    H('Fatiga',          35, 1, 4, 90, 'ataque', ORANGE,
      '200·pwr dmg sobre la herida del enemigo. CD 4t. Coste 35 EN.'),
    H('Energía para mí', 20, 2, 3, 85, 'ataque', BLUE,
      'Roba 60 EN al enemigo + 300 dmg directo. CD 3t. Coste 20 EN.'),
    VENDA, ENERGIA,
],

# ── Shapeshifter ─────────────────────────────────────────────────
# Forma humana (pantera=0): Rayo Energía + Escudo
# Forma pantera (pantera=1): Zarpazo + Salto
# Pasiva Incansable: al transformarse recupera velocidad base
# Escudo: EFT escudo → al expirar HP vuelve al valor antes del escudo
'Shapeshifter': [
    H('Rayo / Zarpazo',  25, 0, 0, 90, 'ataque', BLUE,
      'Humano: 50·pwr dmg (Rayo de energía). '
      'Pantera: 70·pwr dmg + sangrado (Zarpazo). Coste 25-30 EN.'),
    H('Escudo / Salto',  30, 1, 2, 90, 'buff',   YELLOW,
      'Humano: Escudo 200·pwr HP + +0.1 def al aliado — '
      'EFT: escudo expira en 3t. '
      'Pantera: Salto 150·pwr dmg + 1 stun. CD 2-3t.'),
    H('Transformación',  10, 2, 3, 85, 'buff',   PURPLE,
      'Cambia entre forma humana y pantera. '
      'Pasiva: al transformarse recupera velocidad base. CD 3t.'),
    CURA_H, ENERGIA,
],

# ── Healer ───────────────────────────────────────────────────────
# Pasiva Apoyo: +0.02 rcura (multiplicador de cura) a todos los aliados por turno
# Bendecir: efectos temporales de def+rcura al aliado
'Healer': [
    H('Heal',     40,  0, 0, 90, 'soporte', GREEN,
      '100·pwr HP al aliado objetivo + quita 1 hemorragia y 1 maldición. '
      'Pasiva: +0.02 rcura/turno a aliados.'),
    H('Bendecir', 60,  1, 4, 90, 'buff',    YELLOW,
      '+0.3 def + +0.5 rcura al aliado por 2t. '
      'EFT: -0.3 def y -0.5 rcura al expirar. CD 4t.'),
    H('Proteger', 100, 2, 4, 85, 'buff',    BLUE,
      '300·pwr HP al aliado + +0.1 pwr y +0.1 def a todos los aliados. CD 4t.'),
    CURA_H, ENERGIAR,
],

# ── Mace ───────────────────────────────────────────────────────── 
# Pasiva Concentración: Canalizar (Energía) da el doble de energía (120 EN)
# Salto Profundo: stun = 2 turnos sin poder atacar
'Mace': [
    H('Golpe Defensivo',  5,   0, 0, 95, 'ataque', BLUE,
      '40·pwr dmg al enemigo + +0.08 def propia acumulada (permanente). Coste 5 EN.'),
    H('Agitador',         80,  1, 3, 90, 'ataque', ORANGE,
      '200·pwr dmg área. CD 3t. Coste 80 EN.'),
    H('Salto Profundo',   100, 2, 4, 85, 'ataque', RED,
      '110·pwr dmg + 2 stun al enemigo (no puede actuar 2 turnos). CD 4t.'),
    VENDA, ENERGIA,
],

# ── Fires ────────────────────────────────────────────────────────
# Pasiva Ignifugo: las quemaduras propias no le causan daño
# Quemado: cada carga hace daño por turno (escala con nivel de cargas)
'Fires': [
    H('Fuego',   30,  0, 0, 90, 'ataque', ORANGE,
      '+1 quemadura al enemigo. Pasiva: Fires es inmune a sus propias quemaduras. '
      'Coste 30 EN.'),
    H('Llamas',  40,  1, 0, 90, 'buff',   YELLOW,
      '+0.5·pwr def propia temporal (2t aprox). Coste 40 EN.'),
    H('Volcán',  120, 2, 4, 85, 'ataque', RED,
      '+4 quemaduras a todos los enemigos a la vez. CD 4t. Coste 120 EN.'),
    VENDA, ENERGIA,
],

# ── Snake Charmer ────────────────────────────────────────────────
# Pasiva Amigo: la serpiente ataca al inicio de cada turno (35 dmg, 15% veneno)
# Bocajarro: hits aleatorios entre 10 y 50, cada uno hace 5·pwr dmg
'Snake Charmer': [
    H('Bocajarro',  30,  0, 0, 90, 'ataque', ORANGE,
      'Multi-hit aleatorio (10-50 golpes) × 5·pwr dmg cada uno. '
      '20% sangrado por golpe. Pasiva: serpiente +35 dmg al inicio del turno. Coste 30 EN.'),
    H('Ágil',       40,  1, 0, 90, 'buff',   TEAL,
      '+8 velocidad al aliado objetivo. Coste 40 EN.'),
    H('Serpiente',  160, 2, 3, 85, 'ataque', GREEN,
      '200·pwr dmg + 2 venenos + 1 stun al enemigo. CD 3t. Coste 160 EN.'),
    VENDA, ENERGIA,
],

# ── Apostador ────────────────────────────────────────────────────
# Nunca falla (preci=100)
# Pasiva Maleta: inmune locura; sombras invocadas hacen 30 dmg/turno
# Apostar: 3 resultados posibles al azar (180 dmg / cura 80 HP / +0.1 pwr)
# Bomba: 50/50 → 800·pwr al enemigo O 600 dmg a sí mismo
'Apostador': [
    H('Apostar',  3,  0, 0, 100, 'ataque', YELLOW,
      'Azar (1/3 cada): A) 180 dmg al enemigo / B) cura 80 HP propio / '
      'C) +0.1 pwr propio. Nunca falla. Coste 3 EN.'),
    H('Invocar',  10, 1, 0, 100, 'buff',   PURPLE,
      'Invoca una entidad aleatoria: Sombra (30 dmg/t), Sol (cura), '
      'Lluvia (elimina quemaduras), Pájaro (+vel)... Nunca falla.'),
    H('Bomba',    20, 2, 2, 100, 'ataque', RED,
      '50% de probabilidad: A) 800·pwr dmg al enemigo / '
      'B) 600 HP de daño propio. Nunca falla. CD 2t.'),
    VENDA, ENERGIA,
],

# ── Natural ──────────────────────────────────────────────────────
# mutado=0 → Zarza disponible | mutado=1 → Protección disponible
# Pasiva Extra: Precisión de Naturaleza es inamovible (no puede reducirse)
# Protección: EFT adefensa → +0.3 def al aliado 3t (se revierte al expirar)
'Natural': [
    H('Plantar',    8,   0, 0, 90, 'ataque', DGREEN,
      '+1 carga de cura al aliado objetivo. '
      'Quita quemaduras activas del aliado. Coste 8 EN.'),
    H('Zarza',      60,  1, 0, 90, 'ataque', GREEN,
      '[mutado=0] 140 dmg + 1 sangrado al enemigo. Coste 60 EN.'),
    H('Protección', 40,  1, 0, 90, 'buff',   TEAL,
      '[mutado=1] 252·pwr escudo + EFT +0.3 def al aliado 3t '
      '(def se revierte al expirar). Coste 40 EN.'),
    H('Naturaleza', 100, 2, 3, 85, 'soporte',DGREEN,
      'Cura a todos los aliados según sus cargas_cura acumuladas. CD 3t.'),
    PASTO, CURA_H, ENERGIA,
],

# ── Natural Heal ─────────────────────────────────────────────────
# Variante soporte de Natural: siempre mutado=1, sin Zarza
'Natural Heal': [
    H('Plantar',    8,  0, 0, 90, 'soporte', DGREEN,
      '+cargas de cura a todos los aliados + quita quemaduras.'),
    H('Naturaleza', 40, 1, 0, 85, 'soporte', GREEN,
      'Cura a todos los aliados: 28 × cargas_cura por aliado.'),
    H('Protección', 50, 2, 3, 85, 'buff',    TEAL,
      'Cura + EFT +0.3 def 3t al aliado objetivo (se revierte al expirar). CD 3t.'),
    PASTO, CURA_H, ENERGIAR,
],

# ── Diablillo ────────────────────────────────────────────────────
# Pasiva Corazón de Fuego: al aplicar 1 quemadura → recupera +15 HP y +0.04 pwr
# Todos los ataques generan quemaduras y curan vida propia
'Diablillo': [
    H('Llamarada Ígnea', 30,  0, 2, 90, 'ataque', ORANGE,
      '80 dmg + 1 quemadura al enemigo + cura 15 HP propio. '
      'Pasiva: +0.04 pwr al aplicar quemadura. CD 2t.'),
    H('Mordida Ígnea',   55,  1, 2, 90, 'ataque', RED2,
      '2 quemaduras al enemigo + cura 30 HP propio. CD 2t.'),
    H('Ráfaga Ígnea',    180, 2, 4, 80, 'ataque', RED,
      '260 dmg + 3 quemaduras al enemigo + cura 45 HP propio. CD 4t.'),
    VENDA, ENERGIA,
],

# ── Chiquitin ────────────────────────────────────────────────────
# Pasiva Regenerativo: recupera TODO su HP al inicio de cada turno
# Stats base muy bajos (HP=400) pero la pasiva lo compensa
'Chiquitin': [
    H('Bocajarro',    2,  0, 2, 95, 'ataque', ORANGE,
      'Multi-hit (10-50 golpes) × 5·pwr dmg. 20% sangrado por golpe. CD 2t.'),
    H('Mordida Ígnea',8,  1, 2, 90, 'ataque', RED2,
      '2 quemaduras al enemigo (sin escalar con poder). CD 2t.'),
    H('Ira',          10, 2, 2, 85, 'buff',   YELLOW,
      '+1 pwr permanente propio (no se revierte). CD 2t.'),
    VENDA, ENERGIA,
],

# ── Guadaña ──────────────────────────────────────────────────────
# Pasiva Concentración: Canalizar da doble energía (120 EN)
# Corte Mortal: EFT bdefensa → -0.3 def al enemigo 2t (se recupera al expirar)
'Guadaña': [
    H('Golpe Desgarrador', 20, 0, 0, 90, 'ataque', RED,
      'Dmg variable según % HP del enemigo + 1 sangrado. Coste 20 EN.'),
    H('Corte Mortal',      50, 1, 4, 90, 'ataque', RED2,
      '140 dmg + EFT -0.3 def al enemigo 2t (def se recupera al expirar). CD 4t.'),
    H('Segar',             90, 2, 5, 85, 'ataque', DPURPLE,
      '200 dmg (segundo impacto de la guadaña). CD 5t. Coste 90 EN.'),
    VENDA, ENERGIA,
],

# ── Crossbow ─────────────────────────────────────────────────────
# Pasiva Mochila: daño de Crossbow es irreflejable; x2 tras 2 ataques consecutivos
# Disparo Explosivo: 50·pwr inmediato + EFT daño 350·pwr en el siguiente turno
'Crossbow': [
    H('Flecha Explosiva',    3,  0, 0, 90, 'ataque', ORANGE,
      '90·pwr dmg (dispara 2 flechas). Daño irreflejable. '
      'Pasiva: x2 daño tras 2 ataques seguidos. Coste 3 EN.'),
    H('Eliminador de Ruido', 40, 1, 4, 90, 'ataque', PURPLE,
      '120·pwr dmg + 2 silenciados al enemigo. CD 4t.'),
    H('Disparo Explosivo',   90, 2, 5, 80, 'ataque', RED,
      '50·pwr dmg inmediato + EFT: bomba explota el siguiente turno '
      '(350·pwr dmg adicional). CD 5t.'),
    VENDA, ENERGIA,
],

# ── Support ──────────────────────────────────────────────────────
# Pasiva Maleta:
#   - Puede usar Curar y Energiar sobre aliados
#   - Sobrecargar tiene precisión inamovible (no puede reducirse)
'Support': [
    H('Escudo',      10, 0, 0,  90, 'buff',    BLUE,
      '80·pwr escudo HP + +0.05 def al aliado objetivo. Coste 10 EN.'),
    H('Agilizar',    30, 1, 2,  90, 'buff',    TEAL,
      '+8 velocidad al aliado objetivo. CD 2t.'),
    H('Purificador', 0,  2, 0,  90, 'soporte', WHITE,
      'Quita TODAS las cargas de TODOS los personajes del campo. Gratuito.'),
    H('Sobrecargar', 20, None,4,85, 'buff',    YELLOW,
      '+3 pwr al aliado objetivo por ~3t. Precisión inamovible.'),
    CURA_H, ENERGIAR,
],

# ── Loco ─────────────────────────────────────────────────────────
# Energía base solo 18 — muy limitado
# Pasiva Locuraaaa: locura escala daño de ataques; Calma cura HP = valor locura
# Moneda: azar → cara (+100 locura propia +30 al enemigo) / cruz (-locura propia)
'Loco': [
    H('Puñetazo', 4,  0, 2, 90, 'ataque', RED,
      'Dmg físico al enemigo + 1 silenciado al enemigo. '
      'La locura puede redirigir el golpe hacia uno mismo. CD 2t. Coste 4 EN.'),
    H('Calma',    7,  1, 0, 90, 'soporte',GREEN,
      'Te curas HP exactamente igual a tu locura actual. '
      'Reduce tu locura. Coste 7 EN.'),
    H('Moneda',   18, 2, 3, 85, 'buff',   YELLOW,
      'Cara: +100 locura propia y +30 locura al enemigo. '
      'Cruz: -locura propia. Azar puro. CD 3t.'),
    VENDA, ENERGIA,
],

# ── Root ─────────────────────────────────────────────────────────
# Pasiva Empezar con Buen Pie: primeros 3 turnos regenera HP máximo
# Conexión: transfiere el daño recibido por el objetivo a Root durante 3t
'Root': [
    H('Defensa Suprema', 15, 0, 2, 90, 'buff',    BLUE,
      '+0.2 def propia (por 2t aprox). CD 2t. Coste 15 EN.'),
    H('Raíces',          30, 1, 4, 90, 'ataque',  DGREEN,
      '130 dmg + 2 inmovilizado al enemigo (no puede atacar 2t). CD 4t.'),
    H('Conexión',        50, 2, 6, 85, 'buff',    TEAL,
      'Todo el daño que reciba el objetivo durante 3t te es transferido '
      '(o al revés: Conexión Inversa). CD 6t. Coste 50 EN.'),
    CURA_H, ENERGIA,
],

# ── Santa Claus ──────────────────────────────────────────────────
# Energía base solo 15 — muy limitado
# Pasiva Nieve: 25% de congelar al enemigo con cada habilidad
# Estrés Navideño: -0.6 pwr al enemigo (permanente, no es EFT)
'Santa Claus': [
    H('Bola de Nieve',   2,  0, 2, 90, 'ataque', LBLUE,
      '+1 hielo (congelación 1t) al enemigo. '
      'Pasiva: 25% congelar extra con cualquier habilidad. Coste 2 EN.'),
    H('Mierda de Reno',  8,  1, 4, 90, 'ataque', ORANGE,
      '+2 silenciados + +1 hielo al enemigo. CD 4t. Coste 8 EN.'),
    H('Estrés Navideño', 10, 2, 0, 85, 'ataque', RED,
      '-0.6 pwr permanente al enemigo (no se revierte). Coste 10 EN.'),
    VENDA, ENERGIA,
],

# ── Werewolf ─────────────────────────────────────────────────────
# Energía regenera +5/turno (en vez de +2)
# Pasiva Sangreee:
#   Cada 3 turnos: si sangre > 100 → cura 5 × (sangre-100) HP propio
#   Si sangre enemigo llega a 0 → ese enemigo pierde 400 HP
# Ensangrentar: roba 1-5 gotas sangre + 35% añade 1 sangrado
# Morder: roba 4-8 gotas + lifesteal (cura % del daño infligido)
# Abalanzarse: roba 10-20 gotas + 60% inflige 1 hemorragia
'Werewolf': [
    H('Ensangrentar', 10, 0, 0, 90, 'ataque', RED,
      '45 dmg al enemigo + roba 1-5 gotas de sangre. '
      '35% añade 1 sangrado. Pasiva: cura cada 3t con sangre excedente.'),
    H('Morder',       30, 1, 2, 90, 'ataque', RED2,
      '80 dmg + roba 4-8 gotas sangre + lifesteal (cura % del daño). CD 2t.'),
    H('Abalanzarse',  60, 2, 4, 85, 'ataque', DPURPLE,
      '120 dmg + roba 10-20 gotas sangre. 60% inflige 1 hemorragia. CD 4t.'),
    PASTO, ENERGIA,
],

# ── Runeforge ────────────────────────────────────────────────────
# Pasiva Aprender: +20 vida_runa por turno; mejora calidad piezas forjadas
# Runa: mientras tenga vida_runa > 0 el aliado es invulnerable
# Forjar: calidad aleatoria → sube pwr O def del aliado (resultado variable)
'Runeforge': [
    H('Aplastar', 10, 0, 0, 90, 'ataque', ORANGE,
      '90 dmg al enemigo con el martillo. Coste 10 EN.'),
    H('Forjar',   30, 1, 5, 90, 'buff',   YELLOW,
      'Forja una pieza de calidad aleatoria para el aliado: '
      'sube pwr O def según resultado. CD 5t. Coste 30 EN.'),
    H('Runa',     90, 2, 7, 80, 'buff',   TEAL,
      'Aliado invulnerable mientras la runa tenga vida (vida_runa: +20/turno). '
      '+1 carga invencible. CD 7t. Coste 90 EN.'),
    VENDA, ENERGIA,
],

# ── Serenità ─────────────────────────────────────────────────────
# Maga curativa de Parma — NO inflige daño directo
# Pasiva Costanza: al inicio de SU turno, todos los aliados +30 HP
# Armonia: cura según el HP del aliado:
#   HP > 50% → 150·pwr cura + +0.05 pwr al objetivo
#   HP < 50% → 250·pwr cura
#   HP muy bajo → 350·pwr cura + +0.15 pwr al objetivo
# Scelta: elige automáticamente lo más beneficioso: +0.15 def O +0.15 pwr
# Luce: purifica estados negativos + duplica Costanza (30→60 HP/t) por 4t
'Serenità': [
    H('Armonia',  15, 0, 2, 100, 'soporte', GREEN,
      'Cura al aliado según su HP: >50% → 150·pwr (+ +0.05 pwr); '
      '<50% → 250·pwr; muy bajo → 350·pwr (+ +0.15 pwr). CD 2t.'),
    H('Scelta',   40, 1, 4,  90, 'buff',    YELLOW,
      'Elige lo más beneficioso para el aliado: '
      '+0.15 def O +0.15 pwr (permanente). CD 4t. Coste 40 EN.'),
    H('Luce',     60, 2, 6,  90, 'buff',    LBLUE,
      'Purifica todos los estados negativos del aliado + '
      'duplica Costanza (30→60 HP/t) durante 4t. CD 6t.'),
    CURA_H, ENERGIAR,
],
}

# ──────────────────────────────────────────────────────────────────
#  PASIVAS
# ──────────────────────────────────────────────────────────────────
PASIVAS = {
    # ── Warrior: mutado=1 → +0.05 pwr/turno; mutado=0 (Tank) → +0.025 def/turno
    'Warrior':
        '⚔ Juicio Final\n'
        'Cada turno: +0.05 de poder acumulado.\n'
        '(Warrior Tank: +0.025 de defensa acumulada en su lugar)',

    'Warrior Tank':
        '🛡 Juicio Final (versión tanque)\n'
        'Cada turno: +0.025 de defensa acumulada permanentemente.\n'
        'Misma clase que Warrior pero orientado a aguante.',

    # ── Magician: frenesí → 40% de lanzar un segundo Orbe tras el primero
    'Magician':
        '🌀 Frenesí\n'
        'Al lanzar Orbe (ataque 1) tiene un 40% de probabilidades\n'
        'de lanzar un segundo Orbe automáticamente.',

    # ── Hereje: frenesí igual → 40% segundo ataque 1; pwr sube con Ira
    'Hereje':
        '🌀 Frenesí\n'
        'Al lanzar Flecha (ataque 1) tiene un 40% de probabilidades\n'
        'de disparar una segunda Flecha automáticamente.',

    # ── Maldi: maestro de pociones → 50% de envenenar al atacar con ataque 1
    'Maldi':
        '🧪 Maestro de Pociones\n'
        'Al usar Mal (ataque 1) tiene un 50% de probabilidades\n'
        'de lanzar una poción venenosa extra (+1 carga veneno).\n'
        '(1% de probabilidad: poción concentrada, +2 cargas veneno)',

    # ── Thief: suerte de principiante → primer turno: Daga da 5 golpes fijos + invisible 3t
    'Thief':
        '🍀 Suerte de Principiante\n'
        'Si el PRIMER ataque del combate es Daga: garantiza 5 golpes\n'
        'y empieza invisible durante 3 turnos.\n'
        'Cada golpe de Daga da +0.1 pwr permanente.',

    # ── Shapeshifter: Incansable → al transformarse recupera velocidad por defecto
    'Shapeshifter':
        '🐆 Incansable\n'
        'Al usar Transformación recupera su velocidad base:\n'
        '→ Forma humana: vel=32.  → Forma pantera: vel=78.\n'
        'Zarpazo (pantera) hace más daño que Rayo (humano).',

    # ── Healer: Apoyo → puede usar "curar" y "energiar" con el objetivo
    'Healer':
        '💚 Apoyo\n'
        'Puede canalizar su cura a un objetivo usando "Curar",\n'
        'y dar energía usando "Energiar".\n'
        'NO hace daño directo — personaje de soporte puro.',

    # ── Mace: concentración → en una canalización recupera el doble de energía
    'Mace':
        '🔋 Concentración\n'
        'Al usar la canalización de Energía recupera el DOBLE\n'
        'de energía (120 en lugar de 60).',

    # ── Fires: ignífugo → las quemaduras NO le hacen daño a sí mismo
    'Fires':
        '🔥 Ignífugo\n'
        'Las quemaduras no le hacen daño.\n'
        'No tiene ataques directos de daño — solo aplica quemaduras.\n'
        'Volcán aplica 4×pwr quemaduras en área.',

    # ── Snake Charmer: amigo → serpiente ataca junto con cada acción (35 dmg, 15% veneno)
    'Snake Charmer':
        '🐍 Amigo (Serpiente)\n'
        'Al inicio de CADA turno su serpiente ataca al objetivo\n'
        'haciendo 35 de daño (ignora poder/defensa).\n'
        'La serpiente tiene un 15% de añadir +1 carga de veneno.',

    # ── Apostador: maleta (3 pasivas) + casinooo + amigo (sombras)
    'Apostador':
        '🎰 Maleta (3 pasivas)\n'
        '• Casinooo: inmune a volverse loco (locura no le afecta).\n'
        '• Amigo: sus sombras atacan junto a él (30 dmg/sombra, ignora poder).\n'
        '  Invocar genera +1 sombra. Las sombras atacan al objetivo cada turno.',

    # ── Natural: extra → ataque 3 (Naturaleza) con precisión que no se puede bajar
    'Natural':
        '🌿 Extra\n'
        'Su ataque super (Naturaleza) tiene precisión que no puede\n'
        'ser reducida por ningún efecto.\n'
        'mutado=0: accede a Zarza.  mutado=1: accede a Protección.',

    # ── Natural Heal: igual que Natural (mismo personaje con mutado=1)
    'Natural Heal':
        '🌿 Extra (variante curativa)\n'
        'Su ataque super (Naturaleza) tiene precisión que no puede\n'
        'ser reducida. Orientada a curación — mutado=1 (Protección).\n'
        'Pasto cura un 0.5% HP máx a todos cada turno.',

    # ── Diablillo: Corazón de Fuego → al aplicar 1 quemadura se cura 15 HP y 15 EN
    'Diablillo':
        '❤️‍🔥 Corazón de Fuego\n'
        'Cada vez que aplica 1 quemadura a un enemigo:\n'
        '  +15 HP (no afecta poder) y +15 energía para sí mismo.\n'
        'Llamarada: +15 HP. Mordida Ígnea: +30 HP. Ráfaga: +45 HP.',

    # ── Chiquitin: regenerativo → al PRINCIPIO de su turno recupera TODA la vida
    'Chiquitin':
        '💖 Regenerativo\n'
        'Al INICIO de su turno recupera TODA la vida al máximo\n'
        '(sube a maxHP completo antes de actuar).\n'
        'Tiene solo 400 HP base, pero es prácticamente inmortal.',

    # ── Guadaña: concentración → doble energía en canalización (igual que Mace)
    'Guadaña':
        '🔋 Concentración\n'
        'Al usar la canalización de Energía recupera el DOBLE\n'
        'de energía (120 en lugar de 60).\n'
        'Segar hace daño doble si el objetivo tiene menos de 50% HP.',

    # ── Crossbow: mochila (3 pasivas) → x2 tras 2 ataques 1, daño no reflejable
    'Crossbow':
        '🎒 Mochila (3 pasivas)\n'
        '• x2: después de lanzar 2 ataques básicos seguidos,\n'
        '  el siguiente disparo es doble (2 flechas).\n'
        '• Solo ida: su daño NO puede ser reflejado por ningún efecto.',

    # ── Loco: locuraaaa → su locura potencia los ataques en lugar de debilitarle
    'Loco':
        '🤪 Locuraaaa\n'
        'Su locura POTENCIA sus ataques (daño × (locura/100 + 1))\n'
        'en lugar de volverle contra sí mismo.\n'
        'Calma: se cura HP igual al valor actual de locura y la resetea a 0.',

    # ── Root: Empezar con buen pie → primeros 3 turnos regenera vida al máximo
    'Root':
        '🌱 Empezar con Buen Pie\n'
        'Durante los PRIMEROS 3 TURNOS del combate regenera\n'
        'su vida al máximo al inicio de cada uno de esos turnos.\n'
        'Conexión: enlaza con objetivo — comparte daño recibido.',

    # ── Santa Claus: nieve → 25% de congelar al objetivo con cada habilidad
    'Santa Claus':
        '❄️ Nieve\n'
        'Con CADA habilidad que use tiene un 25% de probabilidades\n'
        'de congelar al objetivo durante 1 turno extra.',

    # ── Werewolf: sangreee → cada 3 turnos se cura según su exceso de sangre
    'Werewolf':
        '🐺 Sangreee\n'
        'Cada 3 turnos: si tiene más de 100 gotas de sangre,\n'
        'se cura 5 HP por cada gota de exceso (sangre − 100).\n'
        'Si la sangre del enemigo llega a 0: ese enemigo pierde 400 HP.',

    # ── Support: maleta (3 pasivas) → apoyo + extra + sobrecargar sin reducción prec.
    'Support':
        '🎒 Maleta (3 pasivas)\n'
        '• Apoyo: puede usar Curar y Energiar sobre aliados.\n'
        '• Extra: Sobrecargar tiene precisión que no puede reducirse.\n'
        'NO hace daño directo — personaje de soporte puro.',

    # ── Runeforge: aprender → cada turno sube vida_runa +20 y mejora calidad piezas
    'Runeforge':
        '📖 Aprender\n'
        'Por cada turno que pasa su runa gana +20 de vida máxima\n'
        'y aumenta la probabilidad de forjar piezas de mayor calidad.\n'
        'Runa: invulnerabilidad total mientras la runa tenga vida.',

    # ── Serenità: Costanza → cada turno cura 30 HP a todos los aliados vivos
    'Serenità':
        '✨ Costanza (Constancia)\n'
        'Mientras Serenità esté viva, al inicio de CADA turno\n'
        'todos sus aliados recuperan 30 HP (ignora poder/defensa).\n'
        'Luce duplica Costanza a 60 HP/turno durante 4 turnos.',
}


# ──────────────────────────────────────────────────────────────────
#  ESCENARIOS (del motor original, escenario=randint(1,11))
# ──────────────────────────────────────────────────────────────────
import random as _random

ESCENARIOS = {
    # id: (nombre, png_file, descripcion_corta, efecto_tipo, valor)
    # efecto_tipo: None | 'locura' | 'def_agil' | 'pwr_mago' |
    #              'def_vel_guerrero' | 'vel_misterioso' |
    #              'preci_menos' | 'vel_invertida' | 'energia_inf'
    1:  ('Pradera',          'fondo_pradera.png',
         'Bella pradera — sin efectos especiales.',
         None, 0),
    2:  ('Pradera',          'fondo_pradera.png',
         'Bella pradera — sin efectos especiales.',
         None, 0),
    3:  ('Pradera',          'fondo_pradera.png',
         'Bella pradera — sin efectos especiales.',
         None, 0),
    4:  ('Caos',             'fondo_caos.png',
         'El caos consume a todos: +20 locura inicial.',
         'locura', 20),
    5:  ('Bosque',           'fondo_bosque.png',
         'Bosque: personajes agiles +0.25 def.',
         'def_agil', 0.25),
    6:  ('Dimension Psiquica','fondo_psiquico.png',
         'Dimension psiquica: magos +0.25 pwr.',
         'pwr_mago', 0.25),
    7:  ('Ciudad',           'fondo_ciudad.png',
         'Ciudad: guerreros +0.2 def y +25 vel.',
         'def_vel_guerrero', (0.2, 25)),
    8:  ('Metaverso',        'fondo_metaverso.png',
         'Metaverso: personajes misteriosos +60 vel.',
         'vel_misterioso', 60),
    9:  ('Noche',            'fondo_noche.png',
         'Noche: todos -20% precision.',
         'preci_menos', 20),
    10: ('Patas Arriba',     'fondo_patosarriba.png',
         'Patas arriba: el mas lento ataca primero.',
         'vel_invertida', 0),
    11: ('Fuente de Energia','fondo_energia.png',
         'Fuente infinita: todos +100000 energia.',
         'energia_inf', 100000),
}

# Tipo de personaje para aplicar efectos de escenario
# 0=misterioso, 1=guerrero, 2=agil, 3=mago
TIPO_PERSONAJE = {
    'Warrior':      1, 'Warrior Tank':  1, 'Mace':      1,
    'Magician':     3, 'Hereje':        3, 'Maldi':     3,
    'Fires':        3, 'Serenita':      3, 'Serenita':  3,
    'Thief':        2, 'Snake Charmer': 2, 'Diablillo': 2,
    'Chiquitin':    2, 'Werewolf':      2,
    'Shapeshifter': 0, 'Apostador':     0, 'Loco':      0,
    'Root':         0, 'Santa Claus':   0, 'Runeforge': 1,
    'Healer':       3, 'Natural':       3, 'Natural Heal': 3,
    'Crossbow':     1, 'Support':       3, 'Guadana':   1,
}

def aplicar_escenario(escenario_id: int, luchadores: list, log) -> str:
    """Aplica los efectos del escenario a los luchadores. Devuelve desc."""
    esc = ESCENARIOS.get(escenario_id)
    if not esc:
        return 'Escenario desconocido'
    nombre, png, desc, efecto, val = esc
    if efecto is None:
        return desc
    for lf in luchadores:
        tipo = TIPO_PERSONAJE.get(lf.personaje, -1)
        if efecto == 'locura':
            lf.cargas['locura'] = lf.cargas.get('locura', 0) + val
            log.add(f'Escenario {nombre}: {lf.jugador} +{val} locura')
        elif efecto == 'def_agil' and tipo == 2:
            lf.defn += val
            log.add(f'Escenario {nombre}: {lf.jugador} (agil) +{val} def')
        elif efecto == 'pwr_mago' and tipo == 3:
            lf.pwr += val
            log.add(f'Escenario {nombre}: {lf.jugador} (mago) +{val} pwr')
        elif efecto == 'def_vel_guerrero' and tipo == 1:
            lf.defn += val[0]; lf.vel += val[1]
            log.add(f'Escenario {nombre}: {lf.jugador} (guerrero) +def +vel')
        elif efecto == 'vel_misterioso' and tipo == 0:
            lf.vel += val
            log.add(f'Escenario {nombre}: {lf.jugador} (misterioso) +{val} vel')
        elif efecto == 'preci_menos':
            lf.preci_mod = getattr(lf, 'preci_mod', 0) - val
            log.add(f'Escenario {nombre}: {lf.jugador} -{val}% precision')
        elif efecto == 'energia_inf':
            lf.en = min(lf.maxen, lf.en + 1000)  # no 100k para no romper UI
            log.add(f'Escenario {nombre}: {lf.jugador} +energia')
    return desc

# ──────────────────────────────────────────────────────────────────
#  LUCHADOR
# ──────────────────────────────────────────────────────────────────
class Luchador:
    def __init__(self, jugador, personaje, casco, armadura, botas, pos_idx):
        self.jugador   = jugador
        self.personaje = personaje
        self.pos_idx   = pos_idx

        # Stats base
        hp, en, pwr, defn, vel = STATS_BASE.get(personaje, (1000,100,1.0,1.0,50))
        self.maxhp  = hp
        self.hp     = hp
        self.maxen  = en
        self.en     = en
        self.pwr    = pwr
        self.defn   = defn
        self.vel    = vel
        self.rcura  = 1.0   # multiplicador de cura recibida

        # Build
        self.casco    = casco    or ''
        self.armadura = armadura or ''
        self.botas    = botas    or ''

        # Cargas de estado
        self.cargas = {k:0 for k in [
            'sangrado','quemado','veneno','stun','hielo','silenciado',
            'paralizado','inmovilizado','maldita','hemorragia','invencible',
            'cura','escudo','apower','bpower','adefensa','bdefensa','locura',
        ]}

        # Efectos temporales: lista de (nombre_efecto, turnos_restantes)
        self.efectos_temp = []  # [(nombre, turnos_restantes, valor)]

        # Cooldowns: [cd_slot0, cd_slot1, cd_slot2]
        self.cooldowns = [0, 0, 0]
        # Cooldown build
        self.cd_build = 0

        self.robovida  = 0.0
        self.reflejar  = 0.0
        self.sangre    = 10
        self.pantera   = 0   # 0=humano, 1=pantera (Shapeshifter)
        self.mutado    = 0   # 0 o 1 para personajes con dos formas

        # Cooldowns de build: {nombre_item: nturnos_disponible}
        self.cd_build_dict = {}

        # Visual
        self.sprite    = None
        self._load_sprite()
        self.flash_timer = 0   # frames de flash rojo al recibir daño
        self.mensaje   = ''
        self.msg_timer = 0

        # Salud previa para detectar daño
        self._prev_hp = hp

    def _load_sprite(self):
        path = os.path.join('sprites', f'{self.personaje}.png')
        if os.path.exists(path):
            try:
                img = pygame.image.load(path).convert_alpha()
                self.sprite = pygame.transform.smoothscale(img, (110, 110))
            except:
                self.sprite = None

    @property
    def vivo(self): return self.hp > 0

    def recibir_dano(self, dano):
        if self.cargas['invencible'] > 0:
            return 0
        real = max(0, dano)
        self.hp -= real
        self.flash_timer = 12
        return real

    def curar(self, cantidad):
        curado = min(cantidad * self.rcura, self.maxhp - self.hp)
        self.hp = min(self.maxhp, self.hp + cantidad * self.rcura)
        return curado

    def aplicar_cargas_inicio_turno(self, log):
        """Aplica sangrado, veneno, quemado, hemorragia, maldita al inicio del turno"""
        msgs = []

        # Chiquitin: regenera toda la vida
        if self.personaje == 'Chiquitin':
            self.hp = self.maxhp
            msgs.append(f'{self.jugador} regenera toda su vida!')

        # Veneno >= 10 → muerte
        if self.cargas['veneno'] >= 10:
            self.hp = -999999
            msgs.append(f'💀 {self.jugador} muere por exceso de veneno!')
            return msgs

        # Sangrado x3 → hemorragia
        if self.cargas['sangrado'] >= 3:
            self.cargas['hemorragia'] += 1
            msgs.append(f'🩸 {self.jugador} desarrolla hemorragia!')

        # Veneno
        if self.cargas['veneno'] >= 1:
            dmg = 5 * self.cargas['veneno']
            self.hp -= dmg
            msgs.append(f'☠ Veneno: {self.jugador} -{dmg} HP')

        # Quemadura
        if self.cargas['quemado'] >= 1:
            dmg = 36 * self.cargas['quemado']
            self.hp -= dmg
            msgs.append(f'🔥 Quemadura: {self.jugador} -{dmg} HP')

        # Sangrado
        if self.cargas['sangrado'] >= 1:
            dmg = 15 * self.cargas['sangrado']
            self.hp -= dmg
            self.sangre -= 1
            msgs.append(f'🩸 Sangrado: {self.jugador} -{dmg} HP')

        # Hemorragia
        if self.cargas['hemorragia'] >= 1:
            dmg = 60 * self.cargas['hemorragia']
            self.hp -= dmg
            self.sangre -= 3
            msgs.append(f'💀 Hemorragia: {self.jugador} -{dmg} HP')

        # Maldición
        if self.cargas['maldita'] >= 1:
            dmg = 30 * self.cargas['maldita']
            self.hp -= dmg
            msgs.append(f'👻 Maldición: {self.jugador} -{dmg} HP')

        # Cura por cargas
        if self.cargas['cura'] >= 1 and self.hp > 0:
            curado = 28 * self.cargas['cura'] * self.rcura
            self.hp = min(self.maxhp, self.hp + curado)
            msgs.append(f'💚 Cargas curan: {self.jugador} +{int(curado)} HP')

        return msgs

    def decrementar_efectos_temporales(self, nturnos, log):
        """Decrementa stun/hielo/paralizado/silenciado/inmovilizado por turno"""
        for k in ['stun','hielo','paralizado','silenciado','inmovilizado']:
            if self.cargas[k] > 0:
                self.cargas[k] -= 1

        # Efectos temporales de stats
        nuevos = []
        for (efecto, turnos, val) in self.efectos_temp:
            if turnos <= 1:
                # revertir
                if efecto == 'apower':   self.pwr  -= val
                elif efecto == 'bpower': self.pwr  += val
                elif efecto == 'adef':   self.defn -= val
                elif efecto == 'bdef':   self.defn += val
            else:
                nuevos.append((efecto, turnos-1, val))
        self.efectos_temp = nuevos

    def puede_actuar(self):
        """Devuelve (puede, razon)"""
        if self.cargas['stun'] > 0:
            return False, f'{self.jugador} está aturdido!'
        if self.cargas['hielo'] > 0:
            return False, f'{self.jugador} está congelado!'
        if self.cargas['inmovilizado'] > 0:
            return False, f'{self.jugador} está inmovilizado!'
        if self.cargas['paralizado'] > 0:
            if randint(0,100) <= 40:
                return False, f'{self.jugador} está paralizado!'
        return True, ''

    def pasiva_inicio_turno(self, nturnos):
        """Aplica la pasiva del personaje al inicio de su turno (según motor original)."""
        p = self.personaje

        # ── Warrior / Warrior Tank: "Juicio Final"
        # Warrior (mutado=1) → +0.05 pwr;  Warrior Tank (mutado=0) → +0.025 def
        if p == 'Warrior':
            if self.mutado == 1: self.pwr  += 0.05
            else:                self.defn += 0.025
        elif p == 'Warrior Tank':
            self.defn += 0.025

        # ── Root: "Empezar con buen pie" → primeros 3 turnos regenera toda la vida
        elif p == 'Root':
            if nturnos < 3:
                self.hp = self.maxhp

        # ── Chiquitin: "Regenerativo" → recupera TODA la vida cada turno
        elif p == 'Chiquitin':
            self.hp = self.maxhp

        # ── Werewolf: "Sangreee" → cada 3 turnos cura por exceso de sangre
        elif p == 'Werewolf':
            if nturnos > 0 and nturnos % 3 == 0:
                if self.sangre > 100:
                    sobrante = self.sangre - 100
                    self.sangre -= sobrante
                    curacion = sobrante * 5
                    self.hp = min(self.maxhp, self.hp + curacion)

        # ── Runeforge: "Aprender" → cada turno vida_runa sube +20
        elif p == 'Runeforge':
            if not hasattr(self, 'vida_runa'): self.vida_runa = 380
            self.vida_runa += 20

        # ── Serenità: "Costanza" → cura a TODOS los aliados vivos cada turno
        # La cura se aplica desde GestorCombate al inicio del turno de Serenità
        # porque necesita la lista completa de luchadores. Ver GestorCombate._iniciar_turno.

        # ── Snake Charmer: "Amigo" → la serpiente ataca al inicio del turno
        # (se aplica en _ejecutar_hab o en el gestor, aquí guardamos la flag)
        # La serpiente ataca al objetivo activo; se aplica en GestorCombate

        # Pasivas que NO tienen efecto de inicio de turno
        # (frenesí, maestro de pociones, suerte principiante, nieve, locuraaaa,
        #  corazón de fuego, concentración, ignífugo, incansable, extra, apoyo,
        #  mochila/x2/solo ida) → se aplican al ejecutar habilidades


# ──────────────────────────────────────────────────────────────────
#  EJECUTAR HABILIDAD
# ──────────────────────────────────────────────────────────────────
def ejecutar_habilidad(hab_nombre, atacante, objetivo, todos, nturnos, log):
    """Ejecuta la habilidad y devuelve lista de mensajes."""
    msgs = []
    atk = atacante
    tgt = objetivo
    p   = atk.personaje

    def dmg_base(base):
        d = base * atk.pwr / tgt.defn
        if tgt.cargas['invencible'] > 0: d = 0
        reflejo = d * atk.reflejar
        d -= reflejo
        d = max(0, d)
        tgt.recibir_dano(d)
        atk.hp -= reflejo
        if atk.robovida > 0:
            rob = d * min(1, atk.robovida)
            atk.hp = min(atk.maxhp, atk.hp + rob)
            if rob > 0: msgs.append(f'🩸 {atk.jugador} roba {int(rob)} HP')
        return d

    def check_preci(pct):
        return randint(0,100) <= pct

    # ─── Soporte ──────────────────────────────
    if hab_nombre == 'Venda':
        atk.curar(80)
        atk.cargas['quemado'] = max(0, atk.cargas['quemado'] - randint(1,3))
        atk.cargas['hemorragia'] = max(0, atk.cargas['hemorragia'] - randint(1,2))
        msgs.append(f'💊 {atk.jugador} usa Venda: +80 HP, quita quemaduras/hemorragias')
        return msgs

    if hab_nombre == 'Curar':
        cantidad = 100 * atk.pwr
        tgt.curar(cantidad)
        for k in ['veneno','sangrado','quemado','maldita']:
            tgt.cargas[k] = 0
        msgs.append(f'💚 {atk.jugador} cura a {tgt.jugador}: +{int(cantidad)} HP, purificado')
        return msgs

    if hab_nombre == 'Energía':
        atk.en = min(atk.maxen, atk.en + 60)
        msgs.append(f'⚡ {atk.jugador} canaliza: +60 energía')
        return msgs

    if hab_nombre == 'Energiar':
        tgt.en = min(tgt.maxen, tgt.en + 60)
        msgs.append(f'⚡ {atk.jugador} da energía a {tgt.jugador}: +60 EN')
        return msgs

    if hab_nombre == 'Pasto':
        for lf in todos:
            if lf.vivo:
                lf.curar(lf.maxhp * 0.005)
        msgs.append(f'🌿 {atk.jugador} usa Pasto: +0.5% HP a todos')
        return msgs

    if hab_nombre == 'Saltar':
        atk.en = min(atk.maxen, atk.en + 4)
        msgs.append(f'⏭ {atk.jugador} salta el turno (+4 EN)')
        return msgs

    # ─── Warrior ──────────────────────────────
    if p in ('Warrior', 'Warrior Tank'):
        if hab_nombre == 'Tajo':
            if not check_preci(95):
                msgs.append(f'💨 {atk.jugador} falla Tajo!')
            else:
                d = dmg_base(30)
                msgs.append(f'⚔ Tajo: {atk.jugador} → {tgt.jugador} -{int(d)} HP')
                if randint(0,100) <= 70:
                    tgt.cargas['sangrado'] += 1
                    msgs.append(f'🩸 Sangrado aplicado a {tgt.jugador}')
            atk.en -= 2
        elif hab_nombre == 'Estocada':
            if not check_preci(90):
                msgs.append(f'💨 {atk.jugador} falla Estocada!')
                atk.en -= 17
            else:
                d = dmg_base(101)
                msgs.append(f'⚔ Estocada: {atk.jugador} → {tgt.jugador} -{int(d)} HP')
                atk.en -= 45
        elif hab_nombre == 'Caballero':
            if atk.mutado == 0:
                tgt.hp = min(tgt.maxhp, tgt.hp + 120)
                tgt.defn += 0.2
                msgs.append(f'🛡 Caballero: escudo +120HP, +0.2 def a {tgt.jugador}')
                atk.en -= 60
            else:
                atk.pwr += 4
                msgs.append(f'💢 Furia: {atk.jugador} +4 pwr 1t')
                atk.en -= 60
        elif hab_nombre == 'Furia':
            atk.pwr += 4
            msgs.append(f'💢 Furia: {atk.jugador} +4 pwr 1t')
            atk.en -= 60

    # ─── Magician ──────────────────────────────
    elif p == 'Magician':
        if hab_nombre == 'Orbe':
            if not check_preci(90): msgs.append(f'💨 {atk.jugador} falla Orbe!')
            else:
                d = dmg_base(25)
                tgt.cargas['hielo'] = max(tgt.cargas['hielo'], 1)
                msgs.append(f'🔵 Orbe: -{int(d)} HP + congela 1t {tgt.jugador}')
            atk.en -= 20
        elif hab_nombre == 'Fuerza':
            atk.pwr += 0.2
            msgs.append(f'💪 {atk.jugador} +0.2 pwr permanente')
            atk.en -= 30
        elif hab_nombre == 'Tornado Fuego':
            tgt.cargas['quemado'] += 2
            msgs.append(f'🌪🔥 {atk.jugador} aplica 2 quemaduras a {tgt.jugador}')
            atk.en -= 60

    # ─── Hereje ──────────────────────────────
    elif p == 'Hereje':
        if hab_nombre == 'Flecha':
            if not check_preci(95): msgs.append(f'💨 {atk.jugador} falla Flecha!')
            else:
                d = dmg_base(40)
                msgs.append(f'🏹 Flecha: -{int(d)} HP a {tgt.jugador}')
            atk.en -= 20
        elif hab_nombre == 'Flecha Vampiro':
            if not check_preci(90): msgs.append(f'💨 {atk.jugador} falla Flecha Vampiro!')
            else:
                d = dmg_base(50)
                rob = d * 0.10
                atk.hp = min(atk.maxhp, atk.hp + rob)
                msgs.append(f'🏹🩸 Flecha Vampiro: -{int(d)} HP, +{int(rob)} HP robado')
            atk.en -= 35
        elif hab_nombre == 'Ira':
            atk.pwr += 1.0
            msgs.append(f'💢 {atk.jugador} +1 pwr permanente (Ira)')
            atk.en -= 40

    # ─── Maldi ──────────────────────────────
    elif p == 'Maldi':
        if hab_nombre == 'Mal':
            if not check_preci(95): msgs.append(f'💨 {atk.jugador} falla Mal!')
            else:
                d = dmg_base(40)
                tgt.cargas['maldita'] += 1
                msgs.append(f'👻 Mal: -{int(d)} HP + maldición a {tgt.jugador}')
            atk.en -= 20
        elif hab_nombre == 'Perforador Oscuro':
            if not check_preci(90): msgs.append(f'💨 {atk.jugador} falla Perforador Oscuro!')
            else:
                d = dmg_base(120)
                tgt.defn = max(0.1, tgt.defn - 0.4)
                msgs.append(f'🌑 Perforador: -{int(d)} HP, -0.4 def a {tgt.jugador}')
            atk.en -= 55
        elif hab_nombre == 'Diablo':
            atk.hp = min(atk.maxhp, atk.hp + atk.maxhp * 0.5)
            atk.pwr += 1.5
            msgs.append(f'😈 Diablo: {atk.jugador} +50% HP, +1.5 pwr 2t')
            atk.en -= 70

    # ─── Thief ──────────────────────────────
    elif p == 'Thief':
        if hab_nombre == 'Daga':
            if not check_preci(95): msgs.append(f'💨 {atk.jugador} falla Daga!')
            else:
                d = dmg_base(35)
                tgt.cargas['veneno'] += 1
                rob = d * 0.05
                atk.hp = min(atk.maxhp, atk.hp + rob)
                atk.pwr += 0.1
                msgs.append(f'🗡 Daga: -{int(d)} HP, veneno, +{int(rob)} HP robado, +0.1 pwr')
            atk.en -= 5
        elif hab_nombre == 'Fatiga':
            if not check_preci(90): msgs.append(f'💨 {atk.jugador} falla Fatiga!')
            else:
                d = dmg_base(80)
                msgs.append(f'🗡 Fatiga: -{int(d)} HP a {tgt.jugador}')
            atk.en -= 40
        elif hab_nombre == 'Energía para mí':
            robada = min(60, tgt.en)
            tgt.en -= robada
            atk.en = min(atk.maxen, atk.en + robada)
            d = dmg_base(300)
            msgs.append(f'⚡🗡 {atk.jugador} roba {int(robada)} EN y hace -{int(d)} HP')
            atk.en -= 0

    # ─── Shapeshifter ──────────────────────────────
    elif p == 'Shapeshifter':
        if hab_nombre in ('Rayo / Zarpazo', 'Rayo','Zarpazo'):
            if atk.pantera == 0:
                d = dmg_base(50)
                msgs.append(f'⚡ Rayo: -{int(d)} HP a {tgt.jugador}')
            else:
                d = dmg_base(70)
                if randint(0,100)<=60: tgt.cargas['sangrado']+=1
                msgs.append(f'🐾 Zarpazo: -{int(d)} HP + sangrado a {tgt.jugador}')
            atk.en -= 30
        elif hab_nombre in ('Escudo / Salto', 'Escudo'):
            tgt.hp = min(tgt.maxhp, tgt.hp + 200*atk.pwr)
            tgt.defn += 0.1
            msgs.append(f'🛡 Escudo: +{int(200*atk.pwr)} HP, +0.1 def a {tgt.jugador}')
            atk.en -= 60
        elif hab_nombre == 'Transformación':
            atk.pantera = 1 - atk.pantera
            forma = 'PANTERA 🐾' if atk.pantera else 'HUMANO ⚡'
            msgs.append(f'🔄 {atk.jugador} se transforma en {forma}')
            atk.en -= 50

    # ─── Healer ──────────────────────────────
    elif p == 'Healer':
        if hab_nombre == 'Heal':
            c = 100 * atk.pwr * atk.rcura
            tgt.curar(c)
            for k in ['veneno','sangrado','quemado','maldita']: tgt.cargas[k] = 0
            msgs.append(f'💚 Heal: +{int(c)} HP + purificado a {tgt.jugador}')
            atk.en -= 40
        elif hab_nombre == 'Bendecir':
            tgt.defn += 0.3
            tgt.cargas['cura'] += 3
            msgs.append(f'✨ Bendición: +0.3 def + 3 cargas cura a {tgt.jugador}')
            atk.en -= 50
        elif hab_nombre == 'Proteger':
            for lf in todos:
                if lf.vivo and lf != atk:
                    lf.hp = min(lf.maxhp, lf.hp + 300*atk.pwr)
            msgs.append(f'🛡 Proteger: +{int(300*atk.pwr)} HP a todos los aliados')
            atk.en -= 80

    # ─── Mace ──────────────────────────────
    elif p == 'Mace':
        if hab_nombre == 'Golpe Defensivo':
            if not check_preci(95): msgs.append(f'💨 {atk.jugador} falla Golpe Defensivo!')
            else:
                d = dmg_base(40)
                atk.defn += 0.08
                msgs.append(f'🔨 Golpe Defensivo: -{int(d)} HP a {tgt.jugador}, +0.08 def')
            atk.en -= 10
        elif hab_nombre == 'Agitador':
            if not check_preci(90): msgs.append(f'💨 {atk.jugador} falla Agitador!')
            else:
                for lf in todos:
                    if lf != atk and lf.vivo:
                        d = dmg_base(200) if lf == tgt else lf.recibir_dano(200*atk.pwr/lf.defn)
                msgs.append(f'🌍 Agitador: daño en área ({int(200*atk.pwr)} aprox)')
            atk.en -= 55
        elif hab_nombre == 'Salto Profundo':
            if not check_preci(85): msgs.append(f'💨 {atk.jugador} falla Salto Profundo!')
            else:
                d = dmg_base(300)
                tgt.cargas['stun'] = max(tgt.cargas['stun'], 1)
                msgs.append(f'💥 Salto Profundo: -{int(d)} HP + stun a {tgt.jugador}')
            atk.en -= 80

    # ─── Fires ──────────────────────────────
    elif p == 'Fires':
        if hab_nombre == 'Fuego':
            n = max(1, int(atk.pwr))
            tgt.cargas['quemado'] += n
            msgs.append(f'🔥 Fuego: {n} quemaduras a {tgt.jugador}')
            atk.en -= 15
        elif hab_nombre == 'Llamas':
            atk.defn += 0.5 * atk.pwr
            msgs.append(f'🔥 Llamas: +{0.5*atk.pwr:.2f} def a {atk.jugador} 2t')
            atk.en -= 30
        elif hab_nombre == 'Volcán':
            n = max(4, int(4*atk.pwr))
            for lf in todos:
                if lf != atk and lf.vivo:
                    lf.cargas['quemado'] += n
            msgs.append(f'🌋 Volcán: {n} quemaduras a todos los enemigos')
            atk.en -= 70

    # ─── Snake Charmer ──────────────────────────────
    elif p == 'Snake Charmer':
        if hab_nombre == 'Bocajarro':
            golpes = randint(10,50)
            d = (5 * atk.pwr / tgt.defn) * golpes
            if randint(0,100)<=20: tgt.cargas['sangrado']+=1
            tgt.recibir_dano(d)
            msgs.append(f'👊 Bocajarro: {golpes} golpes = -{int(d)} HP a {tgt.jugador}')
            atk.en -= 10
        elif hab_nombre == 'Ágil':
            tgt.vel += 10
            msgs.append(f'💨 Ágil: +10 vel a {tgt.jugador}')
            atk.en -= 30
        elif hab_nombre == 'Serpiente':
            if not check_preci(80): msgs.append(f'💨 {atk.jugador} falla Serpiente!')
            else:
                d = dmg_base(100)
                tgt.cargas['veneno'] += 2
                tgt.cargas['stun'] = max(tgt.cargas['stun'],1)
                msgs.append(f'🐍 Serpiente: -{int(d)} HP, 2 venenos, stun a {tgt.jugador}')
            atk.en -= 60

    # ─── Apostador ──────────────────────────────
    elif p == 'Apostador':
        if hab_nombre == 'Apostar':
            r = randint(1,3)
            if r == 1:
                d = dmg_base(180)
                msgs.append(f'🎲 Suerte! Apostador: -{int(d)} HP a {tgt.jugador}')
            elif r == 2:
                atk.curar(80)
                msgs.append(f'🎲 Suerte media: Apostador +80 HP')
            else:
                atk.pwr += 0.1
                msgs.append(f'🎲 Pequeña suerte: Apostador +0.1 pwr')
        elif hab_nombre == 'Invocar':
            r = randint(1,3)
            msgs.append(f'🎲 Apostador invoca criatura #{r} (efecto especial)')
        elif hab_nombre == 'Bomba':
            if randint(0,100) <= 50:
                d = dmg_base(800)
                msgs.append(f'💣 BOMBA! -{int(d)} HP a {tgt.jugador}')
            else:
                dmg = 600 * atk.pwr / atk.defn
                atk.hp -= dmg
                msgs.append(f'💣 La bomba explota a {atk.jugador}: -{int(dmg)} HP propio!')

    # ─── Natural / Natural Heal ──────────────────────────────
    elif p in ('Natural','Natural Heal'):
        if hab_nombre == 'Plantar':
            tgt.cargas['cura'] += 2
            tgt.cargas['quemado'] = max(0, tgt.cargas['quemado']-1)
            msgs.append(f'🌿 Plantar: 2 cargas cura + -1 quemadura a {tgt.jugador}')
            atk.en -= 20
        elif hab_nombre in ('Zarza',):
            d = dmg_base(140)
            tgt.cargas['sangrado'] += 1
            msgs.append(f'🌵 Zarza: -{int(d)} HP + sangrado a {tgt.jugador}')
            atk.en -= 40
        elif hab_nombre in ('Protección',):
            atk.curar(100*atk.pwr)
            atk.defn += 0.3
            msgs.append(f'🛡 Protección: +{int(100*atk.pwr)} HP, +0.3 def a {atk.jugador}')
            atk.en -= 50
        elif hab_nombre == 'Naturaleza':
            for lf in todos:
                if lf.vivo:
                    c = 28 * lf.cargas['cura'] * lf.rcura
                    lf.curar(c)
            msgs.append(f'🌿 Naturaleza: cura por cargas a todos')
            atk.en -= 40

    # ─── Diablillo ──────────────────────────────
    elif p == 'Diablillo':
        if hab_nombre == 'Llamarada Ígnea':
            d = dmg_base(80)
            tgt.cargas['quemado'] += 1
            atk.hp = min(atk.maxhp, atk.hp + 15)
            msgs.append(f'😈🔥 Llamarada: -{int(d)} HP, quemadura a {tgt.jugador}, +15 HP propio')
            atk.en -= 15
        elif hab_nombre == 'Mordida Ígnea':
            tgt.cargas['quemado'] += 2
            atk.hp = min(atk.maxhp, atk.hp + 30)
            msgs.append(f'😈 Mordida Ígnea: 2 quemaduras a {tgt.jugador}, +30 HP propio')
            atk.en -= 25
        elif hab_nombre == 'Ráfaga Ígnea':
            d = dmg_base(260)
            tgt.cargas['quemado'] += 3
            atk.hp = min(atk.maxhp, atk.hp + 45)
            msgs.append(f'😈💥 Ráfaga Ígnea: -{int(d)} HP, 3 quemaduras, +45 HP propio')
            atk.en -= 60

    # ─── Chiquitin ──────────────────────────────
    elif p == 'Chiquitin':
        if hab_nombre == 'Bocajarro':
            golpes = randint(10,50)
            d = (5 * atk.pwr / tgt.defn) * golpes
            if randint(0,100)<=20: tgt.cargas['sangrado']+=1
            tgt.recibir_dano(d)
            msgs.append(f'👊 Bocajarro: {golpes} golpes = -{int(d)} HP a {tgt.jugador}')
            atk.en -= 2
        elif hab_nombre == 'Mordida Ígnea':
            tgt.cargas['quemado'] += 2
            msgs.append(f'😈 Mordida Ígnea: 2 quemaduras a {tgt.jugador}')
            atk.en -= 8
        elif hab_nombre == 'Ira':
            atk.pwr += 1.0
            msgs.append(f'💢 Ira: {atk.jugador} +1 pwr')
            atk.en -= 10

    # ─── Guadaña ──────────────────────────────
    elif p == 'Guadaña':
        if hab_nombre == 'Golpe Desgarrador':
            d = dmg_base(60)
            tgt.cargas['sangrado'] += 1
            msgs.append(f'⚔ Golpe Desgarrador: -{int(d)} HP + sangrado a {tgt.jugador}')
            atk.en -= 20
        elif hab_nombre == 'Corte Mortal':
            d = dmg_base(140)
            tgt.defn = max(0.1, tgt.defn - 0.3)
            msgs.append(f'⚔ Corte Mortal: -{int(d)} HP, -0.3 def a {tgt.jugador}')
            atk.en -= 50
        elif hab_nombre == 'Segar':
            d1 = dmg_base(200)
            d2 = dmg_base(200)
            msgs.append(f'💀 Segar: doble impacto -{int(d1+d2)} HP total a {tgt.jugador}')
            atk.en -= 80

    # ─── Crossbow ──────────────────────────────
    elif p == 'Crossbow':
        if hab_nombre == 'Flecha Explosiva':
            d1 = dmg_base(50); d2 = dmg_base(50)
            msgs.append(f'🏹💥 Flecha Explosiva: 2×{int((d1+d2)/2)} = -{int(d1+d2)} HP a {tgt.jugador}')
            atk.en -= 30
        elif hab_nombre == 'Eliminador de Ruido':
            d = dmg_base(120)
            tgt.cargas['silenciado'] = max(tgt.cargas['silenciado'],2)
            msgs.append(f'🔇 Eliminar Ruido: -{int(d)} HP + silencia 2t a {tgt.jugador}')
            atk.en -= 50
        elif hab_nombre == 'Disparo Explosivo':
            d = dmg_base(150)
            msgs.append(f'💥 Disparo Explosivo: -{int(d)} HP + bomba 350 próx turno a {tgt.jugador}')
            atk.en -= 70

    # ─── Support ──────────────────────────────
    elif p == 'Support':
        if hab_nombre == 'Escudo':
            e = 80 * atk.pwr
            tgt.hp = min(tgt.maxhp, tgt.hp + e)
            tgt.defn += 0.1
            msgs.append(f'🛡 Escudo: +{int(e)} HP, +0.1 def a {tgt.jugador}')
            atk.en -= 40
        elif hab_nombre == 'Agilizar':
            tgt.vel += 10
            msgs.append(f'💨 Agilizar: +10 vel a {tgt.jugador}')
            atk.en -= 30
        elif hab_nombre == 'Purificador':
            for k in ['veneno','sangrado','quemado','maldita','hemorragia',
                      'stun','hielo','paralizado','silenciado','inmovilizado']:
                tgt.cargas[k] = 0
            msgs.append(f'✨ Purificador: todas las cargas negativas de {tgt.jugador} limpiadas')
            atk.en -= 50
        elif hab_nombre == 'Sobrecargar':
            tgt.pwr += 3
            msgs.append(f'💪 Sobrecargar: {tgt.jugador} +3 pwr por 3t')
            atk.en -= 80

    # ─── Loco ──────────────────────────────
    elif p == 'Loco':
        if hab_nombre == 'Puñetazo':
            if not check_preci(90): msgs.append(f'💨 {atk.jugador} falla Puñetazo!')
            else:
                d = dmg_base(50)
                tgt.cargas['silenciado'] = max(tgt.cargas['silenciado'],1)
                msgs.append(f'👊 Puñetazo: -{int(d)} HP + silencia 1t a {tgt.jugador}')
            atk.en -= 20
        elif hab_nombre == 'Calma':
            c = atk.cargas['locura']
            atk.curar(c)
            msgs.append(f'😌 Calma: {atk.jugador} cura {c} HP (= locura)')
            atk.en -= 30
        elif hab_nombre == 'Moneda':
            if randint(0,1): atk.cargas['locura'] = min(100, atk.cargas['locura']+20)
            else:             atk.cargas['locura'] = max(0,   atk.cargas['locura']-10)
            msgs.append(f'🎲 Moneda: locura de {atk.jugador} → {atk.cargas["locura"]}')

    # ─── Root ──────────────────────────────
    elif p == 'Root':
        if hab_nombre == 'Defensa Suprema':
            atk.defn += 0.2
            msgs.append(f'🌱 Defensa: {atk.jugador} +0.2 def 2t')
            atk.en -= 30
        elif hab_nombre == 'Raíces':
            d = dmg_base(130)
            tgt.cargas['inmovilizado'] = max(tgt.cargas['inmovilizado'],2)
            msgs.append(f'🌿 Raíces: -{int(d)} HP + inmoviliza 2t a {tgt.jugador}')
            atk.en -= 50
        elif hab_nombre == 'Conexión':
            msgs.append(f'🔗 Conexión: {atk.jugador} enlaza daño con {tgt.jugador} 2t')
            atk.en -= 60

    # ─── Santa Claus ──────────────────────────────
    elif p == 'Santa Claus':
        if hab_nombre == 'Bola de Nieve':
            if not check_preci(90): msgs.append(f'💨 {atk.jugador} falla Bola de Nieve!')
            else:
                d = dmg_base(40)
                tgt.cargas['hielo'] = max(tgt.cargas['hielo'],1)
                msgs.append(f'❄ Bola de Nieve: -{int(d)} HP + congela {tgt.jugador}')
            atk.en -= 15
        elif hab_nombre == 'Mierda de Reno':
            d = dmg_base(60)
            tgt.cargas['silenciado'] = max(tgt.cargas['silenciado'],2)
            msgs.append(f'🦌💩 Mierda de Reno: -{int(d)} HP + silencia 2t {tgt.jugador}')
            atk.en -= 30
        elif hab_nombre == 'Estrés Navideño':
            for lf in todos:
                if lf != atk and lf.vivo:
                    lf.pwr = max(0.1, lf.pwr - 0.6)
            msgs.append(f'😰 Estrés Navideño: -0.6 pwr a todos los enemigos 2t')
            atk.en -= 60

    # ─── Werewolf ──────────────────────────────
    elif p == 'Werewolf':
        if hab_nombre == 'Ensangrentar':
            d = dmg_base(45)
            tgt.cargas['sangrado'] += 1
            rob = d * 0.04
            atk.hp = min(atk.maxhp, atk.hp + rob)
            msgs.append(f'🐺 Ensangrentar: -{int(d)} HP + sangrado + {int(rob)} HP robado')
            atk.en -= 20
        elif hab_nombre == 'Morder':
            d = dmg_base(80)
            rob = d * 0.04
            atk.hp = min(atk.maxhp, atk.hp + rob)
            msgs.append(f'🐺 Morder: -{int(d)} HP + {int(rob)} HP robado a {tgt.jugador}')
            atk.en -= 35
        elif hab_nombre == 'Abalanzarse':
            d = dmg_base(120)
            tgt.cargas['hemorragia'] += 1
            msgs.append(f'🐺💀 Abalanzarse: -{int(d)} HP + hemorragia a {tgt.jugador}')
            atk.en -= 60

    # ─── Runeforge ──────────────────────────────
    elif p == 'Runeforge':
        if hab_nombre == 'Aplastar':
            d = dmg_base(90)
            msgs.append(f'🔨 Aplastar: -{int(d)} HP a {tgt.jugador}')
            atk.en -= 30
        elif hab_nombre == 'Runa':
            tgt.cargas['invencible'] = max(tgt.cargas['invencible'],1)
            msgs.append(f'[Runa] {tgt.jugador} es invulnerable 1t (la runa acumula vida cada turno)')
            atk.en -= 90
        elif hab_nombre == 'Forjar':
            tgt.pwr += 0.4; tgt.defn += 0.3
            msgs.append(f'[Forja] {tgt.jugador} +0.4 pwr, +0.3 def 2t')
            atk.en -= 30

    elif p == 'Serenità':
        if hab_nombre == 'Armonia':
            # >50% HP: cura 150·pwr + +0.05 pwr al objetivo
            # <50% HP: cura 250·pwr (emergencia)
            # =50% HP (caso raro): cura 350·pwr + +0.15 pwr
            pct_hp = tgt.hp / tgt.maxhp if tgt.maxhp > 0 else 1
            if pct_hp > 0.50:
                cantidad = 150 * atk.pwr * atk.rcura
                tgt.curar(cantidad)
                tgt.pwr += 0.05
                msgs.append(f'🎵 Armonia: {tgt.jugador} +{int(cantidad)} HP, +0.05 pwr')
            else:
                cantidad = 250 * atk.pwr * atk.rcura
                tgt.curar(cantidad)
                msgs.append(f'🎵 Armonia (emergencia): {tgt.jugador} +{int(cantidad)} HP')
            atk.en -= 15
        elif hab_nombre == 'Scelta':
            # La elección se hace automáticamente basada en la necesidad del objetivo:
            # si pwr < defn → sube pwr; si defn < pwr → sube defn; si igual → sube pwr
            if tgt.pwr <= tgt.defn:
                tgt.pwr += 0.15 * atk.pwr
                msgs.append(f'🌟 Scelta: {tgt.jugador} +{0.15*atk.pwr:.3f} pwr')
            else:
                tgt.defn += 0.15 * atk.pwr
                msgs.append(f'🌟 Scelta: {tgt.jugador} +{0.15*atk.pwr:.3f} def')
            atk.en -= 40
        elif hab_nombre == 'Luce':
            # Purifica todos los estados negativos del objetivo
            for k in ['veneno','sangrado','quemado','hemorragia','maldita',
                      'stun','hielo','silenciado','inmovilizado','paralizado']:
                tgt.cargas[k] = 0
            # Duplicar Costanza durante 4 turnos
            if not hasattr(atk, 'costanza'): atk.costanza = 30
            if not hasattr(atk, 'tcostanza'): atk.tcostanza = 0
            atk.costanza   = 60
            atk.tcostanza  = nturnos + 5   # expira en nturnos+5
            msgs.append(f'💫 Luce di Parma: {tgt.jugador} purificado, Costanza ×2 (4 turnos)')
            atk.en -= 60

    # Regenerar energía base
    atk.en = min(atk.maxen, atk.en + 4)

    if not msgs:
        msgs.append(f'{atk.jugador} usa {hab_nombre}')
    return msgs


# ──────────────────────────────────────────────────────────────────
#  BUILD: descripciones e implementación de habilidades de equipo
# ──────────────────────────────────────────────────────────────────
DESC_BUILD = {
    # CASCOS
    "Hábito de monje":      ("🧘 Paz",         0,  6,  "Regenera 120 de energía durante 3 turnos"),
    "Capucha de niebla":    ("🌫 Niebla",       20, 8,  "Silencia a TODOS (incluido tú) 3 turnos"),
    "Casco de truenos":     ("⚡ Tormenta",     36, 7,  "120 daño + stun 1t en área"),
    "Casco del sacrificio": ("💔 Sacrificio",   28, 4,  "Pierde 5% HP propio, cura 5% HP del objetivo"),
    "Casco meteórico":      ("☄ Meteorito",    55, 10, "200 daño + stun 2t al objetivo (90% prec)"),
    "Capucha de rebote":    ("🪞 Rebote",       60, 10, "Reflejas 75% del daño recibido 2 turnos"),
    "Hábito de infinidad":  ("♾ Infinito",     0,  9,  "No gastas energía durante 2 turnos"),
    "Hábito de hielo":      ("🧊 Hielo",        0,  8,  "Invulnerable 3t PERO te congelas 3 turnos"),
    "Capucha de reset":     ("🔄 Reset",        0,  12, "Resetea el cooldown de tu armadura"),
    # ARMADURAS
    "Armadura de fuerza":   ("🛡 Campo",        62, 11, "+0.4 def + escudo + +60% cura recibida 3t"),
    "Armadura de debilidad":("💀 Guardián",     48, 11, "-0.6 pwr a todos (aliados y enemigos) 3t"),
    "Armadura de demonio":  ("😈 Protec. Demonio",49,11,"Reflejo +30%, aliados +0.2def, tú -0.3def 3t"),
    "Chaqueta de combustión":("🔥 Autocomb.",   45, 11, "300 daño en área (sin def) 3t, -33% cura propia"),
    "Chaqueta de sangre":   ("🩸 Sed Sangre",   40, 11, "Robas 55% del daño directo como HP 2 turnos"),
    "Túnica de salvación":  ("🌟 Salvación",    42, 11, "Si recibes daño: invulnerable 2t + +35% pwr/cura"),
    # BOTAS
    "Botas de la venganza": ("⚔ Venganza",     0,  11, "+pwr según %HP: 100%→+0.1, 5%→+2.0"),
    "Botas del gigante":    ("🦶 Gigante",      0,  7,  "+50% vida máx y actual 2 turnos"),
    "Botas imparables":     ("🏃 Imparable",    0,  12, "Inmune a stun/hielo/inmov/parálisis/silencio 3t"),
    "Sandalias de putrefacción":("☠ Putref.",   0,  10, "Cuerpo a cuerpo: -0.3def -80% cura recibida 2t al enemigo"),
    "Sandalias de poder":   ("💪 Poder",        0,  8,  "+0.5 pwr / -0.5 def 3 turnos"),
    "Botas de escudo":      ("🛡 Carga Escudo", 0,  9,  "Escudo 400 HP 3t a ti y al objetivo"),
}

def ejecutar_build(item_nombre, item_tipo, atacante, objetivo, todos, nturnos):
    """Ejecuta la habilidad de un ítem de build. Devuelve lista de mensajes."""
    msgs = []
    atk = atacante
    tgt = objetivo
    n = item_nombre

    # ─── CASCOS ───
    if n == "Hábito de monje":
        atk.cargas['cura'] += 3   # 3 cargas × 28 = 84 por turno aprox (motor: 120/3t)
        msgs.append(f'🧘 Paz: {atk.jugador} regenera energía durante 3 turnos (+cargas cura)')
    elif n == "Capucha de niebla":
        for lf in todos:
            if lf.vivo:
                lf.cargas['silenciado'] = max(lf.cargas['silenciado'], 3)
        msgs.append(f'🌫 Niebla: TODOS silenciados 3 turnos (incluyendo {atk.jugador})')
        atk.en -= 20
    elif n == "Casco de truenos":
        for lf in todos:
            if lf != atk and lf.vivo:
                lf.hp -= 120
                lf.cargas['stun'] = max(lf.cargas['stun'], 1)
        msgs.append(f'⚡ Tormenta: 120 daño + stun 1t en área')
        atk.en -= 36
    elif n == "Casco del sacrificio":
        coste = atk.maxhp * 0.05
        ganado = tgt.maxhp * 0.05
        atk.hp -= coste
        tgt.hp = min(tgt.maxhp, tgt.hp + ganado)
        msgs.append(f'💔 Sacrificio: {atk.jugador} -{int(coste)} HP, {tgt.jugador} +{int(ganado)} HP')
        atk.en -= 28
    elif n == "Casco meteórico":
        from random import randint as _r
        if _r(0,100) <= 90:
            tgt.hp -= 200
            tgt.cargas['stun'] = max(tgt.cargas['stun'], 2)
            msgs.append(f'☄ Meteorito: -{200} HP + stun 2t a {tgt.jugador}')
        else:
            msgs.append(f'☄ Meteorito: FALLA!')
        atk.en -= 55
    elif n == "Capucha de rebote":
        atk.reflejar = 0.75
        msgs.append(f'🪞 Rebote: {atk.jugador} refleja 75% del daño recibido 2 turnos')
        atk.en -= 60
    elif n == "Hábito de infinidad":
        msgs.append(f'♾ Infinito: {atk.jugador} no gastará energía 2 turnos (pendiente impl.)')
    elif n == "Hábito de hielo":
        atk.cargas['invencible'] = max(atk.cargas['invencible'], 3)
        atk.cargas['hielo'] = max(atk.cargas['hielo'], 3)
        msgs.append(f'🧊 Hielo: {atk.jugador} invulnerable 3t PERO congelado 3t')
    elif n == "Capucha de reset":
        atk.cd_build = 0
        msgs.append(f'🔄 Reset: cooldown de armadura reseteado para {atk.jugador}')

    # ─── ARMADURAS ───
    elif n == "Armadura de fuerza":
        atk.defn += 0.4
        atk.rcura += 0.6
        msgs.append(f'🛡 Campo: {atk.jugador} +0.4 def, +60% cura recibida 3t')
        atk.en -= 62
    elif n == "Armadura de debilidad":
        for lf in todos:
            if lf.vivo:
                lf.pwr = max(0.1, lf.pwr - 0.6)
        msgs.append(f'💀 Guardián: -0.6 pwr a TODOS 3 turnos')
        atk.en -= 48
    elif n == "Armadura de demonio":
        for lf in todos:
            if lf != atk and lf.vivo:
                lf.reflejar += 0.30
                lf.defn += 0.2
        atk.defn = max(0.1, atk.defn - 0.3)
        msgs.append(f'😈 Protec. Demonio: aliados +reflejo +def, tú -0.3 def')
        atk.en -= 49
    elif n == "Chaqueta de combustión":
        for lf in todos:
            if lf != atk and lf.vivo:
                lf.cargas['quemado'] += 3
        atk.rcura -= 0.33
        msgs.append(f'🔥 Autocomb.: 3 quemaduras en área, {atk.jugador} -33% cura recibida')
        atk.en -= 45
    elif n == "Chaqueta de sangre":
        atk.robovida = 0.55
        msgs.append(f'🩸 Sed Sangre: {atk.jugador} roba 55% del daño directo 2 turnos')
        atk.en -= 40
    elif n == "Túnica de salvación":
        msgs.append(f'🌟 Salvación: {atk.jugador} si recibe daño → invulnerable 2t +35% pwr (pend.)')
        atk.en -= 42

    # ─── BOTAS ───
    elif n == "Botas de la venganza":
        pct = atk.hp / atk.maxhp if atk.maxhp > 0 else 1
        bonus = 2.0 if pct<=0.05 else 1.5 if pct<=0.20 else 1.0 if pct<=0.40 else 0.75 if pct<=0.60 else 0.4 if pct<=0.80 else 0.1
        atk.pwr += bonus
        msgs.append(f'⚔ Venganza: {atk.jugador} +{bonus} pwr (HP {int(pct*100)}%)')
    elif n == "Botas del gigante":
        extra = atk.maxhp * 0.50
        atk.maxhp += int(extra)
        atk.hp = min(atk.maxhp, atk.hp + int(extra))
        msgs.append(f'🦶 Gigante: {atk.jugador} +50% HP máx y actual 2 turnos')
    elif n == "Botas imparables":
        for k in ['stun','hielo','paralizado','silenciado','inmovilizado']:
            atk.cargas[k] = 0
        msgs.append(f'🏃 Imparable: {atk.jugador} inmune a estados negativos 3 turnos')
    elif n == "Sandalias de putrefacción":
        tgt.defn = max(0.1, tgt.defn - 0.3)
        tgt.rcura -= 0.80
        msgs.append(f'☠ Putref.: {tgt.jugador} -0.3 def, -80% cura recibida 2t')
    elif n == "Sandalias de poder":
        atk.pwr += 0.5
        atk.defn = max(0.1, atk.defn - 0.5)
        msgs.append(f'💪 Poder: {atk.jugador} +0.5 pwr, -0.5 def 3 turnos')
    elif n == "Botas de escudo":
        atk.hp = min(atk.maxhp, atk.hp + 400)
        tgt.hp = min(tgt.maxhp, tgt.hp + 400)
        msgs.append(f'🛡 Carga Escudo: {atk.jugador} y {tgt.jugador} +400 HP de escudo 3t')
    else:
        msgs.append(f'🎽 {item_nombre}: efecto aplicado')

    # Regenerar energía base
    atk.en = min(atk.maxen, atk.en + 4)
    return msgs
def sanitize(txt):
    """Elimina/sustituye emojis y caracteres no-ASCII por equivalentes legibles."""
    repl = {
        '💀':'[X]','🩸':'[sg]','☠':'[vn]','🔥':'[qm]','👻':'[ml]','💚':'[+]',
        '💊':'[+hp]','⚡':'[en]','🌿':'[nat]','⏭':'[>>]','💨':'[miss]',
        '⚔':'[atk]','🛡':'[def]','💢':'[!]','🔵':'[orb]','💪':'[pwr]',
        '🌪':'[torm]','🏹':'[arc]','👿':'[dem]','🗡':'[dag]','🐾':'[zrp]',
        '🔄':'[trn]','✨':'[*]','💥':'[boom]','🌋':'[volc]','👊':'[boca]',
        '😈':'[diab]','🌑':'[dark]','🔨':'[maz]','🌍':'[area]','🩹':'[vnd]',
        '🎵':'[arm]','🌟':'[luce]','🏆':'[win]','🎯':'[obj]','🎰':'[apos]',
        '🐍':'[serp]','🌱':'[root]','❤':'[hp]','🎒':'[moch]','🤪':'[loc]',
        '📖':'[aprn]','❄':'[ice]','🧊':'[ice2]','⭐':'[stun]','🔇':'[sl]',
        '⛓':'[inmov]','🧘':'[paz]','🌫':'[nieb]','💔':'[sacr]','☄':'[met]',
        '🪞':'[reb]','♾':'[inf]','🔋':'[conc]','⚙':'[gear]','→':'->',
        '←':'<-','▶':'>','►':'>','✓':'ok','✗':'x','–':'-','—':'-',
        '\u200d':'',  # zero-width joiner
    }
    out = ''
    for ch in txt:
        if ord(ch) < 128:
            out += ch
        else:
            out += repl.get(ch, repl.get(ch, ''))
    return out


class LogCombate:
    MAX_LINES = 120   # histórico total
    VISIBLE_H_MIN = 46   # altura mínima (1 línea + padding)
    VISIBLE_H_MAX = 200  # altura máxima expandida

    def __init__(self):
        self.lineas    = []
        self.expandido = False   # False = mini (90px), True = maxi (200px)

    def add(self, msg):
        if isinstance(msg, list):
            for m in msg: self.lineas.append(sanitize(str(m)))
        else:
            self.lineas.append(sanitize(str(msg)))
        self.lineas = self.lineas[-self.MAX_LINES:]

    def altura(self):
        return self.VISIBLE_H_MAX if self.expandido else 90

    def draw(self, surf, x, y, w, h):
        draw_rect_alpha(surf, PANEL_BG, (x, y, w, h), 215, 8)
        pygame.draw.rect(surf, PANEL_BD, (x, y, w, h), 1, border_radius=8)

        line_h  = 13
        padding = 5
        # Reservar 18px arriba para la barra de título + botón
        inner_y  = y + 18
        inner_h  = h - 18 - padding
        max_lines = max(1, inner_h // line_h)
        lineas   = self.lineas[-max_lines:]

        # Dibujar líneas de abajo hacia arriba
        fy = inner_y + inner_h - line_h
        for lin in reversed(lineas):
            r = F12.render(lin[:78], True, LGRAY)
            surf.blit(r, (x + padding, fy))
            fy -= line_h
            if fy < inner_y: break

        # ── Barra de título + botón +/- ────────────────────────────
        draw_rect_alpha(surf, (25, 30, 60), (x, y, w, 17), 230, 8)
        tit = F11.render('CONSOLA  /  LOG', True, BLUE)
        surf.blit(tit, (x + padding, y + 3))

        # Botón +/-
        btn_w, btn_h = 28, 15
        btn_x = x + w - btn_w - 4
        btn_y = y + 1
        lbl   = '[+]' if not self.expandido else '[-]'
        col   = TEAL if self.expandido else PANEL_BD
        draw_rect_alpha(surf, col, (btn_x, btn_y, btn_w, btn_h), 230, 4)
        pygame.draw.rect(surf, WHITE, (btn_x, btn_y, btn_w, btn_h), 1, border_radius=4)
        r = F11.render(lbl, True, WHITE)
        surf.blit(r, (btn_x + btn_w//2 - r.get_width()//2,
                      btn_y + btn_h//2 - r.get_height()//2))
        # Devolver rect del botón para el gestor
        return pygame.Rect(btn_x, btn_y, btn_w, btn_h)

    def toggle(self):
        self.expandido = not self.expandido


# ──────────────────────────────────────────────────────────────────
#  BOTÓN
# ──────────────────────────────────────────────────────────────────
class Btn:
    def __init__(self, label, x, y, w, h, color=PANEL_BD, disabled=False):
        self.label = label
        self.rect  = pygame.Rect(x, y, w, h)
        self.color = color
        self.disabled = disabled
        self.hover = False

    def update(self, mx, my):
        self.hover = self.rect.collidepoint(mx, my)

    def draw(self, surf):
        col = GRAY if self.disabled else (self.color if not self.hover else tuple(min(255,c+40) for c in self.color))
        pygame.draw.rect(surf, col, self.rect, border_radius=6)
        pygame.draw.rect(surf, WHITE if not self.disabled else LGRAY, self.rect, 1, border_radius=6)
        draw_text_center(surf, FB14, self.label, WHITE if not self.disabled else LGRAY,
                         self.rect.centerx, self.rect.centery)

    def clicked(self, pos):
        return not self.disabled and self.rect.collidepoint(pos)


# ──────────────────────────────────────────────────────────────────
#  TOOLTIP
# ──────────────────────────────────────────────────────────────────
class Tooltip:
    def __init__(self):
        self.texto = ''
        self.visible = False

    def show(self, texto):
        self.texto = texto
        self.visible = True

    def hide(self):
        self.visible = False

    def draw(self, surf, mx, my):
        if not self.visible or not self.texto: return
        lineas = self.texto.split('\n')
        wt = max(F12.size(l)[0] for l in lineas) + 16
        ht = len(lineas)*16 + 10
        tx = min(mx+10, surf.get_width()-wt-4)
        ty = max(my-ht-4, 4)
        draw_rect_alpha(surf, (20,20,40), (tx,ty,wt,ht), 230, 6)
        pygame.draw.rect(surf, PANEL_BD, (tx,ty,wt,ht), 1, border_radius=6)
        for i,l in enumerate(lineas):
            r = F12.render(l, True, WHITE)
            surf.blit(r, (tx+8, ty+5+i*16))


# ──────────────────────────────────────────────────────────────────
#  PANEL STATS
# ──────────────────────────────────────────────────────────────────
class PanelStats:
    def __init__(self):
        self.visible  = False
        self.luchador = None

    def toggle(self, lf):
        if self.visible and self.luchador == lf:
            self.visible = False
        else:
            self.visible = True
            self.luchador = lf

    def draw(self, surf):
        if not self.visible or not self.luchador: return
        lf = self.luchador

        # Calcular altura necesaria según la pasiva
        pasiva_txt = PASIVAS.get(lf.personaje, 'Sin pasiva especial.')
        pasiva_lines = []
        for raw_line in pasiva_txt.split('\n'):
            # Wrap a 34 chars por línea
            while len(raw_line) > 34:
                pasiva_lines.append(raw_line[:34])
                raw_line = raw_line[34:]
            pasiva_lines.append(raw_line)

        W = 300
        H = 260 + len(pasiva_lines) * 13 + 10
        x = (surf.get_width()  - W) // 2
        y = (surf.get_height() - H) // 2

        draw_rect_alpha(surf, (10,10,25), (x,y,W,H), 245, 10)
        pygame.draw.rect(surf, PANEL_BD, (x,y,W,H), 2, border_radius=10)

        _FB18 = pygame.font.SysFont('segoeui', 18, bold=True)
        _FB14 = pygame.font.SysFont('segoeui', 14, bold=True)
        _FB13 = pygame.font.SysFont('segoeui', 13, bold=True)
        _F13  = pygame.font.SysFont('segoeui', 13)
        _F12  = pygame.font.SysFont('segoeui', 12)
        _F11  = pygame.font.SysFont('segoeui', 11)

        fy = y + 10
        draw_text_center(surf, _FB18, f'STATS  –  {lf.personaje}', YELLOW, x+W//2, fy+8); fy += 26
        draw_text_center(surf, _FB14, f'Jugador: {lf.jugador}',    LGRAY,  x+W//2, fy+5); fy += 20

        def row(label, val, col=WHITE):
            nonlocal fy
            surf.blit(_FB13.render(f'{label}:', True, LGRAY), (x+12, fy))
            surf.blit(_F13.render(str(val),     True, col),   (x+130, fy))
            fy += 16

        row('HP',       f'{max(0,int(lf.hp))} / {lf.maxhp}', bar_color(lf.hp/lf.maxhp if lf.maxhp>0 else 0))
        row('Energía',  f'{int(lf.en)} / {lf.maxen}',         EN_C)
        row('Poder',    f'{lf.pwr:.3f}',                       YELLOW)
        row('Defensa',  f'{lf.defn:.3f}',                      BLUE)
        row('Velocidad',f'{lf.vel}',                            TEAL)
        row('Sangre',   f'{lf.sangre}',                         RED)

        fy += 4
        surf.blit(_FB13.render('Cargas:', True, LGRAY), (x+12, fy)); fy += 14
        cline = '  '.join(f'{k}:{v}' for k,v in lf.cargas.items() if v>0) or 'ninguna'
        for chunk in [cline[i:i+36] for i in range(0, len(cline), 36)]:
            surf.blit(_F12.render(chunk, True, ORANGE), (x+12, fy)); fy += 13

        fy += 6
        surf.blit(_FB13.render('Pasiva:', True, PASIVA_COL), (x+12, fy)); fy += 14
        for line in pasiva_lines:
            surf.blit(_F11.render(line, True, PASIVA_COL), (x+12, fy)); fy += 13

        # Botón cerrar
        close = pygame.Rect(x+W-24, y+4, 20, 20)
        pygame.draw.rect(surf, RED2, close, border_radius=4)
        draw_text_center(surf, _FB14, 'X', WHITE, close.centerx, close.centery)
        return close

    def handle_click(self, pos):
        if not self.visible: return False
        lf = self.luchador
        if not lf: return False
        pasiva_txt = PASIVAS.get(lf.personaje, '')
        n_lines = sum(max(1, (len(l)+33)//34) for l in pasiva_txt.split('\n'))
        W = 300; H = 260 + n_lines * 13 + 10
        x = (960 - W)//2; y = (540 - H)//2
        close = pygame.Rect(x+W-24, y+4, 20, 20)
        if close.collidepoint(pos):
            self.visible = False; return True
        if not pygame.Rect(x, y, W, H).collidepoint(pos):
            self.visible = False; return True
        return True


# ──────────────────────────────────────────────────────────────────
#  TARJETA DE LUCHADOR
# ──────────────────────────────────────────────────────────────────
CARD_W, CARD_H = 155, 218

def draw_card(surf, lf, x, y, activo, seleccionable, nturnos):
    """Dibuja la tarjeta de un luchador. Números HP/EN encima de la barra."""
    col_bd = YELLOW if activo else (TEAL if seleccionable else PANEL_BD)
    alpha  = 230 if activo else 190
    draw_rect_alpha(surf, PANEL_BG, (x,y,CARD_W,CARD_H), alpha, 8)

    # Parpadeo si seleccionable
    if seleccionable:
        t = pygame.time.get_ticks()
        if (t//400) % 2 == 0:
            draw_rect_alpha(surf, TEAL, (x,y,CARD_W,CARD_H), 55, 8)

    pygame.draw.rect(surf, col_bd, (x,y,CARD_W,CARD_H), 2, border_radius=8)

    # Flash rojo al recibir daño
    if lf.flash_timer > 0:
        draw_rect_alpha(surf, RED, (x,y,CARD_W,CARD_H), 90, 8)
        lf.flash_timer -= 1

    # Muerto: overlay gris
    if not lf.vivo:
        draw_rect_alpha(surf, (30,30,30), (x,y,CARD_W,CARD_H), 160, 8)
        # Muerto: texto con emoji si disponible
        render_emoji_line(surf, FB18, '☠ MUERTO', RED, x + CARD_W//2 - 42, y+CARD_H//2 - 9, 18)
        return pygame.Rect(x, y, CARD_W, CARD_H)

    sy = y + 5

    # Sprite o placeholder
    SPR = 90
    if lf.sprite:
        img = pygame.transform.smoothscale(lf.sprite, (SPR, SPR))
        surf.blit(img, (x+(CARD_W-SPR)//2, sy))
    else:
        draw_rect_alpha(surf, DGRAY, (x+(CARD_W-SPR)//2, sy, SPR, SPR), 200, 4)
        draw_text_center(surf, F11, lf.personaje[:13], LGRAY, x+CARD_W//2, sy+SPR//2)
    sy += SPR + 4

    # Jugador + personaje
    nom = lf.jugador if len(lf.jugador)<=11 else lf.jugador[:10]+'…'
    draw_text_center(surf, FB13, nom, YELLOW if activo else WHITE, x+CARD_W//2, sy); sy+=14
    draw_text_center(surf, F11, lf.personaje[:18], LGRAY, x+CARD_W//2, sy); sy+=12

    PAD = 7
    bw  = CARD_W - PAD*2

    # ── HP: número encima, barra debajo ──
    pct = max(0, lf.hp) / lf.maxhp if lf.maxhp > 0 else 0
    hp_str = f'HP  {max(0,int(lf.hp))} / {lf.maxhp}'
    r_hp = F11.render(hp_str, True, bar_color(pct))
    surf.blit(r_hp, (x+PAD, sy)); sy += 13
    draw_bar(surf, x+PAD, sy, bw, 8, max(0,lf.hp), lf.maxhp, bar_color(pct)); sy += 10

    # ── EN: número encima, barra debajo ──
    en_str = f'EN  {int(lf.en)} / {lf.maxen}'
    r_en = F11.render(en_str, True, EN_C)
    surf.blit(r_en, (x+PAD, sy)); sy += 13
    draw_bar(surf, x+PAD, sy, bw, 6, lf.en, lf.maxen, EN_C); sy += 9

    # ── Cargas activas con colores y emojis ──────────────────────────
    CARGA_DEFS = [
        ('sangrado',    '🩸', (220, 50,  80)),
        ('quemado',     '🔥', (240,140,  30)),
        ('veneno',      '☠',  ( 80,200,  60)),
        ('hemorragia',  '💀', (180, 20,  60)),
        ('maldita',     '💜', (160, 60, 220)),
        ('stun',        '⭐', (240,220,  50)),
        ('hielo',       '❄',  ( 80,200, 240)),
        ('silenciado',  '🔇', (160,160, 200)),
        ('inmovilizado','⛓',  (100,130, 200)),
        ('paralizado',  '⚡', (200,180,  60)),
        ('invencible',  '🛡', (200,200,  60)),
        ('cura',        '💚', ( 60,220, 120)),
    ]
    active = [(em, col, lf.cargas[k]) for k,em,col in CARGA_DEFS if lf.cargas.get(k,0) > 0]
    if active:
        cx2 = x + PAD
        for em, col, v in active:
            # Mini pastilla coloreada
            pw = 26
            draw_rect_alpha(surf, col, (cx2, sy, pw, 12), 160, 3)
            render_emoji_line(surf, F10, f'{em}{v}', WHITE, cx2+1, sy, 11)
            cx2 += pw + 2
            if cx2 > x + CARD_W - 8: break

    return pygame.Rect(x, y, CARD_W, CARD_H)


# ──────────────────────────────────────────────────────────────────
#  MENÚ DE HABILIDADES  (abajo a la derecha)
# ──────────────────────────────────────────────────────────────────
class MenuHabilidades:
    BTN_H   = 30
    BTN_W   = 210
    PAD     = 4
    # Posición: pegado a la esquina inferior derecha
    PANEL_X = 960 - 218   # 742
    PANEL_Y = 540 - 10    # se calcula dinámicamente
    TAB_H   = 26

    def __init__(self):
        self.luchador    = None
        self.habilidades = []
        self.btns        = []
        self.modo        = 'ataques'
        self.tab_btns    = []
        self._rebuild()

    def set_luchador(self, lf, nturnos):
        self.luchador = lf
        self._rebuild(nturnos)

    def _hab_list(self):
        if not self.luchador: return []
        habs = HABILIDADES.get(self.luchador.personaje, [])
        SOPORTE_NAMES = ('Venda','Curar','Cura','Pasto','Energía','Energiar','Saltar')
        if self.modo == 'ataques':
            lista = [h for h in habs if h.nombre not in SOPORTE_NAMES]
            return lista
        elif self.modo == 'soporte':
            sop = [h for h in habs if h.nombre in SOPORTE_NAMES]
            if not any(h.nombre == 'Saltar' for h in sop):
                sop.append(SALTAR)
            return sop
        elif self.modo == 'build':
            bs = []
            lf = self.luchador
            for item_nombre in [lf.casco, lf.armadura, lf.botas]:
                if item_nombre and item_nombre in DESC_BUILD:
                    label, costo, cd, desc = DESC_BUILD[item_nombre]
                    color = TEAL if lf.casco == item_nombre else (BLUE if lf.armadura == item_nombre else ORANGE)
                    h = H(f'{label}', costo, None, cd, 100, 'build', color, desc, 'build')
                    h._item_real = item_nombre
                    h._item_tipo = 'casco' if lf.casco == item_nombre else ('armadura' if lf.armadura == item_nombre else 'botas')
                    bs.append(h)
                elif item_nombre:
                    color = TEAL
                    h = H(f'{item_nombre[:20]}', 0, None, 0, 100, 'build', color, f'Item: {item_nombre}', 'build')
                    h._item_real = item_nombre
                    h._item_tipo = 'desconocido'
                    bs.append(h)
            return bs
        return []

    def _rebuild(self, nturnos=0):
        self.habilidades = self._hab_list()
        self.btns = []
        lf = self.luchador

        # El panel ocupa de abajo hacia arriba; su borde inferior = 538
        BOTTOM    = 538
        n_btns    = len(self.habilidades)
        panel_h   = n_btns * (self.BTN_H + self.PAD) + self.TAB_H + 12
        panel_top = BOTTOM - panel_h

        y = panel_top + self.TAB_H + 8
        for h in self.habilidades:
            cd = False; no_en = False
            if lf:
                if h.cd_slot is not None and lf.cooldowns[h.cd_slot] > nturnos:
                    cd = True
                if h.tipo == 'build' and hasattr(h, '_item_real'):
                    real_cd = lf.cd_build_dict.get(h._item_real, 0)
                    if real_cd > nturnos: cd = True
                if h.costo > 0 and lf.en < h.costo:
                    no_en = True
            disabled = cd or no_en
            btn = Btn(h.nombre[:26], self.PANEL_X, y, self.BTN_W, self.BTN_H, h.color, disabled)
            btn._cd = cd; btn._no_en = no_en; btn._hab = h
            self.btns.append(btn)
            y += self.BTN_H + self.PAD

        # Tabs encima del panel
        tx = self.PANEL_X
        ty = panel_top
        tw = self.BTN_W // 3
        self.tab_btns = [
            Btn('Ataques', tx,      ty, tw,   self.TAB_H, RED  if self.modo=='ataques' else DGRAY),
            Btn('Soporte', tx+tw,   ty, tw,   self.TAB_H, TEAL if self.modo=='soporte' else DGRAY),
            Btn('Build',   tx+tw*2, ty, tw,   self.TAB_H, BLUE if self.modo=='build'   else DGRAY),
        ]
        self._panel_top = panel_top
        self._panel_h   = panel_h

    def handle_event(self, event, nturnos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.tab_btns[0].clicked(event.pos):
                self.modo='ataques'; self._rebuild(nturnos); return None
            if self.tab_btns[1].clicked(event.pos):
                self.modo='soporte'; self._rebuild(nturnos); return None
            if self.tab_btns[2].clicked(event.pos):
                self.modo='build';   self._rebuild(nturnos); return None
            for btn in self.btns:
                if btn.clicked(event.pos):
                    return btn._hab
        return None

    def get_tooltip(self, mx, my):
        for btn in self.btns:
            if btn.rect.collidepoint(mx,my) and hasattr(btn,'_hab'):
                h = btn._hab
                txt = f'{h.nombre}\n{h.desc}'
                if h.costo > 0: txt += f'\nCosto: {h.costo} EN'
                if h.cd_slot is not None: txt += f'\nCooldown: {h.cd_dur} turnos'
                if hasattr(h,'_item_real') and h.tipo=='build':
                    info = DESC_BUILD.get(h._item_real)
                    if info: txt += f'\nCD build: {info[2]} turnos'
                if btn._cd:    txt += '\n[CD] EN COOLDOWN'
                if btn._no_en: txt += '\n[EN] SIN ENERGIA'
                return txt
        return ''

    def update(self, mx, my, nturnos):
        self._rebuild(nturnos)
        for btn in self.btns + self.tab_btns:
            btn.update(mx, my)

    def draw(self, surf):
        if not hasattr(self, '_panel_top'): return
        # Fondo panel
        draw_rect_alpha(surf, PANEL_BG,
                        (self.PANEL_X-4, self._panel_top-2, self.BTN_W+8, self._panel_h+4),
                        210, 8)
        pygame.draw.rect(surf, PANEL_BD,
                         (self.PANEL_X-4, self._panel_top-2, self.BTN_W+8, self._panel_h+4),
                         1, border_radius=8)
        for tb in self.tab_btns: tb.draw(surf)
        for btn in self.btns:
            btn.draw(surf)
            # Indicador CD/EN en esquina
            if btn._cd:
                r = F10.render('CD', True, ORANGE)
                surf.blit(r, (btn.rect.right-22, btn.rect.top+3))
            elif btn._no_en:
                r = F10.render('EN', True, RED)
                surf.blit(r, (btn.rect.right-18, btn.rect.top+3))


# ──────────────────────────────────────────────────────────────────
#  GESTOR DE COMBATE PRINCIPAL
# ──────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────
#  PANEL DE HABILIDADES (info de los ataques del personaje activo)
# ──────────────────────────────────────────────────────────────────
class PanelHabilidades:
    def __init__(self):
        self.visible   = False
        self.luchador  = None

    def toggle(self, lf):
        if self.luchador == lf:
            self.visible = not self.visible
        else:
            self.luchador = lf
            self.visible  = True

    def draw(self, surf):
        if not self.visible or not self.luchador:
            return
        lf   = self.luchador
        habs = HABILIDADES.get(lf.personaje, [])
        pasiva = PASIVAS.get(lf.personaje, '')

        # Calcular altura necesaria
        PAD = 10
        _fB = pygame.font.SysFont('segoeui', 14, bold=True)
        _fN = pygame.font.SysFont('segoeui', 13)
        _fS = pygame.font.SysFont('segoeui', 11)
        line_h = 15
        # Cada habilidad: nombre (1 línea) + desc wrapeada (~2 líneas) + separador
        n_hab_lines = sum(2 + max(1, (len(h.desc)+48)//48) for h in habs)
        pasiva_lines = []
        for raw in pasiva.split('\n'):
            while len(raw) > 44:
                pasiva_lines.append(raw[:44]); raw = raw[44:]
            pasiva_lines.append(raw)
        total_h = PAD*2 + 24 + n_hab_lines*line_h + 8 + len(pasiva_lines)*13 + 20
        W = 310
        H = min(500, max(200, total_h))
        x = (surf.get_width()  - W) // 2
        y = (surf.get_height() - H) // 2

        draw_rect_alpha(surf, (8, 10, 28), (x, y, W, H), 248, 10)
        pygame.draw.rect(surf, (80, 60, 180), (x, y, W, H), 2, border_radius=10)

        fy = y + PAD
        # Título
        render_emoji_line(surf, _fB, f'Habilidades  —  {lf.personaje}', YELLOW, x+PAD, fy, 14)
        fy += 22

        # Cada habilidad
        for h in habs:
            # Nombre + costo + cd
            meta = ''
            if h.costo > 0: meta += f' | {h.costo} EN'
            if h.cd_slot is not None: meta += f' | CD {h.cd_dur}t'
            if h.preci < 100: meta += f' | {h.preci}% prec'
            render_emoji_line(surf, _fB, h.nombre, h.color, x+PAD, fy, 13)
            fy += 14
            # meta
            surf.blit(_fS.render(meta.strip(' |'), True, LGRAY), (x+PAD+4, fy)); fy += 13
            # desc wrapeada
            desc = h.desc
            while len(desc) > 48:
                surf.blit(_fS.render(desc[:48], True, (190,190,220)), (x+PAD+4, fy))
                desc = desc[48:]; fy += 13
            surf.blit(_fS.render(desc, True, (190,190,220)), (x+PAD+4, fy)); fy += 14
            if fy > y + H - 30: break

        # Pasiva
        fy += 4
        if fy < y + H - 20:
            pygame.draw.line(surf, (60,60,100), (x+PAD, fy), (x+W-PAD, fy)); fy += 6
            render_emoji_line(surf, _fB, 'Pasiva:', PASIVA_COL, x+PAD, fy, 13); fy += 16
            for pl in pasiva_lines:
                if fy > y+H-14: break
                surf.blit(_fS.render(pl, True, PASIVA_COL), (x+PAD, fy)); fy += 13

        # Botón cerrar
        close = pygame.Rect(x+W-22, y+4, 18, 18)
        pygame.draw.rect(surf, RED2, close, border_radius=4)
        draw_text_center(surf, FB14, 'X', WHITE, close.centerx, close.centery)

    def handle_click(self, pos):
        if not self.visible or not self.luchador: return False
        habs = HABILIDADES.get(self.luchador.personaje, [])
        pasiva = PASIVAS.get(self.luchador.personaje, '')
        n_hab_lines = sum(2 + max(1,(len(h.desc)+48)//48) for h in habs)
        pasiva_lines_n = len(pasiva.split('\n'))
        total_h = 20+2 + 24 + n_hab_lines*15 + 8 + pasiva_lines_n*13 + 20
        W = 310; H = min(500, max(200, total_h))
        x = (960-W)//2; y = (540-H)//2
        close = pygame.Rect(x+W-22, y+4, 18, 18)
        if close.collidepoint(pos):
            self.visible = False; return True
        if not pygame.Rect(x, y, W, H).collidepoint(pos):
            self.visible = False; return True
        return True

class GestorCombate:
    def __init__(self, screen, jugadores_data, fondo=None):
        self.screen   = screen
        self.fondo    = fondo
        self.W, self.H = screen.get_size()

        # Crear luchadores
        self.luchadores = []
        for i, d in enumerate(jugadores_data):
            lf = Luchador(
                d.get('jugador','J'+str(i+1)),
                d.get('personaje','Warrior'),
                d.get('casco',''),
                d.get('armadura',''),
                d.get('botas',''),
                i
            )
            self.luchadores.append(lf)

        self.nturnos   = 0
        self.turno_idx = 0  # índice en self.luchadores del jugador activo
        self.fase      = 'menu'   # 'menu' | 'objetivo' | 'fin' | 'cargas'
        self.ganador   = None

        self.hab_pendiente = None   # Habilidad seleccionada esperando objetivo
        self.necesita_objetivo = True

        self.menu_hab  = MenuHabilidades()
        self.log       = LogCombate()
        self.tooltip   = Tooltip()
        self.panel_stats = PanelStats()

        # Botones globales: abajo izquierda
        self.btn_stats  = Btn('Stats',  8,   505, 58, 26, PANEL_BD)
        self.btn_volver = Btn('<- Menu', 72,  505, 64, 26, GRAY)
        self.btn_info   = Btn('? Habs', 142, 505, 62, 26, (60,40,120))

        # ── Panel info de habilidades ──
        self.panel_habs = PanelHabilidades()

        # ── Escenario aleatorio ──
        self.escenario_id  = _random.randint(1, 11)
        _esc = ESCENARIOS.get(self.escenario_id, ESCENARIOS[1])
        self.escenario_nombre = _esc[0]
        self.escenario_png    = _esc[1]
        self.escenario_desc   = _esc[2]
        # Cargar PNG del escenario (si existe), si no usar fondo pasado
        _png_path = self.escenario_png
        if os.path.exists(_png_path):
            try:
                _img = pygame.image.load(_png_path).convert()
                self.fondo = pygame.transform.smoothscale(_img, (self.W, self.H))
            except Exception:
                pass  # usar fondo original
        # Aplicar efectos del escenario
        aplicar_escenario(self.escenario_id, self.luchadores, self.log)

        self._iniciar_turno()

    @property
    def activo(self):
        return self.luchadores[self.turno_idx]

    def _vivos(self):
        return [lf for lf in self.luchadores if lf.vivo]

    def _iniciar_turno(self):
        lf = self.activo
        # Aplicar cargas de daño/cura
        msgs = lf.aplicar_cargas_inicio_turno(self.log)
        if msgs:
            self.log.add(msgs)

        # Verificar si muere por cargas
        if not lf.vivo:
            self.log.add(f'[X] {lf.jugador} ha caido!')
            self._check_fin()
            if self.fase != 'fin':
                self._avanzar_turno()
            return

        # Aplicar pasiva
        lf.pasiva_inicio_turno(self.nturnos)

        # ── Pasiva Serenità: Costanza ──────────────────────────────────
        # Cada vez que es el turno de Serenità, cura a todos sus aliados
        if lf.personaje == 'Serenità' and lf.vivo:
            if not hasattr(lf, 'costanza'): lf.costanza = 30
            if not hasattr(lf, 'tcostanza'): lf.tcostanza = 0
            # Si tcostanza expiró, volver a costanza base
            if lf.tcostanza > 0 and self.nturnos >= lf.tcostanza:
                lf.costanza = 30
                lf.tcostanza = 0
            aliados = [a for a in self.luchadores if a != lf and a.vivo]
            if aliados:
                for aliado in aliados:
                    aliado.hp = min(aliado.maxhp, aliado.hp + lf.costanza)
                self.log.add(f'Costanza: {lf.jugador} cura {int(lf.costanza)} HP a sus aliados')

        # Decrementar efectos temporales
        lf.decrementar_efectos_temporales(self.nturnos, self.log)

        # Verificar si puede actuar
        puede, razon = lf.puede_actuar()
        if not puede:
            self.log.add(f'[!] {razon}')
            lf.en = min(lf.maxen, lf.en + 4)
            self._avanzar_turno()
            return

        # Actualizar menú
        self.menu_hab.set_luchador(lf, self.nturnos)
        self.fase = 'menu'
        self.log.add(f'── Turno de {lf.jugador} ({lf.personaje}) ──')

    def _avanzar_turno(self):
        vivos = self._vivos()
        if len(vivos) <= 1:
            self._check_fin()
            return
        # Siguiente jugador vivo
        n = len(self.luchadores)
        for _ in range(n):
            self.turno_idx = (self.turno_idx + 1) % n
            if self.luchadores[self.turno_idx].vivo:
                break
        # Cuando el turno completo da la vuelta al primero, incrementar nturnos
        if self.turno_idx == 0:
            self.nturnos += 1
        self._iniciar_turno()

    def _check_fin(self):
        vivos = self._vivos()
        if len(vivos) <= 1:
            self.fase = 'fin'
            self.ganador = vivos[0] if vivos else None

    def _ejecutar_hab(self, hab, objetivo):
        atk = self.activo

        # ── Habilidades de Build ──
        if hab.tipo == 'build' and hasattr(hab, '_item_real'):
            item_real = hab._item_real
            # Verificar cooldown de build
            cd_disponible = atk.cd_build_dict.get(item_real, 0)
            if cd_disponible > self.nturnos:
                self.log.add(f'⏳ {item_real} en cooldown ({cd_disponible - self.nturnos} turnos)')
                return
            # Verificar energía
            if hab.costo > 0 and atk.en < hab.costo:
                self.log.add(f'⚡ {atk.jugador} sin energía para {item_real}')
                return
            # Ejecutar
            msgs = ejecutar_build(item_real, hab._item_tipo, atk, objetivo, self.luchadores, self.nturnos)
            self.log.add(msgs)
            # Aplicar cooldown del item
            info = DESC_BUILD.get(item_real)
            if info:
                cd_dur = info[2]
                atk.cd_build_dict[item_real] = self.nturnos + cd_dur
            # Coste energía
            if hab.costo > 0:
                atk.en = max(0, atk.en - hab.costo)
            self._check_fin()
            if self.fase != 'fin':
                self._avanzar_turno()
            return

        # ── Habilidades normales ──
        # Verificar energía
        if hab.costo > 0 and atk.en < hab.costo:
            self.log.add(f'⚡ {atk.jugador} sin energía para {hab.nombre}')
            return

        # Verificar cooldown
        if hab.cd_slot is not None and atk.cooldowns[hab.cd_slot] > self.nturnos:
            self.log.add(f'⏳ {hab.nombre} en cooldown')
            return

        # Ejecutar
        msgs = ejecutar_habilidad(hab.nombre, atk, objetivo, self.luchadores, self.nturnos, self.log)
        self.log.add(msgs)

        # Aplicar cooldown
        if hab.cd_slot is not None and hab.cd_dur > 0:
            atk.cooldowns[hab.cd_slot] = self.nturnos + hab.cd_dur

        self._check_fin()
        if self.fase != 'fin':
            self._avanzar_turno()

    def handle_event(self, event):
        if self.fase == 'fin':
            return

        mx, my = pygame.mouse.get_pos()

        # Panel stats absorbe clicks
        if self.panel_stats.visible:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.panel_stats.handle_click(event.pos)
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and self.fase == 'objetivo':
                self.fase = 'menu'
                self.hab_pendiente = None
                self.log.add('Selección cancelada')

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Panel habs absorbe clicks si visible
            if self.panel_habs.visible:
                self.panel_habs.handle_click(event.pos)
                return
            # Botón +/- del log (consola)
            log_btn = getattr(self, '_log_btn_rect', None)
            if log_btn and log_btn.collidepoint(event.pos):
                self.log.toggle()
                return
            # Botón Stats
            if self.btn_stats.clicked(event.pos):
                self.panel_stats.toggle(self.activo)
                return
            # Botón Info habilidades
            if self.btn_info.clicked(event.pos):
                self.panel_habs.toggle(self.activo)
                return
            # Botón Volver
            if self.btn_volver.clicked(event.pos):
                import sys as _sys
                # Cambiar pantalla sin importar visual_text_legends (evita import circular)
                # Buscamos el game_state en el módulo ya cargado
                vtl = _sys.modules.get('visual_text_legends') or _sys.modules.get('__main__')
                if vtl and hasattr(vtl, 'game_state'):
                    vtl.game_state['screen'] = 'resumen'
                return

            if self.fase == 'menu':
                hab = self.menu_hab.handle_event(event, self.nturnos)
                if hab:
                    # Determinar si necesita objetivo
                    if hab.nombre in ('Saltar','Energía','Pasto','Venda','Calma','Moneda',
                                      'Fuerza','Ira','Furia','Transformación','Bomba','Apostar','Invocar'):
                        # Se auto-aplica
                        self._ejecutar_hab(hab, self.activo)
                    elif hab.tipo in ('soporte','buff') and len(self._vivos()) == 1:
                        self._ejecutar_hab(hab, self.activo)
                    else:
                        self.hab_pendiente = hab
                        self.fase = 'objetivo'
                        self.necesita_objetivo = True
                        self.log.add(f'Selecciona objetivo para {hab.nombre} (ESC=cancelar)')

            elif self.fase == 'objetivo':
                for i, lf in enumerate(self.luchadores):
                    if not lf.vivo: continue
                    cx, cy = self._card_pos(i)
                    rect = pygame.Rect(cx, cy, CARD_W, CARD_H)
                    if rect.collidepoint(event.pos):
                        self._ejecutar_hab(self.hab_pendiente, lf)
                        self.hab_pendiente = None
                        self.fase = 'menu' if self.fase != 'fin' else 'fin'
                        break

    def _card_pos(self, idx, area_w=736, area_y=38, area_h=380):
        """
        Posición X,Y de la tarjeta del luchador idx.
        • Pantalla completa horizontal (area_w ≈ 736px, dejando menú en 742+).
        • Vertical: centradas en el área disponible entre cabecera y botones.
        • 2 jugadores: equipo izquierda ↔ equipo derecha.
        • 3+ jugadores: índices pares = equipo A (izq), impares = equipo B (der).
        """
        n   = len(self.luchadores)
        GAP = 12
        # Centrar verticalmente las tarjetas en el área disponible
        cy  = area_y + max(0, (area_h - CARD_H)) // 2

        if n == 1:
            return (area_w - CARD_W) // 2, cy

        if n == 2:
            # J1 pegado izquierda, J2 pegado derecha
            margen = 14
            positions = [margen, area_w - CARD_W - margen]
            return positions[idx], cy

        # 3+ jugadores: par=equipo A (izquierda), impar=equipo B (derecha)
        equipo_a = [i for i in range(n) if i % 2 == 0]
        equipo_b = [i for i in range(n) if i % 2 == 1]
        HALF     = area_w // 2
        MARGEN   = 10

        if idx % 2 == 0:                          # Equipo A — izquierda
            pos = equipo_a.index(idx)
            total = len(equipo_a)
            bloque_w = total * CARD_W + (total - 1) * GAP
            sx = MARGEN + max(0, (HALF - MARGEN*2 - bloque_w) // 2)
            return sx + pos * (CARD_W + GAP), cy
        else:                                      # Equipo B — derecha
            pos = equipo_b.index(idx)
            total = len(equipo_b)
            bloque_w = total * CARD_W + (total - 1) * GAP
            sx = HALF + MARGEN + max(0, (HALF - MARGEN*2 - bloque_w) // 2)
            return sx + pos * (CARD_W + GAP), cy

    def update(self):
        mx, my = pygame.mouse.get_pos()
        self.menu_hab.update(mx, my, self.nturnos)
        self.btn_stats.update(mx, my)
        self.btn_volver.update(mx, my)
        self.btn_info.update(mx, my)
        txt = self.menu_hab.get_tooltip(mx, my)
        if txt:
            self.tooltip.show(txt)
        else:
            self.tooltip.hide()

    def draw(self):
        surf = self.screen
        W, H = self.W, self.H   # 960 × 540

        # ── Constantes de layout ──────────────────────────────────────
        HEAD_H   = 34
        LOG_H    = self.log.altura()      # dinámico: 90 o 200
        LOG_Y    = H - LOG_H - 2
        BTNS_Y   = LOG_Y - 30
        CARDS_Y  = HEAD_H + 4
        CARDS_H  = BTNS_Y - CARDS_Y - 6
        MENU_X   = 742
        CARDS_W  = MENU_X - 6

        # Reposicionar botones en tiempo real
        self.btn_stats.rect.x  = 8
        self.btn_stats.rect.y  = BTNS_Y
        self.btn_volver.rect.x = 72
        self.btn_volver.rect.y = BTNS_Y
        self.btn_info.rect.x   = 142
        self.btn_info.rect.y   = BTNS_Y

        # ── Fondo ────────────────────────────────────────────────────
        if self.fondo:
            surf.blit(self.fondo, (0, 0))
        else:
            surf.fill(BG_DARK)
        draw_rect_alpha(surf, (0,0,0), (0,0,W,H), 50, 0)

        # ── Cabecera ─────────────────────────────────────────────────
        draw_rect_alpha(surf, PANEL_BG, (0,0,W,HEAD_H), 220, 0)
        # Nombre escenario izquierda
        esc_col = TEAL
        surf.blit(F12.render(f'[ {self.escenario_nombre} ]', True, esc_col), (8, 10))
        # Título centro
        draw_text_center(surf, FB16, 'TEXT LEGENDS', WHITE, W//2, HEAD_H//2)
        # Ronda + turno activo derecha
        surf.blit(F12.render(f'Ronda {self.nturnos+1}', True, YELLOW), (MENU_X - 85, 4))
        if self.activo and self.fase in ('menu','objetivo'):
            ra = F12.render(f'> {self.activo.jugador} ({self.activo.personaje})', True, TEAL)
            surf.blit(ra, (MENU_X - ra.get_width() - 4, 20))
        # Banner escenario debajo de cabecera (solo primeros 3 turnos)
        if self.nturnos < 3:
            bdesc = self.escenario_desc
            rd = F11.render(bdesc, True, (180,220,255))
            bw = rd.get_width() + 16
            draw_rect_alpha(surf, (0,20,50), (W//2-bw//2, HEAD_H, bw, 16), 200, 4)
            surf.blit(rd, (W//2 - rd.get_width()//2, HEAD_H+1))

        # ── Línea divisoria de equipos (≥3 jugadores) ────────────────
        if len(self.luchadores) >= 3:
            div_x = CARDS_W // 2
            pygame.draw.line(surf, (70,70,110),
                             (div_x, HEAD_H+2), (div_x, BTNS_Y-4), 1)
            draw_text_center(surf, F11, 'EQUIPO  A', (110,110,180),
                             div_x // 2, HEAD_H + 8)
            draw_text_center(surf, F11, 'EQUIPO  B', (110,110,180),
                             div_x + div_x // 2, HEAD_H + 8)

        # ── Tarjetas ─────────────────────────────────────────────────
        for i, lf in enumerate(self.luchadores):
            cx, cy = self._card_pos(i, CARDS_W, CARDS_Y, CARDS_H)
            activo       = (lf == self.activo and self.fase in ('menu','objetivo'))
            seleccionable = (self.fase == 'objetivo' and lf.vivo)
            draw_card(surf, lf, cx, cy, activo, seleccionable, self.nturnos)

        # ── Indicador "elige objetivo" ────────────────────────────────
        if self.fase == 'objetivo':
            hab_n = self.hab_pendiente.nombre if self.hab_pendiente else ''
            msg   = f'>> Elige objetivo para "{hab_n}"   (ESC = cancelar)'
            r = FB14.render(msg, True, YELLOW)
            bw = r.get_width() + 20
            draw_rect_alpha(surf, (20,18,0), (CARDS_W//2 - bw//2, BTNS_Y - 26, bw, 22), 210, 6)
            surf.blit(r, (CARDS_W//2 - r.get_width()//2, BTNS_Y - 25))

        # ── Botones Stats / Volver / Info ────────────────────────────
        self.btn_stats.draw(surf)
        self.btn_volver.draw(surf)
        self.btn_info.draw(surf)

        # ── Log al fondo ──────────────────────────────────────────────
        self._log_btn_rect = self.log.draw(surf, 4, LOG_Y, CARDS_W - 2, LOG_H)

        # ── Menú habilidades (derecha) ────────────────────────────────
        self.menu_hab.draw(surf)

        # ── Tooltip ──────────────────────────────────────────────────
        mx2, my2 = pygame.mouse.get_pos()
        self.tooltip.draw(surf, mx2, my2)

        # ── Panel Stats overlay ───────────────────────────────────────
        self.panel_stats.draw(surf)

        # ── Panel Habilidades overlay ─────────────────────────────────
        self.panel_habs.draw(surf)

        # ── Pantalla FIN ──────────────────────────────────────────────
        if self.fase == 'fin':
            self._draw_fin(surf)

    def _draw_fin(self, surf):
        draw_rect_alpha(surf, (0,0,0), (0,0,self.W,self.H), 160, 0)
        W,H = 400,200
        x=(self.W-W)//2; y=(self.H-H)//2
        draw_rect_alpha(surf, PANEL_BG, (x,y,W,H), 240, 12)
        pygame.draw.rect(surf, YELLOW, (x,y,W,H), 2, border_radius=12)
        draw_text_center(surf, FB24, '! FIN DEL COMBATE !', YELLOW, self.W//2, y+40)
        if self.ganador:
            draw_text_center(surf, FB20, f'[WIN]  {self.ganador.jugador}  gana!', WHITE, self.W//2, y+80)
            draw_text_center(surf, F16, f'({self.ganador.personaje})', LGRAY, self.W//2, y+104)
        else:
            draw_text_center(surf, FB20, '!! EMPATE !!', WHITE, self.W//2, y+80)
        draw_text_center(surf, F14, 'Cierra la ventana o vuelve al menú', LGRAY, self.W//2, y+140)
        self.btn_volver.draw(surf)
