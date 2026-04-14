from random import *
#flash ideas
#personaje medico de la plaga
#arreglar def eleminar_cargas
#hacer que def purificar tmb quite los efectos por tiempo malos

personajesgrupal = 'Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge'

def printdatos (me, enemy):
    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,', tiene', enemy.cargas['hemorragia'], 'hemorragias,', enemy.cargas['sangrado'], 'sangrados,', enemy.cargas['quemado'], 'quemaduras,', enemy.cargas['cura'], 'cargas de cura,', enemy.cargas['veneno'], 'cargas de veneno', enemy.cargas['maldita'], 'cargas malditas y está', enemy.cargas['hielo'] + enemy.cargas['stun'] + enemy.cargas['paralizado'], 'turnos congelados/stuneados/paralizados')
    print ('Tienes', me.health, 'puntos de vida, tu poder es de', me.power, ', tu defensa es de', me.defense,'y tu velocidad de', me.velocity, ', te quedan', me.energy, 'puntos de energía, tienes', me.cargas['hemorragia'], 'hemorragias,', me.cargas['sangrado'], 'sangrados,', me.cargas['quemado'], 'quemaduras,', me.cargas['cura'],'cargas de cura,', me.cargas['veneno'], 'cargas de veneno y', me.cargas['maldita'], 'cargas malditas y estás', me.cargas['hielo'] + me.cargas['stun'] + me.cargas['paralizado'], 'turnos congelados/stuneados/paralizados', '\n')

def printdatosIT (me, enemy):
    print ('A', enemy.name, 'restano', enemy.health, 'punti vita,', enemy.energy, 'punti energia, il suo potere è', enemy.power, ', la sua difesa è', enemy.defense,'e la sua velocità è', enemy.velocity, ', ha', enemy.cargas['hemorragia'], 'emorragie,', enemy.cargas['sangrado'], 'sanguinamenti,', enemy.cargas['quemado'], 'ustioni,', enemy.cargas['cura'], 'cariche di guarigione,', enemy.cargas['veneno'], 'cariche di veleno,', enemy.cargas['maldita'], 'cariche maledette ed è per', enemy.cargas['hielo'] + enemy.cargas['stun'] + enemy.cargas['paralizado'], 'turni congelato/stordito/paralizzato')
    print ('Hai', me.health, 'punti vita, il tuo potere è', me.power, ', la tua difesa è', me.defense,'e la tua velocità è', me.velocity, ', ti restano', me.energy, 'punti energia, hai', me.cargas['hemorragia'], 'emorragie,', me.cargas['sangrado'], 'sanguinamenti,', me.cargas['quemado'], 'ustioni,', me.cargas['cura'],'cariche di guarigione,', me.cargas['veneno'], 'cariche di veleno e', me.cargas['maldita'], 'cariche maledette e sei per', me.cargas['hielo'] + me.cargas['stun'] + me.cargas['paralizado'], 'turni congelato/stordito/paralizzato', '\n')

def printdatosshapeshifter (me, enemy):
    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,', tiene', enemy.cargas['hemorragia'], 'hemorragias,', enemy.cargas['sangrado'], 'sangrados,', enemy.cargas['quemado'], 'quemaduras,', enemy.cargas['cura'], 'cargas de cura,', enemy.cargas['veneno'], 'cargas de veneno', enemy.cargas['maldita'], 'cargas malditas y está', enemy.cargas['hielo'] + enemy.cargas['stun'] + enemy.cargas['paralizado'], 'turnos congelados/stuneados/paralizados')
    print ('Tienes', me.health, 'puntos de vida, tu poder es de', me.power, ', tu defensa es de', me.defense,'y tu velocidad de', me.velocity, ', te quedan', me.energy, 'puntos de energía, tienes', me.cargas['hemorragia'], 'hemorragias,', me.cargas['sangrado'], 'sangrados,', me.cargas['quemado'], 'quemaduras,', me.cargas['cura'],'cargas de cura,', me.cargas['veneno'], 'cargas de veneno y', me.cargas['maldita'], 'cargas malditas y estás', me.cargas['hielo'] + me.cargas['stun'] + me.cargas['paralizado'], 'turnos congelados/stuneados/paralizados tienes', me.carga_cambiaforma, 'cargas de cambiaformas', me.carga_pantera, 'cargas de pantera y', me.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')

def infocascos():
    print ('A - Hábito de monje: "Paz" Regenera 120 de energia durante 3 turnos, tiene un cooldown de 6 turnos')
    print ('B - Capucha de tinieblas: "Niebla" Silencia a todos los personajes (incluyendote) durante 3 turnos, tiene un cooldown de 8 turnos y gasta 20 de energia')
    print ('C - Casco de truenos: "Tormenta" Lanza rayos en todas direcciones infligiendo 120 de daño y aturdiendo 1 turno, tiene un cooldown de 7 turnos y gasta 36 de energia')
    print ('D - Casco del sacrificio: "Sacrificio" Pierde un 5% de tu vida máxima para regenerar un 5% de la vida máxima de tu objetivo, tiene 4 turnos de cooldown y gasta 28 de energia')
    print ('E - Casco meteorico, "Meteorito" Lanza un meteorito a tu oponente que le inflige 200 de daño y lo aturde 2 turnos, tiene 10 turnos de cooldown, gasta 55 de energia y tiene un 90% de precisión')
    print ('F - Capucha de rebote, "Rebote" Durante los próximos 2 turnos reflefas un 75% del daño recibido, tiene 10 turnos de cooldown y gasta 60 de energia')
    print ('G - Hábito de infinidad, "Infinito" Durante los próximos 2 turnos no gastarás energia, tiene 9 turnos de cooldown')
    print ('H - Hábito de hielo, "Hielo" Te vuelves invulnerable al daño por 3 turnos pero te congelas 3 turnos, tiene 8 turnos de cooldown')
    print ('I - Capucha de reset, "Reset" Resetea el cooldown de la armadura, tiene 12 turnos de cooldown')

def infoarmaduras():
    print ('A - Armadura de fuerza: "campo de fuerza" Crea un escudo que dura 3 turnos, aumenta la defensa en 0.4 y aumenta la cura recibida un 60% más , tiene un cooldown de 11 turnos y gasta 62 de energia')
    print ('B - Armadura de debilidad: "guardian" Crea un aura de debilidad que dura 3 turnos, te afecta a tí y a tus enemigos que disminuye el poder en 0.6 , tiene un cooldown de 11 turnos y gasta 48 de energia')
    print ('C - Armadura de demonio: "proteccion del demonio" Aumenta la cantidad de daño que reflejais tú y tus aliados en un 30% durante 3 turnos, además aumenta la defensa de tus aliados en un 0.2 y disminuye la tuya un 0.3, tiene un cooldown de 11 turnos y cuesta 49 de energia')
    print ('D - Chaqueta de combustión: "autocombistion" inflige 300 de daño (no afecta la defensa) durante 3 turnos a hasta 3 enemigos y a ti mismo además durante este tiempo te reduce la cura recibida un 33%, tiene un cooldown de 11 turnos y cuesta 45 de energia')
    print ('E - Chaqueta de sangre: "sed de sangre" Durante los 2 proximos turnos robarás 55% de vida de todo el daño directo que hagas, tiene un cooldown de 11 turnos y cuesta 40 de energia')
    print ('F - Túnica de salvación: "salvacion" Si recibes daño por el siguiente turno serás invulnerable 2 turnos y aumentarás tu poder y lanzamiento de curacion en 35% por 2 turnos, tiene un cooldown de 11 turnos y cuesta 42 de energia')

def infobotas():
    print ('A - Botas de la venganza: "venganza" Según cuanto porciento de vida te quede aumentas tu poder 0.1/0.4/0.75/1/1.5/2 100%/80%/60%/40%/20%/5%, tiene un cooldown de 11 turnos')
    print ('B - Botas del gigante: "gigante" Aumenta tu vida máxima y tu vida actual en un 50% durante 2 turnos, tiene un cooldown de 7 turnos')
    print ('C - Botas imparables: "imparable" Durante los próximos 3 turnos no puedes ser aturdido, congelado, inmovilizado, paralizado, silenciado, ni dormido, tiene un cooldown de 12 turnos')
    print ('D - Sandalias de putrefacción: "suelo podrido" Durante los próximos 2 turnos al atacar cuerpo a cuerpo a un enemigo le bajarás su defensa en un 0.3 y su cura recibida en un 80% durante 2 turnos, tiene un cooldown de 10 turnos')
    print ('E - Sandalias de poder: "poder" Aumenta tu poder en 0.5 pero baja tu defensa en 0.5 durante 3 turnos, tiene un cooldown de 8 turnos')
    print ('F - Botas de escudo: "carga de escudo" Aplica a ti y a tu objetivo un escudo de 400 de vida que dura 3 turnos, tiene un cooldown de 9 turnos')

def infocapas():
    print ('A - Capa de Montaña: Si tu vida actual está por debajo del 40% tu defensa es aumentada por 3 por 2 turnos, tiene un cooldown de 9 turnos')
    print ('B - Capa de Cansancio: Si tu nivel de energia es menor a 50 regeneras 120 de energia, tiene un cooldown de 9 turnos')
    print ('C - Capa de Furia contenida: Si tu vida actual está por debajo del 80% tu poder es aumentada por 2 por 2 turnos, tiene un cooldown de 7 turnos')
    print ('D - Capa de Muerto Vivo: Si tu vida baja por debajo del 10% te vuelves invisible por 3 turnos y te reduce el poder en 0.4 por 3 turnos')

def infoamuletos():
    print ('A - Piedra de afilar/Libro de hechillos avanzados: +0.2 de poder')
    print ('B - Zapatos de Hermes: +15 de velocidad')
    print ('C - Tónico de vigor: +10% de vida')
    print ('D - Totem de sangre: +5% de robo de vida')
    print ('E - Medallón del muerto: +0.5 de poder y -0.2 de defensa')
    print ('F - Cota de malla: +0.2 de defensa')

def botas_venganza(ones):
    venganza = 1
    hp = ones.health
    maxhp = ones.maxhealth
    cincoporcieen = maxhp * 5 / 100
    veinteporcieen = maxhp * 20 / 100
    cuarentaporcieen = maxhp * 40 / 100
    sesentaporcieen = maxhp * 60 / 100
    ochentaporcieen = maxhp * 80 / 100
    
    if hp < cincoporcieen:
        venganza = 6
    elif hp < veinteporcieen:
        venganza = 5
    elif hp < cuarentaporcieen:
        venganza = 4
    elif hp < sesentaporcieen:
        venganza = 3
    elif hp < ochentaporcieen:
        venganza = 2

    if venganza == 1:
        ones.power += 0.1
        print ('Alimenta tus ganas de venganza y aumenta tu poder en 0.1', '\n')
    elif venganza == 2:
        ones.power += 0.4
        print ('Alimenta tus ganas de venganza y aumenta tu poder en 0.4', '\n')
    elif venganza == 3:
        ones.power += 0.75
        print ('Alimenta tus ganas de venganza y aumenta tu poder en 0.75', '\n')
    elif venganza == 4:
        ones.power += 1
        print ('Alimemta tus ganas de venganza y aumenta tu poder en 1', '\n')
    elif venganza == 5:
        ones.power += 1.5
        print ('Alimenta tus ganas de venganza y aumenta tu poder en 1.5', '\n')
    elif venganza == 6:
        ones.power += 2
        print ('Alimenta tus ganas de venganza y aumenta tu poder en 2', '\n')
    else:
        print ('Error, informa de este error')

def HechizoDeBuild (hechizoo, equipamientox, enemy, numjug): 
    global uno
    global dos
    global tres
    global cuatro
    global cinco
    global seis
    global siete
    global ocho
    global nueve
    global diez
    turn = input('¿Que hechizo lanzas del equipamiento?: (0 - cancelar) (9 - mirar cooldown)')
    if turn.lower() == 'paz':
        if equipamientox.casco == 'habdruida':
            if equipamientox.cooldowncasco <= campo.nturnos:
                for i in range(1, 6):  
                    if hechizoo.efectod[i] == '':
                        hechizoo.efectod[i] = 'aenergia'
                        hechizoo.efectodn[i] = 40
                        hechizoo.tiempod[i] = campo.nturnos + 3
                        equipamientox.cooldowncasco = campo.nturnos + 7 
                        break
                print ('Conectas con el más allá y regeneras 120 de energia durante 3 turnos', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado el hábito de monje', '\n')
            
    elif turn.lower() == 'niebla':
        if equipamientox.casco == 'capvandalo':
            if equipamientox.cooldowncasco <= campo.nturnos:
                if hechizoo.energy <= 20:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    jugadores = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez]
                    for i in range(len (jugadores)):
                        if jugadores [i] != '':
                            jugadores[i].cargas['silenciado'] += 3
                    hechizoo.energy -= 20
                    equipamientox.cooldowncasco = campo.nturnos + 9
                    print ('De tú casco sale un densa niebla morada que silencia a todos los personajes por 3 turnos', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la capucha de tinieblas', '\n')

    elif turn.lower() == 'tormenta':
        if equipamientox.casco == 'casjuez':
            if equipamientox.cooldowncasco <= campo.nturnos:
                if hechizoo.energy <= 36:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    if numjug == 2:
                        uno.health -= 120
                        uno[num].cargas['stun'] += 1
                        dos[num].health -= 120
                        dos[num].cargas['stun'] += 1
                        hechizoo.health += 120
                        hechizoo.cargas['stun'] -= 1

                    elif numjug == 'tres' or numjug == 'cuatro' or numjug == 'cinco' or numjug == 'seis' or numjug == 'diez':
                        enemys = input ('Di el número de los jugadores enemigos para pegarles')
                        enemy1 = enemys.find('1')
                        if enemy1 != -1:
                            uno.health -= 120
                            uno.cargas['stun'] += 1
                        enemy2 = enemys.find('2')
                        if enemy2 != -1:
                            dos.health -= 120
                            dos.cargas['stun'] += 1
                        enemy3 = enemys.find('3')
                        if enemy3 != -1:
                            tres.health -= 120
                            tres.cargas['stun'] += 1
                        enemy4 = enemys.find('4')
                        if enemy4 != -1:
                            cuatro.health -= 120
                            cuatro.cargas['stun'] += 1
                        enemy5 = enemys.find('5')
                        if enemy5 != -1:
                            cinco.health -= 120
                            cinco.cargas['stun'] += 1
                        enemy6 = enemys.find('6')
                        if enemy6 != -1:
                            seis.health -= 120
                            seis.cargas['stun'] += 1
                        enemy7 = enemys.find('7')
                        if enemy7 != -1:
                            tres.health -= 120
                            tres.cargas['stun'] += 1
                        enemy8 = enemys.find('8')
                        if enemy8 != -1:
                            cuatro.health -= 120
                            cuatro.cargas['stun'] += 1
                        enemy9 = enemys.find('9')
                        if enemy9 != -1:
                            cinco.health -= 120
                            cinco.cargas['stun'] += 1
                        enemy10 = enemys.find('10')
                        if enemy10 != -1:
                            seis.health -= 120
                            seis.cargas['stun'] += 1
                        enemybr = enemys.find('roja')
                        if enemybr != -1:
                            boxred.health -= 120
                        enemybb = enemys.find('azul')
                        if enemybb != -1:
                            boxblue.health -= 120
                        hechizoo.energy -= 36
                        equipamientox.cooldowncasco = campo.nturnos + 8
                        print (hechizoo.name, 'lanza rayos en todas direcciones infligiendo 120 de daño y aturdiendo 1 turno a sus enemigos', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado el casco de tormentas', '\n')

    elif turn.lower() == 'sacrificio':
        if equipamientox.casco == 'cazguarda':
            if equipamientox.cooldowncasco <= campo.nturnos:
                if enemy.invisible > 0:
                    print ('El objetivo está invisible por lo que no se puede seleccionar')
                elif hechizoo.energy <= 28:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    hechizoo.health -= hechizoo.maxhealth * 5 / 100
                    enemy.health += enemy.maxhealth * 5 / 100
                    hechizoo.energy -= 28
                    equipamientox.cooldowncasco = campo.nturnos + 5
                    print (hechizoo.name, 'se sacrifica y pierde un 5% de su vida máxima para regenerar el 5% de la vida máxima de', enemy.name, '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado el casco de sacrificio', '\n')

    elif turn.lower() == 'meteorito':
        if equipamientox.casco == 'casreal':
            if equipamientox.cooldowncasco <= campo.nturnos:
                if enemy.invisible > 0:
                    print ('El objetivo está invisible por lo que no se puede seleccionar')
                elif hechizoo.energy <= 55:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    meteoritoo = randint (1, 100)
                    if meteoritoo > 90:
                        print (enemy.name, 'esquiva el meteorito con mucha agilidad')
                        hechizoo.energy -= 14
                    else:
                        enemy.health -= 200
                        enemy.cargas['stun'] += 2
                        hechizoo.energy -= 28
                        print (hechizoo.name, 'lanza un meteorito sobre', enemy.name, ', le quita 200 de vida y lo aturde 2 turnos', '\n')
                    equipamientox.cooldowncasco = campo.nturnos + 11
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado el casco meteorico', '\n')

    elif turn.lower() == 'rebote':
        if equipamientox.casco == 'capcazador':
            if equipamientox.cooldowncasco <= campo.nturnos:
                if hechizoo.energy <= 60:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    for i in range(1, 6):  
                        if hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'arebote'
                            hechizoo.efecton[i] = 0.75
                            hechizoo.tiempo[i] = campo.nturnos + 3
                            hechizoo.reflejar += 0.75
                            equipamientox.cooldowncasco = campo.nturnos + 10
                            break
                    print ('Te aplicas un escudo por 2 turnos que reflejará el 75% del daño recibido', '\n')
                    hechizoo.energy -= 60
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la capucha de rebote', '\n')

    elif turn.lower() == 'infinito':
        if equipamientox.casco == 'habreal':
            if equipamientox.cooldowncasco <= campo.nturnos:
                if hechizoo.energy <= -90020007000000001000020203930232001:
                    print (hechizoo.name, 'no tiene suficiente energia xd')
                else:
                    for i in range (0, 4):
                        if hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'energyinf'
                            hechizoo.efecton[i] = hechizoo.energy
                            hechizoo.tiempo[i] = campo.nturnos + 2
                            hechizoo.energy += 100000000000
                            equipamientox.cooldowncasco = campo.nturnos + 10
                            break
                    print ('Tienes energia infinita por 2 turnos', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado el hábito de infinidad', '\n')

    elif turn.lower() == 'hielo':
        if equipamientox.casco == 'habcle':
            if equipamientox.cooldowncasco <= campo.nturnos:
                hechizoo.cargas['hielo'] += 3
                for i in range (0, 4):
                    if hechizoo.efecto[i] == '':
                        hechizoo.efecto[i] = 'invencible'
                        hechizoo.efecton[i] = 0
                        hechizoo.tiempo[i] = campo.nturnos + 3
                        hechizoo.cargas['invencible'] += 1
                equipamientox.cooldowncasco = campo.nturnos + 9
                print (hechizoo.name, 'se congela 3 turnos y se vuelve invulnerable al daño', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado el hábito de hielo', '\n')

    elif turn.lower() == 'reset':
        if equipamientox.casco == 'capespec':
            if equipamientox.cooldowncasco <= campo.nturnos:
                equipamientox.cooldownarmaduras = 0
                print ('Reseteas el cooldown de tu armadura', '\n')
                equipamientox.cooldowncasco = campo.nturnos + 13
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la capucha de reset', '\n')

    elif turn.lower() == 'campo de fuerza': 
        if equipamientox.armadura == 'armjuez':
            if equipamientox.cooldownarmaduras <= campo.nturnos:
                if hechizoo.energy <= 62:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    aliados = input('Di el número de los jugadores aliados para aplicaros el escudo incluyete a ti mismo (ej: soy el jugador 1 y escribo "1" para aplicarme el escudo)')

                    jugadores = {
                        '1': uno if 'uno' else None,
                        '2': dos if 'dos' else None,
                        '3': tres if 'tres' else None,
                        '4': cuatro if 'cuatro' else None,
                        '5': cinco if 'cinco' else None,
                        '6': seis if 'seis' else None,
                        '7': siete if 'siete' else None,
                        '8': ocho if 'ocho' else None,
                        '9': nueve if 'nueve' else None,
                        '10': diez if 'diez' else None
                    }

                    efectos = [
                        ('adefensa', 'defense', 0.4),
                        ('arcura', 'rcura', 0.6)
                    ]

                    for num, jugador in jugadores.items():
                        if num in aliados and jugador is not None:
                            for efecto, atributo, valor in efectos:
                                for i in range(0, 4):
                                    if jugador.efecto[i] == '':
                                        jugador.efecto[i] = efecto
                                        jugador.efecton[i] = valor
                                        jugador.tiempo[i] = campo.nturnos + 3
                                        setattr(jugador, atributo, getattr(jugador, atributo) + valor)
                                        break

                    print ('Protege con un escudo a tus aliados y a ti que aumenta vuestra defensa en 0.4 y vuestra cura recibida en 0.6', '\n')
                    hechizoo.energy -= 62
                equipamientox.cooldownarmaduras = campo.nturnos + 12
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la armadura de fuerza', '\n')

    elif turn.lower() == 'guardian':
        if equipamientox.armadura == 'armguard':
            if equipamientox.cooldownarmaduras <= campo.nturnos:
                if hechizoo.energy <= 62:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    aliados = input ('Di el número de los jugadores enemigos para aplicaros el debuff (ej: soy el jugador 4 y escribo "3 2 1" para bajarles el daño)')
                    aliado1 = aliados.find('1')
                    if aliado1 != -1:
                        for i in range (0, 4):
                            if uno.efecto[i] == '':
                                uno.efecto[i] = 'bpower'
                                uno.efecton[i] = 0.6
                                uno.tiempo[i] = campo.nturnos + 4
                                uno.power -= 0.6
                                break

                    aliado2 = aliados.find('2')
                    if aliado2 != -1:
                        for i in range (0, 4):
                            if dos.efecto[i] == '':
                                dos.efecto[i] = 'bpower'
                                dos.efecton[i] = 0.6
                                dos.tiempo[i] = campo.nturnos + 4
                                dos.power -= 0.6
                                break

                    aliado3 = aliados.find('3')
                    if aliado3 != -1:
                        for i in range (0, 4):
                            if tres.efecto[i] == '':
                                tres.efecto[i] = 'bpower'
                                tres.efecton[i] = 0.6
                                tres.tiempo[i] = campo.nturnos + 4
                                tres.power -= 0.6
                                break

                    aliado4 = aliados.find('4')
                    if aliado4 != -1:
                        for i in range (0, 4):
                            if cuatro.efecto[i] == '':
                                cuatro.efecto[i] = 'bpower'
                                cuatro.efecton[i] = 0.6
                                cuatro.tiempo[i] = campo.nturnos + 4
                                cuatro.power -= 0.6
                                break

                    aliado5 = aliados.find('5')
                    if aliado5 != -1:
                        for i in range (0, 4):
                            if cinco.efecto[i] == '':
                                cinco.efecto[i] = 'bpower'
                                cinco.efecton[i] = 0.6
                                cinco.tiempo[i] = campo.nturnos + 4
                                cinco.power -= 0.6
                                break

                    aliado6 = aliados.find('6')
                    if aliado6 != -1:
                        for i in range (0, 4):
                            if seis.efecto[i] == '':
                                seis.efecto[i] = 'bpower'
                                seis.efecton[i] = 0.6
                                seis.tiempo[i] = campo.nturnos + 4
                                seis.power -= 0.6
                                break
                    
                    aliado7 = aliados.find('7')
                    if aliado7 != -1:
                        for i in range (0, 4):
                            if siete.efecto[i] == '':
                                siete.efecto[i] = 'bpower'
                                siete.efecton[i] = 0.6
                                siete.tiempo[i] = campo.nturnos + 4
                                siete.power -= 0.6
                                break

                    aliado8 = aliados.find('8')
                    if aliado8 != -1:
                        for i in range (0, 4):
                            if ocho.efecto[i] == '':
                                ocho.efecto[i] = 'bpower'
                                ocho.efecton[i] = 0.6
                                ocho.tiempo[i] = campo.nturnos + 4
                                ocho.power -= 0.6
                                break

                    aliado9 = aliados.find('9')
                    if aliado9 != -1:
                        for i in range (0, 4):
                            if nueve.efecto[i] == '':
                                nueve.efecto[i] = 'bpower'
                                nueve.efecton[i] = 0.6
                                nueve.tiempo[i] = campo.nturnos + 4
                                nueve.power -= 0.6
                                break

                    aliado10 = aliados.find('10')
                    if aliado10 != -1:
                        for i in range (0, 4):
                            if diez.efecto[i] == '':
                                diez.efecto[i] = 'bpower'
                                diez.efecton[i] = 0.6
                                diez.tiempo[i] = campo.nturnos + 4
                                diez.power -= 0.6
                                break

                    for i in range (0, 4):
                        if hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'bpower'
                            hechizoo.efecton[i] = 0.6
                            hechizoo.tiempo[i] = campo.nturnos + 4
                            hechizoo.power -= 0.6
                            break
                    print ('Crea un aura debilitadora que reduce tu daño y el de tus enemigo en 0.6', '\n')
                    hechizoo.energy -= 48
                equipamientox.cooldownarmaduras = campo.nturnos + 12
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la armadura de debilidad', '\n')

    elif turn.lower() == 'proteccion del demonio' or turn.lower() == 'protección del demonio':
        if equipamientox.armadura == 'armdemon':
            if equipamientox.cooldownarmaduras <= campo.nturnos:
                if hechizoo.energy <= 0:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    aliados = input ('Di el número de los jugadores aliados para aplicaros la protección incluyete a ti mismo (ej: soy el jugador 1 y escribo "1 2" para aplicarnos la protección)')
                    aliado1 = aliados.find('1')
                    if aliado1 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if uno.efecto[i] == '' and alredy:
                                uno.efecto[i] = 'adefensa'
                                uno.efecton[i] = 0.2
                                uno.tiempo[i] = campo.nturnos + 3
                                uno.defense += 0.2
                                alredy = False

                            elif uno.efecto[i] == '':
                                uno.efecto[i] = 'areflejo'
                                uno.efecton[i] = 0.3
                                uno.tiempo[i] = campo.nturnos + 3
                                uno.reflejar += 0.3
                                break

                    aliado2 = aliados.find('2')
                    if aliado2 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if dos.efecto[i] == '' and alredy:
                                dos.efecto[i] = 'adefensa'
                                dos.efecton[i] = 0.2
                                dos.tiempo[i] = campo.nturnos + 3
                                dos.defense += 0.2

                            elif dos.efecto[i] == '':
                                dos.efecto[i] = 'areflejo'
                                dos.efecton[i] = 0.3
                                dos.tiempo[i] = campo.nturnos + 3
                                dos.reflejar += 0.3
                                break

                    aliado3 = aliados.find('3')
                    if aliado3 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if tres.efecto[i] == '' and alredy:
                                tres.efecto[i] = 'adefensa'
                                tres.efecton[i] = 0.2
                                tres.tiempo[i] = campo.nturnos + 3
                                tres.defense += 0.2
                                alredy = False

                            if tres.efecto[i] == '':
                                tres.efecto[i] = 'areflejo'
                                tres.efecton[i] = 0.3
                                tres.tiempo[i] = campo.nturnos + 3
                                tres.reflejar += 0.3
                                break

                    aliado4 = aliados.find('4')
                    if aliado4 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if cuatro.efecto[i] == '' and alredy:
                                cuatro.efecto[i] = 'adefensa'
                                cuatro.efecton[i] = 0.2
                                cuatro.tiempo[i] = campo.nturnos + 3
                                cuatro.defense += 0.2
                                alredy = False

                            if cuatro.efecto[i] == '':
                                cuatro.efecto[i] = 'areflejo'
                                cuatro.efecton[i] = 0.3
                                cuatro.tiempo[i] = campo.nturnos + 3
                                cuatro.reflejar += 0.3
                                break

                    aliado5 = aliados.find('5')
                    if aliado5 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if cinco.efecto[i] == '' and alredy:
                                cinco.efecto[i] = 'adefensa'
                                cinco.efecton[i] = 0.2
                                cinco.tiempo[i] = campo.nturnos + 3
                                cinco.defense += 0.2
                                alredy = False

                            if cinco.efecto[i] == '':
                                cinco.efecto[i] = 'areflejo'
                                cinco.efecton[i] = 0.3
                                cinco.tiempo[i] = campo.nturnos + 3
                                cinco.reflejar += 0.3
                                break

                    aliado6 = aliados.find('6')
                    if aliado6 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if seis.efecto[i] == '' and alredy:
                                seis.efecto[i] = 'adefensa'
                                seis.efecton[i] = 0.2
                                seis.tiempo[i] = campo.nturnos + 3
                                seis.defense += 0.2
                                alredy = False

                            if seis.efecto[i] == '' and alredy:
                                seis.efecto[i] = 'areflejo'
                                seis.efecton[i] = 0.3
                                seis.tiempo[i] = campo.nturnos + 3
                                seis.reflejar += 0.3
                                break
                            
                    aliado7 = aliados.find('7')
                    if aliado7 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if siete.efecto[i] == '' and alredy:
                                siete.efecto[i] = 'adefensa'
                                siete.efecton[i] = 0.2
                                siete.tiempo[i] = campo.nturnos + 3
                                siete.defense += 0.2
                                alredy = False

                            if siete.efecto[i] == '':
                                siete.efecto[i] = 'areflejo'
                                siete.efecton[i] = 0.3
                                siete.tiempo[i] = campo.nturnos + 3
                                siete.reflejar += 0.3
                                break

                    aliado8 = aliados.find('8')
                    if aliado8 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if ocho.efecto[i] == '' and alredy:
                                ocho.efecto[i] = 'adefensa'
                                ocho.efecton[i] = 0.2
                                ocho.tiempo[i] = campo.nturnos + 3
                                ocho.defense += 0.2
                                alredy = False

                            if ocho.efecto[i] == '':
                                ocho.efecto[i] = 'areflejo'
                                ocho.efecton[i] = 0.3
                                ocho.tiempo[i] = campo.nturnos + 3
                                ocho.reflejar += 0.3
                                break

                    aliado9 = aliados.find('9')
                    if aliado9 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if nueve.efecto[i] == '' and alredy:
                                nueve.efecto[i] = 'adefensa'
                                nueve.efecton[i] = 0.2
                                nueve.tiempo[i] = campo.nturnos + 3
                                nueve.defense += 0.2
                                alredy = False

                            if nueve.efecto[i] == '':
                                nueve.efecto[i] = 'areflejo'
                                nueve.efecton[i] = 0.3
                                nueve.tiempo[i] = campo.nturnos + 3
                                nueve.reflejar += 0.3
                                break

                    aliado10 = aliados.find('10')
                    if aliado10 != -1:
                        alredy = True
                        for i in range (0, 4):
                            if diez.efecto[i] == '' and alredy:
                                diez.efecto[i] = 'adefensa'
                                diez.efecton[i] = 0.2
                                diez.tiempo[i] = campo.nturnos + 3
                                diez.defense += 0.2
                                alredy = False

                            if diez.efecto[i] == '' and alredy:
                                diez.efecto[i] = 'areflejo'
                                diez.efecton[i] = 0.3
                                diez.tiempo[i] = campo.nturnos + 3
                                diez.reflejar += 0.3
                                break

                    for i in range (0, 4):
                        if hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'bdefense'
                            hechizoo.efecton[i] = 0.3
                            hechizoo.tiempo[i] = campo.nturnos + 3
                            hechizoo.defense -= 0.3
                            break
                    print ('Crea una protección para tus aliados que les hace reflejar todo el daño en un 0.3 y les sube la defensa en 0.4, aunque te baja tu propia defensa en 0.5', '\n')
                    hechizoo.energy -= 49
                equipamientox.cooldownarmaduras = campo.nturnos + 12
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la armadura de demonio', '\n')

    elif turn.lower() == 'autocombustion' or turn.lower() == 'autocombustión':
        if equipamientox.armadura == 'armespec':
            if equipamientox.cooldownarmaduras <= campo.nturnos:
                if hechizoo.energy <= 0:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    aliados = input ('Di el número de los jugadores enemigos para dañarles (cajas no) (ej: soy el jugador 1 y escribo "4 5 6" para dañarles)')
                    aliado1 = aliados.find('1')
                    if aliado1 != -1:
                        for i in range (0, 4):
                            if uno.efectod[i] == '':
                                uno.efectod[i] = 'daño'
                                uno.efectodn[i] = 100
                                uno.tiempod[i] = campo.nturnos + 3
                                break
                    
                    aliado2 = aliados.find('2')
                    if aliado2 != -1:
                        for i in range (0, 4):
                            if dos.efectod[i] == '':
                                dos.efectod[i] = 'daño'
                                dos.efectodn[i] = 100
                                dos.tiempod[i] = campo.nturnos + 3
                                break

                    aliado3 = aliados.find('3')
                    if aliado3 != -1:
                        for i in range (0, 4):
                            if tres.efectod[i] == '':
                                tres.efectod[i] = 'daño'
                                tres.efectodn[i] = 100
                                tres.tiempod[i] = campo.nturnos + 3
                                break

                    aliado4 = aliados.find('4')
                    if aliado4 != -1:
                        for i in range (0, 4):
                            if cuatro.efectod[i] == '':
                                cuatro.efectod[i] = 'daño'
                                cuatro.efectodn[i] = 100
                                cuatro.tiempod[i] = campo.nturnos + 3
                                break

                    aliado5 = aliados.find('5')
                    if aliado5 != -1:
                        for i in range (0, 4):
                            if cinco.efectod[i] == '':
                                cinco.efectod[i] = 'daño'
                                cinco.efectodn[i] = 100
                                cinco.tiempod[i] = campo.nturnos + 3
                                break

                    aliado6 = aliados.find('6')
                    if aliado6 != -1:
                        for i in range (0, 4):
                            if seis.efectod[i] == '':
                                seis.efectod[i] = 'daño'
                                seis.efectodn[i] = 100
                                seis.tiempod[i] = campo.nturnos + 3
                                break

                    aliado7 = aliados.find('7')
                    if aliado7 != -1:
                        for i in range (0, 4):
                            if siete.efectod[i] == '':
                                siete.efectod[i] = 'daño'
                                siete.efectodn[i] = 100
                                siete.tiempod[i] = campo.nturnos + 3
                                break

                    aliado8 = aliados.find('8')
                    if aliado8 != -1:
                        for i in range (0, 4):
                            if ocho.efectod[i] == '':
                                ocho.efectod[i] = 'daño'
                                ocho.efectodn[i] = 100
                                ocho.tiempod[i] = campo.nturnos + 3
                                break

                    aliado9 = aliados.find('9')
                    if aliado9 != -1:
                        for i in range (0, 4):
                            if nueve.efectod[i] == '':
                                nueve.efectod[i] = 'daño'
                                nueve.efectodn[i] = 100
                                nueve.tiempod[i] = campo.nturnos + 3
                                break

                    aliado10 = aliados.find('10')
                    if aliado10 != -1:
                        for i in range (0, 4):
                            if diez.efectod[i] == '':
                                diez.efectod[i] = 'daño'
                                diez.efectodn[i] = 100
                                diez.tiempod[i] = campo.nturnos + 3
                                break

                    alredy = True
                    for i in range (0, 4):
                        if hechizoo.efectod[i] == '' and alredy:
                            hechizoo.efectod[i] = 'daño'
                            hechizoo.efectodn[i] = 100
                            hechizoo.tiempod[i] = campo.nturnos + 3
                            print ('se le atribuye quemadura de 300 durante 3')
                            alredy = False

                        elif hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'brcura'
                            hechizoo.efecton[i] = 0.33
                            hechizoo.tiempo[i] = campo.nturnos + 3
                            hechizoo.rcura -= 0.33
                            break

                        equipamientox.cooldowncasco = campo.nturnos + 12
                    print ('Incendiate y haz 300 de daño a ti y tus enemigos, además te reduce la cura recibida en 33', '\n')
                    hechizoo.energy -= 45
                equipamientox.cooldownarmaduras = campo.nturnos + 12
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la chaqueta de combustión', '\n')

    elif turn.lower() == 'sed de sangre':
        if equipamientox.armadura == 'chamerc':
            if equipamientox.cooldownarmaduras <= campo.nturnos:
                if hechizoo.energy <= 40:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    for i in range (0, 4):
                        if hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'arobovida'
                            hechizoo.efecton[i] = 0.55
                            hechizoo.tiempo[i] = campo.nturnos + 3
                            hechizoo.robovida += 0.55
                            break
                    print ('Robas el 55% de todo el daño directo que hagas por los próximos 2 turnos', '\n')
                    hechizoo.energy -= 40
                equipamientox.cooldownarmaduras = campo.nturnos + 12
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la chaqueta de sangre', '\n')

    elif turn.lower() == 'salvacion' or turn.lower() == 'salvación':
        if equipamientox.armadura == 'tuncle':
            if equipamientox.cooldownarmaduras <= campo.nturnos:
                if hechizoo.energy <= 42:
                    print (hechizoo.name, 'no tiene suficiente energia')
                else:
                    for i in range (0, 4):
                        if hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'salvacion'
                            hechizoo.efecton[i] = hechizoo.health
                            hechizoo.tiempo[i] = campo.nturnos + 1
                            break
                    print ('Si recibes daño por el siguiente turno serás invulnerable 2 turnos y aumentarás tu poder y lanzamiento de curacion en 35% por 2 turnos', '\n')
                    hechizoo.energy -= 42
                equipamientox.cooldownarmaduras = campo.nturnos + 12
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado la túnica de salvación', '\n')

    elif turn.lower() == 'venganza':
        if equipamientox.botas == 'botdemon':
            if equipamientox.cooldownbotas <= campo.nturnos:
                botas_venganza (hechizoo)
                equipamientox.cooldownbotas = campo.nturnos + 12
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado las botas de venganza', '\n')

    elif turn.lower() == 'gigante':
        if equipamientox.botas == 'botguard':
            if equipamientox.cooldownbotas <= campo.nturnos:
                for i in range (0, 4):
                    if hechizoo.efecto[i] == '':
                        hechizoo.efecto[i] = 'avidapor'
                        hechizoo.efecton[i] = 50
                        hechizoo.tiempo[i] = campo.nturnos + 2
                        hechizoo.maxhealth = hechizoo.maxhealth + hechizoo.maxhealth * 50 / 100
                        hechizoo.health = hechizoo.health + hechizoo.health * 50 / 100
                        break
                print (hechizoo.name, 'se vuelve gigante aumentando su vida máxima y actual en un 50%')
                equipamientox.cooldownbotas = campo.nturnos + 8
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado las botas del gigante', '\n')

    elif turn.lower() == 'imparable':
        if equipamientox.botas == 'botguarda':
            if equipamientox.cooldownbotas <= campo.nturnos:
                for i in range (0, 4):
                    if hechizoo.efecto[i] == '':
                        hechizoo.efecto[i] = 'imparable'
                        hechizoo.efecton[i] = 0
                        hechizoo.tiempo[i] = campo.nturnos + 3
                        hechizoo.imparable = 1
                        break
                equipamientox.cooldownbotas = campo.nturnos + 13
                print ('Vuelvete imparable y durante los siguientes 3 turnos no puedes ser aturdido, congelado, paralizado, inmovilizado, silenciado, ni dormido', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado las botas imparables', '\n')

    elif turn.lower() == 'suelo podrido':
        if equipamientox.botas == 'sandsect':
            if equipamientox.cooldownbotas <= campo.nturnos:
                hechizoo.cargas['putrefacción'] = 2
                equipamientox.cooldownbotas = campo.nturnos + 11
                print ('Pudre tu arma y los siguientes 2 turnos tus ataques cuerpo a cuerpo bajaran la defensa de tu enemigo en 0.3 y su cura recivida en 0.8', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado las sandalias de putrefacción', '\n')

    elif turn.lower() == 'poder':
        if equipamientox.botas == 'sandreal':
            if equipamientox.cooldownbotas <= campo.nturnos:
                for i in range (0, 4):
                    if hechizoo.efecto[i] == '':
                        hechizoo.efecto[i] = 'apower'
                        hechizoo.efecton[i] = 0.5
                        hechizoo.tiempo[i] = campo.nturnos + 4
                        hechizoo.power += 0.5
                        break

                for i in range (0, 4):
                    if hechizoo.efecto[i] == '':
                        hechizoo.efecto[i] = 'bdefense'
                        hechizoo.efecton[i] = 0.5
                        hechizoo.tiempo[i] = campo.nturnos + 3
                        hechizoo.defense -= 0.5
                        break

                equipamientox.cooldownbotas = campo.nturnos + 9
                print ('Te efureces aumentando tu poder en 0.5 pero te descuidas bajando tu defensa en 0.5', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado las sandalias de poder', '\n')
    elif turn.lower() == 'carga de escudo':
        if equipamientox.botas == 'botcab':
            if equipamientox.cooldownbotas <= campo.nturnos:
                if hechizoo == enemy:
                    for i in range (0, 4):
                        if hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'escudo'
                            hechizoo.efecton[i] = hechizoo.health
                            hechizoo.tiempo[i] = campo.nturnos + 3
                            hechizoo.health += 400
                            break
                else:
                    for i in range (0, 4):
                        if hechizoo.efecto[i] == '':
                            hechizoo.efecto[i] = 'escudo'
                            hechizoo.efecton[i] = hechizoo.health
                            hechizoo.tiempo[i] = campo.nturnos + 3
                            hechizoo.health += 400
                            break

                    for i in range (0, 4):
                        if enemy.efecto[i] == '':
                            enemy.efecto[i] = 'escudo'
                            enemy.efecton[i] = enemy.health
                            enemy.tiempo[i] = campo.nturnos + 3
                            enemy.health += 400
                            break

                equipamientox.cooldownbotas = campo.nturnos + 10
                print ('Aplica sobre tu objetivo y sobre ti mismo un escudo que cubre 400 de vida por los siguientes 3 turnos', '\n')
            else:
                print ('La habilidad aún está en cooldown', '\n')
        else:
            print ('No tienes equipado las botas de escudo', '\n')
    
    if turn == '0':
        return True
    elif turn == '9':
        print ('La habilidad del casco para mi se puede volver a lanzar en el turno', equipamientox.cooldowncasco)
        print ('La habilidad de la armadura para mi se puede volver a lanzar en el turno', equipamientox.cooldownarmaduras)
        print ('La habilidad de las botas para mi se puede volver a lanzar en el turno', equipamientox.cooldownbotas, '\n')
        HechizoDeBuild (hechizoo, equipamientox, enemy, numjug)
    else: 
        return False
        
def EfectosPorTiempo(personaje, n):
    efectos_dicc = {
        "avida": ("maxhealth", -1),
        "bvida": ("maxhealth", 1),
        "cura": ("health", 1),
        "curapor": ("health", "percentage"),
        "daño": ("health", -1),
        "dañopor": ("health", "percentage"),
        "aenergia": ("energy", 1),
        "benergia": ("energy", -1),
        "adefensa": ("defense", -1),
        "bdefensa": ("defense", 1),
        "apower": ("power", -1),
        "bpower": ("power", 1),
        "areflejo": ("reflejar", -1),
        "breflejo": ("reflejar", 1),
        "arcura": ("rcura", -1),
        "brcura": ("rcura", 1),
        "arobovida": ("robovida", -1),
        "brobovida": ("robovida", 1),
        "alcura": ("lcura", -1),
        "blcura": ("lcura", 1),
    }

    for i in range(n): 
        efecto = personaje.efecto[i]
        if efecto and personaje.tiempo[i] <= campo.nturnos:  
            if efecto in efectos_dicc:  
                atributo, operacion = efectos_dicc[efecto]
                cantidad = float(personaje.efecton[i])  
                
                if operacion == "percentage":
                    setattr(personaje, atributo, getattr(personaje, atributo) * (1 - cantidad / 100))
                else:
                    setattr(personaje, atributo, getattr(personaje, atributo) + cantidad * operacion)

                print(f"Se ha eliminado/aplicado el efecto {efecto} en {personaje.name}.")

            elif efecto == 'avidapor':
                vida_perdida = personaje.maxhealth - personaje.health
                vida_perdida_reducida = vida_perdida * (personaje.efecton[i] / 100)
                personaje.maxhealth = personaje.healthbase
                personaje.health = personaje.maxhealth - vida_perdida_reducida
                print (f"El efecto {efecto} ha terminado en {personaje.name}.")

            elif efecto == 'bvidapor':
                vida_perdida = personaje.maxhealth - personaje.health
                vida_perdida_maximisada = vida_perdida / (personaje.efecton[i] / 100)
                personaje.maxhealth = personaje.healthbase
                personaje.health = personaje.maxhealth - vida_perdida_maximisada
                print (f"El efecto {efecto} ha terminado en {personaje.name}.")

            elif efecto == "imparable":
                personaje.cargas['imparable'] = 0
                print(f"El efecto {efecto} ha terminado en {personaje.name}.")

            elif efecto == "invencible":
                personaje.cargas['invencible'] -= 1
                print(f"El efecto {efecto} ha terminado en {personaje.name}.")

            elif efecto == "escudo":
                if personaje.health > personaje.efecton[i]:
                    personaje.health = personaje.efecton[i]
                    print(f"El escudo de vida se ha disipado en {personaje.name}.")
            
            elif efecto == "salvacion":
                if personaje.health < personaje.efecton[i]:
                    for j in range (0, 4):
                        if personaje.efecto[j] == '':
                            personaje.efecto[j] = 'invencible'
                            personaje.efecton[j] = 1
                            personaje.tiempo[j] = campo.nturnos + 2
                            personaje.cargas['invencible'] += 1
                            break

                    for j in range (0, 4):
                        if personaje.efecto[j] == '':
                            personaje.efecto[j] = 'apower'
                            personaje.efecton[j] = 0.35
                            personaje.tiempo[j] = campo.nturnos + 2
                            personaje.power += 0.35
                            break

                    for j in range (0, 4):
                        if personaje.efecto[j] == '':
                            personaje.efecto[j] = 'alcura'
                            personaje.efecton[j] = 0.35
                            personaje.tiempo[j] = campo.nturnos + 2
                            personaje.lcura += 0.35
                            break
                    print(f"Se ha activado el escudo de salvación en {personaje.name}.")

            elif efecto == "energyinf":
                if personaje.energy > personaje.efecton[i]:
                    personaje.energy = personaje.efecton[i]
                    print(f"La energía infinita ha desaparecido en {personaje.name}.")

            elif efecto == 'diablo':
                if personaje.cargas['maldita'] == 0:
                    dano = 100 * personaje.efecton[i] / personaje.defense

                elif personaje.cargas['maldita'] == 1:
                    dano = 150 * personaje.efecton[i] / personaje.defense

                elif personaje.cargas['maldita'] == 2:
                    dano = 250 * personaje.efecton[i] / personaje.defense

                elif personaje.cargas['maldita'] == 3:
                    dano = 500 * personaje.efecton[i] / personaje.defense

                elif personaje.cargas['maldita'] >= 4:
                    dano = 800 * personaje.efecton[i] / personaje.defense
                if personaje.cargas['invencible'] == 1:
                    dano = 0
                print ('El diablo inflige', dano, 'de daño a', personaje.name)
                personaje.health -= dano
                personaje.cargas['cura'] = 0
                personaje.cargas['maldita'] = 0
            else:
                print(f"Efecto desconocido {efecto} eliminado de {personaje.name}.")

            personaje.efecto[i] = ''
            personaje.efecton[i] = ''
            personaje.tiempo[i] = ''

def EfectosPorTurnosEnTiempo (number):
    for i in range (len(number.efectod)):
        if number.efectod[i] == 'aenergia':
            number.energy += number.efectodn[i]

        elif number.efectod[i] == 'benergia':
            number.energy -= number.efectodn[i]

        elif number.efectod[i] == 'daño':
            number.health -= number.efectodn[i]
            print (number.name, 'recibe', number.efectodn[i], 'de daño')

        elif number.efectod[i] == 'dañopor':
            number.health = number.health - number.health * number.efectodn[i] / 100

        elif number.efectod[i] == 'cura':
            number.health += number.efectodn[i]

        elif number.efectod[i] == 'curapor':
            number.health = number.health + number.health * number.efectodn[i] / 100


def EfectosPorTurnosEnTiempoComprobando (character):
    for i in range (len(character.efectod)):
        if character.efectod[i] != '':
            if character.tiempod[i] >= campo.nturnos:
                EfectosPorTurnosEnTiempo (character)

def tempo (quien):
    EfectosPorTiempo(quien, len(quien.efecto))
    EfectosPorTurnosEnTiempoComprobando(quien)

def checar_campos ():
    if campo.lluvia > 0:
        campo.lluvia = 0
        print ('Deja de llover')
    if campo.nevar > 0:
        campo.nevar = 0
        print ('Para de nevar')
    if campo.hierba > 0:
        campo.hierba = 0
        print ('El encantamiento de la hierba pierde su poder')
    if campo.sol > 0:
        campo.sol = 0
        print ('El poder solar se calma')
    if campo.purificador > 0:
        campo.purificador = 0
        print ('Otro campo aparece y sustituye a la purificación')

def purificar (obj):
    elicarg = ['sangrado', 'quemado', 'veneno', 'hemorragia', 'hielo', 'stun', 'paralizado', 'maldita', 'silenciado', 'inmovilizado', 'corrupción', 'dormido']
    for i in elicarg:
        obj.cargas[i] = 0
    obj.locura = 0


def refuerzos (cuantos):
    if cuantos == 'uno':
        players = [uno]
    elif cuantos == 'dos':
        players = [uno, dos]
    elif cuantos == 'tres':
        players = [uno, dos, tres]
    elif cuantos == 'cuatro':
        players = [uno, dos, tres, cuatro]
    elif cuantos == 'cinco':
        players = [uno, dos, tres, cuatro, cinco]
    elif cuantos == 'seis':
        players = [uno, dos, tres, cuatro, cinco, seis]
    elif cuantos == 'diez':
        players = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez]
    for i in players:
        if i.tipo == 0:
            print (i.name, 'saca de la manga 50 de energia')
            i.energy += 50
        elif i.tipo == 1:
            print ('¡', i.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
            i.defense += 0.25
        elif i.tipo == 3:
            print ('¡', i.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
            i.power += 0.25
        elif i.tipo == 2:
            print ('¡', i.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
            i.power += 0.15
            i.defense += 0.15
        elif i.tipo == 4:
            print ('¡', i.name, '!¡Llegan refuerzos! Te tomas una poción que te regenera 2% de tu salud máxima')
            i.health += i.maxhealth * 2 / 100 
        elif i.tipo == 5:
            print ('¡', i.name, '!¡Llegan refuerzos! Te vuelves más salvaje que nunca y aumentas tu velocidad en 8 y tu poder en 0.10')
            i.power += 0.1
            i.velocity += 8

def estampida (cuantos):
    print ('Una estampida cruza la arena aturdiendo a todos, bajando sus precisiones en 3')
    if cuantos == 'uno':
        players = [uno]
    elif cuantos == 'dos':
        players = [uno, dos]
    elif cuantos == 'tres':
        players = [uno, dos, tres]
    elif cuantos == 'cuatro':
        players = [uno, dos, tres, cuatro]
    elif cuantos == 'cinco':
        players = [uno, dos, tres, cuatro, cinco]
    elif cuantos == 'seis':
        players = [uno, dos, tres, cuatro, cinco, seis]
    elif cuantos == 'diez':
        players = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez]

    for i in players:
        i.preci1 -= 3
        i.preci2 -= 3
        i.preci3 -= 3
        i.precicura -= 3
        i.precienergia -= 3

def eliminar_cargas (cuantos):
    if cuantos == 'uno':
        jugadores = [uno]
    elif cuantos == 'dos':
        jugadores = [uno, dos]
    elif cuantos == 'tres':
        jugadores = [uno, dos, tres]
    elif cuantos == 'cuatro':
        jugadores = [uno, dos, tres, cuatro]
    elif cuantos == 'cinco':
        jugadores =[uno, dos, tres, cuatro, cinco]
    elif cuantos == 'seis':
        jugadores = [uno, dos, tres, cuatro, cinco, seis]
    elif cuantos == 'diez':
        players = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez]
    cargas = ["carga_cura", "carga_hemorragia", "carga_hielo", "carga_maldita", 
            "carga_paralizado", "carga_quemado", "carga_sangrado", "carga_stun", "carga_veneno"]

    for jugador in jugadores:
        for carga in cargas:
            setattr(jugador, carga, 0)

    print ('Se purifica el ambiente', '\n')

def cargas (cargadoo):
    if cargadoo.cargas['veneno'] >= 10 and cargadoo.name != 'Caja Azul' and cargadoo.name != 'Caja Roja':
        print (cargadoo.name, 'está tan lleno de veneno que acaba por morir')
        cargadoo.health = -1000000

    if cargadoo.cargas['sangrado'] >= 3:
        print ('Tanto sangrado provoca una hemorragia en', cargadoo.name)
        cargadoo.cargas['hemorragia'] += 1

    if cargadoo.cargas['veneno'] >= 1:
        print ('El veneno inflige', 5 * cargadoo.cargas['veneno'], 'a', cargadoo.name)
        cargadoo.health -= 5 * cargadoo.cargas['veneno']

    if cargadoo.cargas['quemado'] >= 1:
        print ('La quemadura inflige', 36 * cargadoo.cargas['quemado'], 'a', cargadoo.name)
        cargadoo.health -= 36 * cargadoo.cargas['quemado']

    if cargadoo.cargas['sangrado'] >= 1:
        print ('El sangrado inflige', 15 * cargadoo.cargas['sangrado'], 'a', cargadoo.name, 'que además pierde 2 gotas de sangre')
        cargadoo.health -= 15 * cargadoo.cargas['sangrado']
        cargadoo.sangre -= 1

    if cargadoo.cargas['hemorragia'] >= 1:
        print ('La hemorragia inflige', 60 * cargadoo.cargas['hemorragia'], 'a', cargadoo.name, 'que además pierde 10 gotas de sangre')
        cargadoo.health -= 60 * cargadoo.cargas['hemorragia']
        cargadoo.sangre -= 3

    if cargadoo.cargas['maldita'] >= 1:
        print ('La maldición inflige', 30 * cargadoo.cargas['maldita'], 'a', cargadoo.name)
        cargadoo.health -= 30 * cargadoo.cargas['maldita']

    if cargadoo.health > 0:
        if cargadoo.cargas['cura'] >= 1:
            print ('Tus cargas te curan', 28 * cargadoo.cargas['cura'] * cargadoo.rcura, 'puntos de vida')
            cargadoo.health += 28 * cargadoo.cargas['cura'] * cargadoo.rcura

def startturn (ones):
    if ones.velocity == first:
        campo.nturnos += 1
    if ones.cargas['imparable'] == 1:
        ones.cargas['hielo'] = 0
        ones.cargas['paralizado'] = 0
        ones.cargas['stun'] = 0
        ones.cargas['inmovilizado'] = 0
        ones.cargas['silenciado'] = 0
        ones.cargas['dormido'] = 0
    if ones.invisible > 0:
        ones.invisible -= 1
        if ones.invisible == 0:
            print ('Se le acaba la invisibilidad a',ones.name)

def correct (who, enemy):
    pass

def equipbuild (numberequip, mee):
    while True:
        casco1 = input ('Que casco escoges para la batalla jugador? (Escribe la letra que represente al casco) (escribe "info" para información de los cascos)')
        if casco1.lower() == 'info':
            infocascos()
        elif casco1.lower() == 'a':
            numberequip.casco = 'habdruida'
            break
        elif casco1.lower() == 'b':
            numberequip.casco = 'capvandalo'
            break
        elif casco1.lower() == 'c':
            numberequip.casco = 'casjuez'
            break
        elif casco1.lower() == 'd':
            numberequip.casco = 'cazguarda'
            break
        elif casco1.lower() == 'e':
            numberequip.casco = 'casreal'
            break
        elif casco1.lower() == 'f':
            numberequip.casco = 'capcazador'
            break
        elif casco1.lower() == 'g':
            numberequip.casco = 'habreal'
            break
        elif casco1.lower() == 'h':
            numberequip.casco = 'habcle'
            break
        elif casco1.lower() == 'i':
            numberequip.casco = 'capespec'
            break

    while True:
        armadura1 = input ('Que armadura escoges para la batalla? (escribe "info" para información de los cascos)')
        if armadura1.lower() == 'info':
            infoarmaduras()
        elif armadura1.lower() == 'a':
            numberequip.armadura = 'armjuez'
            break
        elif armadura1.lower() == 'b':
            numberequip.armadura = 'armguard'
            break
        elif armadura1.lower() == 'c':
            numberequip.armadura = 'armdemon'
            break
        elif armadura1.lower() == 'd':
            numberequip.armadura = 'armespec'
            break
        elif armadura1.lower() == 'e':
            numberequip.armadura = 'chamerc'
            break
        elif armadura1.lower() == 'f':
            numberequip.armadura = 'tuncle'
            break

    while True:
        botas1 = input ('Que botas escoges para la batalla? (escribe "info" para información de las botas)')
        if botas1.lower() == 'info':
            infobotas()
        elif botas1.lower() == 'a':
            numberequip.botas = 'botdemon'
            break
        elif botas1.lower() == 'b':
            numberequip.botas = 'botguard'
            break
        elif botas1.lower() == 'c':
            numberequip.botas = 'botguarda'
            break
        elif botas1.lower() == 'd':
            numberequip.botas = 'sandsect'
            break
        elif botas1.lower() == 'e':
            numberequip.botas = 'sandreal'
            break
        elif botas1.lower() == 'f':
            numberequip.botas = 'botcab'
            break
    while True:
        capas1 = input ('Que capa escoges para la batalla? (escribe "info" para información de las capas)')
        if capas1.lower() == 'info':
            infocapas()
        elif capas1.lower() == 'a':
            numberequip.capa = 'capmont'
            break
        elif capas1.lower() == 'b':
            numberequip.capa = 'capcans'
            break
        elif capas1.lower() == 'c':
            numberequip.capa = 'capfuri'
            break
        elif capas1.lower() == 'd':
            numberequip.capa = 'capamuer'
            break
    while True:
        amuleto1 = input ('Que amuleto escoges para la batalla? (escribe "info" para información de los amuletos)')
        if amuleto1.lower() == 'info':
            infoamuletos()
        elif amuleto1.lower() == 'a':
            numberequip.amuleto = 'apower'
            break
        elif amuleto1.lower() == 'b':
            numberequip.amuleto = 'avelocity'
            break
        elif amuleto1.lower() == 'c':
            numberequip.amuleto = 'ahealth'
            break
        elif amuleto1.lower() == 'd':
            numberequip.amuleto = 'alifesteal'
            break
        elif amuleto1.lower() == 'e':
            numberequip.amuleto = 'apowerbdefense'
            break
        elif amuleto1.lower() == 'f':
            numberequip.amuleto = 'adefense'
            break

def aplicar_amuletos (players):
    for i in players:
        equipo = questinum(i)
        if equipo.amuleto == 'apower':
            i.power += 0.2
        elif equipo.amuleto == 'avelocity':
            i.velocity += 15
        elif equipo.amuleto == 'ahealth':
            i.maxhealth = i.healthbase + i.healthbase * 90 / 100
            i.health += i.healthbase + i.healthbase * 90 / 100
            i.healthbase += i.healthbase + i.healthbase * 90 / 100
        elif equipo.amuleto == 'apower':
            i.power += 0.2
        elif equipo.amuleto == 'apower':
            i.power += 0.2
        elif equipo.amuleto == 'apower':
            i.power += 0.2

def check_capa (me, numberequip, enemy):
    if numberequip.capa == 'capmont' and me.health <= me.maxhealth * 40 / 100:
        for i in range(1, 6):  
            if me.efecto[i] == '':
                me.efecto[i] = 'adefensa'
                me.efecton[i] = 3
                me.tiempo[i] = campo.nturnos + 3
                numberequip.cooldowncapa = campo.nturnos + 9
                me.defense += 3
                break
    elif numberequip.capa == 'capcans' and me.energy <= 50:
        me.energy += 120
    elif numberequip.capa == 'capfuri' and me.health <= me.maxhealth * 80 / 100:
        for i in range(1, 6):  
            if me.efecto[i] == '':
                me.efecto[i] = 'apower'
                me.efecton[i] = 2
                me.tiempo[i] = campo.nturnos + 3
                numberequip.cooldowncapa = campo.nturnos + 9
                me.defense += 3
                break
    elif numberequip.capa == 'capmuer' and me.health <= me.maxhealth * 10 / 100:
        me.invisible += 3
        me.power -= 0.4

def check_dies (team, total):
    if total == 4:
        if team:
            if uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0:
                print ('Es un EMPATE. ¿¿Cómo?? JAJAJAJA')
                exit()
            elif uno.health <= 0 and dos.health <= 0:
                print ('Players 3 & 4 WIIIIN')
                exit()
            elif tres.health <= 0 and cuatro.health <= 0:
                print ('Players 1 & 2 WIIIIN')
                exit()
        else:
            if uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0:
                print ('Es un EMPATE. ¿¿Cómo?? JAJAJAJA')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                print ('Players 4 WIIIIN')
                exit()
            elif tres.health <= 0 and cuatro.health <= 0 and uno.health <= 0:
                print ('Players 2 WIIIIN')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and cuatro.health <= 0:
                print ('Players 3 WIIIIN')
                exit()
            elif tres.health <= 0 and cuatro.health <= 0 and dos.health <= 0:
                print ('Players 1 WIIIIN')
                exit()

    elif total == 6:
        if team == '2v2v2':
            if uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Es un EMPATE. ¿¿Cómo?? JAJAJAJA')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 3 & 4 WIIIIN')
                exit()
            elif tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 1 & 2 WIIIIN')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health:
                print ('Players 5 & 6 WIIIIN')
                exit()
        elif team == '3v3':
            if uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Es un EMPATE. ¿¿Cómo?? JAJAJAJA')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                print ('Players 4, 5 & 6 WIIIIN')
                exit()
            elif cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 1, 2 & 3 WIIIIN')
                exit()
        elif team:
            if uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Es un EMPATE. ¿¿Cómo?? JAJAJAJA')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 3 WIIIIN')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 4 WIIIIN')
                exit()
            elif uno.health <= 0 and tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 2 WIIIIN')
                exit()
            elif dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 1 WIIIIN')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and cuatro.health <= 0 and tres.health <= 0 and seis.health <= 0:
                print ('Players 5 WIIIIN')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health and cinco.health <= 0:
                print ('Players 6 WIIIIN')
                exit()
    elif total == 10:
        if team == '2v2v2v2v2':
            if uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Es un EMPATE. ¿¿Cómo?? JAJAJAJA')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 3 & 4 WIIIIN')
                exit()
            elif tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 1 & 2 WIIIIN')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health:
                print ('Players 5 & 6 WIIIIN')
                exit()
        elif team == '5v5':
            if uno.health <= 0 and dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Es un EMPATE. ¿¿Cómo?? JAJAJAJA')
                exit()
            elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                print ('Players 4, 5 & 6 WIIIIN')
                exit()
            elif cuatro.health <= 0 and cinco.health <= 0 and seis.health <= 0:
                print ('Players 1, 2 & 3 WIIIIN')
                exit()
        elif team:
            print ('Work on progress, report this')
            exit()

def check_personaje (selff):
    if selff == her:
        ok = True
        while ok:
            try:
                integer = int(input ('Numero di alleati?'))
            except ValueError:
                print ('Questo non è un numero')
            else:
                ok = False
        for i in range (integer):
            ok = True
            while ok:
                ali = ('Numero alleato: (1, 2, 3... 0-annullare)')
                if ali == '1':
                    her.aliados.append(uno)
                elif ali == '2':
                    her.aliados.append(dos)
                elif ali == '3':
                    her.aliados.append(tres)
                elif ali == '4':
                    her.aliados.append(cuatro)
                elif ali == '5':
                    her.aliados.append(cinco)
                elif ali == '6':
                    her.aliados.append(seis)
                elif ali == '7':
                    her.aliados.append(siete)
                elif ali == '8':
                    her.aliados.append(ocho)
                elif ali == '9':
                    her.aliados.append(nueve)
                elif ali == '10':
                    her.aliados.append(diez)
                elif ali == '0':
                    pass
                else:
                    print ("Questa non è un'opzione")

def dacac (propio, hechizoo): #despues atacar cuerpo a cuerpo
    if propio.cargas['putrefacción'] > 0:
        for i in range (0, 4):
            if hechizoo.efecto[i] == '':
                hechizoo.efecto[i] = 'brcura'
                hechizoo.efecton[i] = 0.8
                hechizoo.tiempo[i] = campo.nturnos + 2
                hechizoo.rcura -= 0.8

        for i in range (0, 4):
            if hechizoo.efecto[i] == '':
                hechizoo.efecto[i] = 'bdefense'
                hechizoo.efecton[i] = 0.3
                hechizoo.tiempo[i] = campo.nturnos + 2
                hechizoo.defense -= 0.3

        propio.cargas['putrefacción'] -= 1
        print ('Tú putrefacción invade a', hechizoo.name, 'y reduces su defensa en 0.3 y su cura recibida en 0.8 por 2 turnos')
        if propio.cargas['putrefacción'] == 0:
            print ('Se te ha acabado tu efecto de pudrefacción')

def questinum (qui):
    if qui == uno:
        return equipamiento1
    if qui == dos:
        return equipamiento2
    if qui == tres:
        return equipamiento3
    if qui == cuatro:
        return equipamiento4
    if qui == cinco:
        return equipamiento5
    if qui == seis:
        return equipamiento6
    if qui == siete:
        return equipamiento7
    if qui == ocho:
        return equipamiento8
    if qui == nueve:
        return equipamiento9
    if qui == diez:
        return equipamiento10

def play(me, howmuch, number):
    mapa_todos = {
        'dos':   [uno, dos],
        'tres':  [uno, dos, tres],
        'cuatro':[uno, dos, tres, cuatro],
        'seis':  [uno, dos, tres, cuatro, cinco, seis],
        'diez':  [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez],
    }
    todos = mapa_todos[howmuch]

    # Mapa de nombre/número → entidad, para el input del jugador
    mapa_input = {f'jugador {i+1}': e for i, e in enumerate(todos)}
    mapa_input.update({e.name.lower(): e for e in todos})

    startturn(me)
    tempo(me)

    for turnnn in range(1):

        # ── Efectos de campo ─────────────────────────────────────────────────
        if campo.lluvia == 1:
            for e in todos:
                e.cargas['quemado'] = 0
            print('La lluvia apaga las quemaduras y los moja')

        elif campo.nevar == 1:
            nieve = randint(1, 100)
            if nieve <= 20:
                me.cargas['hielo'] += 1
                print(me.name, 'se congela durante un turno')
            else:
                print(me.name, 'resiste el frío de la nieve')

        elif campo.hierba == 1:
            mult = 0.8 if me.tipo == 4 else 0.5
            cura = me.maxhealth * mult / 100
            me.health += cura
            print(me.name, 'se cura', cura, 'de vida gracias al pasto sanador')

        elif campo.purificador == 1:
            eliminar_cargas(howmuch)

        if me.health <= 0:
            break

        # ── Selección de objetivo (jugador humano) ───────────────────────────
        if me.cargas['stun'] <= 0 and me.cargas['hielo'] <= 0:
            objective = None
            while objective is None:
                print(f'¿Quién es tu objetivo, jugador {number}?')
                who = input().strip().lower()

                # Runa (caso especial)
                if who == 'runa':
                    if runa.runa_on:
                        objective = runa
                    else:
                        print('No hay runa activa')
                    continue

                # Buscar en el mapa de jugadores
                target = mapa_input.get(who)
                if target is None:
                    print('Objetivo no reconocido, intenta de nuevo')
                    continue

                if target == me:
                    print('No puedes seleccionarte a ti mismo como objetivo')
                    continue

                if target.invisible > 0:
                    print(f'{target.name} está invisible y no se puede seleccionar')
                    continue

                if target.mundo != me.mundo:
                    print(f'{target.name} está en un mundo diferente y no se puede seleccionar')
                    continue

                objective = target
        else:
            objective = uno

        # ── Fenómenos aleatorios ─────────────────────────────────────────────
        fenomeno = randint(1, 100)

        if fenomeno <= 5:
            if campo.trrr == 0:
                terremoto = randint(1, 4)
                print('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                for e in todos:
                    e.cargas['stun'] += terremoto
                campo.trrr = terremoto * 2
            else:
                campo.trrr -= 1

        elif fenomeno <= 12:
            refuerzos(howmuch)

        elif fenomeno <= 15:
            estampida(howmuch)

        elif fenomeno <= 20:
            ventisca = randint(1, 100)
            if ventisca <= 40:
                print('Una fuerte ventisca azota a', me.name, ',', me.name, 'resiste y no se congela')
            elif ventisca <= 75:
                print('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 1 turno')
                me.cargas['hielo'] += 1
            elif ventisca <= 95:
                print('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 2 turnos')
                me.cargas['hielo'] += 2
            else:
                print('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 3 turnos')
                me.cargas['hielo'] += 3

        elif fenomeno <= 24:
            print('Unos rayos azotan la arena quebrantando la armadura de todos bajando su defensa en 0.1')
            for e in todos:
                e.defense -= 0.1

        elif fenomeno <= 29:
            print('Tregua. Se realiza una tregua en la cuál todos descansan regenerando 30 de energia')
            for e in todos:
                e.energy += 30

        elif fenomeno <= 33:
            print('Una lluvia ácida cae sobre todos envenenandoles x2')
            for e in todos:
                e.cargas['veneno'] += 2

        elif fenomeno <= 35:
            print('Extenuar. Todos quedan extenuados y con 20 de energia menos')
            for e in todos:
                e.energy -= 20

        # ── Combate ──────────────────────────────────────────────────────────
        check_capa(me, questinum(me), objective)

        running = True
        while running:
            me.turno(objective)

            if objective.health <= 0:
                print(me.name, 'mató a', objective.name)
                running = False
            elif me.health <= 0:
                print(me.name, 'murió en su turno')
                running = False

            if me.armorspell == 1:
                ttt = HechizoDeBuild(me, questinum(me), objective, howmuch)
                if objective.health <= 0:
                    print(me.name, 'mató a', objective.name)
                    running = False
                elif me.health <= 0:
                    print(me.name, 'murió en su turno')
                    running = False
                if ttt == False:
                    running = False  # corregido: era 'runing' (typo tuyo)
                me.armorspell = 0
            else:
                running = False

# ── Helpers globales ──────────────────────────────────────────────────────────

def calcular_punt(entity):
    return (50 / (entity.prio + 4)) + (1500 / entity.health)

def mejor_objetivo(candidatos):
    """Mayor puntuación; desempate por mayor health."""
    return max(candidatos, key=lambda e: (calcular_punt(e), e.health))

def get_equipos(todos, team):
    """Devuelve lista de equipos según el modo de juego."""
    if not team:                 return [[e] for e in todos]          # FFA
    if team is True:             return [todos[:2], todos[2:4]]       # 2v2
    if team == '3v3':            return [todos[:3], todos[3:6]]       # 3v3
    if team == '2v2v2':          return [todos[:2], todos[2:4], todos[4:6]]
    if team == '1v1v1':          return [[todos[0]], [todos[1]], [todos[2]]]
    if team == '1v1v1v1':        return [[e] for e in todos[:4]]
    if team == '5v5':            return [todos[:5], todos[5:10]]
    if team == '2v2v2v2v2':      return [todos[i:i+2] for i in range(0, 10, 2)]
    if team == 'ffa10':          return [[e] for e in todos]
    return [[e] for e in todos]  # fallback FFA

def seleccionar_objetivo(me, todos, team):
    """
    Devuelve el mejor objetivo para 'me'.
    - Soporte (healer/FSD) en equipo real → elige entre sus aliados.
    - Cualquier otro caso → elige entre sus enemigos.
    """
    equipos   = get_equipos(todos, team)
    mi_equipo = next(eq for eq in equipos if me in eq)
    es_soporte = me.rol in ('healer', 'FSD')

    if es_soporte and len(mi_equipo) > 1:
        candidatos = mi_equipo       
    else:
        candidatos = [e for e in todos if e not in mi_equipo]

    return mejor_objetivo(candidatos)



def playIA(me, howmuch, number, team):
    mapa_todos = {
        'dos':   [uno, dos],
        'tres':  [uno, dos, tres],
        'cuatro':[uno, dos, tres, cuatro],
        'seis':  [uno, dos, tres, cuatro, cinco, seis],
        'diez':  [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez],
    }
    todos = mapa_todos[howmuch]

    startturn(me)
    tempo(me)

    for turnnn in range(1):
        if campo.lluvia == 1:
            for e in todos:
                e.cargas['quemado'] = 0
            print('La lluvia apaga las quemaduras y los moja')

        elif campo.nevar == 1:
            nieve = randint(1, 100)
            if nieve <= 20:
                me.cargas['hielo'] += 1
                print(me.name, 'se congela durante un turno')
            else:
                print(me.name, 'resiste el frío de la nieve')

        elif campo.hierba == 1:
            mult = 0.8 if me.tipo == 4 else 0.5
            cura = me.maxhealth * mult / 100
            me.health += cura
            print(me.name, 'se cura', cura, 'de vida gracias al pasto sanador')

        elif campo.purificador == 1:
            eliminar_cargas(howmuch)

        if me.health <= 0:
            break

        if me.cargas['stun'] <= 0 and me.cargas['hielo'] <= 0:
            objective = seleccionar_objetivo(me, todos, team)
        else:
            objective = uno 

        fenomeno = randint(1, 100)

        if fenomeno <= 5:
            if campo.trrr == 0:
                terremoto = randint(1, 4)
                print('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                for e in todos:
                    e.cargas['stun'] += terremoto
                campo.trrr = terremoto * 2
            else:
                campo.trrr -= 1

        elif fenomeno <= 12:
            refuerzos(howmuch)

        elif fenomeno <= 15:
            estampida(howmuch)

        elif fenomeno <= 20:
            ventisca = randint(1, 100)
            if ventisca <= 40:
                print('Una fuerte ventisca azota a', me.name, ',', me.name, 'resiste y no se congela')
            elif ventisca <= 75:
                print('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 1 turno')
                me.cargas['hielo'] += 1
            elif ventisca <= 95:
                print('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 2 turnos')
                me.cargas['hielo'] += 2
            else:
                print('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 3 turnos')
                me.cargas['hielo'] += 3

        elif fenomeno <= 24:
            print('Unos rayos azotan la arena quebrantando la armadura de todos bajando su defensa en 0.1')
            for e in todos:
                e.defense -= 0.1

        elif fenomeno <= 29:
            print('Tregua. Se realiza una tregua en la cuál todos descansan regenerando 30 de energia')
            for e in todos:
                e.energy += 30

        elif fenomeno <= 33:
            print('Una lluvia ácida cae sobre todos envenenandoles x2')
            for e in todos:
                e.cargas['veneno'] += 2

        elif fenomeno <= 35:
            print('Extenuar. Todos quedan extenuados y con 20 de energia menos')
            for e in todos:
                e.energy -= 20

        check_capa(me, questinum(me), objective)

        running = True
        while running:
            me.turnoIA(objective)

            murio_objetivo = objective.health <= 0
            murio_yo       = me.health <= 0

            if murio_objetivo:
                print(me.name, 'mató a', objective.name)
                running = False
            elif murio_yo:
                print(me.name, 'murió en su turno')
                running = False

            if me.armorspell == 1:
                ttt = HechizoDeBuild(me, questinum(me), objective, howmuch)
                if objective.health <= 0:
                    print(me.name, 'mató a', objective.name)
                    running = False
                elif me.health <= 0:
                    print(me.name, 'murió en su turno')
                    running = False
                if ttt == False:
                    running = False
                me.armorspell = 0
            else:
                running = False

def playatraco (me, howmuch):
    startturn (me)
    tempo()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.cargas['quemado'] = 0
            dos.cargas['quemado'] = 0
            tres.cargas['quemado'] = 0
            cuatro.cargas['quemado'] = 0
            cinco.cargas['quemado'] = 0
            seis.cargas['quemado'] = 0
            boxblue.cargas['quemado'] = 0
            boxred.cargas['quemado'] = 0
            print ('La lluvia apaga las quemaduras y los moja')

        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                me.cargas['hielo'] += 1
                print (me.name, 'se congela durante un turno')
            else:
                print (me.name, 'resiste el frío de la nieve')

        elif campo.hierba == 1:
            if me.tipo == 4:
                cura = me.maxhealth * 0.8 / 100
                me.health += cura
                print (me.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = me.maxhealth * 0.5 / 100
                me.health += cura
                print (me.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas ()
        if me.ko == 1:
            print (me.name, 'se levanta y puede seguir peleando')
            me.health = me.maxhealth
            me.ko = 0
            me.cargas['cura'] = 0
            me.cargas['hemorragia'] = 0
            me.cargas['hielo'] = 0
            me.cargas['maldita'] = 0
            me.cargas['paralizado'] = 0
            me.cargas['quemado'] = 0
            me.cargas['sangrado'] = 0
            me.cargas['stun'] = 0
            me.cargas['veneno'] = 0
        if me.ko > 1:
            print ('Estás noqueado, jugador 1', '\n')
            me.ko -= 1
        else:
            if me.cargas['stun'] <= 0 and me.cargas['hielo'] <= 0:
                who = input ('¿Quién es tu objetivo, jugador 1?') 
                if who.lower() == 'jugador 2': #
                    objective = dos
                elif who.lower() == 'jugador 1': 
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 1?')
                    if who.lower() == 'jugador 2': #
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.cargas['stun'] += terremoto
                    dos.cargas['stun'] += terremoto
                    tres.cargas['stun'] += terremoto
                    cuatro.cargas['stun'] += terremoto
                    cinco.cargas['stun'] += terremoto
                    seis.cargas['stun'] += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', me.name, ',', me.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 1 turno')
                    me.cargas['hielo'] += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 3 turnos')
                    me.cargas['hielo'] += 3
                else:
                    print ('Una fuerte ventisca azota a', me.name, ',', me.name, 'se congela 2 turnos')
                    me.cargas['hielo'] += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective.health <= 0:
                running = True
                while running:
                    me.turno(objective)
                    if me.health <= 0:
                        print (me.name, 'murió en su turno')
                        me.ko = 3
                        running = False
                    if me.armorspell == 1:
                        ttt = HechizoDeBuild(me, questinum(me), objective, howmuch)
                        if me.health <= 0:
                            print (me.name, 'murió en su turno')
                            me.ko = 3
                            running = False
                        if ttt == False:
                            runing = False
                        me.armorspell = 0
                    else:
                        running = False
            else:
                running = True
                while running:
                    me.turno(objective)
                    if objective.health <= 0:
                        print( me.name,'mató a', objective.name)
                        objective.ko = 3
                        running = False

                    elif me.health <= 0:
                        print (me.name, 'murió en su turno')
                        me.ko = 3
                        running = False

                    if me.armorspell == 1:
                        ttt = HechizoDeBuild(me, questinum(me), objective, howmuch)
                        if objective.health <= 0:
                            print( me.name,'mató a', objective.name)
                            objective.ko = 3
                            running = False
                        elif me.health <= 0:
                            print (me.name, 'murió en su turno')
                            me.ko = 3
                            running = False
                        if ttt == False:
                            runing = False
                        me.armorspell = 0
                    else:
                        running = False

class Hero ():
    def __init__ (self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth #número
        self.healthbase = maxhealth
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.cargas = {
            "sangrado": 0, "quemado": 0, "veneno": 0, "hemorragia": 0, "cura": 0, "hielo": 0,
            "stun": 0, "paralizado": 0, "maldita": 0, "silenciado": 0, "inmovilizado": 0,
            "corrupción": 0, "dormido": 0, "imparable": 0, "invencible": 0, "putrefacción": 0
        }
        self.tipo = tipo
        self.mundo = mundo
        self.ko = 0
        self.lcura = 1
        self.rcura = 1
        self.sangre = 100
        self.mutado = mutado
        self.efecto = ['', '', '', '', ''] #efecto (duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efecton = [0, 0, 0, 0, 0] #efecto numero)
        self.tiempo = [0, 0, 0, 0, 0] #tiempo 
        self.efectod = ['', '', '', '', ''] #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efectodn = [0, 0, 0, 0, 0] #efecto (numero)
        self.tiempod = [0, 0, 0, 0, 0]
        self.locura = locura
        self.reflejar = reflejar
        self.agro = agro
        self.cooldown = [0, 0, 0]
        self.armorspell = 0
        self.robovida = robovida
        self.invisible = invisible
        self.rol = rol
        self.prio = prio
        self.att1 = 0

    def canplay (self, enemy):
        if campo.sol == 1:
            if self.cargas['hielo'] > 0:
                print ('El calor descongela a', self.name)
                self.cargas['hielo'] = 0
            if self.cargas['stun'] > 0:
                print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                self.cargas['stun'] = 0
        if self.cargas['hielo'] > 0:
            print (self.name, 'está congelado y no puede hacer nada')
            self.cargas['hielo'] -= 1
            printdatos(self, enemy)
            return False
        elif self.cargas['stun'] > 0:
            cargas(self)
            self.cargas['stun'] -= 1
            print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.cargas['stun'])
            printdatos(self, enemy)
            return False
        if self.health <= 0:
            return False
        else:
            return True

    def atacar(self, objetivo, damage, mele): #Loco no pasa por aqui!!
        if runa.runa_on and objetivo == runa:
            runa.recibir_dano_runa(damage)
        else: 
            dano = damage * self.power / objetivo.defense
            if objetivo.cargas['invencible'] == 1:
                dano = 0
            reflejo = dano * objetivo.reflejar 
            dano_total = dano - reflejo
            objetivo.health -= damage
            self.health -= reflejo
            if self.robovida > 1:
                self.robovida = 1
            elif self.robovida < 0:
                self.robovida = 0
            robado = dano_total * self.robovida
            if objetivo.reflejar > 0:
                print (objetivo.name, 'refleja', reflejo, 'de daño')
            if robado != 0:
                print (self.name, 'roba', robado, 'de vida')
                self.health += robado
            return dano_total

    def venda (self, enemy):
        #cargas
        cargas(self)
        #el turno
        if self.cargas['silenciado'] > 0:
            print (self.name, 'está silenciado y no puede curarse')
            self.cargas['silenciado'] -= 1
            return
        elif self.cargas['paralizado'] > 0:
            paraliza = randint (0, 100)
            if paraliza <= 40:
                print (self.name, 'está paralizado y no puede hacer nada')
                self.cargas['paralizado'] -= 1
                return
            else:
                print (self.name, 'no se paraliza')
                self.cargas['paralizado'] -= 1
        if self.energy <= 70:
            print (self.name, 'no tiene suficiente energia')
            self.energy += 3
            return
        curaaaaa = randint(1, 100)
        if curaaaaa > self.precicura: 
            print ('¡falla la venda!')
            self.energy -= 25
            self.energy += 3
        else:
            if self.health >= self.maxhealth - 80 * self.power and self.health < self.maxhealth:
                print ('Te pones una venda que te cura toda la vida')
                self.health = self.maxhealth
            elif self.health > self.maxhealth:
                print ('Ya supera la vida máxima, por lo tanto no se puede curar')
            else:
                print ('Te pones una venda que te cura', 80 * self.power ,'de vida')
                self.health += 80 * self.power
            if self.cargas['hemorragia'] > 0:
                if self.cargas['hemorragia'] > 1:
                    pastooo = randint (1, 2)
                    print ('Además te curas', pastooo,'hemorragias/s') 
                    self.cargas['hemorragia'] -= pastooo
                else:
                    print ('Además te curas 1 hemorragia')
                    self.cargas['hemorragia'] -= 1
            if self.cargas['quemado'] > 0:
                if self.cargas['quemado'] > 1:
                    pastooo = randint (1, 3)
                    print ('Además te curas', pastooo,'quemadura/s')
                    self.cargas['quemado'] -= pastooo
                else:
                    print ('Además te curas 1 quemadura')
                    self.cargas['quemado'] -= 1
            self.energy -= 50
            self.energy += 2
            printdatos(self, enemy)

    def cura (self, enemy):
        cargas(self)
        if self.cargas['silenciado'] > 0:
            print (self.name, 'está silenciada y no puede curarse')
            self.cargas['silenciado'] -= 1
            return
        elif self.cargas['paralizado'] > 0:
            paraliza = randint (0, 100)
            if paraliza <= 40:
                print (self.name, 'está paralizado y no puede hacer nada')
                self.cargas['paralizado'] -= 1
                return
            else:
                print (self.name, 'no se paraliza')
                self.cargas['paralizado'] -= 1
        if self.energy <= 70:
            print (self.name, 'no tiene suficiente energia')
            self.energy += 4
        else:
            curaaa = randint(0, 100)
            if curaaa > self.precicura: 
                print ('Se rompe la poción!')
                self.energy -= 25
                self.energy += 4
            else:
                if self.health >= self.maxhealth - 100 * self.power and self.health < self.maxhealth:
                    print ('Te tomas una poción que te cura toda la vida')
                    self.health = self.maxhealth
                elif self.health > self.maxhealth:
                    print ('Ya supera la vida máxima, por lo tanto no se cura')
                else:
                    print ('Te tomas una poción que te cura', 100 * self.power ,'de vida')
                    self.health += 100 * self.power
                if self.cargas['hemorragia'] > 0:
                    if self.cargas['hemorragia'] > 1:
                        pastooo = randint (1, 2)
                        print ('Además te curas', pastooo,'hemorragia/s')
                        self.cargas['hemorragia'] -= pastooo
                    else:
                        print ('Además te curas 1 hemorragia')
                        self.cargas['hemorragia'] -= 1
                if self.cargas['quemado'] > 0:
                    if self.cargas['quemado'] > 1:
                        pastooo = randint (1, 3)
                        print ('Además te curas', pastooo,'quemadura/s')
                        self.cargas['quemado'] -= pastooo
                    else:
                        print ('Además te curas 1 quemadura')
                        self.cargas['quemado'] -= 1
                self.energy -= 50
                self.energy += 4
        printdatos(self, enemy)

    def curar (self, enemy):
        cargas(self)
        if self.cargas['silenciado'] > 0:
            print (self.name, 'está silenciada y no puede curarse')
            self.cargas['silenciado'] -= 1
            return
        elif self.cargas['paralizado'] > 0:
            paraliza = randint (0, 100)
            if paraliza <= 40:
                print (self.name, 'está paralizado y no puede hacer nada')
                self.cargas['paralizado'] -= 1
                return
            else:
                print (self.name, 'no se paraliza')
                self.cargas['paralizado'] -= 1
        if self.energy <= 70:
            print (self.name, 'no tiene suficiente energia')
            self.energy += 4
        else:
            curaaa = randint(0, 100)
            if curaaa > self.precicura: 
                print ('Se rompe la poción!')
                self.energy -= 25
                self.energy += 4
            else:
                print ('Le das una poción a', enemy.name, 'que le cura', 100 * self.power ,'de vida')
                enemy.health += 100 * self.power
                if self.cargas['hemorragia'] > 0:
                    if self.cargas['hemorragia'] > 1:
                        pastooo = randint (1, 2)
                        print ('Además le curas', pastooo,'hemorragia/s')
                        self.cargas['hemorragia'] -= pastooo
                    else:
                        print ('Además le curas 1 hemorragia')
                        self.cargas['hemorragia'] -= 1
                if self.cargas['quemado'] > 0:
                    if self.cargas['quemado'] > 1:
                        pastooo = randint (1, 3)
                        print ('Además le curas', pastooo,'quemadura/s')
                        self.cargas['quemado'] -= pastooo
                    else:
                        print ('Además le curas 1 quemadura')
                        self.cargas['quemado'] -= 1
                self.energy -= 50
                self.energy += 2
        printdatos(self, enemy)
            
    def energia (self, enemy):
        cargas(self)
        if self.cargas['silenciado'] > 0:
            print (self.name, 'está silenciada y no puede curarse')
            self.cargas['silenciado'] -= 1
            return
        elif self.cargas['paralizado'] > 0:
            paraliza = randint (0, 100)
            if paraliza <= 40:
                print (self.name, 'está paralizado y no puede hacer nada')
                self.cargas['paralizado'] -= 1
                return
            else:
                print (self.name, 'no se paraliza')
                self.cargas['paralizado'] -= 1
        energiaa = randint(0, 100)
        if energiaa > self.precienergia: 
            print (self.name, 'falla la canalización!')
            self.energy + 3
        else:
            print (self.name, 'canaliza y recupera,', 60 * self.power,'de energía')
            if self.tipo == 0:
                self.energy += 4 * self.power
                self.energy += 2
            elif self.tipo == 1:
                self.energy += 60 * self.power
                self.energy += 2
            elif self.tipo == 2:
                self.energy += 60 * self.power
                self.energy += 3
            elif self.tipo == 3 or self.tipo == 4:
                self.energy += 80 * self.power
                self.energy += 4
            elif self.tipo == 5:
                self.energy += 100 * self.power
                self.energy += 5
        printdatos(self, enemy)

    def energiar (self, enemy):
        cargas(self)
        if self.cargas['silenciado'] > 0:
            print (self.name, 'está silenciada y no puede curarse')
            self.cargas['silenciado'] -= 1
            return
        elif self.cargas['paralizado'] > 0:
            paraliza = randint (0, 100)
            if paraliza <= 40:
                print (self.name, 'está paralizado y no puede hacer nada')
                self.cargas['paralizado'] -= 1
                return
            else:
                print (self.name, 'no se paraliza')
                self.cargas['paralizado'] -= 1
        energiaa = randint(0, 100)
        if energiaa > self.precienergia: 
            print (self.name, 'falla la canalización!')
            self.energy + 3
        else:
            print (self.name, 'canaliza y recupera', 80 * self.power, 'de energía para', enemy.name)
            enemy.energy += 80 * self.power
            self.energy += 3
        printdatos(self, enemy)

    def _robovida_clamp(self):
        self.robovida = max(0, min(1, self.robovida))

    def _aplicar_robovida(self, dano):
        self._robovida_clamp()
        robado = dano * self.robovida
        if robado != 0:
            print(self.name, 'roba', robado, 'de vida')
            self.health += robado

    def _check_paralizado(self):
        """Devuelve True si puede actuar, False si queda paralizado."""
        if self.cargas['paralizado'] > 0:
            paraliza = randint(0, 100)
            self.cargas['paralizado'] -= 1
            if paraliza <= 40:
                print(self.name, 'está paralizado y no puede hacer nada')
                return False
            else:
                print(self.name, 'no se paraliza')
        return True

    def _check_inmovilizado(self):
        """Devuelve True si puede moverse, False si está inmovilizado."""
        if self.cargas['inmovilizado'] > 0:
            print(self.name, 'está inmovilizado y no puede atacar')
            self.cargas['inmovilizado'] -= 1
            return False
        return True

    def _puede_usar(self, coste_energia, indice_cooldown=None, requiere_no_silenciado=False, requiere_moverse=False):
        """
        Comprueba si una habilidad puede usarse sin modificar nada.
        requiere_moverse=True → también comprueba inmovilizado (ataques melé/físicos).
        """
        if requiere_no_silenciado and self.cargas['silenciado'] > 0:
            return False
        if requiere_moverse and self.cargas['inmovilizado'] > 0:
            return False
        if self.energy <= coste_energia:
            return False
        if indice_cooldown is not None and self.cooldown[indice_cooldown] > campo.nturnos:
            return False
        return True

    def turnoIA(self, enemy):
        """Punto de entrada IA. Gestiona estados comunes y delega en _elegir_accion_IA."""
        if self.health <= 0:
            return
        if not self.canplay(enemy):
            return

        cargas(self)

        # Silenciado: descuenta y sigue (puede usar ataques físicos)
        if self.cargas['silenciado'] > 0:
            self.cargas['silenciado'] -= 1

        # Paralizado: puede bloquear el turno
        if not self._check_paralizado():
            return

        self._elegir_accion_IA(enemy)

    def _elegir_accion_IA(self, enemy):
        """Cada subclase sobreescribe este método con su propia prioridad."""
        pass


    def printinfo(self, enemy):
        print ('La precisión del ataque uno es de: ', self.preci1, '%')
        print ('La precisión del ataque dos es de: ', self.preci1, '%')
        print ('La precisión del ataque tres es de: ', self.preci3, '%')
        print ('La precisión de la cura es de: ', self.precicura, '%')
        print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
        print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
        print ('La cura recibida es de:', self.rcura * 100, '%')
        print ('La cantidad de sangre es de', self.sangre,'/100')
        print ('Robas', self.robovida * 100, '% de vida')
        print ('La locura es del:', self.locura,'%')
        print ('Estás inmovilizado por', self.cargas['inmovilizado'], 'turnos')
        print ('Reflejas un', self.reflejar,'% del daño recibido')
        print ('Estás invisible por', self.invisible, 'turnos')

class Warrior (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Guerrero')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "tajo", inflige 30 de daño, cuesta 2 de energía, tiene un', self.preci1,'% precisión y un 70% de probabilidades de infligir un sangrado en su enemigo')
        print ('Ataque 2: "estocada", inflige 101 de daño, cuesta 45 de energía y tiene un', self.preci2,'% precisión')
        if self.mutado == 0:
            print ('Ataque super: "Caballero", aplica un escudo a tu objetivo (puedes autotirartelo) que aumenta tu vida en 120 y tu defensa en 0.2 (no afecta el poder), cuesta 60 de energía, tiene un', self.preci3,'% precisión y 2 turnos de cooldown')
        elif self.mutado == 1:
            print ('Ataque super: "Furia", aumentas tu poder en 4 por un turno, cuesta 60 de energía, tiene un', self.preci3,'% precisión y 3 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene un', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y tiene un', self.precienergia,'% precisión')
        if self.mutado == 0:
            print ('Habilidad pasiva: "juicio final", al principio de cada turno aumenta su poder en 0.05')
        elif self.mutado == 1:
            print ('Habilidad pasiva: "juicio final", al principio de cada turno aumenta su defensa en 0.025')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un valiente guerrero llega a la arena, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for warriorrr in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del guerrero:')
                    if self.mutado == 0:
                        self.power += 0.05
                    elif self.mutado == 1:
                        self.defense += 0.025
                    if turn.lower() == 'tajo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 2:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoo = randint (0,100)
                        if unoo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 1
                            
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                sng = randint (0, 100)
                                dano = 30 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, True)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Un potenete tajo le hace una brecha en la piel del enemigo que inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                if sng <= 70:
                                    print (self.name, 'inflige un sangrado en', enemy.name)
                                    enemy.cargas['sangrado'] += 1
                                self.energy -= 2
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    sng = randint (0, 100)
                                    print ('A causa de su locura ', self.name,' se hace un tajo en el brazo que le hece', 30 * self.power / self.defense, 'de daño')
                                    if sng <= 70:
                                        print (self.name, 'se auto-inflige un sangrado en', enemy.name)
                                        self.cargas['sangrado'] += 1
                                    self.health -= 30 * self.power / self.defense
                                    self.energy -= 2
                                    self.energy += 2
                                else:
                                    sng = randint (0, 100)
                                    dano = 30 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Un potenete tajo le hace una brecha en la piel del enemigo que inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    if sng <= 70:
                                        print (self.name, 'inflige un sangrado en', enemy.name)
                                        enemy.cargas['sangrado'] += 1
                                    enemy.health -= 10 * self.power / enemy.defense
                                    self.energy -= 2
                                    
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'estocada':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 45:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doos = randint(0, 100)
                        if doos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 17
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 101 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, True)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Una increíble estocada atraviesa al enemigo y le inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                self.energy -= 45
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Una terrible locura invade a ', self.name,'lo que lo lleva a atravezarse con su propia espada infligiedose', 101 * self.power / self.defense, 'de daño')
                                    self.health -= 101 * self.power / self.defense
                                    self.energy -= 45
                                    
                                    self.energy += 2
                                else:
                                    dano = 101 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una increíble estocada atraviesa al enemigo y le inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.energy -= 45
                                    
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'caballero' and self.mutado == 0:
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está stuneado y no llega a coger el escudo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        trees = randint(0, 100)
                        if trees > self.preci3: 
                            print ('¡El escudo se estropea!')
                            self.energy -= 30
                            
                            self.energy += 2
                        else:
                            print ('Coges un escudo de tu caballo que cubre', 160 * self.power ,'de daño en', enemy.name, 'y aumenta su defensa en 0.2')
                            for i in range (0, 4):
                                if enemy.efecto[i] == '':
                                    enemy.efecto[i] = 'escudo'
                                    enemy.efecton[i] = enemy.health
                                    enemy.tiempo[i] = campo.nturnos + 3
                                    enemy.health += 160 * self.power
                                    break
                            enemy.defense += 0.2
                            self.energy -= 60
                            self.energy += 2
                        self.cooldown[2] = campo.nturnos + 3
                        printdatos(self, enemy)
                    elif turn.lower() == 'furia' and self.mutado == 1:
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está stuneado y no llega a coger el escudo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        trees = randint(0, 100)
                        if trees > self.preci3: 
                            print ('¡Te apaciguas!')
                            self.energy -= 30
                            self.energy += 2
                        else:
                            print ('Te enfureces y aumentas tu poder en 4 por 1 turno')
                            for i in range (0, 4):
                                if self.efecto[i] == '':
                                    self.efecto[i] = 'apower'
                                    self.efecton[i] = 4
                                    self.tiempo[i] = campo.nturnos + 2
                                    self.power += 4
                                    break
                            self.energy -= 60
                            self.energy += 2
                        self.cooldown[2] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower () == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad caballero se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
        
    def _ia_caballero_o_furia(self, enemy):
        if not self._puede_usar(60, 2, requiere_no_silenciado=True):
            return False
        if self.mutado == 0:
            self.power += 0.05  # pasiva juicio final
        elif self.mutado == 1:
            self.defense += 0.025
        hit = randint(0, 100)
        if hit > self.preci3:
            print(self.name, 'falla la super!')
            self.energy += -30 + 2
        else:
            if self.mutado == 0:
                print(self.name, 'aplica escudo a', enemy.name, ', le da', 160 * self.power, 'de vida y +0.2 defensa')
                for i in range(4):
                    if enemy.efecto[i] == '':
                        enemy.efecto[i] = 'escudo'; enemy.efecton[i] = enemy.health
                        enemy.tiempo[i] = campo.nturnos + 3; enemy.health += 160 * self.power; break
                enemy.defense += 0.2
            else:
                print(self.name, 'entra en furia, aumenta su poder en 4 por 1 turno')
                for i in range(4):
                    if self.efecto[i] == '':
                        self.efecto[i] = 'apower'; self.efecton[i] = 4
                        self.tiempo[i] = campo.nturnos + 2; self.power += 4; break
            self.energy += -60 + 2
        self.cooldown[2] = campo.nturnos + (3 if self.mutado == 0 else 4)
        printdatos(self, enemy)
        return True

    def _ia_estocada(self, enemy):
        if not self._puede_usar(45, 1, requiere_no_silenciado=True, requiere_moverse=True):
            return False
        if self.mutado == 0: self.power += 0.05
        elif self.mutado == 1: self.defense += 0.025
        hit = randint(0, 100)
        if hit > self.preci2:
            print(self.name, 'falla la estocada!')
            self.energy += -17 + 2
        else:
            if self.locura > 0 and randint(1, 100) < self.locura:
                dano = 101 * self.power / self.defense
                print('La locura lleva a', self.name, 'a atravesarse con su espada, se inflige', dano, 'de daño')
                self.health -= dano
            else:
                dano = 101 * self.power / enemy.defense
                if enemy.cargas['invencible'] == 1: dano = 0
                reflejo = dano * enemy.reflejar
                dano_total = dano - reflejo
                enemy.health -= dano_total
                self.health -= reflejo
                self._aplicar_robovida(dano_total)
                print(self.name, 'clava una estocada en', enemy.name, ', le inflige', dano_total, 'de daño')
            self.energy += -45 + 2
        printdatos(self, enemy)
        return True

    def _ia_tajo(self, enemy):
        if not self._puede_usar(2, requiere_moverse=True):
            return False
        if self.mutado == 0: self.power += 0.05
        elif self.mutado == 1: self.defense += 0.025
        hit = randint(0, 100)
        if hit > self.preci1:
            print(self.name, 'falla el tajo!')
            self.energy += -1 + 2
        else:
            if self.locura > 0 and randint(1, 100) < self.locura:
                dano = 30 * self.power / self.defense
                sng = randint(0, 100)
                print('La locura lleva a', self.name, 'a hacerse un tajo, se inflige', dano, 'de daño')
                self.health -= dano
                if sng <= 70: self.cargas['sangrado'] += 1
            else:
                dano = 30 * self.power / enemy.defense
                if enemy.cargas['invencible'] == 1: dano = 0
                reflejo = dano * enemy.reflejar
                dano_total = dano - reflejo
                enemy.health -= dano_total
                self.health -= reflejo
                self._aplicar_robovida(dano_total)
                sng = randint(0, 100)
                print(self.name, 'da un tajo a', enemy.name, ', le inflige', dano_total, 'de daño')
                if sng <= 70:
                    print(self.name, 'inflige un sangrado en', enemy.name)
                    enemy.cargas['sangrado'] += 1
            self.energy += -2 + 2
        dacac(self, enemy)
        printdatos(self, enemy)
        return True

    def _elegir_accion_IA(self, enemy):  # Warrior
        # Super: caballero buffea al aliado más débil (soporte), furia se la usa a sí mismo
        if self._ia_caballero_o_furia(enemy): return
        # Ataque 2
        if self._ia_estocada(enemy): return
        # Ataque básico con límite de att1
        if self.att1 >= 3:
            self.att1 = 0
            super().energia(enemy)
            return
        if self._ia_tajo(enemy):
            self.att1 += 1
            return
        super().energia(enemy)

tank = Warrior ('Kenric', 2500, 120, 0.95, 1.2, 42, 100, 95, 95, 100, 100, 1, 1, 0, 0, 0, 60, 0, 0, 'DPS', 4)
guerrero = Warrior ('Kenric', 1740, 130, 1.2, 0.975, 42, 100, 120, 95, 100, 100, 1, 1, 1, 0, 0, 30, 0, 0, 'DPS', 3)

class Magician (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Mago')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "orbe", inflige 72 de daño, cuesta 4 de energía, tiene', self.preci1,'% precisión y un 25% de probabilidades de congelar al enemigo 1 turno')
        print ('Ataque 2: "Fuerza", aumenta tu poder en 0.2 (no afecta el poder) y aumenta tu precición de super en 1%, cuesta 60 de energía y tiene', self.preci2,'% precisión')
        print ('Ataque super: "Tornado fuego", inflige 800 de daño verdadero durante 4 turnos, cuesta 150 de energía, tiene', self.preci3,'% precisión, 6 turnos de cooldown y aplica dos quemaduras en tu enemigo')
        print ('Poción curativa: "cura", cura 100 de vida, cura 1-2 hemorragia y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "frenesí", tiene un 40% de probabilidades de lanzar un segundo ataque 1')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un mago se teletransporta a la arena, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for magiciannn in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del mago:')
                    if turn.lower() == 'orbe':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 4:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla el golpe!')
                            self.energy -= 2
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                dano = 72 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, False)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Un orbe impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                orbeee = randint (1,100)
                                if orbeee <= 25:
                                    print (self.name, 'congela a', enemy.name, '1 turno')
                                    enemy.cargas['hielo'] += 1
                                self.energy -= 4
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                                seconddd = randint (1,100)
                                if seconddd <= 40:
                                    dano = 72 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, False)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Un segundo orbe impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    orbeee = randint (1,100)
                                    if orbeee <= 25:
                                        print (self.name, 'congela a', enemy.name, '1 turno')
                                        enemy.cargas['hielo'] += 1
                                    self.energy -= 4
                                    
                                    self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Debido a tu locura te lanzas un orbe que te inflige', 72 * self.power / self.defense, 'de daño')
                                    orbeee = randint (1,100)
                                    if orbeee <= 25:
                                        print (self.name, 'se auto-congela 1 turno')
                                        self.cargas['hielo'] += 1
                                    self.health -= 72 * self.power / self.defense
                                    self.energy -= 4
                                    
                                    self.energy += 4
                                    seconddd = randint (1,100)
                                    if seconddd <= 30:
                                        print ('Un segundo orbe impacta sobre ti, te inflige', 72 * self.power / self.defense, 'de daño')
                                        orbeee = randint (1,100)
                                        if orbeee <= 25:
                                            print (self.name, ' se auto-congela 1 turno')
                                            self.cargas['hielo'] += 1
                                        self.health -= 72 * self.power / self.defense
                                        self.energy -= 4
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                else:
                                    dano = 72 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, False)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Un orbe impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    orbeee = randint (1,100)
                                    if orbeee <= 25:
                                        print (self.name, 'congela a', enemy.name, '1 turno')
                                        enemy.cargas['hielo'] += 1
                                    self.energy -= 4
                                    
                                    self.energy += 4
                                    seconddd = randint (1,100)
                                    if seconddd <= 40:
                                        dano = 72 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, False)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Un segundo orbe impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        orbeee = randint (1,100)
                                        if orbeee <= 25:
                                            print (self.name, 'congela a', enemy.name, '1 turno')
                                            enemy.cargas['hielo'] += 1
                                        self.energy -= 4
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                            else:
                                print ('ERROR')
                        printdatos(self, enemy)
                    elif turn.lower() == 'fuerza':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0: 
                            print (self.name, 'está silenciado y no puede tomarse la poción')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        dooos = randint(1, 100)
                        if dooos > self.preci2: 
                            print ('¡Se rompe la poción!')
                            self.energy -= 30
                            self.energy += 4
                        else:
                            print (self.name, 'toma un poción que aumenta su poder en 0.2 y la precisión del super en', 1 * self.power)
                            self.preci3 += 1 * self.power
                            self.power += 0.2
                            self.energy -= 60
                            self.energy += 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'tornado fuego':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 150:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'falla el golpe!')
                            self.energy -= 75
                            
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                print (self.name, 'usa todas sus fuerzas e invoca un tornado ígneo quemando a', enemy.name +', que recibirá 600 de daño durante 6 turnos y creandole 2 quemaduras')
                                for i in range (0, 4):
                                    if enemy.efectod[i] == '':
                                        enemy.efectod[i] = 'daño'
                                        enemy.efectodn[i] = 200
                                        enemy.tiempod[i] = campo.nturnos + 4
                                        break
                                enemy.cargas['quemado'] += 2
                                self.energy -= 150
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, 'usa todas sus fuerzas e invoca un tornado ígneo sobre si mismo debido a su locura, quemadose de manera que rebirirá 600 de daño durante 6 turnos y creadose 2 quemaduras')
                                    for i in range (0, 4):
                                        if self.efectod[i] == '':
                                            self.efectod[i] = 'daño'
                                            self.efectodn[i] = 200
                                            self.tiempod[i] = campo.nturnos + 4
                                            break
                                    self.cargas['quemado'] += 2
                                    self.energy -= 150
                                    self.energy += 4
                                else:
                                    print (self.name, 'usa todas sus fuerzas e invoca un tornado ígneo quemando a', enemy.name +', que recibirá 600 de daño durante 6 turnos y creandole 2 quemaduras')
                                    for i in range (0, 4):
                                        if enemy.efectod[i] == '':
                                            enemy.efectod[i] = 'daño'
                                            enemy.efectodn[i] = 200
                                            enemy.tiempod[i] = campo.nturnos + 4
                                            break
                                    enemy.cargas['quemado'] += 2
                                    self.energy -= 150
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        self.cooldown[2] = campo.nturnos + 7
                        printdatos(self, enemy)
                    elif turn.lower() == 'cura':
                        super().cura(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad tornado fuego se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
mago = Magician('Gandalf', 1580, 170, 1, 1, 30, 100, 80, 75, 100, 100, 3, 1, 0, 0, 0, 30, 0, 0, 'DPS', 3)

class Hereje (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "flecha", inflige 40 de daño, cuesta 3 de energía, tiene', self.preci1,'% precisión y tiene 20% de probabilidades de infligir una hemorragia en tu enemigo')
        print ('Ataque 2: "flecha vampiro", inflige 110 de daño, te cura 25 de vida (aumentado por la mitad del poder), cuesta 40 de energía,', self.preci2,'% precisión y 1 turno de cooldown')
        print ('Ataque super: "Ira", aumenta tu poder en 1 (no afecta el poder), cuesta 70 de energía, tiene', self.preci3,'% precisión y 1 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía  y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "frenesí", tiene un 40% de probabilidades de lanzar un segundo ataque 1')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Como caído del cielo aparece un hereje arquero, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for herejeee in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del arquero:')
                    if turn.lower() == 'flecha':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 3:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 1.5
                            
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 40 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, False)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                print ('Una flecha se clava en tu enemigo, le inflige', dano_total ,'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                flechaaa = randint (1, 100)
                                if flechaaa <= 20:
                                    enemy.cargas['hemorragia'] += 1
                                    print ('Tras un fuerte flechazo una peligrosa hemorragia surge en', enemy.name)
                                self.energy -= 3
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                                secondd = randint (1,100)
                                if secondd <= 40:
                                    dano = 40 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, False)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una segunda flecha se clava en tu enemigo, le inflige', dano_total ,'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    flechaaaa = randint (1, 100)
                                    if flechaaaa <= 20:
                                        enemy.cargas['hemorragia'] += 1
                                        print ('Tras un fuerte flechazo una peligrosa hemorragia surge en', enemy.name)
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('A causa de la locura', self.name,'se clava una flecha en el pie, se inflige', 40 * self.power / self.defense ,'de daño')
                                    self.health -= 40 * self.power / self.defense
                                    flechaaa = randint (1, 100)
                                    if flechaaa <= 20:
                                        self.cargas['hemorragia'] += 1
                                        print ('Tras el fuerte flechazo una peligrosa hemorragia surge en', self.name)
                                    self.energy -= 3
                                    self.energy += 3
                                    secondd = randint (1,100)
                                    if secondd <= 30:
                                        print ('Una segunda flecha se clava en ti infligiendote', 40 * self.power / self.defense ,'de daño')
                                        self.health -= 40 * self.power / self.defense
                                        flechaaaa = randint (1, 100)
                                        if flechaaaa <= 20:
                                            self.cargas['hemorragia'] += 1
                                            print ('Tras el fuerte flechazo una peligrosa hemorragia surge en', self.name)
                                else:
                                    dano = 40 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, False)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una flecha se clava en tu enemigo, le inflige', dano_total ,'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    flechaaa = randint (1, 100)
                                    if flechaaa <= 20:
                                        enemy.cargas['hemorragia'] += 1
                                        print ('Tras un fuerte flechazo una peligrosa hemorragia surge en', enemy.name)
                                    self.energy -= 3
                                    self.energy += 3
                                    secondd = randint (1,100)
                                    if secondd <= 30:
                                        dano = 40 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, False)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Una segunda flecha se clava en tu enemigo, le inflige', dano_total ,'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        flechaaaa = randint (1, 100)
                                        if flechaaaa <= 20:
                                            enemy.cargas['hemorragia'] += 1
                                            print ('Tras un fuerte flechazo una peligrosa hemorragia surge en', enemy.name)
                            else:
                                print ('ERROR')
                        printdatos(self, enemy)
                    elif turn.lower() == 'flecha vampiro':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 20
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 110 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, False)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Una flecha se clava en tu enemigo, le inflige', dano_total, 'de daño a', enemy.name, '¡Y te cura', 25 * (self.power / 2) * self.lcura * self.rcura,'de vida!')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                self.health += 25 * (self.power / 2) * self.lcura * self.rcura
                                self.energy -= 40
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('A causa de la locura', self.name,'se dispara una flecha en su torso, se inflige', 110 * self.power / self.defense, 'de daño ¡Y te cura', 25 * (self.power / 2) * self.lcura * self.rcura,'de vida!')
                                    self.health -= 110 * self.power / self.defense
                                    self.health += 25 * (self.power / 2) * self.lcura * self.rcura
                                    self.energy -= 40
                                    self.energy += 3
                                else:
                                    dano = 110 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, False)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una flecha se clava en tu enemigo, le inflige', dano_total, 'de daño a', enemy.name, '¡Y te cura', 25 * (self.power / 2) * self.lcura * self.rcura,'de vida!')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.health += 25 * (self.power / 2) * self.lcura * self.rcura
                                    self.energy -= 40
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown[1] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'ira':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar enfurecerse')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 35
                            
                            self.energy += 3
                        else:
                            print (self.name, 'se enfurece y aumenta su poder en uno, ¡', enemy.name, 'apurate en matarlo!!')
                            self.power += 1
                            self.energy -= 70
                            self.energy += 3
                        self.cooldown[2] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad ira se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
arquero = Hereje('Alaric', 1700, 145, 1, 1, 59, 100, 80, 75, 100, 100, 2, 1, 0, 0, 0, 0, 0, 0, 'DPS', 2)

class Maldi (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Mago')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "mal", inflige 22 de daño y aplica una maldición al objetivo (máximo 4) y si tiene quitas una cargas de cura a tu objetivo, cuesta 10 de energía y tiene', self.preci1,'% precisión')
        print ('Ataque 2: "perforador oscuro", inflige 120 de daño y reduce la defensa del enemigo en 0.4 por 2 turnos, cuesta 55 de energía, tiene', self.preci2,'% precisión y 3 turnos de cooldown')
        print ('Ataque super: "Diablo", inflige 100 | 150 | 250 | 500 | 800 de daño después de 2 turnos dependiendo de la cantidad de maldiciones que tenga el enemigo en el momento del daño (afecta el poder del momento del lanzamiento y la defensa cuando se inflige el daño), cuesta 80 de energía, consume todas las maldiciones del enemigo, tiene', self.preci3,'% precisión, 3 turnos de cooldown y quita todas las cargas de cura de tu enemigo')
        print ('Poción curativa: "cura", cura 100 de vida, cura 1-2 hemorragia y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "maestro de pociones" al lanzar un ataque 1 tiene un 50% de posibilidades de envenenar a su objetivo')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Salido de la oscuridad, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for maldiii in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del mago maldito:')
                    if turn.lower() == 'mal':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                return
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unooooo = randint(0, 100)
                        if unooooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 5
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                dano = 22 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, False)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                print ('una ola de mal inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                enemy.cargas['maldita'] += 1
                                if enemy.cargas['cura'] > 0:
                                    enemy.cargas['cura'] -= 1
                                if enemy.cargas['maldita'] >= 5:
                                    enemy.cargas['maldita'] = 4
                                venenoo = randint (1, 100)
                                if venenoo <= 50:
                                    print ('Además', self.name, 'lanza una pocion venenosa a', enemy.name, 'y lo envenena')
                                    enemy.cargas['veneno'] += 1
                                if venenoo == 100:
                                    print ('Además', self.name, 'lanza una pocion venenosa concentrada a', enemy.name, 'y lo envenena (dos carga de veneno)')
                                    enemy.cargas['veneno'] += 2
                                self.energy -= 10
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Una ola de mal inflige', 22 * self.power / self.defense, 'de daño a', self.name, 'debido a su locura')
                                    self.health -= 22 * self.power / self.defense
                                    self.cargas['maldita'] += 1
                                    if self.cargas['cura'] > 0:
                                        self.cargas['cura'] -= 1
                                    if self.cargas['maldita'] >= 5:
                                        self.cargas['maldita'] = 4
                                    venenoo = randint (1, 100)
                                    if venenoo <= 50:
                                        print ('Además', self.name, 'se toma una pocion venenosa debido a su locura y se envenena')
                                        self.cargas['veneno'] += 1
                                    if venenoo == 100:
                                        print ('Además', self.name, 'se toma una pocion venenosa concentrada debido a su locura y se envenena (dos carga de veneno)')
                                        self.cargas['veneno'] += 2
                                    self.energy -= 10
                                    self.energy += 4
                                else:
                                    dano = 22 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, False)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('una ola de mal inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    enemy.cargas['maldita'] += 1
                                    if enemy.cargas['cura'] > 0:
                                        enemy.cargas['cura'] -= 1
                                    if enemy.cargas['maldita'] >= 5:
                                        enemy.cargas['maldita'] = 4
                                    venenoo = randint (1, 100)
                                    if venenoo <= 50:
                                        print ('Además', self.name, 'lanza una pocion venenosa a', enemy.name, 'y lo envenena')
                                        enemy.cargas['veneno'] += 1
                                    if venenoo == 100:
                                        print ('Además', self.name, 'lanza una pocion venenosa concentrada a', enemy.name, 'y lo envenena (dos carga de veneno)')
                                        enemy.cargas['veneno'] += 2
                                    self.energy -= 10
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        printdatos(self, enemy)
                    elif turn.lower() == 'perforador oscuro':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        dooooos = randint(0, 100)
                        if dooooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            
                            self.energy += 4
                        else:
                            if self.locura <= 0:
                                dano = 120 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, False)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Perforas a tu enemigo infligiendo 120 de daño y reduciendo su defensa en 0.4 por 2 turnos')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                for i in range (0, 4):
                                    if enemy.efecto[i] == '':
                                        enemy.efecto[i] = 'bdefense'
                                        enemy.efecton[i] = 0.4
                                        enemy.tiempo[i] = campo.nturnos + 2
                                        enemy.defense -= 0.4
                                        break
                                self.energy -= 30
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    dano = 120 * self.power / enemy.defense
                                    if self.cargas['invencible'] == 1:
                                        dano = 0
                                    print ('Perforas a tu enemigo infligiendo 120 de daño y reduciendo su defensa en 0.4 por 2 turnos')
                                    self.health -= dano
                                    for i in range (0, 4):
                                        if self.efecto[i] == '':
                                            self.efecto[i] = 'bdefense'
                                            self.efecton[i] = 0.3
                                            self.tiempo[i] = campo.nturnos + 2
                                            self.defense -= 0.3
                                            break
                                    self.energy -= 30
                                    self.energy += 4
                                else:
                                    dano = 120 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, False)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Perforas a tu enemigo infligiendo 120 de daño y reduciendo su defensa en 0.4 por 2 turnos')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    for i in range (0, 4):
                                        if enemy.efecto[i] == '':
                                            enemy.efecto[i] = 'bdefense'
                                            enemy.efecton[i] = 0.3
                                            enemy.tiempo[i] = campo.nturnos + 2
                                            enemy.defense -= 0.3
                                            break
                                    self.energy -= 30
                                    self.energy += 4
                        self.cooldown[1] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'diablo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 80:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeeees = randint(0, 100)
                        if treeeees > self.preci3:
                            print (self.name, 'falla el golpe!')
                            self.energy -= 40
                            
                            self.energy += 4
                            enemy.cargas['maldita'] == 0
                        else:
                            if self.locura <= 0:
                                print (self.name, 'invoca el diablo sobre', enemy.name)
                                for i in range (0, 4):
                                    if enemy.efecto[i] == '':
                                        enemy.efecto[i] = 'diablo'
                                        enemy.efecton[i] = self.power
                                        enemy.tiempo[i] = campo.nturnos + 2
                                        break
                                    self.energy -= 80
                                    self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, 'invoca el diablo pero este se vuelve contra él y le maldice')
                                    for i in range (0, 4):
                                        if self.efecto[i] == '':
                                            self.efecto[i] = 'diablo'
                                            self.efecton[i] = self.power
                                            self.tiempo[i] = campo.nturnos + 2
                                            break
                                    self.energy -= 80
                                    self.energy += 4
                                else:
                                    print (self.name, 'invoca el diablo sobre', enemy.name)
                                    for i in range (0, 4):
                                        if enemy.efecto[i] == '':
                                            enemy.efecto[i] = 'diablo'
                                            enemy.efecton[i] = self.power
                                            enemy.tiempo[i] = campo.nturnos + 2
                                            break
                                    self.energy -= 80
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        self.cooldown[2] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'cura':
                        super().cura(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad perforador oscuro se puede volver a lanzar en el turno', self.cooldown[1])
                            print ('La habilidad diablo se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
maldito = Maldi ('Drago', 1530, 180, 1, 1, 16, 89, 79, 99, 100, 100, 3, 1, 0, 0, 0, 30, 0, 0, 'DPS', 3)

class Thief (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "daga", golpea un nuemero aleatorio de veces del 0 al 5, 1º golpe hace 45 de daño, 2º golpe roba 5 de vida, 3º golpe aumenta tu poder en 0.1, 4º golpe infliges una carga venenosa, 5º golpe haces 80 de daño extra, cuesta 10 de energía y tiene', self.preci1,'% precisión')
        print ('Ataque 2: "sangrado", inflije daño en función de la vida restante del enemigo 300-<50% 50-<100%, cuesta 16 de energía, tiene', self.preci2,'% precisión y 2 turnos de cooldown')
        print ('Ataque super: "energia para mi", roba 50 de energia al rival (no afecta el poder), cuesta 30 de energía, tiene ', self.preci3,'% precisión y 2 turnos de cooldown (si tras el ataque tu enemigo se queda con energia negativa perderá 400 de vida)')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "suerte de principiante", si el primer ataque es "daga" da 5 golpes asegurado y empieza invisible por 3 turnos')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Con una reluciente daga, el ladrón  ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for thiefff in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del ladrón:')
                    if turn.lower() == 'daga':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoooooo = randint(0, 100)
                        if unoooooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 5
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                if campo.nturnos == 1:
                                    self.power += 0.1
                                    dano = 125 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una daga se clava en', enemy.name, '5 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    enemy.cargas['veneno'] += 1
                                    self.energy -= 10
                                    self.energy += 3
                                    printdatos(self, enemy)
                                    break
                                dddd = randint (0, 5)
                                if dddd == 0:
                                    print (enemy.name, 'esquiva la daga y sobrevive')
                                
                                elif dddd == 1:
                                    dano = 45 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una daga se clava en', enemy.name, ' 1 vez y le inflijes', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.energy -= 10
                                
                                elif dddd == 2:
                                    dano = 45 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una daga se clava en', enemy.name, ' 2 veces, le inflijes', dano_total, 'de daño y le robas', 5 * self.power * self.lcura * self.rcura, 'de vida')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    self.energy -= 10
                                    
                                elif dddd == 3:
                                    self.power += 0.1
                                    dano = 45 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una daga se clava en', enemy.name, ' 3 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida y te enfureces aumentando tu poder en 0,1')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    self.energy -= 10

                                elif dddd == 4:
                                    self.power += 0.1
                                    dano = 45 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una daga se clava en', enemy.name, ' 4 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    enemy.cargas['veneno'] += 1
                                    self.energy -= 10

                                elif dddd == 5:
                                    self.power += 0.1
                                    dano = 125 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Una daga se clava en', enemy.name, ' 5 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    enemy.cargas['veneno'] += 1
                                    self.energy -= 10
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    if campo.nturnos == 1:
                                        self.power += 0.1
                                        print ('La daga de', self.name, 'toma vida propia rebeladose y le apuñala 5 veces, infligiedose', 125 * self.power / self.defense, 'de daño, te robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y te envenenas')
                                        self.health -= 125 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.cargas['veneno'] += 1
                                        self.energy -= 10
                                        self.energy += 3
                                        printdatos(self, enemy)
                                        break
                                    dddd = randint (0, 5)
                                    if dddd == 0:
                                        print (self.name, 'se vuelve loco y se intenta apuñalar, afortunadamente esquiva la daga y sobrevive')
                                    elif dddd == 1:
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 1 vez y infligiedose', 45 * self.power / self.defense, 'de daño')
                                        self.health -= 45 * self.power / self.defense
                                        self.energy -= 10
                                    elif dddd == 2:
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 2 veces y infligiedose', 45 * self.power / self.defense, 'de daño y se robas', 5 * self.power * self.lcura * self.rcura, 'de vida')
                                        self.health -= 45 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.energy -= 10
                                    elif dddd == 3:
                                        self.power += 0.1
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 3 veces y infligiedose', 45 * self.power / self.defense, 'de daño, se robas', 5 * self.power * self.lcura * self.rcura, 'de vida y te enfureces aumentando tu poder en 0,1')
                                        self.health -= 45 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.energy -= 10
                                    elif dddd == 4:
                                        self.power += 0.1
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 4 veces y infligiedose', 45 * self.power / self.defense, 'de daño, se robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y se envenenas')
                                        self.health -= 45 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.cargas['veneno'] += 1
                                        self.energy -= 10
                                    elif dddd == 5:
                                        self.power += 0.1
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 5 veces y infligiedose', 125 * self.power / self.defense, 'de daño, se robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y se envenenas')
                                        self.health -= 125 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.cargas['veneno'] += 1
                                        self.energy -= 10
                                    
                                    self.energy += 3
                                else:
                                    if campo.nturnos == 1:
                                        self.power += 0.1
                                        dano = 125 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Una daga se clava en', enemy.name, '5 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        enemy.cargas['veneno'] += 1
                                        self.energy -= 10
                                        self.energy += 3
                                        printdatos(self, enemy)
                                        break
                                    dddd = randint (0, 5)
                                    if dddd == 0:
                                        print (enemy.name, 'esquiva la daga y sobrevive')
                                    
                                    elif dddd == 1:
                                        dano = 45 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Una daga se clava en', enemy.name, ' 1 vez y le inflijes', dano_total, 'de daño')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.energy -= 10
                                    
                                    elif dddd == 2:
                                        dano = 45 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Una daga se clava en', enemy.name, ' 2 veces, le inflijes', dano_total, 'de daño y le robas', 5 * self.power * self.lcura * self.rcura, 'de vida')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.energy -= 10
                                    
                                    elif dddd == 3:
                                        self.power += 0.1
                                        dano = 45 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Una daga se clava en', enemy.name, ' 3 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida y te enfureces aumentando tu poder en 0,1')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.energy -= 10

                                    elif dddd == 4:
                                        self.power += 0.1
                                        dano = 45 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Una daga se clava en', enemy.name, ' 4 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        enemy.cargas['veneno'] += 1
                                        self.energy -= 10

                                    elif dddd == 5:
                                        self.power += 0.1
                                        dano = 125 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Una daga se clava en', enemy.name, ' 5 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        enemy.cargas['veneno'] += 1
                                        self.energy -= 10
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'sangrado':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede correr')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 35:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooooos = randint(0, 100)
                        if doooooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 10
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                if enemy.health <= enemy.maxhealth / 2:
                                    dano = 300 * self.power / enemy.defense
                                else:
                                    dano = 50 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Atacas sobre la herida de', enemy.name + ', infligiendole', dano_total, 'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    if self.health <= self.maxhealth / 2:
                                        dano = 300 * self.power / self.defense
                                    else:
                                        dano = 50 * self.power / self.defense
                                    if self.cargas['invencible'] == 1:
                                        dano = 0
                                    self.health -= dano
                                    print ('Te vuelves loco y te clavas tu propia daga sobre una de tus heridas, infligiendote', dano, 'de daño')
                                else:
                                    if enemy.health <= enemy.maxhealth / 2:
                                        dano = 300 * self.power / enemy.defense
                                    else:
                                        dano = 50 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Atacas sobre la herida de', enemy.name + ', infligiendole', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                            self.energy -= 20
                            self.energy += 3
                        self.cooldown[1] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'energia para mi':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar el hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 20:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeeeees = randint(0, 100)
                        if treeeeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 20
                            self.energy += 3
                        else:
                            print ('¡',self.name, 'saca algo de su mochila! Saca un libro de encantamientos... (', self.name,': ¡robado!) conjura un hechizo y le roba 60 de energia a', self.name)
                            enemy.energy -= 50
                            self.energy += 50
                            self.energy -= 30
                            if enemy.energy < 0:
                                enemy.health -= 400
                            self.energy += 3
                        self.cooldown[2] = campo.nturnos + 3
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad energia para mi se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
robador = Thief('Leoric', 1850, 160, 1, 1, 65, 120, 85, 70, 80, 100, 2, 1, 0, 0, 0, 30, 0, 3, 'DPS', 3)

class Shapeshifter (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci11, preci2, preci22, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        self.preci11 = preci11
        self.preci22 = preci22
        self.carga_cambiaforma = 0
        self.carga_pantera = 0
        self.pantera = 0
    def print_info(self):
        print ('Tipo: Mago')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "rayo energia"(humano), inflige 50 de daño, cuesta 25 de energía, tiene', self.preci1,'% precisión y te da una carga de cambiaforma (Máx. 5)//"zarpazo" (pantera), inflige 70 de daño, cuesta 30 de energia, tiene', self.preci11,'% de precisión, si tienes una carga de cambiaformas se gasta y te da una carga de pantera, tras tres cargas de pantera infliges 500 de daño')
        print ('Ataque 2: "escudo"(humano), aplica un escudo a tu objetivo que aumenta su vida en 200 por 3 turnos y su defensa en 0.1 y te da una carga de cambiaforma, cuesta 30 de energía, tiene', self.preci2,'% precisión y 1 turno de cooldown//"salto"(pantera), le inflges 20 de daño, cuesta 40 de energia, tiene', self.preci22,'% de precisión y 2 turnos de cooldown , si tienes una carga de cambiaformas esta se consume y infliges 80 más de daño')
        print ('Ataque super: "transformación", pasa de humano a pantera y viseversa, cuesta 10 de energía, tiene', self.preci3,'% precisión y 2 turnos de cooldown')
        print ('Poción curativa: "cura", cura 100 de vida, cura 1-2 hemorragia y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "Incansable", cuando se transforma recupera su velocidad por defecto')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un cambiaforma se abalanza entre los arboles a la arena, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for shapeshifterrr in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del cambiaformas:')
                    if turn.lower() == 'rayo energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 25:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        if self.pantera == 0:
                            unooooooo = randint(0, 100)
                            if unooooooo > self.preci1: 
                                print ('¡', self.name, 'falla el golpe!')
                                self.energy -= 12.5
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                if self.locura == 0:
                                    dano = 50 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, False)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Un rayo de energía impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.carga_cambiaforma += 1
                                    if self.carga_cambiaforma > 5:
                                        self.carga_cambiaforma = 5
                                    self.energy -= 25
                                    
                                    self.energy += 4
                                elif self.locura > 0 and self.locura <= 100:
                                    locuraaa = randint (1, 100)
                                    if locuraaa < self.locura:
                                        print ('Una gran locura inunde a', self.name, 'y conjura un rayo de energía que impacta en él, se inflige', 50 * self.power / self.defense, 'de daño')
                                        self.health -= 50 * self.power / self.defense
                                        self.carga_cambiaforma += 1
                                        if self.carga_cambiaforma > 5:
                                            self.carga_cambiaforma = 5
                                        self.energy -= 25
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                    else:
                                        dano = 50 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, False)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Un rayo de energía impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.carga_cambiaforma += 1
                                        if self.carga_cambiaforma > 5:
                                            self.carga_cambiaforma = 5
                                        self.energy -= 25
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                else:
                                    print ('ERROR')
                            printdatosshapeshifter(self, enemy)
                        elif self.pantera == 1:
                            
                            self.energy += 4
                            print ('Estás en forma de pantera, no puedes lanzar este ataque')
                            printdatosshapeshifter(self, enemy)
                    elif turn.lower() == 'zarpazo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        if self.pantera == 0:
                            self.energy += 4
                            print ('Estas en forma humana, no puedes lanzar este ataque')
                            printdatosshapeshifter(self, enemy)
                        elif self.pantera == 1:
                            unooooooo = randint(0, 100)
                            if unooooooo > self.preci11: 
                                print ('¡', self.name, 'falla el golpe!')
                                self.energy -= 15
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                if self.locura == 0:
                                    dano = 70 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Un zarpazo inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    if self.carga_cambiaforma > 0:
                                        self.carga_pantera += 1
                                        self.carga_cambiaforma -= 1
                                    if self.carga_pantera >= 3:
                                        dano = 500 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Un gran zarpazo atraviesa a', enemy.name, 'y le inflige', dano_total, 'de daño')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.carga_pantera = 0
                                    self.energy -= 30
                                    self.energy += 4
                                elif self.locura > 0 and self.locura <= 100:
                                    locuraaa = randint (1, 100)
                                    if locuraaa < self.locura:
                                        print ('De la locura', self.name, 'se da un zarpazo a si mismo, infligiedose', 70 * self.power / self.defense, 'de daño')
                                        self.health -= 70 * self.power / self.defense
                                        if self.carga_cambiaforma > 0:
                                            self.carga_pantera += 1
                                            self.carga_cambiaforma -= 1
                                        if self.carga_pantera >= 3:
                                            print ('Un gran zarpazo atraviesa a', self.name, 'y le inflige', 500 * self.power / self.defense, 'de daño')
                                            self.health -= 500 * self.power / self.defense
                                            self.carga_pantera = 0
                                        self.energy -= 30
                                        self.energy += 4
                                    else:
                                        dano = 70 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print ('Un zarpazo inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        if self.carga_cambiaforma > 0:
                                            self.carga_pantera += 1
                                            self.carga_cambiaforma -= 1
                                        if self.carga_pantera >= 3:
                                            dano = 500 * self.power / enemy.defense
                                            if enemy.cargas['invencible'] == 1:
                                                dano = 0
                                            reflejo = dano * enemy.reflejar 
                                            dano_total = dano - reflejo
                                            super().atacar(enemy, dano_total, True)
                                            self.health -= reflejo
                                            if self.robovida > 1:
                                                self.robovida = 1
                                            elif self.robovida < 0:
                                                self.robovida = 0
                                            robado = dano_total * self.robovida
                                            print ('Un gran zarpazo atraviesa a', enemy.name, 'y le inflige', dano_total, 'de daño')
                                            if enemy.reflejar > 0:
                                                print (enemy.name, 'refleja', reflejo, 'de daño')
                                            if robado != 0:
                                                print (self.name, 'roba', robado, 'de vida')
                                                self.health += robado
                                            self.carga_pantera = 0
                                        self.energy -= 30
                                        self.energy += 4
                                else:
                                    print ('ERROR')
                            dacac (self, enemy)
                        printdatosshapeshifter(self, enemy)
                    elif turn.lower() == 'escudo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        if self.pantera == 0:
                            dooos = randint(0, 100)
                            if dooos > self.preci2: 
                                print ('¡Fallas!')
                                self.energy -= 15
                                self.energy += 4
                            else:
                                print (self.name, 'llama a la naturaleza para aplicar un escudo a',enemy.name,'que aumenta su vida en 200 por 3 turnos y su defensa en 0.1, además te da una carga de cambiaforma')
                                for i in range (0, 4):
                                    if enemy.efecto[i] == '':
                                        enemy.efecto[i] = 'escudo'
                                        enemy.efecton[i] = enemy.health
                                        enemy.tiempo[i] = campo.nturnos + 3
                                        enemy.health += 200 * self.power
                                        break
                                enemy.defense += 0.1
                                self.carga_cambiaforma += 1
                                self.energy -= 30
                                self.energy += 4
                            printdatosshapeshifter(self, enemy)
                        elif self.pantera == 1:
                            
                            self.energy += 4
                            print ('Estas en forma de pantera, no puedes lanzar este ataque')
                            printdatosshapeshifter(self, enemy)
                        self.cooldown[1] = campo.nturnos + 2
                    elif turn.lower() == 'salto':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        if self.pantera == 1:
                            dooos = randint(0, 100)
                            if dooos > self.preci22: 
                                print ('¡Fallas!')
                                self.energy -= 20
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                if self.carga_cambiaforma > 0:
                                    danosalto = 100
                                    self.carga_cambiaforma -= 1
                                elif self.carga_cambiaforma == 0:
                                    danosalto = 20
                                if self.locura == 0:
                                    dano = danosalto * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print (self.name, 'se lanza a por', enemy.name, 'infligiendole', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.energy -= 40
                                    self.energy += 4
                                elif self.locura > 0 and self.locura <= 100:
                                    locuraaa = randint (1, 100)
                                    if locuraaa < self.locura:
                                        print (self.name, 'se lanza a por', enemy.name, ', pero de la locura lo confunde con un árbol y se choca contra este infligiedose', danosalto *self.power / self.defense, 'de daño')
                                        self.health -= danosalto * self.power / self.defense
                                        self.energy -= 40
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                    else:
                                        dano = danosalto * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        super().atacar(enemy, dano_total, True)
                                        self.health -= reflejo
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano_total * self.robovida
                                        print (self.name, 'se lanza a por', enemy.name, 'infligiendole', dano_total, 'de daño')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                        self.energy -= 40
                                        self.energy += 4
                                else:
                                    print ('ERROR')
                                dacac (self, enemy)
                            printdatosshapeshifter(self, enemy)
                        elif self.pantera == 0:
                            self.energy += 4
                            print ('Estas en forma humana, no puedes lanzar este ataque')
                            printdatosshapeshifter(self, enemy)
                        self.cooldown[1] = campo.nturnos + 3
                    elif turn.lower() == 'transformacion':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede transformarse')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        trees = randint(1, 100)
                        if trees > self.preci3: 
                            print ('¡', self.name, 'falla el golpe!')
                            self.energy -= 5
                            self.energy += 4
                        else:
                            if self.pantera == 0:
                                print (self.name, 'pasa a ser una pantera')
                                self.pantera += 1
                                self.velocity = 78
                                self.energy -= 10
                                self.energy += 4
                            elif self.pantera == 1:
                                print (self.name, 'pasa a ser un humano')
                                self.pantera -= 1
                                self.carga_pantera = 0
                                self.energy -= 10
                                self.velocity = 32
                                self.energy += 4
                        self.cooldown[2] = campo.nturnos + 3
                        printdatosshapeshifter(self, enemy)
                    elif turn.lower() == 'cura':
                        super().cura(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad transformación se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
pantera = Shapeshifter('Hildegund', 2100, 300, 1, 1, 33, 85, 120, 85, 90, 200, 100, 100, 3, 1, 0, 0, 0, 35, 0, 0, 'DPS', 4)

class Healer (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Maga')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "Heal", cura 1 hemorragia y 100 de vida a tu objetivo y lo purificas quitandole 1 maldición, cuesta 40 de energía, tiene', self.preci1,'% precisión')
        print ('Ataque 2: "Bendecir", aumenta la defensa de tu objetivo en 0.3 y la cura recibida en 0.5 por 2 turnos, cuesta 60 de energía, tiene', self.preci2,'% precisión y 3 turno de cooldown')
        print ('Ataque super: "Proteger", cura a tu objetivo 150 de vida y aumenta su poder y su defensa en 0.1, cuesta 100 de energía, tiene', self.preci3,'% precisión y 3 turnos de cooldown')
        print ('Poción curativa: "cura", cura 100 de vida, cura 1-2 hemorragia y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "Apoyo", puedes dar tu cura a tu objetivo escribiendo "curar", además de poder canalizar para tu objetivo escribiendo "energiar"')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Una curandera aparece en arena, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for healerrr in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno de la curandera:')
                    if turn.lower() == 'heal':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla la cura!')
                            self.energy -= 20
                            
                            self.energy += 4
                        else:
                            print (self.name, 'cura 1 hemorragia y', 100 * self.power * self.lcura * enemy.rcura, 'de vida a tu objetivo y lo purificas quitandole 1 maldición')
                            enemy.health += 100 * self.power * self.lcura * enemy.rcura
                            if enemy.cargas['hemorragia'] > 0:
                                enemy.cargas['hemorragia'] -= 1
                            if enemy.cargas['maldita'] > 0:
                                enemy.cargas['maldita'] -= 1
                            self.energy -= 40
                            
                            self.energy += 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'bendecir':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print (self.name, 'se confunde de hechizo y convierte una hoja de pasto en un gusano')
                            self.energy -= 30
                            self.energy += 4
                        else:
                            print (self.name, 'bendice a', enemy.name, 'aumentando su defensa en 0.3 y cura recibida en 0.5 todo por 2 turnos')
                            if enemy.efecto[0] == '':
                                enemy.efecto[0] = 'adefense'
                                enemy.efecton[0] = 0.3
                                enemy.tiempo[0] = campo.nturnos + 3
                                enemy.defense += 0.3

                            elif enemy.efecto[1] == '':
                                enemy.efecto[1] = 'adefense'
                                enemy.efecton[1] = 0.3
                                enemy.tiempo[1] = campo.nturnos + 3
                                enemy.defense += 0.3

                            elif enemy.efecto[2] == '':
                                enemy.efecto[2] = 'adefense'
                                enemy.efecton[2] = 0.3
                                enemy.tiempo[2] = campo.nturnos + 3
                                enemy.defense += 0.3

                            elif enemy.efecto[3] == '':
                                enemy.efecto[3] = 'adefense'
                                enemy.efecton[3] = 0.3
                                enemy.tiempo[3] = campo.nturnos + 3
                                enemy.defense += 0.3

                            elif enemy.efecto[4] == '':
                                enemy.efecto[4] = 'adefense'
                                enemy.efecton[4] = 0.3
                                enemy.tiempo[4] = campo.nturnos + 3
                                enemy.defense += 0.3

                            if enemy.efecto[0] == '':
                                enemy.efecto[0] = 'arcura'
                                enemy.efecton[0] = 0.5
                                enemy.tiempo[0] = campo.nturnos + 3
                                enemy.rcura += 0.5

                            elif enemy.efecto[1] == '':
                                enemy.efecto[1] = 'arcura'
                                enemy.efecton[1] = 0.5
                                enemy.tiempo[1] = campo.nturnos + 3
                                enemy.rcura += 0.5

                            elif enemy.efecto[2] == '':
                                enemy.efecto[2] = 'arcura'
                                enemy.efecton[2] = 0.5
                                enemy.tiempo[2] = campo.nturnos + 3
                                enemy.rcura += 0.5

                            elif enemy.efecto[3] == '':
                                enemy.efecto[3] = 'arcura'
                                enemy.efecton[3] = 0.5
                                enemy.tiempo[3] = campo.nturnos + 3
                                enemy.rcura += 0.5

                            elif enemy.efecto[4] == '':
                                enemy.efecto[4] = 'arcura'
                                enemy.efecton[4] = 0.5
                                enemy.tiempo[4] = campo.nturnos + 3
                                enemy.rcura += 0.5
                        self.cooldown[1] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'proteger': 
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 100:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treees = randint(1, 100)
                        if treees >= self.preci3: 
                            print ('¡', self.name, 'se equivoca de hechizo y invoca una arañita inofensiva!')
                            self.energy -= 50
                            self.energy += 4
                        else:
                            print (self.name, 'protege a',enemy.name, 'curandole', 300 * self.power * self.lcura * enemy.rcura, 'de vida y aumentandole el poder y la defensa en 0.1')
                            enemy.health += 300 * self.power * self.lcura * enemy.rcura
                            enemy.power += 0.1
                            enemy.defense += 0.1
                            self.energy -= 100
                            self.energy += 4
                        self.cooldown[2] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'cura':
                        super().cura(enemy)
                    elif turn.lower() == 'curar':
                        super().curar(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'energiar':
                        super().energiar(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad proteger se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)

    def _ia_proteger(self, enemy):
        if not self._puede_usar(100, 2, requiere_no_silenciado=True):
            return False
        hit = randint(1, 100)
        if hit >= self.preci3:
            print(self.name, 'falla proteger!')
            self.energy += -50 + 4
        else:
            print(self.name, 'protege a', enemy.name, ', le cura', 300 * self.power * self.lcura * enemy.rcura, 'de vida y +0.1 poder y defensa')
            enemy.health += 300 * self.power * self.lcura * enemy.rcura
            enemy.power += 0.1
            enemy.defense += 0.1
            self.energy += -100 + 4
        self.cooldown[2] = campo.nturnos + 4
        printdatos(self, enemy)
        return True

    def _ia_bendecir(self, enemy):
        if not self._puede_usar(60, 1, requiere_no_silenciado=True):
            return False
        hit = randint(0, 100)
        if hit > self.preci2:
            print(self.name, 'falla bendecir!')
            self.energy += -30 + 4
        else:
            print(self.name, 'bendice a', enemy.name, ', +0.3 defensa y +0.5 cura recibida por 2 turnos')
            for efx, val, attr in [('adefense', 0.3, 'defense'), ('arcura', 0.5, 'rcura')]:
                for i in range(5):
                    if enemy.efecto[i] == '':
                        enemy.efecto[i] = efx; enemy.efecton[i] = val
                        enemy.tiempo[i] = campo.nturnos + 3
                        setattr(enemy, attr, getattr(enemy, attr) + val)
                        break
            self.energy += -60 + 4
        self.cooldown[1] = campo.nturnos + 4
        printdatos(self, enemy)
        return True

    def _ia_heal(self, enemy):
        if not self._puede_usar(40, 0):
            return False
        hit = randint(0, 100)
        if hit > self.preci1:
            print(self.name, 'falla heal!')
            self.energy += -20 + 4
        else:
            print(self.name, 'cura', 100 * self.power * self.lcura * enemy.rcura, 'de vida a', enemy.name, 'y le quita 1 hemorragia y 1 maldición')
            enemy.health += 100 * self.power * self.lcura * enemy.rcura
            if enemy.cargas['hemorragia'] > 0: enemy.cargas['hemorragia'] -= 1
            if enemy.cargas['maldita'] > 0: enemy.cargas['maldita'] -= 1
            self.energy += -40 + 4
        printdatos(self, enemy)
        return True

    def _elegir_accion_IA(self, enemy):  # Healer
        # 1. Super si el aliado está muy bajo (<30% vida)
        if enemy.health < enemy.maxhealth * 0.30:
            if self._ia_proteger(enemy): return
        # 2. Bendecir si el aliado no tiene el buff (no gastar si ya lo tiene)
        tiene_adefense = any(enemy.efecto[i] == 'adefense' for i in range(5))
        if not tiene_adefense:
            if self._ia_bendecir(enemy): return
        # 3. Heal básico
        if self.att1 >= 3:
            self.att1 = 0
            super().energia(enemy)
            return
        if self._ia_heal(enemy):
            self.att1 += 1
            return
        # 4. Proteger si tiene energía aunque el aliado no esté crítico
        if self._ia_proteger(enemy): return
        super().energia(enemy)

curandera = Healer('Hawise', 1700, 200, 1, 1, 35, 100, 80, 85, 100, 100, 3, 1, 0, 0, 0, 50, 0, 0, 'healer', 1)


class Mace (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
    def print_info(self):
        print ('Tipo: Guerrero')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "Golpe defensivo", haces 40 de daño y aumentas tu defensa en 0.08, cuesta 5 de energía y tiene un', self.preci1,'% precisión')
        print ('Ataque 2: "Agitador de tierra", inflige 200 de daño, cuesta 80 de energía, tiene un', self.preci2,'% precisión y 2 turnos de cooldown')
        print ('Ataque super: "Salto profundo", inflige 110 de daño y aturdes a tu enemigo 2 turnos (se acumula si tu enemigo ya está aturdido), cuesta 100 de energía, tiene un', self.preci3,'% precisión, y 3 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene un', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y tiene un', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "concentración" en una canalización recuperas el doble de energia')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un valiente guerrero llega a la arena con una pezada maza, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for maceee in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del macero:')
                    if turn.lower() == 'golpe defensivo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 5:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoo = randint (0,100)
                        if unoo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 2.5
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 40 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, True)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Un mazazo le hace un gran golpe en el enemigo que le inflige', dano_total, 'de daño a', enemy.name, ', y aumentas tu propia defensa en 0.08')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                self.defense += 0.08
                                self.energy -= 5
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('De la locura te pegas un mazazo que te inflige', 40 * self.power / self.defense, 'de daño, y aumentas tu propia defensa en 0.08')
                                    self.health -= 40 * self.power / self.defense
                                    self.defense += 0.08
                                    self.energy -= 5
                                    self.energy += 2
                                else:
                                    dano = 40 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Un mazazo le hace un gran golpe en el enemigo que le inflige', dano_total, 'de daño a', enemy.name, ', y aumentas tu propia defensa en 0.08')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.defense += 0.08
                                    self.energy -= 5
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'agitador de tierra':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 80:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doos = randint(0, 100)
                        if doos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 40
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 200 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, True)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Agita la tierra alrededor del enemigo y le inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                self.energy -= 80
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Te vuelves loco y al querer azotar la tierra con tu maza te partes el pie, te infliges', 200 * self.power / self.defense, 'de daño')
                                    self.health -= 200 * self.power / self.defense
                                    self.energy -= 80
                                    self.energy += 2
                                else:
                                    dano = 200 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Agita la tierra alrededor del enemigo y le inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.energy -= 80
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[1] = campo.nturnos + 3
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'salto profundo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 100:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        trees = randint(0, 100)
                        if trees > self.preci3: 
                            print ('¡Fallas!')
                            self.energy -= 50
                            
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 110 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, True)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print ('Saltas sobre tu enemigo infligiendole', dano_total, 'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                if enemy.cargas['stun'] == 0:
                                    enemy.cargas['stun'] += 2
                                    print('Aturdes a', enemy.name, '2 turnos')
                                else:
                                    print(enemy.name, 'ya está stuneado')
                                self.energy -= 100
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Saltas sobre tu enemigo pero de la locura te das con tu propio mazo en toda tu cabeza infligiendote', 110 * self.power / self.defense, 'de daño')
                                    self.health -= 110 * self.power / self.defense
                                    self.cargas['stun'] += 2
                                    print('Te aturdes 2 turnos')
                                    self.energy -= 100
                                    self.energy += 2
                                else:
                                    dano = 110 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print ('Saltas sobre tu enemigo infligiendole', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    if enemy.cargas['stun'] == 0:
                                        enemy.cargas['stun'] += 2
                                        print('Aturdes a', enemy.name, '2 turnos')
                                    else:
                                        print(enemy.name, 'ya está stuneado')
                                    self.energy -= 100
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[2] = campo.nturnos + 4
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad salto profundo se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
maza = Mace ('Björn', 1980, 220, 1, 1.1, 39, 90, 95, 85, 100, 100, 1, 1, 0, 0, 0, 55, 0, 0, 'DPS', 4)

class Fires (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "fuego", aplica 1 quemadura en tu enemigo, cuesta 30 de energía y tiene', self.preci1,'% precisión')
        print ('Ataque 2: "llamas", aumentas tu defensa en 0.5 por 2 turnos, cuesta 45 de energía y tiene', self.preci2,'% precisión')
        print ('Ataque super: "Volcan", aplicas 3 quemaduras (afecta tu poder, pero no su defensa), cuesta 140 de energía, tiene', self.preci3,'% precisión y 3 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "ignifugo", las quemaduras no te hacen daño')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Como un ave fénix, de entre las llamas, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for firesss in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del ígneo:')
                    if turn.lower() == 'fuego':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                print ('Quemas a', enemy.name, ',le aplicas', 1 * self.power, 'quemaduras')
                                enemy.cargas['quemado'] += 1 * self.power
                                self.energy -= 30
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Te vuelves loco y te quemas, te aplicas', 1 * self.power, 'quemaduras')
                                    self.cargas['quemado'] += 1 * self.power
                                    self.energy -= 30
                                    
                                    self.energy += 3
                                else:
                                    print ('Quemas a', enemy.name, ',le aplicas', 1 * self.power, 'quemaduras')
                                    enemy.cargas['quemado'] += 1 * self.power
                                    self.energy -= 30
                                    
                                    self.energy += 3
                            else:
                                print ('ERROR')

                        printdatos(self, enemy)
                    elif turn.lower() == 'llamas':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 22.5
                            self.energy += 3
                        else:
                            print ('Te envuelves en llamas que aumentan tu defensa en', 0.5 * self.power,'por 2 turnos')
                            if enemy.efecto[0] == '':
                                enemy.efecto[0] = 'adefensa'
                                enemy.efecton[0] = 0.5*self.power
                                enemy.tiempo[0] = campo.nturnos + 2

                            elif enemy.efecto[1] == '':
                                enemy.efecto[1] = 'adefensa'
                                enemy.efecton[1] = 0.5*self.power
                                enemy.tiempo[1] = campo.nturnos + 2

                            elif enemy.efecto[2] == '':
                                enemy.efecto[2] = 'adefensa'
                                enemy.efecton[2] = 0.5*self.power
                                enemy.tiempo[2] = campo.nturnos + 2

                            elif enemy.efecto[3] == '':
                                enemy.efecto[3] = 'adefensa'
                                enemy.efecton[3] = 0.5*self.power
                                enemy.tiempo[3] = campo.nturnos + 2

                            elif enemy.efecto[4] == '':
                                enemy.efecto[4] = 'adefensa'
                                enemy.efecton[4] = 0.5*self.power
                                enemy.tiempo[4] = campo.nturnos + 2
                            self.defense += 0.5 *self.power
                            self.energy -= 45
                        self.energy += 3
                        printdatos(self, enemy)
                    elif turn.lower() == 'volcan':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 120:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 60
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                print (self.name, 'invoca la fuerza de un volcán y aplica', 4 * self.power,'quemaduras a', enemy.name)
                                enemy.cargas['quemado'] += 4 * self.power
                                self.energy -= 120
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, 'invoca la fuerza de un volcán, pero se vuelve loco y se auto-aplica', 4 * self.power,'quemaduras')
                                    self.cargas['quemado'] += 4 * self.power
                                    self.energy -= 120
                                    self.energy += 3
                                else:
                                    print (self.name, 'invoca la fuerza de un volcán y aplica', 3 * self.power,'quemaduras a', enemy.name)
                                    enemy.cargas['quemado'] += 3 * self.power
                                    self.energy -= 120
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown[2] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad volcan se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
igneo = Fires('Finnian', 1630, 130, 1, 1, 64, 80, 90, 100, 100, 100, 2, 1, 0, 0, 0, 30, 0, 0, 'DPS', 3)

class Snake_Charmer(Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "bocajarro", inflige 5 de daño entre 10 a 50 veces, cuesta 30 de energía, tiene', self.preci1,'% precisión y tiene 20% de probabilidades de infligir un sangrado en tu enemigo')
        print ('Ataque 2: "agil", aumenta la velocidad de tu objetivo en 16 (aumentado por la mitad del poder), cuesta 40 de energía,', self.preci2,'% precisión y 2 turnos de cooldown')
        print ('Ataque super: "serpiente", tu serpiente inflige 200 de daño, 2 venenos y lo aturde 1 turno, cuesta 160 de energía, tiene', self.preci3,'% precisión y 2 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "amigo", tu serpiente ataca contigo haciendo 35 de daño y tiene un 15% de probabilidades de infligir un veneno (cuidado con el autoapuntado)')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. ¿De donde sale esa música?, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for snake_charmerrr in range (1):
            if self.health <= 0:
                print ('Sigues muerto')
                return
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    veneno = randint(1, 100)
                    if veneno <= 15:
                        print ('Tu serpiente inflige 35 de daño y un veneno a', enemy.name)
                        enemy.health -= 35
                        enemy.cargas['veneno'] += 1
                    else:
                        print ('Tu serpiente inflige 35 de daño a', enemy.name)
                        enemy.health -= 35
                    turn = input('Turno del encantador de serpientes:')
                    if turn.lower() == 'bocajarro':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                bocajarro = randint (10, 50)
                                dano = (5 * self.power / enemy.defense) * bocajarro
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                super().atacar(enemy, dano_total, True)
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print (self.name, 'le da un bocajarro de', bocajarro, 'golpes a', enemy.name, ', le inflige', dano_total, 'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                punetazooo = randint (1, 100)
                                if punetazooo <= 20:
                                    enemy.cargas['sangrado'] += 1
                                    print ('Tras un fuerte puñetazo un sangrado surge en', enemy.name)
                                self.energy -= 30
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    bocajarro = randint (10, 50)
                                    dano = (5 * self.power / self.defense) * bocajarro
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'se vuelve loco, se da un bocajarro de', bocajarro, 'golpes infligiedose', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    punetazooo = randint (1, 100)
                                    if punetazooo <= 20:
                                        self.cargas['sangrado'] += 1
                                        print ('Tras un fuerte puñetazo un sangrado surge en', self.name)
                                    self.energy -= 30
                                    self.energy += 3
                                else:
                                    bocajarro = randint (10, 50)
                                    dano = (5 * self.power / enemy.defense) * bocajarro
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    super().atacar(enemy, dano_total, True)
                                    self.health -= reflejo
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print (self.name, 'le da un bocajarro de', bocajarro, 'golpes a', enemy.name, ', le inflige', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    punetazooo = randint (1, 100)
                                    if punetazooo <= 20:
                                        enemy.cargas['sangrado'] += 1
                                        print ('Tras un fuerte puñetazo un sangrado surge en', enemy.name)
                                    self.energy -= 30
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'agil' or turn.lower() == 'ágil':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (self.name, 'se tropieza!')
                            self.energy -= 20
                            self.energy += 3
                        else:
                            print ('Aumentas la velocidad de', enemy.name,'en', 16 * (self.power / 2))
                            enemy.velocity += 16 * (self.power / 2)
                            self.energy -= 40
                            self.energy += 3
                        self.cooldown[1] += 3
                        printdatos(self, enemy)
                    elif turn.lower() == 'serpiente':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print ('La serpiente de', self.name, 'está silenciada')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 160:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 80
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 200 * self.power / enemy.defense 
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                dano_total = dano
                                super().atacar(enemy, dano_total, False)
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print (self.name, 'lanza su serpiente a', enemy.name, 'le hace',dano_total,'de daño, le aplica 3 venenos y lo aturde 1 turno')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                enemy.cargas['veneno'] += 2
                                enemy.cargas['stun'] += 1
                                self.energy -= 160
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, 'lanza su serpiente pero está se vuelve loca y te muerde, haciendole', 200 * self.power / self.defense,'aplicandole 3 venenos y aturdiendole 1 turno')
                                    self.health -= 200 * self.power / self.defense
                                    self.cargas['veneno'] += 2
                                    self.cargas['stun'] += 1
                                    self.energy -= 160
                                    self.energy += 3
                                else:
                                    dano = 200 * self.power / enemy.defense 
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    dano_total = dano
                                    super().atacar(enemy, dano_total, False)
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano_total * self.robovida
                                    print (self.name, 'lanza su serpiente a', enemy.name, 'le hace',dano_total,'de daño, le aplica 3 venenos y lo aturde 1 turno')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    enemy.cargas['veneno'] += 2
                                    enemy.cargas['stun'] += 1
                                    self.energy -= 160
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown[2] = campo.nturnos + 3
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad serpiente se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
serpientero = Snake_Charmer('Rayder', 1900, 140, 1, 1, 58, 120, 80, 95, 100, 100, 2, 1, 0, 0, 0, 30, 0, 0, 'DPS', 3)

class Apostador(Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        self.sombra = 1

    def print_info(self):
        print ('Tipo: ¿¿??')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "apostar", tiene un 20% de probabilidades de infligir 180 de daño, tiene un 20% de probabilidades de curarte 80 de vida, tiene un 20% de probabilidades de aumentar tu poder en 0.1 (no afecta el poder), tiene un 20% de probabilidades de aumentar tu defensa en 0.1 (no afecta el poder) y tiene un 20% de probabilidades de aumentar tu velocidad en 10, cuesta 3 de energía, tiene', self.preci1,'% precisión')
        print ('Ataque 2: "invocar", genera una sombra, cuesta 10 de energía y', self.preci2,'% precisión')
        print ('Ataque super: "bomba", tienes un 40% de probabilidades de infligir a tu enemigo 800 de daño , 60% de probabilidades de auto infligirte 600 de daño (no afecta la defensa superior a 1), cuesta 20 de energía, tiene', self.preci3,'% precisión y 1 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 5 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 4 de energía y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "maleta", tienes dos habilidades pasivas extra')
        print ('Habilidad pasiva: "casinooo", no puedes volverte loco (no más de lo que ya estás)')
        print ('Habilidad pasiva: "amigo", tus sombras atacan a tu objetivo junto a ti(30 de daño por sombra (no afecta poder))')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Salido del casino, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for apostadorrr in range (1):
            if self.health <= 0:
                return
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    if self.sombra > 0:
                        print ('Tus sombras infligen', 30 * self.sombra,'a', enemy.name)
                        enemy.health -= 30 * self.sombra
                    turn = input('Turno del apostador:')
                    if turn.lower() == 'apostar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 3:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print ('Pierdes la apuesta')
                            self.energy -= 1.5
                            self.energy += 2
                        else:
                            cccc = randint (0, 4)
                            if cccc == 0:
                                print ('En la apuesta sale que', enemy.name, 'pierde', super().atacar(enemy, 180, False))
                                self.energy -= 3
                            elif cccc == 1:
                                print ('En la apuesta sale que', self.name, 'recupera', 80 * self.power * self.lcura * self.rcura, 'de vida')
                                self.health += 80 * self.power  * self.lcura * self.rcura
                                self.energy -= 3
                            elif cccc == 2:
                                print ('En la apuesta sale que', self.name, 'aumenta su poder en 0.1')
                                self.power += 0.1 
                                self.energy -= 3
                            elif cccc == 3:
                                print ('En la apuesta sale que', self.name, 'aumenta su defensa en 0.1')
                                self.defense += 0.1
                                self.energy -= 3
                            elif cccc == 4:
                                self.power += 0.1
                                print ('En la apuesta sale que', self.name, 'aumenta su velocidad en', 10 * self.power)
                                self.velocity += 10 * self.power
                                self.energy -= 3
                            
                            self.energy += 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'invocar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede invocar sombras')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print ('Salió el sol y no hay sombras!')
                            self.energy -= 5
                            self.energy += 2
                        else:
                            print ('invocas una sombra')
                            self.sombra += 1
                            self.energy -= 10
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.cargas['hemorragia'], 'hemorragias,', enemy.cargas['sangrado'], 'sangrados,', enemy.cargas['quemado'], 'quemaduras,', enemy.cargas['cura'], 'cargas de cura,', enemy.cargas['veneno'], 'cargas de veneno', enemy.cargas['maldita'], 'cargas malditas y está', enemy.cargas['hielo'] + enemy.cargas['stun'] + enemy.cargas['paralizado'], 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.cargas['hemorragia'], 'hemorragias,', self.cargas['sangrado'], 'sangrados,', self.cargas['quemado'], 'quemaduras,', self.cargas['cura'],'cargas de cura,', self.cargas['veneno'], 'cargas de veneno y', self.cargas['maldita'], 'cargas malditas, estás', self.cargas['hielo'] + self.cargas['stun'] + self.cargas['paralizado'], 'turnos congelados/stuneados/paralizados y tienes', self.sombra, 'sombras', '\n')
                    elif turn.lower() == 'bomba':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede detonar sus bombas')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 20:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print ('La bomba explota en el aire')
                            self.energy -= 10
                            self.energy += 2
                        else:
                            boombaaa = randint (1, 100)
                            if boombaaa <= 50:
                                print (self.name, 'lanza una bomba nuclear a', enemy.name, 'y le quita', super().atacar(enemy, 800, False), 'de vida')
                            elif boombaaa >= 51:
                                if enemy.defense > 1:
                                    print (self.name, 'lanza una bomba nuclear a', enemy.name, ', aunque la bomba se detona antes y, ', self.name, 'se quita 600 de vida')
                                    self.health -= 600 * self.power
                                else:
                                    print (self.name, 'lanza una bomba nuclear a', enemy.name, ', aunque la bomba se detona antes y, ', self.name, 'se quita 600 de vida')
                                    self.health -= 600 * self.power / self.defense
                            self.energy -= 20
                            self.energy += 2
                        self.cooldown[2] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad bomba se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
poker = Apostador('@#-·-#@', 1820, 10, 1, 1, 29, 300, 300, 300, 100, 100, 0, 1, 0, 0, 0, 60, 0, 0, 'DPS+buff', 3)

class Natural (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Natural')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "plantar", aplica 1 carga de cura en tu objetivo (max. 4 y no afecta el poder) y quita 1 quemadura (no afecta el poder), cuesta 8 de energía, tiene', self.preci1,'% precisión')
        if self.mutado == 0:
            print ('Ataque 2: "zarza", hace 140 de daño (si afecta el poder) y aplica 1 sangrado (no afecta el poder), cuesta 60 de energía y tiene', self.preci2,'% precisión')
        elif self.mutado == 1:
            print ('Ataque 2: "proteccion", cura 252 de vida durante 3 turnos (si afecta el poder) y aumenta la defensa de tu objetivo en 0.3 por 3 turnos (no afecta el poder), cuesta 40 de energía y tiene', self.preci2,'% precisión')
        print ('Ataque 3: "pasto" encanta el pasto curando a los jugadores 0.5% de su salud máxima y en un 0.8% a los personajes de tipo natural, no cuesta energia')
        print ('Ataque super: "naturaleza", dependiendo de las cargas de cura que tenga el objetivo a curar: 0-80/1-180/2-260/3-390/4+-500 (no afecta el poder), consume las cargas de cura, cuesta 100 de energía, tiene', self.preci3,'% precisión y tiene 2 turnos de cooldown')
        print ('Poción curativa: "cura", cura 100 de vida, cura 1-2 hemorragia y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "extra", tienes un ataque tres al que no se puede bajar la precisión')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Una druida aparece de entre los árboles, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for naturalll in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno de la druida:')
                    if turn.lower() == 'plantar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 8:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla la cura!')
                            self.energy -= 4
                            self.energy += 4
                        else:
                            print (self.name, 'cura 1 quemadura y aplicas una carga curativa a', enemy.name)
                            enemy.cargas['cura'] += 1
                            if enemy.cargas['cura'] > 4:
                                (enemy.name, 'sobrepasa el límite de cargas de cura')
                                enemy.cargas['cura'] = 4
                            if enemy.cargas['quemado'] > 0:
                                enemy.cargas['quemado'] -= 1
                            self.energy -= 8
                            self.energy += 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'zarza' and self.mutado == 0:
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print (self.name, 'se confunde de hechizo y convierte una hoja de pasto en un gusano')
                            self.energy -= 30
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                print ('Una zarza mágica abraza a', enemy.name, 'infligiendole', super().atacar(enemy, 140, False), 'de daño y creandole un sangrado')
                                enemy.cargas['sangrado'] += 1
                                self.energy -= 60
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, 'se vuelve loca e invoca unas dagas mágicas que la atacan y le infligen', 140 * self.power / self.defense, 'de daño y creandole un sangrado')
                                    self.health -= 140 * self.power / self.defense
                                    self.cargas['sangrado'] += 1
                                    self.energy -= 60
                                    self.energy += 4
                                else:
                                    print ('Una zarza mágica abraza a', enemy.name, 'infligiendole', super().atacar(enemy, 140, False), 'de daño y creandole un sangrado')
                                    enemy.cargas['sangrado'] += 1
                                    self.energy -= 60
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        printdatos(self, enemy)
                    elif turn.lower() == 'proteccion':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print ('¡', self.name, 'falla la cura!')
                            self.energy -= 20
                            self.energy += 4
                        else:
                            curacion = 252 * self.power / 3
                            print (self.name, 'cura', curacion * 3,'a', enemy.name)
                            for i in range (0, 4):
                                if enemy.efectod[i] == '':
                                    enemy.efectod[i] = 'cura'
                                    enemy.efectodn[i] = curacion
                                    enemy.tiempod[i] = campo.nturnos + 3
                                    break
                            for i in range (0, 4):
                                if enemy.efecto[i] == '':
                                    enemy.efecto[i] = 'adefensa'
                                    enemy.efecton[i] = 0.3
                                    enemy.tiempo[i] = campo.nturnos + 3
                                    enemy.defense += 0.3
                                    break
                            self.energy -= 40
                            self.energy += 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'pasto':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 0:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        print (self.name, 'encanta el pasto curando a los jugadores 0.5% de su salud máxima y en un 0.8% a los personajes de tipo natural')
                        checar_campos()
                        campo.hierba = 1 
                        self.energy += 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'naturaleza':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (1, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 100:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'se equivoca de hechizo y invoca una serpiente bebé inofensiva!')
                            self.energy -= 50
                            self.energy += 4
                        else:
                            if enemy.cargas['cura'] == 0:
                                natur = 80 * self.lcura * enemy.rcura
                            elif enemy.cargas['cura'] == 1:
                                natur = 180 * self.lcura * enemy.rcura
                            elif enemy.cargas['cura'] == 2:
                                natur = 260 * self.lcura * enemy.rcura
                            elif enemy.cargas['cura'] == 3:
                                natur = 390 * self.lcura * enemy.rcura
                            elif enemy.cargas['cura'] >= 4:
                                natur = 500 * self.lcura * enemy.rcura
                            print (self.name, 'invoca el poder de la naturaleza para curar', natur ,'de vida a',enemy.name)
                            enemy.health += natur
                            enemy.cargas['cura'] = 0
                            self.energy -= 100
                            self.energy += 4
                        self.cooldown[2] = campo.nturnos + 3
                        printdatos(self, enemy)
                    elif turn.lower() == 'cura':
                        super().cura(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad naturaleza se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
natural = Natural ('Groa', 1600, 220, 1, 1, 37, 100, 90, 120, 100, 100, 4, 1, 0, 0, 0, 40, 0, 0, 'DPS+healer', 1)
natural_heal = Natural ('Groa', 1600, 220, 1, 1, 37, 100, 90, 120, 100, 100, 4, 1, 1, 0, 0, 45, 0, 0, 'healer', 1)

class Diablillo (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "llamarada ignea", inflige 80 de daño (si afecta el poder) y le haces 1 quemadura (no afecta el poder), cuesta 30 de energía, tiene', self.preci1,'% precisión y 1 turno de cooldown')
        print ('Ataque 2: "Mordida ignea", aplicas a tu enemigo 2 quemadura (no afecta el poder), cuesta 55 de energía y tiene', self.preci2,'% precisión y tiene un cooldown de 1 turno')
        print ('Ataque super: "Rafaga ignea", inflige 260 de daño (si afecta el poder) y le haces 3 quemadura (no afecta el poder), cuesta 180 de energía, tiene', self.preci3,'% precisión y tiene un cooldown de 3 turnos')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene',self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y',self.precienergia,'% precisión')
        print ('Habilidad pasiva: "Corazon de fuego", se cura 15 de vida y energia (no afecta el poder) al aplicar 1 quemadura (no afecta el poder)')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. No es fuego volador, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for diablillooo in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del diablillo:')
                    if turn.lower() == 'llamarada ignea':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                print (self.name, 'quema a', enemy.name, 'aplicandole 1 quemadura y haciendole', super().atacar(enemy, 80, False), 'de daño')
                                enemy.cargas['quemado'] += 1
                                self.health += 15 * self.lcura * self.rcura
                                self.energy -= 12
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, ' se vuelve loco y se quema a si mismo aplicadose 1 quemadura y haciedose', 80 * self.power / self.defense, 'de daño')
                                    self.health -= 80 * self.power / self.defense
                                    self.cargas['quemado'] += 1
                                    self.health += 15 * self.lcura * self.rcura
                                    self.energy += 15
                                    self.energy -= 30
                                    self.energy += 3
                                else:
                                    print (self.name, 'quema a', enemy.name, 'aplicandole 1 quemadura y haciendole', super().atacar(enemy, 80, False), 'de daño')
                                    enemy.cargas['quemado'] += 1
                                    self.health += 15 * self.lcura * self.rcura
                                    self.energy -= 12
                            else:
                                print ('ERROR')
                        self.cooldown[0] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'mordida ignea':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede hacer nada')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 55:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (enemy.name, 'se aparta y no le alcanzas')
                            self.energy -= 26.5
                            self.energy += 3
                        else:
                            print (uno.name, 'se abalanza sobre', enemy.name, ', echando fuego por la boca lo muerdes haciendole 2 quemaduras')
                            enemy.cargas['quemado'] += 2
                            super().atacar(enemy, 0, True)
                            self.health += 30 * self.lcura * self.rcura
                            self.energy += 30
                            self.energy -= 55
                            self.cooldown[1] += campo.nturnos + 2
                            self.energy += 3
                        self.cooldown[1] = campo.nturnos + 2
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'rafaga ignea':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede atacar')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 180:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 90
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                print (self.name, 'lanza una ráfaga de bolas ígneas aplicando 3 quemaduras a', enemy.name, 'e infligiendole', super().atacar(enemy, 260, False),'de daño')
                                enemy.cargas['quemado'] += 3
                                self.health += 45 * self.lcura * self.rcura
                                self.energy += 45
                                self.energy -= 180
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, 'se vuelve loco y lanza una ráfaga de bolas ígneas a si mismo aplicadose 3 quemaduras e infligiedose', 260 * self.power / self.defense,'de daño')
                                    self.health -= 260 * self.power / self.defense
                                    self.cargas['quemado'] += 3
                                    self.health += 45 * self.lcura * self.rcura
                                    self.energy += 45
                                    self.energy -= 180
                                    self.energy += 3
                                else:
                                    print (self.name, 'lanza una ráfaga de bolas ígneas aplicando 3 quemaduras a', enemy.name, 'e infligiendole', super().atacar(enemy, 260, False),'de daño')
                                    enemy.cargas['quemado'] += 3
                                    self.health += 45 * self.lcura * self.rcura
                                    self.energy += 45
                                    self.energy -= 180
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown[2] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad rafaga ignea se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
diablillo = Diablillo('Gillmore', 2000, 145, 1, 1, 75, 100, 90, 90, 100, 100, 2, 1, 0, 0, 0, 35, 0, 0, 'DPS', 3)

class Support (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        self.cargado = ''
        self.cargadocooldown = 0

    def print_info(self):
        print ('Tipo: mago')
        print ('Nivel de salud:', self.health)
        print ('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "escudo", aplica un escudo sobre tu objetivo que cubre 80 de vida durante 2 turnos y aumenta la defensa en 0.05, cuesta 12 de energía, tiene',self.preci1,'% precisión')
        print ('Ataque 2: "agilizar", aumenta la velocidad en 8, cuesta 30 de energía y tiene', self.preci2 ,'% precisión, y 1 turno de cooldown')
        print ('Ataque 3: "purificador" carga el aire de un hechizo que quita todas las cargas de todos los personajes (en cada turno), no cuesta energia')
        print ('Ataque super: "sobrecargar", aumenta el poder de tu objetivo en 3 después de 3 turnos esa potenciación se quita y con ella 300 de vida, además tiene un 15% de probabilidades de quitarse 200 de vida extra, cuesta 20 de energía, tiene ', self.preci3 ,'% precisión y un cooldown de 3 turnos')
        print ('Poción curativa: "cura", cura 100 de vida, cura 1-2 hemorragia y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura ,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia ,'% precisión')
        print ('Habilidad pasiva: "maleta", tienes dos habilidades pasivas extras')
        print ('Habilidad pasiva: "apoyo", puedes dar tu cura a tu objetivo escribiendo "curar", además de poder canalizar para tu objetivo escribiendo "energiar"')
        print ('Habilidad pasiva: "extra", tienes un ataque tres al que no se puede bajar la precisión')
        print ('(Cada turno recuperas 4 de energia) (Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for suporttt in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del mago ayudante:')
                    if turn.lower() == 'escudo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla el encantamiento!')
                            self.energy -= 5
                            self.energy += 4
                        else:
                            print ('Invocas un escudo sobre', enemy.name, 'que protege', 80 * self.power,'de vida y aumenta su defensa en', 0.05 * self.power)
                            if enemy.efecto[0] == '':
                                enemy.efecto[0] = 'escudo'
                                enemy.efecton[0] = enemy.health
                                enemy.tiempo[0] = campo.nturnos + 2

                            elif enemy.efecto[1] == '':
                                enemy.efecto[1] = 'escudo'
                                enemy.efecton[1] = enemy.health
                                enemy.tiempo[1] = campo.nturnos + 2

                            elif enemy.efecto[2] == '':
                                enemy.efecto[2] = 'escudo'
                                enemy.efecton[2] = enemy.health
                                enemy.tiempo[2] = campo.nturnos + 2

                            elif enemy.efecto[3] == '':
                                enemy.efecto[3] = 'escudo'
                                enemy.efecton[3] = enemy.health
                                enemy.tiempo[3] = campo.nturnos + 2

                            elif enemy.efecto[4] == '':
                                enemy.efecto[4] = 'escudo'
                                enemy.efecton[4] = enemy.health
                                enemy.tiempo[4] = campo.nturnos + 2

                            enemy.health += 80 * self.power
                            enemy.defense += 0.05 * self.power
                            self.energy -= 10
                            self.energy += 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'agilizar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print (self.name, 'se confunde de hechizo y convierte uno de sus calcetines en un gorrión')
                            self.energy -= 15
                            self.energy += 4
                        else:
                            print ('Aumentas la velocidad de', enemy.name, 'en', 8 * self.power)
                            enemy.velocity += 8 * self.power
                            self.energy -= 30
                            self.energy += 4
                        self.cooldown[1] = campo.nturnos +  2
                        printdatos(self, enemy)
                    elif turn.lower() == 'purificador':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['stun'] > 0:
                            print (self.name, 'está stuneado y no puede hacer nada')
                            self.cargas['stun'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 0:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        print (self.name, 'carga el aire de un hechizo que quita todas las cargas de todos los personajes')
                        checar_campos()
                        campo.purificador = 1 
                        self.energy += 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'sobrecargar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (1, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 20:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'se equivoca de hechizo y convierte su bota en una manzana!')
                            self.energy -= 10
                            self.energy += 4
                        else:
                            self.cargado = enemy
                            if self.cargado == support:
                                print ('Te cargas durante 3 turnos para aumentar tu poder en 3')
                                self.power += 3
                                self.cooldown[2] += campo.nturnos + 4
                                self.energy -= 20
                                self.energy += 4
                                printdatos(self, enemy)
                                break
                            print ('Cargas a', enemy.name, 'durante 3 turnos para aumentar su poder en 3')
                            enemy.power += 3
                            self.energy -= 20
                            self.energy += 4
                        self.cooldown[2] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'cura':
                        super().cura(enemy)
                    elif turn.lower() == 'curar':
                        super().curar(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'energiar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        energiaaa = randint(1, 100)
                        if energiaaa > self.precienergia: 
                            print ('¡', self.name, 'falla la canalización!')
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 80 * self.power, 'de energía para', enemy.name)
                            enemy.energy += 80 * self.power
                            self.energy += 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad sobrecargar se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
                    if self.cargadocooldown > 0:
                        self.cargadocooldown -= 1
                        if self.cargadocooldown == 0:
                            print ('A', self.cargado.name, 'se le acaba el poder de la sobrecarga')
                            self.cargado.power -= 3
                            sobrecargaaaa = randint (1, 100)
                            if sobrecargaaaa <= 15:
                                self.cargado.health -= 800
                                print (self.cargado.name, 'se quita 800 de vida debido a la repentina bajada de poder')
                            else:
                                self.cargado.health -= 500
                                print (self.cargado.name, 'se quita 500 de vida debido a la repentina bajada de poder')
support = Support ('Wymond', 1780, 180, 1, 1, 36, 120, 120, 200, 100, 100, 3, 1, 0, 0, 0, 28, 0, 0, 'FSD', 2)

class Chiquitin(Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: misterioso')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "bocajarro", inflige 5 de daño entre 10 a 50 veces, cuesta 2 de energía, tiene', self.preci1 ,'% precisión, 1 turno de cooldown y tiene 20% de probabilidades de infligir un sangrado en tu enemigo')
        print ('Ataque 2: "mordida ignea", aplicas 2 quemadura (no afecta el poder), cuesta 8 de energía, tiene 1 turno de cooldown y un', self.preci2 ,'% precisión')
        print ('Ataque super: "Ira", aumenta tu poder en 1 (no afecta el poder), cuesta 10 de energía, tiene ', self.preci3 ,'% precisión y 1 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 5 de energía y tiene ', self.precicura ,'% precisión')
        print ('Canalización: "energia", recupera 4 de energía y ', self.precienergia ,'% precisión')
        print ('Habilidad pasiva: "regenerativo", al principio de tu turno recuperas toda tu vida')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Pequeño pero matón, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for chiquitin in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    self.health = self.maxhealth
                    print (self.name, 'regenera su vida')
                    turn = input('Turno del chiquitín:')
                    if turn.lower() == 'bocajarro':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 2:
                            print (self.name, 'no tiene suficiente energia)', '\n')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print ('Fallas el golpe')
                            self.energy -= 1
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                bocajarro = randint (10, 50)
                                dano = (5 * self.power / enemy.defense) * bocajarro
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano_total * self.robovida
                                print (self.name, 'le da un bocajarro de', bocajarro, 'golpes a', enemy.name, ', le inflige', dano_total ,'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                punetazooo = randint (1, 100)
                                if punetazooo <= 20:
                                    enemy.cargas['sangrado'] += 1
                                    print ('Tras un fuerte puñetazo un sangrado surge en', enemy.name)
                                self.energy -= 2
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    bocajarro = randint (10, 50)
                                    print (self.name, 'se vuelve loco y se da un bocajarro de', bocajarro, 'golpes a si mismo, se inflige', (5 * self.power / self.defense) * bocajarro, 'de daño')
                                    self.health -= (5 * self.power / self.defense) * bocajarro
                                    punetazooo = randint (1, 100)
                                    if punetazooo <= 20:
                                        self.cargas['sangrado'] += 1
                                        print ('Tras un fuerte puñetazo un sangrado surge en', self.name)
                                    self.energy -= 2
                                    self.energy += 2
                                else:
                                    bocajarro = randint (10, 50)
                                    dano = 5 * bocajarro
                                    print (self.name, 'le da un bocajarro de', bocajarro, 'golpes a', enemy.name, ', le inflige', super().atacar(enemy, dano, True), 'de daño')
                                    punetazooo = randint (1, 100)
                                    if punetazooo <= 20:
                                        enemy.cargas['sangrado'] += 1
                                        print ('Tras un fuerte puñetazo un sangrado surge en', enemy.name)
                                    self.energy -= 2
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[0] = campo.nturnos + 2
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'mordida ignea':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede atacar')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 8:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (enemy.name, 'se aparta y no le alcanzas')
                            self.energy -= 4
                            self.energy += 2
                        else:
                            print (uno.name, 'se abalanza sobre', enemy.name, ', echando fuego por la boca lo muerdes haciendole 2 quemaduras')
                            enemy.cargas['quemado'] += 2
                            self.energy -= 8
                            self.energy += 2
                        self.cooldown[1] = campo.nturnos + 2
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'ira':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede enfurecerse')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia', '\n')
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print ('Fallas!')
                            self.energy -= 5
                            self.energy += 2
                        else:
                            print (self.name, 'se enfurece y aumenta su poder en uno, ¡', enemy.name, 'apurate en matarlo!!')
                            self.power += 1
                            self.energy -= 10
                            self.energy += 2
                        self.cooldown[2] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad ira se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
chiquitin = Chiquitin('$)¬"#@', 400, 10, 1, 1, 32, 120, 90, 75, 100, 100, 0, 1, 0, 0, 0, 20, 0, 0, 'DPS+buff', 3)

class Guadana (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Guerrero')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "golpe desgarrador", infliges un sangrado en tu enemigo, cuesta 20 de energía y tiene un', self.preci1,'% precisión')
        print ('Ataque 2: "corte mortal", inflige 140 de daño y reduce la defensa de tu enemigo en 0.3 duante 2 turnos, cuesta 50 de energía, tiene un', self.preci2,'% precisión y 3 turnos de cooldown')
        print ('Ataque super: "segar", haces 200 de daño y si después la vida de tu enemigo está por debajo del 40% inflige 400 de daño extra si no solo inflige 200 de daño extra, cuesta 90 de energía, tiene un', self.preci3,'% precisión, y 4 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene un', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y tiene un', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "concentración" en una canalización recuperas el doble de energia')
        print ('(Cada turno recuperas 2 de energia)(Si no tienes suficiente energia para lanzar un ataque pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un valiente guerrero llega a la arena con una guadaña, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for guadanaaa in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno de la guadaña:')
                    if turn.lower() == 'golpe desgarrador':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 20:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoo = randint (0,100)
                        if unoo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 10
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                enemy.cargas['sangrado'] += 1
                                print ('Un golpe desgarra la piel de', enemy.name + ', y le provoca un sangrado')
                                self.energy -= 20
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('De la locura te desgarras la piel, y te provocas un sangrado')
                                    self.cargas['sangrado'] += 1
                                    self.energy -= 20
                                    self.energy += 2
                                else:
                                    print ('Un golpe desgarra la piel de', enemy.name + ', y le provoca un sangrado')
                                    self.cargas['sangrado'] += 1
                                    self.energy -= 20
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'corte mortal':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 50:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doos = randint(0, 100)
                        if doos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 25
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                print ('Desgarra un brazo de', enemy.name, 'quitandole', super().atacar(enemy, 140, True), 'de vida y bajando su defensa en 0.3 por 2 turnos')
                                for i in range (0, 4):
                                    if enemy.efecto[i] == '':
                                        enemy.efecto[i] = 'bdefense'
                                        enemy.efecton[i] = 0.3
                                        enemy.tiempo[i] = campo.nturnos + 2
                                        enemy.defense -= 0.3
                                        break
                                self.energy -= 50
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Te vuelves loco desgarrandote un brazo quitandote', 140 * self.power / self.defense, 'de vida y bajando tu defnsa en 0.3 por 2 turnos')
                                    self.health -= 140 * self.power / self.defense
                                    for i in range (0, 4):
                                        if self.efecto[i] == '':
                                            self.efecto[i] = 'bdefense'
                                            self.efecton[i] = 0.3
                                            self.tiempo[i]= campo.nturnos + 2
                                            self.defense -= 0.3
                                            break
                                    self.energy -= 80
                                    self.energy += 2
                                else:
                                    print ('Desgarra un brazo de', enemy.name, 'quitandole', super().atacar(enemy, 140, True), 'de vida y bajando su defnsa en 0.3 por 2 turnos')
                                    for i in range (0, 4):
                                        if enemy.efecto[i] == '':
                                            enemy.efecto[i] = 'bdefense'
                                            enemy.efecton[i] = 0.3
                                            enemy.tiempo[i] = campo.nturnos + 2
                                            enemy.defense -= 0.3
                                            break
                                    self.energy -= 50
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[1] = campo.nturnos + 4
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'segar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 90:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        trees = randint(0, 100)
                        if trees > self.preci3: 
                            print ('¡Fallas!')
                            self.energy -= 45
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                print ('Balancea tu guadaña contra tu enemigo infligiendole', super().atacar(enemy, 200, True), 'de daño')
                                if enemy.health <= enemy.maxhealth - enemy.maxhealth *60 /100:
                                    dano = 400 
                                else:
                                    dano = 200 
                                print ('Balancea tu guadaña una segunda vez contra tu enemigo infligiendole', super().atacar(enemy, dano, True), 'de daño')
                                self.energy -= 90
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Te vuelves loco y balancea tu guadaña contra tí mismo infligiendote', 200 * self.power / self.defense, 'de daño')
                                    self.health -= 200 * self.power / self.defense
                                    if enemy.health <= enemy.maxhealth - enemy.maxhealth *60 /100:
                                        dano = 400 * self.power / self.defense
                                    else:
                                        dano = 200 * self.power / self.defense
                                    print ('Balancea tu guadaña una segunda vez contra tí mismo infligiendote', dano, 'de daño')
                                    self.energy -= 90
                                    self.energy += 2
                                else:
                                    print ('Balancea tu guadaña contra tu enemigo infligiendole', super().atacar(enemy, 200, True), 'de daño')
                                    if enemy.health <= enemy.maxhealth - enemy.maxhealth *60 /100:
                                        dano = 400 
                                    else:
                                        dano = 200 
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    print ('Balancea tu guadaña una segunda vez contra tu enemigo infligiendole', super().atacar(enemy, dano, True), 'de daño')
                                    self.energy -= 90
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[2] = campo.nturnos + 5
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad corte mortal se puede volver a lanzar en el turno', self.cooldown[1])
                            print ('La habilidad segar se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
guadana = Guadana ('Dustin', 1930, 310, 1, 1, 40, 100, 85, 95, 100, 100, 1, 1, 0, 0, 0, 30, 0, 0, 'DPS', 3)

class Crossbow (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        self.count1 = 0
        
    def print_info(self):
        print ('Tipo: Guerrero')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "flecha explosiva", inflige 90 de daño, cuesta 15 de energía, tiene', self.preci1,'% precisión')
        print ('Ataque 2: "eliminador de ruido", inflige 120 de daño y silencia durante 2 turnos, cuesta 40 de energía,', self.preci2,'% precisión y 3 turno de cooldown')
        print ('Ataque super: "disparo explosivo", inflige 50 de daño y después de 1 turno inflige 350 de daño, cuesta 65 de energía, tiene', self.preci3,'% precisión y 3 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "mochila", tienes dos habilidades pasivas extras')
        print ('Habilidad pasiva: "x2", después de lanzar 2 ataques 1 lanzas un doble ataque 1')
        print ('Habilidad pasiva: "solo ida", tu daño no puede ser reflejado')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas sin energia pierdes un turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Con su brillante ballesta aparece, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for crossbowww in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del ballestero:')
                    if turn.lower() == 'flecha explosiva':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 3:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 7.5
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 90 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano * self.robovida
                                print ('Una flecha explota a los pies de tu enemigo, le inflige', dano ,'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                enemy.health -= dano
                                self.count1 += 1
                                if self.count1 >= 3:
                                    dano = 90 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    enemy.health -= dano
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano * self.robovida
                                    self.count1 = 0
                                    print ('Una segunda flecha explota a los pies de tu enemigo, le inflige', dano ,'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                self.energy -= 15
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('A causa de la locura', self.name,'explota una flecha en el pie, se inflige', 90 * self.power / self.defense ,'de daño')
                                    self.health -= 90 * self.power / self.defense
                                    self.count1 += 1
                                    if self.count1 >= 3:
                                        self.health -= 90 * self.power / self.defense
                                        self.count1 = 0
                                        print ('A causa de la locura', self.name,'explota una flecha en el pie, se inflige', 90 * self.power / self.defense ,'de daño')
                                    self.energy -= 15
                                    self.energy += 2
                                else:
                                    dano = 90 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    enemy.health -= dano
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano * self.robovida
                                    print ('Una flecha explota a los pies de tu enemigo, le inflige', dano ,'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    self.count1 += 1
                                    if self.count1 >= 3:
                                        dano = 90 * self.power / enemy.defense
                                        if enemy.cargas['invencible'] == 1:
                                            dano = 0
                                        if self.robovida > 1:
                                            self.robovida = 1
                                        elif self.robovida < 0:
                                            self.robovida = 0
                                        robado = dano * self.robovida
                                        enemy.health -= dano
                                        self.count1 = 0
                                        print ('Una segunda flecha explota a los pies de tu enemigo, le inflige', dano ,'de daño')
                                        if robado != 0:
                                            print (self.name, 'roba', robado, 'de vida')
                                            self.health += robado
                                    self.energy -= 15
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        printdatos(self, enemy)
                    elif turn.lower() == 'eliminador de ruido':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 20
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 120 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano * self.robovida
                                print ('Una flecha se clava en tu enemigo, le inflige', dano, 'de daño a', enemy.name, 'y le silencia 2 turnos')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                enemy.health -= dano
                                enemy.cargas['silenciado'] += 2
                                self.energy -= 40
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('A causa de la locura', self.name,'se clava una flecha en su torso, le inflige', 120 * self.power / self.defense, 'de daño y se silencia 2 turnos')
                                    self.health -= 120 * self.power / self.defense
                                    self.cargas['silenciado'] += 2
                                    self.energy -= 40
                                    self.energy += 2
                                else:
                                    dano = 120 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano * self.robovida
                                    print ('Una flecha se clava en tu enemigo, le inflige', dano, 'de daño a', enemy.name, 'y le silencia 2 turnos')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    enemy.health -= dano
                                    enemy.silenciado += 2
                                    self.energy -= 40
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[1] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'disparo explosivo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar enfurecerse')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 90:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 45
                            
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 50 * self.power / enemy.defense
                                if enemy.cargas['invencible'] == 1:
                                    dano = 0
                                if self.robovida > 1:
                                    self.robovida = 1
                                elif self.robovida < 0:
                                    self.robovida = 0
                                robado = dano * self.robovida
                                print ('Una flecha con una bomba se clava en tu enemigo, le inflige', dano, 'de daño a', enemy.name, 'y en un turno la bomba explota y le hará',350 * self.power,'de daño')
                                if robado != 0:
                                    print (self.name, 'roba', robado, 'de vida')
                                    self.health += robado
                                enemy.health -= dano
                                for i in range (0, 4):
                                    if enemy.efecto[i] == '':
                                        enemy.efecto[i] = 'daño'
                                        enemy.efecton[i] = 350 * self.power
                                        enemy.tiempo[i] = campo.nturnos + 2
                                        break
                                self.energy -= 90
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    dano = 50 * self.power / self.defense
                                    print ('Debido a tu locura te clavas una flecha con una bomba, te infliges', dano, 'de daño y en un turno la bomba explota y te hará 350 de daño')
                                    self.health -= dano
                                    for i in range (0, 4):
                                        if self.efecto[i] == '':
                                            self.efecto[i] = 'daño'
                                            self.efecton[i] = 350
                                            self.tiempo[i] = campo.nturnos + 2
                                            break
                                    self.energy -= 90
                                    self.energy += 2
                                else:
                                    dano = 50 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    if self.robovida > 1:
                                        self.robovida = 1
                                    elif self.robovida < 0:
                                        self.robovida = 0
                                    robado = dano * self.robovida
                                    print ('Una flecha con una bomba se clava en tu enemigo, le inflige', dano, 'de daño a', enemy.name, 'y en un turno la bomba explota y le hará', 350 * self.power,'de daño')
                                    if robado != 0:
                                        print (self.name, 'roba', robado, 'de vida')
                                        self.health += robado
                                    enemy.health -= dano
                                    for i in range (0, 4):
                                        if enemy.efecto[i] == '':
                                            enemy.efecto[i] = 'daño'
                                            enemy.efecton[i] = 350 * self.power
                                            enemy.tiempo[i] = campo.nturnos + 2
                                            break
                                    self.energy -= 90
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[2] = campo.nturnos + 5
                        printdatos(self, enemy)

                    elif turn.lower() == 'venda':
                        super().venda(enemy)

                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad disparo explosivo se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)

    def _ia_disparo_explosivo(self, enemy):
        if not self._puede_usar(90, 2, requiere_no_silenciado=True):
            return False
        hit = randint(0, 100)
        if hit > self.preci3:
            print(self.name, 'falla disparo explosivo!')
            self.energy += -45 + 3
        else:
            if self.locura > 0 and randint(1, 100) < self.locura:
                dano = 50 * self.power / self.defense
                print('Debido a la locura', self.name, 'se clava una flecha bomba, se inflige', dano, 'de daño')
                self.health -= dano
                for i in range(4):
                    if self.efecto[i] == '':
                        self.efecto[i] = 'daño'; self.efecton[i] = 350; self.tiempo[i] = campo.nturnos + 2; break
            else:
                dano = 50 * self.power / enemy.defense
                if enemy.cargas['invencible'] == 1: dano = 0
                print(self.name, 'clava una flecha bomba en', enemy.name, ', inflige', dano, 'de daño. En 1 turno explota y hará', 350 * self.power)
                enemy.health -= dano
                self._aplicar_robovida(dano)
                for i in range(4):
                    if enemy.efecto[i] == '':
                        enemy.efecto[i] = 'daño'; enemy.efecton[i] = 350 * self.power; enemy.tiempo[i] = campo.nturnos + 2; break
        self.energy += -90 + 2
        self.cooldown[2] = campo.nturnos + 5
        printdatos(self, enemy)
        return True

    def _ia_eliminador_de_ruido(self, enemy):
        if not self._puede_usar(40, 1, requiere_no_silenciado=True):
            return False
        hit = randint(0, 100)
        if hit > self.preci2:
            print(self.name, 'falla eliminador de ruido!')
            self.energy += -20 + 2
        else:
            if self.locura > 0 and randint(1, 100) < self.locura:
                dano = 120 * self.power / self.defense
                print('A causa de la locura', self.name, 'se clava una flecha en el torso, se inflige', dano, 'de daño y se silencia 2 turnos')
                self.health -= dano
                self.cargas['silenciado'] += 2
            else:
                dano = 120 * self.power / enemy.defense
                if enemy.cargas['invencible'] == 1: dano = 0
                print(self.name, 'dispara a', enemy.name, ', le inflige', dano, 'de daño y le silencia 2 turnos')
                enemy.health -= dano
                self._aplicar_robovida(dano)
                enemy.cargas['silenciado'] += 2
            self.energy += -40 + 2
        self.cooldown[1] = campo.nturnos + 4
        printdatos(self, enemy)
        return True

    def _ia_flecha_explosiva(self, enemy):
        if not self._puede_usar(3, 0):
            return False
        hit = randint(0, 100)
        if hit > self.preci1:
            print(self.name, 'falla flecha explosiva!')
            self.energy += -7.5 + 2
            printdatos(self, enemy)
            return True
        if self.locura > 0 and randint(1, 100) < self.locura:
            dano = 90 * self.power / self.defense
            print('A causa de la locura', self.name, 'explota una flecha en el pie, se inflige', dano, 'de daño')
            self.health -= dano
            self.count1 += 1
            if self.count1 >= 3:
                self.health -= dano
                self.count1 = 0
                print('Segunda flecha en el pie,', self.name, 'se inflige', dano, 'de daño')
        else:
            dano = 90 * self.power / enemy.defense
            if enemy.cargas['invencible'] == 1: dano = 0
            print(self.name, 'dispara una flecha explosiva a', enemy.name, ', le inflige', dano, 'de daño')
            enemy.health -= dano
            self._aplicar_robovida(dano)
            self.count1 += 1
            if self.count1 >= 3:
                dano2 = 90 * self.power / enemy.defense
                if enemy.cargas['invencible'] == 1: dano2 = 0
                print('Segunda flecha explosiva a', enemy.name, ', le inflige', dano2, 'de daño')
                enemy.health -= dano2
                self._aplicar_robovida(dano2)
                self.count1 = 0
        self.energy += -15 + 2
        printdatos(self, enemy)
        return True

    def _elegir_accion_IA(self, enemy):  
        if self._ia_disparo_explosivo(enemy): return
        if enemy.cargas['silenciado'] <= 0:
            if self._ia_eliminador_de_ruido(enemy): return
        if self.att1 >= 3:
            self.att1 = 0
            super().energia(enemy)
            return
        if self._ia_flecha_explosiva(enemy):
            self.att1 += 1
            return
        super().energia(enemy)

ballesta = Crossbow('Burchard', 1760, 178, 1, 1, 37, 100, 90, 90, 100, 100, 1, 1, 0, 0, 0, 30, 0, 0, 'DPS', 4)

class Loco(Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: misterioso')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "puñetazo", Inflige 77 de daño y silencia un turno, cuesta 4 de energía, tiene', self.preci1,'% precisión, tiene un cooldown de 1 turno')
        print ('Ataque 2: "calma", cura tu locura y tu vida equivalentemente (si tienes 80% locura te curas 80), cuesta 7 de energía y', self.preci2,'% precisión')
        print ('Ataque super: "moneda", tienes un 50% de probabilidades de aumentar tu locura en un 100% y otro 50% de probabilidades aumentarselo a tu enemigo en un 30%, cuesta 18 de energía, tiene', self.preci3,'% precisión y 2 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 5 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 5 de energía y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "locuraaa", será tu locura la que potencie tus ataques')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Salido del manicomio, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for locooo in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del loco:')
                    if turn.lower() == 'puñetazo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['inmovilizado'] > 0:
                            print ('Estás inmovilizado y no puedes atacar')
                            break
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        if self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 4:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print ('fallas el puñetazo')
                            self.energy -= 2
                            self.energy += 2
                        else:
                            dano = 77 * ((self.locura / 100) + 1) / enemy.defense
                            if enemy.cargas['invencible'] == 1:
                                dano = 0
                            reflejo = dano * enemy.reflejar 
                            dano_total = dano - reflejo
                            enemy.health -= dano_total
                            self.health -= reflejo
                            if self.robovida > 1:
                                self.robovida = 1
                            elif self.robovida < 0:
                                self.robovida = 0
                            robado = dano_total * self.robovida
                            print ('Azotas a', enemy.name, 'con un puñetazo infligiendole', dano_total, 'de daño y silenciandolo 1 turno')
                            if enemy.reflejar > 0:
                                print (enemy.name, 'refleja', reflejo, 'de daño')
                            if robado != 0:
                                print (self.name, 'roba', robado, 'de vida')
                                self.health += robado
                            enemy.cargas['silenciado'] += 1
                            self.energy -= 4
                            self.energy += 2
                            self.cooldown[0] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'calma':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede invocar sombras')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                            if self.cargas['inmovilizado'] > 0:
                                self.cargas['inmovilizado'] -= 1
                        if self.energy <= 7:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print ('Te estresas')
                            self.energy -= 3.5
                            self.energy += 2
                        else:
                            print ('Te calmas y te curas', self.locura,'de vida')
                            self.health += self.locura
                            self.locura = 0
                            self.energy -= 7
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.cargas['hemorragia'], 'hemorragias,', enemy.cargas['sangrado'], 'sangrados,', enemy.cargas['quemado'], 'quemaduras,', enemy.cargas['cura'], 'cargas de cura,', enemy.cargas['veneno'], 'cargas de veneno', enemy.cargas['maldita'], 'cargas malditas y está', enemy.cargas['hielo'] + enemy.cargas['stun'] + enemy.cargas['paralizado'], 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.cargas['hemorragia'], 'hemorragias,', self.cargas['sangrado'], 'sangrados,', self.cargas['quemado'], 'quemaduras,', self.cargas['cura'],'cargas de cura,', self.cargas['veneno'], 'cargas de veneno y', self.cargas['maldita'], 'cargas malditas, estás', self.cargas['hielo'] + self.cargas['stun'] + self.cargas['paralizado'], 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'moneda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede detonar sus bombas')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        if self.energy <= 18:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print ('La moneda cayó a la alcantarilla')
                            self.energy -= 9
                            self.energy += 2
                        else:
                            boombaaa = randint (1, 100)
                            if boombaaa <= 50:
                                self.locura += 100
                                print ('Pierdes la apuesta y te vuelves loquisimo, aumentando tu locura en 100%')

                            elif boombaaa >= 51:
                                enemy.locura += 30
                                print ('Ganas la apuesta y te vuelves loquisimo, esto asusta mucho a', enemy.name,'y aumenta su locura en 30%')

                            self.energy -= 18
                            self.energy += 2
                        self.cooldown[2] = campo.nturnos + 3
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad moneda se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
locoloco = Loco('Fiiuuuu', 1888, 18, 1, 1, 46, 99, 200, 500, 100, 100, 0, 1, 0, 0, 0, 20, 0, 0, 'DPS+buff', 2)

class Root (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        self.conexionado = ''
        self.conexinv = ''
        self.conechealth = 0
        self.tempconex = 0
    def print_info(self):
        print ('Tipo: Natural')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "defensa suprema", aumenta tu defensa en 0.2, cuesta 15 de energía, tiene', self.preci1,'% precisión y 1 turno de cooldown')
        print ('Ataque 2: "raices", inflige 130 de daño y inmoviliza a tu enemigo 2 turnos, cuesta 30 de energía, tiene', self.preci2,'% precisión y 3 turnos de cooldown')
        print ('Ataque super: "conexion", todo el daño que reciba tu objetivo te será transferido cada turno por los próximos 3 turnos, cuesta 50 de energía, tiene', self.preci3,'% precisión y tiene 5 turnos de cooldown')
        print ('Ataque super: "conexion inversa", todo el daño que recibas hasta tu próximo turno será transferido a tu objetivo cada turno por los próximos 3 turnos, cuesta 50 de energía, tiene', self.preci3,'% precisión y tiene 5 turnos de cooldown')
        print ('Poción curativa: "cura", cura 100 de vida, cura 1-2 hemorragia y 1-3 quemadura, cuesta 50 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "Empezar con buen pie", Al principio de los tres turnos regeneras tu vida al máximo')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. ¿Quién está ahí?, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for naturalll in range (1):
            if self.conexionado != '':
                if self.tempconex >= campo.nturnos:
                    if self.conexionado.health < self.conechealth:
                        vidavidavida = self.conechealth - self.conexionado.health
                        print ('Transfieres', vidavidavida, 'de daño de', self.conexionado, 'a tí mismo')
                        self.conexionado.health = self.conechealth
                        self.health -= vidavidavida
                    
            if self.conexinv != '':
                if self.tempconex >= campo.nturnos:
                    if self.health < self.conechealth:
                        vidavidavida = self.conechealth - self.health
                        print ('Te transfieres', vidavidavida, 'de daño a', self.conexinv)
                        self.conexinv.health -= vidavidavida
                        self.health = self.conechealth

            if self.health <= 0:
                muertomuertoo = randint (1, 10)
                if muertomuertoo == 1 or muertomuertoo == 2 or muertomuertoo == 3 or muertomuertoo == 4:
                    print ('Sigues muerto, las plantas lloran por ello')
                elif muertomuertoo == 5 or muertomuertoo == 6 or muertomuertoo == 7:
                    print ('Sigues muerto,', enemy.name, 'te saca la lengua, dice que eres muy malo jugando')
                elif muertomuertoo == 8:
                    print ('Reviveeeeeeeeeeeeees')
                    print ('No te lo habrás creído, ¿No? jajaja')
                elif muertomuertoo == 9 or muertomuertoo == 10:
                    print ('Sigues muerto, el sol echa lágrimas de fuego por tu perdida')
            else:
                if campo.nturnos <= 4:
                    self.health = self.healthbase
                    self.maxhealth = self.healthbase
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno de', self.name + ':')
                    if turn.lower() == 'defensa suprema':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 15:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla!')
                            self.energy -= 4
                            self.energy += 4
                        else:
                            print ('Un árbol te proporciona una parte de armadura mejorando tu defensa en 0.2')
                            self.defense += 0.2
                            self.energy -= 15
                            self.energy += 4
                        self.cooldown[0] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'raices':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print (self.name, 'se confunde de hechizo y convierte una hoja de pasto en un gusano')
                            self.energy -= 30
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                print ('Unas raices atrapan las piernas de', enemy.name, 'infligiendole', super().atacar(enemy, 130, False), 'de daño y inmovilizandolo 2 turnos')
                                self.cargas['inmovilizado'] += 2
                                self.energy -= 30
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print ('Unas raices atrapan tus piernas infligiendote', 130 * self.power / self.defense, 'de daño y inmovilizandote 2 turnos')
                                    self.health -= 130 * self.power / self.defense
                                    self.cargas['inmovilizado'] += 2
                                    self.energy -= 30
                                    self.energy += 4
                                else:
                                    print ('Unas raices atrapan las piernas de', enemy.name, 'infligiendole', super().atacar(enemy, 130, False), 'de daño y inmovilizandolo 2 turnos')
                                    enemy.cargas['inmovilizado'] += 2
                                    self.energy -= 30
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        self.cooldown[1] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'conexion' or turn.lower() == 'conexión':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (1, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 50:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'se equivoca de hechizo y invoca una rana bebé inofensiva!')
                            self.energy -= 25
                            self.energy += 4
                        else:
                            self.conexionado = enemy
                            self.conechealth = enemy.health
                            self.tempconex = campo.nturnos + 3
                            print (self.name, 'se conecta con',enemy.name, 'todo el daño que reciba cada turno por los próximos 3 turnos te será transferido')
                            self.energy -= 50
                            self.energy += 4
                        self.cooldown[2] = campo.nturnos + 6
                        printdatos(self, enemy)
                    elif turn.lower() == 'conexion inversa' or turn.lower() == 'conexión inversa':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (1, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 50:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'se equivoca de hechizo y invoca una rana bebé inofensiva!')
                            self.energy -= 25
                            self.energy += 4
                        else:
                            self.conexinv = enemy
                            self.conechealth = self.health
                            self.tempconex = campo.nturnos + 3
                            print (self.name, 'se conecta con',enemy.name, 'todo el daño que recibas cada turno por los próximos 3 turnos le será transferido')
                            self.energy -= 50
                            self.energy += 4
                        self.cooldown[2] = campo.nturnos + 6
                        printdatos(self, enemy)
                    elif turn.lower() == 'cura':
                        super().cura(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad conexion/conexion inversa se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
raiz = Root ('Haywood', 2200, 260, 1, 1, 62, 100, 90, 400, 100, 100, 4, 1, 0, 0, 0, 40, 0, 0, 'DPS+supof', 3)

class SantaClaus(Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Misterioso')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "bola de nieve", congela 1 turno a tu objetivo, cuesta 2 de energía, tiene', self.preci1 ,'% precisión y 1 turno de cooldown')
        print ('Ataque 2: "mierda de reno", silencia al objetivo 2 turnos, cuesta 5 de energía, tiene 3 turno de cooldown y un', self.preci2 ,'% precisión')
        print ('Ataque super: "estres navideño", reduce el poder de tus enemigos en 0.3 por 3 turnos, cuesta 9 de energía, tiene ', self.preci3 ,'% precisión y 4 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 5 de energía y tiene ', self.precicura ,'% precisión')
        print ('Canalización: "energia", recupera 4 de energía y ', self.precienergia ,'% precisión')
        print ('Habilidad pasiva: "nieve", con cada habilidad tienes un 25% de congelar a tu objetivo')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas sin energia pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. JO JO JO, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for santa in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno de Santa Claus:')
                    if turn.lower() == 'bola de nieve':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 2:
                            print (self.name, 'no tiene suficiente energia)', '\n')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print ('Fallas el golpe')
                            self.energy -= 1
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                print (self.name, 'le lanza una bola de nieve a', enemy.name, 'congelandole 1 turno')
                                enemy.cargas['hielo'] += 1
                                nievee = randint (1, 100)
                                if nievee <= 25:
                                    enemy.cargas['hielo'] += 1
                                    print ('La nieve hace que', enemy.name, 'se congele un turno')
                                self.energy -= 2
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, 'se lanza una bola de nieve congeladose 1 turno')
                                    self.cargas['hielo'] += 1
                                    nievee = randint (1, 100)
                                    if nievee <= 25:
                                        self.cargas['hielo'] += 1
                                        print ('La nieve hace que te congeles un turno')
                                    self.energy -= 2
                                    self.energy += 2
                                else:
                                    print (self.name, 'le lanza una bola de nieve a', enemy.name, 'congelandole 1 turno')
                                    enemy.cargas['hielo'] += 1
                                    nievee = randint (1, 100)
                                    if nievee <= 25:
                                        enemy.cargas['hielo'] += 1
                                        print ('La nieve hace que', enemy.name, 'se congele un turno')
                                    self.energy -= 2
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[0] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'mierda de reno':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede atacar')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 8:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (enemy.name, 'se aparta y no le alcanzas')
                            self.energy -= 4
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                print (self.name, 'le lanza una bola de mierda de reno a', enemy.name, 'silenciandole 2 turno')
                                enemy.cargas['silenciado'] += 2
                                nievee = randint (1, 100)
                                if nievee <= 25:
                                    enemy.cargas['hielo'] += 1
                                    print ('La nieve hace que', enemy.name, 'se congele un turno')
                                self.energy -= 5
                                self.energy += 2
                            elif self.locura > 0:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    print (self.name, 'pisa una bola de mierda de reno silenciadose 2 turno')
                                    self.cargas['silenciado'] += 2
                                    nievee = randint (1, 100)
                                    if nievee <= 25:
                                        self.cargas['hielo'] += 1
                                        print ('La nieve hace que te congeles un turno')
                                    self.energy -= 5
                                    self.energy += 2
                                else:
                                    print (self.name, 'le lanza una bola de mierda de reno a', enemy.name, 'silenciandole 2 turno')
                                    enemy.silenciado += 1
                                    nievee = randint (1, 100)
                                    if nievee <= 25:
                                        enemy.cargas['hielo'] += 1
                                        print ('La nieve hace que', enemy.name, 'se congele un turno')
                                    self.energy -= 5
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown[1] = campo.nturnos + 4
                        printdatos(self, enemy)
                    elif turn.lower() == 'estres navideño' or turn.lower() == 'estrés navideño':
                        #cargas
                        cargas(self)
                        #el turno 
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede enfurecerse')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia', '\n')
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print ('Fallas!')
                            self.energy -= 4.5
                            self.energy += 2
                        else:
                            uuuumyenemy = input ('Selecciona multiples enemigos (Ejemplo: "1 2" para atacar a esos jugadores)')
                            if uuuumyenemy.find ('1') != -1:
                                for i in range (0,4):
                                    if uno.efecto[i] == '':
                                        uno.efecto[i] = 'bpower'
                                        uno.efecton[i] = 0.6
                                        uno.tiempo[i] = campo.nturnos + 4
                                        uno.power -= 0.6
                                        break

                            if uuuumyenemy.find ('2') != -1:
                                for i in range (0,4):
                                    if dos.efecto[i] == '':
                                        dos.efecto[i] = 'bpower'
                                        dos.efecton[i] = 0.6
                                        dos.tiempo[i] = campo.nturnos + 4
                                        dos.power -= 0.6
                                        break

                            if uuuumyenemy.find ('3') != -1:
                                for i in range (0,4):
                                    if tres.efecto[i] == '':
                                        tres.efecto[i] = 'bpower'
                                        tres.efecton[i] = 0.6
                                        tres.tiempo[i] = campo.nturnos + 4
                                        tres.power -= 0.6
                                        break

                            if uuuumyenemy.find ('4') != -1:
                                for i in range (0,4):
                                    if cuatro.efecto[0] == '':
                                        cuatro.efecto[0] = 'bpower'
                                        cuatro.efecton[0] = 0.6
                                        cuatro.tiempo[0] = campo.nturnos + 4
                                        cuatro.power -= 0.6
                                        break

                            if uuuumyenemy.find ('5') != -1:
                                for i in range (0,4):
                                    if cinco.efecto[0] == '':
                                        cinco.efecto[0] = 'bpower'
                                        cinco.efecton[0] = 0.6
                                        cinco.tiempo[0] = campo.nturnos + 4
                                        cinco.power -= 0.6
                                        break

                            if uuuumyenemy.find ('6') != -1:
                                for i in range (0,4):
                                    if seis.efecto[0] == '':
                                        seis.efecto[0] = 'bpower'
                                        seis.efecton[0] = 0.6
                                        seis.tiempo[0] = campo.nturnos + 4
                                        seis.power -= 0.6
                                        break

                            if uuuumyenemy.find ('7') != -1:
                                for i in range (0,4):
                                    if siete.efecto[0] == '':
                                        siete.efecto[0] = 'bpower'
                                        siete.efecton[0] = 0.6
                                        siete.tiempo[0] = campo.nturnos + 4
                                        siete.power -= 0.6
                                        break
                                
                            if uuuumyenemy.find ('8') != -1:
                                for i in range (0,4):
                                    if ocho.efecto[0] == '':
                                        ocho.efecto[0] = 'bpower'
                                        ocho.efecton[0] = 0.6
                                        ocho.tiempo[0] = campo.nturnos + 4
                                        ocho.power -= 0.6
                                        break

                            if uuuumyenemy.find ('9') != -1:
                                for i in range (0,4):
                                    if nueve.efecto[0] == '':
                                        nueve.efecto[0] = 'bpower'
                                        nueve.efecton[0] = 0.6
                                        nueve.tiempo[0] = campo.nturnos + 4
                                        nueve.power -= 0.6
                                        break

                            if uuuumyenemy.find ('10') != -1:
                                for i in range (0,4):
                                    if diez.efecto[0] == '':
                                        diez.efecto[0] = 'bpower'
                                        diez.efecton[0] = 0.6
                                        diez.tiempo[0] = campo.nturnos + 4
                                        diez.power -= 0.6
                                        break

                            print (self.name, 'estresa a sus enemigos bajandoles su poder en 0.6 por 3 turnos')
                            nievee = randint (1, 100)
                            if nievee <= 25:
                                enemy.cargas['hielo'] += 1
                                print ('La nieve hace que', enemy.name, 'se congele un turno')
                            self.power += 1
                            self.energy -= 9
                            self.energy += 2
                        self.cooldown[2] = campo.nturnos + 6
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad estres navideño se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
papanoel = SantaClaus('Santa Claus', 1790, 15, 1, 1, 32, 120, 90, 75, 100, 100, 0, 1, 0, 0, 0, 25, 0, 0, 'FSO', 3)

class Werewolf (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def print_info(self):
        print ('Tipo: Salvaje')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Robo de vida:', self.robovida * 100, '%')
        print ('Ataque 1: "ensangrentar", infliges 45 de daño, tiene un 35% de infligir un sangrado y robas 1-5 de sangre, cuesta 10 de energía y tiene un', self.preci1,'% precisión')
        print ('Ataque 2: "morder", inflige 80 de daño, te curas un 4% de la vida de tu enemigo y robas 4-8 de sangre, cuesta 30 de energía, tiene un', self.preci2,'% precisión y 1 turnos de cooldown')
        print ('Ataque super: "abalanzarse", infliges 120 de daño, tiene un 80% de infligir una hemorragia y robas 10-20 de sangre, cuesta 60 de energía, tiene un', self.preci3,'% precisión, y 3 turnos de cooldown')
        print ('Curación: "pasto", cura 120 de vida, cura 1-2 hemorragias, 1-3 quemaduras y aumenta tu poder en 0.2 (no afecta el poder), cuesta 60 de energía y tiene un', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 100 de energía y tiene un',self.precienergia,'% precisión')
        print ('Habilidad pasiva: "sangreee" cada tres turnos regenerara vida según la sangre de más que tenga (cada gota de sangre son 5 de vida que regenera), si al enemigo se le acaba la sangre perderá 400 de vida')
        print ('(Cada turno recuperas 5 de energia)(Si no tienes suficiente energia para lanzar un ataque pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)(Los personajes tipo salvaje no pueden volverse loco)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un lobo acecha en la oscuridad, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for werewolfff in range (1):
            if campo.nturnos % 3 == 0:
                if self.sangre > 100:
                    sobrante = self.sangre - 100
                    if sobrante > 0:
                        self.sangre -= sobrante
                        self.health += sobrante * 5
                        print ('Te alimentas de sangre curandote', sobrante * 5, 'puntos de vida')
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    turn = input('Turno del hombre lobo:')
                    if turn.lower() == 'ensangrentar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 5
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoo = randint (0,100)
                        if unoo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 5
                            self.energy += 5
                        else:
                            rojooo = randint (1, 5)
                            if enemy.sangre > rojooo:
                                enemy.sangre -= rojooo
                                self.sangre += rojooo
                            else:
                                rojooo = enemy.sangre
                                enemy.sangre -= rojooo
                                self.sangre += rojooo
                            print (self.name, 'desgarra la piel del brazo izquierdo de', enemy.name + ', el brazo comienza a sangrar, le infliges', super().atacar(enemy, 45, True),'de daño y le quitas', rojooo, 'gotas de sangre')
                            sangriento = randint (1, 100)
                            if sangriento <= 35:
                                print ('Infliges además un sangrado')
                                enemy.cargas['sangrado'] += 1
                            self.energy -= 10
                            self.energy += 5
                        printdatos(self,enemy)
                    elif turn.lower() == 'morder':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 5
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doos = randint(0, 100)
                        if doos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            self.energy += 5
                        else:
                            rojooo = randint (4, 8)
                            if enemy.sangre < rojooo:
                                rojooo = enemy.sangre
                                enemy.sangre -= rojooo
                                self.sangre += rojooo
                            else:
                                enemy.sangre -= rojooo
                                self.sangre += rojooo
                            print ('Muerde a', enemy.name, 'quitandole', super().atacar(enemy, 80, True), 'de vida, curádose', enemy.maxhealth - enemy.maxhealth * 96 / 100,'de vida y robando', rojooo, 'gotas de sangre')
                            self.health += enemy.maxhealth - enemy.maxhealth * 96 / 100
                            self.energy -= 30
                            self.energy += 5
                        self.cooldown[1] = campo.nturnos + 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'abalanzarse':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 5
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        trees = randint(0, 100)
                        if trees > self.preci3: 
                            print ('¡Fallas!')
                            self.energy -= 30
                            self.energy += 5
                        else:
                            rojooo = randint (10, 20)
                            if enemy.sangre > rojooo:
                                enemy.sangre -= rojooo
                                self.sangre += rojooo
                            else:
                                rojooo = enemy.sangre
                                enemy.sangre -= rojooo
                                self.sangre += rojooo
                            print ('Te abalanzas contra tu enemigo infligiendole', super().atacar(enemy, 120, True), 'de daño y quitandole', rojooo, 'gotas de sangre')
                            sangriento = randint (1, 100)
                            if sangriento <= 60:
                                print ('Infliges además una hemorragia')
                                enemy.cargas['hemorragia'] += 1
                            self.energy -= 60
                            self.energy += 5
                        self.cooldown[2] = campo.nturnos + 4
                        printdatos(self,enemy)
                    elif turn.lower() == 'pasto':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['inmovilizado'] > 0:
                            self.cargas['inmovilizado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 5
                            break
                        curaa = randint(0, 100)
                        if curaa > self.precicura: 
                            print ('¡El pasto se seca!')
                            self.energy -= 30
                            self.energy += 5
                        else:
                            if self.health >= self.maxhealth - 120 * self.power and self.health < self.maxhealth:
                                print ('Un pasto sanador te cura toda la vida y aumenta tu poder en 0.2')
                                self.health = self.maxhealth
                                self.power += 0.2
                                if self.cargas['hemorragia'] > 0:
                                    if self.cargas['hemorragia'] > 1:
                                        pastooo = randint (1, 2)
                                        print ('Además te curas', pastooo,'hemorragia/s')
                                        self.cargas['hemorragia'] -= pastooo
                                    else:
                                        print ('Además te curas 1 hemorragia')
                                        self.cargas['hemorragia'] -= 1
                                if self.cargas['quemado'] > 0:
                                    if self.cargas['quemado'] > 1:
                                        pastooo = randint (1, 3)
                                        print ('Además te curas', pastooo,'quemadura/s')
                                        self.cargas['quemado'] -= pastooo
                                    else:
                                        print ('Además te curas 1 quemadura')
                                        self.cargas['quemado'] -= 1
                                self.energy -= 60
                                self.energy += 5
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura aunque aumenta su poder en 0.2')
                                self.power += 0.2
                                if self.cargas['hemorragia'] > 0:
                                    if self.cargas['hemorragia'] > 1:
                                        pastooo = randint (1, 2)
                                        print ('Además te curas', pastooo,'hemorragia/s')
                                        self.cargas['hemorragia'] -= pastooo
                                    else:
                                        print ('Además te curas 1 hemorragia')
                                        self.cargas['hemorragia'] -= 1
                                if self.cargas['quemado'] > 0:
                                    if self.cargas['quemado'] > 1:
                                        pastooo = randint (1, 3)
                                        print ('Además te curas', pastooo,'quemadura/s')
                                        self.cargas['quemado'] -= pastooo
                                    else:
                                        print ('Además te curas 1 quemadura')
                                        self.cargas['quemado'] -= 1
                                self.energy -= 60
                                self.energy += 5
                            else:
                                print ('El pasto sanador te cura', 120 * self.power ,'de vida y aumenta tu poder en 0.2')
                                self.health += 120 * self.power
                                self.power += 0.2
                                if self.cargas['hemorragia'] > 0:
                                    if self.cargas['hemorragia'] > 1:
                                        pastooo = randint (1, 2)
                                        print ('Además te curas', pastooo,'hemorragia/s')
                                        self.cargas['hemorragia'] -= pastooo
                                    else:
                                        print ('Además te curas 1 hemorragia')
                                        self.cargas['hemorragia'] -= 1
                                if self.cargas['quemado'] > 0:
                                    if self.cargas['quemado'] > 1:
                                        pastooo = randint (1, 3)
                                        print ('Además te curas', pastooo,'quemadura/s')
                                        self.cargas['quemado'] -= pastooo
                                    else:
                                        print ('Además te curas 1 quemadura')
                                        self.cargas['quemado'] -= 1
                                self.energy -= 60
                                self.energy += 5
                        printdatos(self,enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad abalanzarse se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
werewolf = Werewolf('Romulus', 1860, 280, 1, 1, 76, 100, 90, 95, 100, 100, 5, 1, 0, 0, 0, 35, 0.08, 0, 'DPS', 3)

class Runeforge (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        self.vida_runa = 380
        self.pr_normal = 50
        self.pr_bueno = 30
        self.pr_notable = 14
        self.pr_sobresaliente = 5
        self.pr_masterpiece = 1

    def print_info(self):
        print ('Tipo: Guerrero')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "aplastar" inflige 90 de daño, cuesta 10 de energía y tiene un', self.preci1,'% precisión')
        print (f'Ataque 2: "forjar" forja una espada o armadura (aleatorio) que aumenta el poder o defensa del objetivo en un número aleatorio según la calidad de la pieza creada (aleatorio; normal (0.1 {self.pr_normal}%), bueno (0.2 {self.pr_bueno}%), notable (0.3 {self.pr_notable}%), sobresaliente (0.5 {self.pr_sobresaliente}%), obra maestra (1 {self.pr_masterpiece}%)), cuesta 30 de energía, tiene un', self.preci2,'% precisión y 4 turnos de cooldown')
        print (f'Ataque super: "runa" invoca una runa con {self.vida_runa} de vida. Mientras la runa dure el objetivo se vuelve invulnerable y no puede recibir daño, si se lo aplicas a alguien que no eres tu la runa tendrá un 40% menos de vida, cuesta 80 de energía, tiene un', self.preci3,'% precisión, y 6 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida, cura 1-2 hemorragias y 1-3 quemadura, cuesta 50 de energía y tiene un', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y tiene un', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "aprender" por cada turno que pase tiene más posibilidad de crear piezas de mayor calidad y runas con más vida (20 de vida por turno)')
        print ('(Cada turno recuperas 2 de energia)(Si no tienes suficiente energia para lanzar un ataque pierdes el turno) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un herrero sale de la forga con martillo en mano, ¡Es', self.name + '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for runeforgeee in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    self.vida_runa += 20
                    self.pr_normal -= 0.7
                    self.pr_bueno -= 0.2
                    self.pr_notable += 0.5
                    self.pr_sobresaliente += 0.3
                    self.pr_masterpiece += 0.1
                    turn = input('Turno del herrero:')
                    if turn.lower() == 'aplastar' or turn == '1':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['inmovilizado'] > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.cargas['inmovilizado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        unoo = randint (0,100)
                        if unoo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 5
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                print (self.name, 'aplasta a', enemy.name, 'con su martillo, infligiendo', super().atacar(enemy, 90, True), 'de daño')
                                self.energy -= 10
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa < self.locura:
                                    dano = 90 * self.power / enemy.defense
                                    if enemy.cargas['invencible'] == 1:
                                        dano = 0
                                    print (self.name, 'se vuelve loco y se aplasta el pie con su martillo, infligiedose', dano, 'de daño')
                                    self.health -= dano
                                    self.energy -= 10
                                    self.energy += 2
                                else:
                                    print (self.name, 'aplasta a', enemy.name, 'con su martillo, infligiendo', super().atacar(enemy, 90, True), 'de daño')
                                    self.energy -= 10
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'forjar' or turn.lower() == '2':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        doos = randint(0, 100)
                        if doos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            self.energy += 2
                        else:
                            forjar = randint (1, 100)
                            if forjar <= self.pr_normal:
                                cuality = 'normal'
                                points = 0.1
                            elif forjar <= self.pr_normal + self.pr_bueno:
                                cuality = 'bueno'
                                points = 0.2
                            elif forjar <= self.pr_normal + self.pr_bueno + self.pr_notable:
                                cuality = 'notable'
                                points = 0.3
                            elif forjar <= self.pr_normal + self.pr_bueno + self.pr_notable + self.pr_sobresaliente:
                                cuality = 'sobresaliente'
                                points = 0.5
                            elif forjar <= self.pr_normal + self.pr_bueno + self.pr_notable + self.pr_sobresaliente + self.pr_masterpiece:
                                cuality = 'obra mestra'
                                points = 1
                            forjar = randint (1, 10)
                            if forjar <= 5:
                                create = 'arma'
                            elif forjar > 5:
                                create = 'armadura'
                            print ('Forjas un/a', create, 'de calidad', cuality, 'por lo que sube su poder/defensa en', points)
                            if create == 'arma':
                                enemy.power += points
                            elif create == 'armadura':
                                enemy.defense += points
                            self.energy -= 30
                            self.energy += 2
                        self.cooldown[1] = campo.nturnos + 5
                        printdatos(self, enemy)
                    elif turn.lower() == 'runa':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 90:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Esta habilidad aún está en cooldown')
                            break
                        trees = randint(0, 100)  
                        if trees > self.preci3: 
                            print ('¡Fallas!')
                            self.energy -= 40
                            self.energy += 2
                        else:
                            if enemy != self:
                                runa.health = self.vida_runa * 40 / 100
                            else:
                                runa.health = self.vida_runa
                            if runa.runa_on:
                                print ('Ya hay una runa activa')
                            else:
                                print ('Protege a', enemy.name, 'con una runa con', runa.health, 'mientras esta runa este con vida', enemy.name, 'es invulnerable al daño')
                                runa.runa_on = True
                                runa.runa_own = enemy
                                enemy.cargas['invencible'] += 1
                            self.energy -= 80
                            self.energy += 2
                        self.cooldown[2] = campo.nturnos + 7
                        dacac (self, enemy)
                        printdatos(self, enemy)
                    elif turn.lower() == 'venda':
                        super().venda(enemy)
                    elif turn.lower() == 'energia':
                        super().energia(enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Tienes:', self.health,'puntos de vida y', self.energy, 'de energia')
                            print ('Estás en el turno', campo.nturnos)
                            print ('La habilidad forjar se puede volver a lanzar en el turno', self.cooldown[1])
                            print ('La habilidad runa se puede volver a lanzar en el turno', self.cooldown[2])
                            super().printinfo(enemy)
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Estás silenciado')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
herrero = Runeforge ('Torvak', 1930, 310, 1, 1, 40, 100, 200, 200, 100, 100, 1, 1, 0, 0, 0, 30, 0, 0, 'DPS+supdef', 2)

class Serenita (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        self.constancia = 1
        self.costanza = 30 * self.constancia
        self.tconstancia = 0
        self.aliados = []
        
    def print_info(self):
        print ('Tipo: Maga')
        print('Salute:', self.health)
        print('Energía:', self.energy)
        print ('Potere:', self.power)
        print ('Difesa:', self.defense)
        print ('Velocità:', self.velocity)
        print ('Attacco 1: Armonia dell’Anima, "Armonia": Cura 150 punti vita. Se l’obiettivo è sotto il 50% → cura 250. Se è sopra il 50% → aumenta il suo potere di 0.05. Costa 15 energia, ha', self.preci1,'% di precisione e 1 turno di recupero')
        print ('Attacco 2: "Scelta": 1 → aumenta la difesa dell’obiettivo di 0.15. 2 → aumenta il potere dell’obiettivo di 0.15. Costa 40 energia, ha', self.preci2,'% di precisione e 3 turni di recupero')
        print ('Attacco supremo: Luce di Parma, "Luce": Rimuove tutti gli stati negativi e raddoppia l’intensità di Costanza per 4 turni. Costa 60 energia, ha', self.preci3,'% di precisione e 5 turni di recupero')
        print ('Pozione curativa: "curar": seleziona un obiettivo e gli cura 100 punti vita, rimuove 1-2 emorragie e 1-3 ustioni. Costa 50 energia e ha', self.precicura,'% di precisione')
        print ('Canalizzazione: "energiar": seleziona un obiettivo e gli ripristina 80 punti energia. Ha', self.precienergia,'% di precisione')
        print ('Abilità passiva: "Costanza": Gli alleati rigenerano 30 punti vita ogni turno finché', self.name,'resta in vita.')
        print ('(Ogni turno recuperi 4 energia) (Se rimani senza energia perdi il turno) (Le tue azioni sono moltiplicate per il potere e i danni ricevuti sono ridotti in base alla difesa)', '\n')
    def hello(self):
        print ('NUOVO EROE. Da Parma arriva la luce che con un sorriso cura anche la malattia più terribile… è', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for elenaaaa in range (1):
            if self.health <= 0:
                pass
            else:
                quiza = super().canplay(enemy)
                if not quiza:
                    return
                else:
                    if self.tconstancia <= campo.nturnos:
                        self.costanza = 1
                    for i in self.aliados:
                        i.health += self.costanza
                        print (self.name, 'regenera', self.costanza, 'de vida a', i.name)
                    turn = input('Il turno di Serenità:')
                    if turn.lower().find('armonia') != -1:
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            self.cargas['silenciado'] -= 1
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'è paralizzato e non può fare nulla')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'non si paralizza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 15:
                            print (self.name, 'non ha abbastanza energia')
                            self.energy += 4
                            break
                        if self.cooldown[0] > campo.nturnos:
                            print ('Questa abilità è ancora in fase di recupero')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('La', self.name, 'fallisce la guarigione!')
                            self.energy -= 7
                        else:
                            if enemy.health > enemy.maxhealth / 2:
                                print (self.name, 'cura', 150 * self.power * self.lcura * enemy.rcura, 'di salute al suo alleato e aumenta il suo potere di 0.05')
                                enemy.health += 150 * self.power * self.lcura * enemy.rcura
                                enemy.power += 0.05
                            elif enemy.health < enemy.maxhealth / 2:
                                print (self.name, 'corre ad aiutare il suo alleato e lo cura di', 150 * self.power * self.lcura * enemy.rcura, 'punti salute')
                                enemy.health += 250 * self.power * self.lcura * enemy.rcura
                            elif enemy.health == enemy.maxhealth / 2:
                                print (self.name, 'trova l’equilibrio perfetto e cura', 350 * self.power * self.lcura * enemy.rcura, 'punti salute aumentando il potere di 0.15')
                                enemy.health += 350 * self.power * self.lcura * enemy.rcura
                                enemy.power += 0.15
                            
                            self.energy -= 15
                        self.cooldown[0] = campo.nturnos + 2
                        self.energy += 4
                        printdatosIT(self, enemy)
                    elif turn.lower() == 'scelta':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'è silenziata e non può lanciare questo incantesimo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'è paralizzato e non può fare nulla')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'non si paralizza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 40:
                            print (self.name, 'non ha abbastanza energia')
                            self.energy += 4
                            break
                        if self.cooldown[1] > campo.nturnos:
                            print ('Questa abilità è ancora in recupero')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print (self.name, 'sbaglia incantesimo e rende il cielo rosa per 2 secondi')
                            self.energy -= 20
                            self.energy += 4
                        else:
                            true = True
                            while true:
                                scelta = input ('1-difesa, 2-potere')
                                if scelta == '1' or scelta == '2':
                                    true = False
                                else:
                                    print ('Questa non è un’opzione')
                            if scelta == '1':
                                print (self.name, 'usa un incantesimo magico per migliorare l’armatura di', enemy.name,'di', 0.15 * self.power)
                                enemy.defense += 0.15 * self.power
                            elif scelta == '2':
                                print (self.name, 'usa un incantesimo magico per aumentare la potenza dell’arma di', enemy.name,'di', 0.15 * self.power)
                                enemy.power += 0.15 * self.power
                        self.energy -= 40
                        self.cooldown[1] = campo.nturnos + 4
                        printdatosIT(self, enemy)
                    elif turn.lower().find('luce') != -1:
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'è silenziata e non può lanciare questo incantesimo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'è paralizzato e non può fare nulla')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'non si paralizza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 60:
                            print (self.name, 'non ha abbastanza energia')
                            self.energy += 4
                            break
                        if self.cooldown[2] > campo.nturnos:
                            print ('Questa abilità è ancora in recupero')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print (self.name, 'sbaglia incantesimo e evoca un piccolo topolino!!')
                            self.energy -= 30
                        else:
                            print (self.name, 'abbraccia',enemy.name, 'rimuovendo tutti gli effetti negativi e raddoppiando il ritmo di Costanza')
                            purificar(enemy)
                            self.constancia = 2
                            self.tconstancia = campo.nturnos + 5
                            self.energy -= 60
                        self.energy += 4
                        self.cooldown[2] = campo.nturnos + 6
                        printdatos(self, enemy)
                    elif turn.lower() == 'curar':
                        cargas(self)
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'è silenziata e non può lanciare questo incantesimo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'è paralizzato e non può fare nulla')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'non si paralizza')
                                self.cargas['paralizado'] -= 1
                        if self.energy <= 50:
                            print (self.name, 'non ha abbastanza energia')
                            self.energy += 4
                        else:
                            curaaa = randint(0, 100)
                            if curaaa > self.precicura: 
                                print ('La pozione si rompe!')
                                self.energy -= 25
                                self.energy += 4
                            else:
                                print ('Dai una pozione a', enemy.name, 'che gli cura', 100 * self.power ,'punti vita')
                                enemy.health += 100 * self.power
                                if self.cargas['hemorragia'] > 0:
                                    if self.cargas['hemorragia'] > 1:
                                        pastooo = randint (1, 2)
                                        print ('Inoltre curi', pastooo,'emorragia/e')
                                        self.cargas['hemorragia'] -= pastooo
                                    else:
                                        print ('Inoltre curi 1 emorragia')
                                        self.cargas['hemorragia'] -= 1
                                if self.cargas['quemado'] > 0:
                                    if self.cargas['quemado'] > 1:
                                        pastooo = randint (1, 3)
                                        print ('Inoltre curi', pastooo,'ustione/i')
                                        self.cargas['quemado'] -= pastooo
                                    else:
                                        print ('Inoltre curi 1 ustione')
                                        self.cargas['quemado'] -= 1
                                self.energy -= 50
                                self.energy += 2
                        printdatos(self, enemy)
                    elif turn.lower() == 'energiar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.cargas['silenciado'] > 0:
                            print (self.name, 'è silenziata e non può lanciare questo incantesimo')
                            self.cargas['silenciado'] -= 1
                            break
                        elif self.cargas['paralizado'] > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'è paralizzato e non può fare nulla')
                                self.cargas['paralizado'] -= 1
                                break
                            else:
                                print (self.name, 'non si paralizza')
                                self.cargas['paralizado'] -= 1
                        energiaaa = randint(0, 100)
                        if energiaaa > self.precienergia: 
                            print (self.name, 'fallisce nel canalizzare!')
                            self.energy += 4
                        else:
                            print (self.name, 'canalizza e recupera', 80 * self.power, 'di energia per', enemy.name)
                            enemy.energy += 80 * self.power
                            self.energy += 4
                        printdatosIT(self, enemy)
                    elif turn.lower() == 'stats':
                        if self.cargas['silenciado'] > 0:
                            print ('Sei silenziato')
                        else:
                            print ('Sei al turno', campo.nturnos)
                            print ('L’abilità Proteggere potrà essere riutilizzata al turno', self.cooldown[2])
                            print ('La precisione dell’attacco uno è:', self.preci1, '%')
                            print ('La precisione dell’attacco due è:', self.preci2, '%')
                            print ('La precisione dell’attacco tre è:', self.preci3, '%')
                            print ('La precisione della guarigione è:', self.precicura, '%')
                            print ('La precisione della canalizzazione è:', self.precienergia, '%')
                            print ('La potenza di guarigione è:', self.lcura * 100 ,'%')
                            print ('La guarigione ricevuta è:', self.rcura * 100, '%')
                            print ('La quantità di sangue è', self.sangre,'/100')
                            print ('Rubi il', self.robovida * 100, '% di vita')
                            print ('Il livello di follia è:', self.locura,'%')
                            print ('Rifletti il', self.reflejar,'% del danno ricevuto')
                        self.turno (enemy)
                    elif turn.lower() == 'info':
                        self.print_info()
                        self.turno (enemy)
                    elif turn.lower() == 'equip':
                        if self.cargas['silenciado'] > 0:
                            print ('Sei silenziato')
                            self.cargas['silenciado'] -= 1
                        else:
                            self.armorspell = 1
                    else:
                        print ('Male', '\n')
                        self.turno (enemy)
her = Serenita('Elena', 1550, 200, 1, 1, 38, 110, 110, 110, 100, 100, 3, 1, 0, 0, 0, 60, 0, 0, 'healer', 1)

class BoxBlue (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)

    def turno (self):
        boxblue.nturnos += 1
        if self.cargas['hielo'] > 0:
            print ('La caja está congelada y no es afectada por efectos de daño continuo')
            self.cargas['hielo'] -= 1
        else:
            cargas(self)
boxblue = BoxBlue ('Caja Azul', 2000, 1000000, 1, 5, 0, 100, 100, 100, 100, 100, 10, 1, 0, 0, 0, 90, 0, 0, 'caja', 0.5)

class BoxRed (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        
    def turno (self):
        boxred.nturnos += 1
        if self.cargas['hielo'] > 0:
            print ('La caja está congelada y no es afectada por efectos de daño continuo')
            self.cargas['hielo'] -= 1
        else:
            cargas(self)
boxred = BoxRed ('Caja Roja', 2000, 1000000, 1, 5, 0, 100, 100, 100, 100, 100, 10, 1, 0, 0, 0, 90, 0, 0, 'caja', 0.5)

class bichos (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
   
    def turno (self, enemy): # enemy = LISTA jugador/es
        agros = list()
        for i in enemy:
            agros.append(i.agro)
        agros.sort()
        golpear = agros[len(enemy) - 1]
        ataque = randint (1, 4)
        if self.tipo == 0:
            pass
bichoprueba = bichos ('Bicho Prueba', 2000, 1000000, 1, 5, 0, 100, 100, 100, 100, 100, 10, 1, 0, 0, 0, 90, 0, 0, 'bicho', 1)

class Externos (Hero):
    def __init__(self, name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio):
        super().__init__(name, maxhealth, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, tipo, mundo , mutado, locura, reflejar, agro, robovida, invisible, rol, prio)
        self.runa_on = False
        self.runa_own = ''
    def recibir_dano_runa (self, damage):
        self.health -= damage
        if self.health <= 0:
            print("¡La runa fue destruida! El escudo de invulnerabilidad ha desaparecido.")
            self.runa_own.cargas['invencible'] -= 1
            self.runa_on = False
        else:
            print(f"¡La runa absorbió el daño! Le quedan {self.health} de vida.")
runa = Externos('runa', 400, 100, 1, 1, 0, 100, 100, 100, 100, 100, 10, 1 , 0, 0, 0, 20, 0, 0, 'runa', 1)

class equips():
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        self.casco = ''
        self.armadura = ''
        self.botas = ''
        self.capa = ''
        self.amuleto = ''
        self.cooldowncasco = 0
        self.cooldownarmaduras = 0
        self.cooldownbotas = 0
        self.cooldowncapa = 0

class equip1(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento1 = equip1('', '', '', '', '', 0, 0, 0, 0)

class equip2(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento2 = equip2('', '', '', '', '', 0, 0, 0, 0)

class equip3(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento3 = equip3('', '', '', '', '', 0, 0, 0, 0)

class equip4(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento4 = equip4('', '', '', '', '', 0, 0, 0, 0)

class equip5(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento5 = equip5('', '', '', '', '', 0, 0, 0, 0)

class equip6(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento6 = equip6('', '', '', '', '', 0, 0, 0, 0)

class equip7(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento7 = equip7('', '', '', '', '', 0, 0, 0, 0)

class equip8(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento8 = equip8('', '', '', '', '', 0, 0, 0, 0)

class equip9(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento9 = equip9('', '', '', '', '', 0, 0, 0, 0)

class equip10(equips):
    def __init__(self, casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa):
        super().__init__(casco, armadura, botas, capa, amuleto, cooldowncasco, cooldownarmaduras, cooldownbotas, cooldowncapa)
equipamiento10 = equip10('', '', '', '', '', 0, 0, 0, 0)

class numerojugadores():
    def __init__(self, numjug):
        self.numjug = numjug
numjuga = numerojugadores (0)

class Campo():
    def __init__ (self, lluvia, hierba, sol, nevar, purificador, trrr, nturnos):
        self.lluvia = lluvia
        self.hierba = hierba
        self.sol = sol
        self.nevar = nevar
        self.purificador = purificador
        self.trrr = trrr
        self.nturnos = nturnos
campo = Campo(0, 0, 0, 0, 0, 0, 0)

#partidas 

uno = ''
dos = ''
tres = ''
cuatro = ''
cinco = ''
seis = ''
siete = ''
ocho = ''
nueve = ''
diez = ''

cuantosplayers = input ('Introduzca un numero (2, 3, 4, 6) para jugar una partida a muerte de ese mismo numero de jugadores o introduzca "atraco" para jugar un 3vs3 a destruir la caja enemiga')
if cuantosplayers == '2':
    numjuga.numjug = 2
    uno = input('Jugador 1, escoja su personaje: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Mace, Fires, Snake Charner, Apostador, Natural, Diablillo, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge')
    if uno.lower() == 'build':
        equipbuild (equipamiento1, uno)
        uno = input('Jugador 1, escoja su personaje:')
    check_personaje(uno)

    while True:
        dos = input('Jugador 2, escoja su personaje: (No repetir)')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break
    if dos.lower() == 'build':
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje: (No repetir)')
            if dos == uno:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(dos)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    jugadores = [uno, dos]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        print ('La pelea está patas arriba y los menos veloces atacan primero')
        uno.hello()
        dos.hello()
        while uno.health >= 0 or dos.health >= 0:
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.sort()
            second = velocities [1]
            first = velocities [0]
            players = [first, second]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'dos', '1')
                if i == dos.velocity:
                    play (dos, 'dos', '2')
                if uno.health <= 0 and dos.health <= 0:
                    print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                elif dos.health <= 0:
                    print ('Jugador 1 WIIIIN')
                elif uno.health <= 0:
                    print ('Jugador 2 WIIIIN')

    if escenario != 10:
        uno.hello()
        dos.hello()
        while uno.health >= 0 or dos.health >= 0:
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.sort()
            first = velocities [1]
            second = velocities [0]
            players = [first, second]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'dos', '1')
                if i == dos.velocity:
                    play (dos, 'dos', '2')
                if uno.health <= 0 and dos.health <= 0:
                    print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                elif dos.health <= 0:
                    print ('Jugador 1 WIIIIN')
                elif uno.health <= 0:
                    print ('Jugador 2 WIIIIN')

if cuantosplayers.find('2') != -1 and cuantosplayers.find('comp') != -1:
    numjuga.numjug = 2
    bloqueo1 = input('Jugador 1, escoja un personaje para bloquear: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Mace, Fires, Snake Charner, Apostador, Natural, Diablillo, Chiquitin, Guadaña, Crossbow, Loco, Root, Werewolf, Runeforge')
    bloqueo2 = input('Jugador 2, escoja un personaje para bloquear')
    print ('jugador 1 seleccione equipamiento:')
    equipbuild (equipamiento1, uno)
    while True:
        uno = input('Jugador 1, escoja su personaje:')
        if uno == bloqueo1 or uno == bloqueo2:
            print ('Ese personaje está bloqueado')
        else:
            break
    check_personaje(uno)

    print ('jugador 2 seleccione equipamiento:')
    equipbuild (equipamiento2, dos)
    while True:
        dos = input('Jugador 2, escoja su personaje: (No repetir)')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        elif dos == bloqueo1 or dos == bloqueo2:
            print ('Ese personaje está bloqueado')
        else:
            break
    check_personaje(dos)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    jugadores = [uno, dos]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            uno.hello()
            dos.hello()
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            while uno.health >= 0 or dos.health >= 0:
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                players = [first, second]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'dos', '1')
                    if i == dos.velocity:
                        play (dos, 'dos', '2')
                    if uno.health <= 0 and dos.health <= 0:
                        print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                    elif dos.health <= 0:
                        print ('Jugador 1 WIIIIN')
                    elif uno.health <= 0:
                        print ('Jugador 2 WIIIIN')

    if escenario != 10 or escenario != 11:
        uno.hello()
        dos.hello()
        while uno.health >= 0 or dos.health >= 0:
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.sort()
            first = velocities [1]
            second = velocities [0]
            players = [first, second]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'dos', '1')
                if i == dos.velocity:
                    play (dos, 'dos', '2')
                if uno.health <= 0 and dos.health <= 0:
                    print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                elif dos.health <= 0:
                    print ('Jugador 1 WIIIIN')
                elif uno.health <= 0:
                    print ('Jugador 2 WIIIIN')

elif cuantosplayers == '3':
    numjuga.numjug = 3
    uno = input('Jugador 1, escoja su personaje: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    if uno.lower() == 'build':
        equipbuild (equipamiento1, uno)
        uno = input('Jugador 1, escoja su personaje:')
    check_personaje(uno)
    while True:
        dos = input('Jugador 2, escoja su personaje: (No repetir)')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break
    if dos.lower() == 'build':
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje: (No repetir)')
            if dos == uno:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(dos)
    while True:
        tres = input('Jugador 3, escoja su personaje:')
        if tres == uno or tres == dos:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if tres.lower() == 'build':
        equipbuild (equipamiento3, tres)
        while True:
            tres = input('Jugador 3, escoja su personaje: (No repetir)')
            if tres == uno or tres == dos:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(tres)
    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    tres = translate(tres)
    jugadores = [uno, dos, tres]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos, tres]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos, tres]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos, tres]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos, tres]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos, tres]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos, tres]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos, tres]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            uno.hello()
            dos.hello()
            tres.hello()
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.append (tres.velocity)
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0:
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                players = [first, second, third]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'tres', '1')
                    if i == dos.velocity:
                        play (dos, 'tres', '2')
                    if i == tres.velocity:
                        play (tres, 'tres', '3')
                    if uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                        print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                    elif dos.health <= 0 and tres.health <= 0:
                        print ('Jugador 1 WIIIIN')
                    elif uno.health <= 0 and tres.health <= 0:
                        print ('Jugador 2 WIIIIN')
                    elif uno.health <= 0 and dos.health <= 0:
                        print ('Jugador 3 WIIIIN')

    if escenario != 10:
        uno.hello()
        dos.hello()
        tres.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0:
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.append (tres.velocity)
            velocities.sort()
            first = velocities [2]
            second = velocities [1]
            third = velocities [0] 
            players = [first, second, third]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'tres', '1')
                if i == dos.velocity:
                    play (dos, 'tres', '2')
                if i == tres.velocity:
                    play (tres, 'tres', '3')
                if uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                    print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                elif dos.health <= 0 and tres.health <= 0:
                    print ('Jugador 1 WIIIIN')
                elif uno.health <= 0 and tres.health <= 0:
                    print ('Jugador 2 WIIIIN')
                elif uno.health <= 0 and dos.health <= 0:
                    print ('Jugador 3 WIIIIN')

elif cuantosplayers.find('3') != -1 and cuantosplayers.find ('comp') != -1:
    numjuga.numjug = 3
    bloqueo1 = input('Jugador 1, escoja un personaje para bloquear: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    bloqueo2 = input('Jugador 2, escoja un personaje para bloquear')
    bloqueo3 = input('Jugador 3, escoja un personaje para bloquear')
    uno == 'build'
    if uno == 'build':
        print ('jugador 1 seleccione equipamiento:')
        equipbuild (equipamiento1, uno)
    while True:
        uno = input('Jugador 1, escoja su personaje:')
        if uno == bloqueo1 or uno == bloqueo2 or uno == bloqueo3:
            print ('Ese personaje está bloqueado')
        else:
            break
    check_personaje(uno)

    dos = 'build'
    if dos.lower() == 'build':
        print ('jugador 2 seleccione equipamiento:')
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje: (No repetir)')
            if dos == uno:
                print ('No se pueden repetir personajes!!')
            elif dos == bloqueo1 or dos == bloqueo2 or dos == bloqueo3:
                print ('Ese personaje está bloqueado')
            else:
                break
    check_personaje(dos)

    tres = 'build'
    if tres.lower() == 'build':
        print ('jugador 3 seleccione equipamiento:')
        equipbuild (equipamiento3, tres)
    while True:
        tres = input('Jugador 3, escoja su personaje:')
        if tres == uno or tres == dos:
            print ('No se pueden repetir personajes!!')
        elif tres == bloqueo1 or tres == bloqueo2 or tres == bloqueo3:
            print ('Ese personaje está bloqueado')
        else:
            break
    check_personaje(tres)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    tres = translate(tres)
    jugadores = [uno, dos, tres]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos, tres]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos, tres]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos, tres]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos, tres]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos, tres]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos, tres]
        for i in players:
            i.jpreci1 -= 20
            i.jpreci2 -= 20
            i.jpreci3 -= 20
            i.jprecicura -= 20
            i.jprecienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos, tres]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            uno.hello()
            dos.hello()
            tres.hello()
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.append (tres.velocity)
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0:
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                players = [first, second, third]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'tres', '1')
                    if i == dos.velocity:
                        play (dos, 'tres', '2')
                    if i == tres.velocity:
                        play (tres, 'tres', '3')
                    if uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                        print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                    elif dos.health <= 0 and tres.health <= 0:
                        print ('Jugador 1 WIIIIN')
                    elif uno.health <= 0 and tres.health <= 0:
                        print ('Jugador 2 WIIIIN')
                    elif uno.health <= 0 and dos.health <= 0:
                        print ('Jugador 3 WIIIIN')
                                        
    if escenario != 10:
        uno.hello()
        dos.hello()
        tres.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0:
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.append (tres.velocity)
            velocities.sort()
            first = velocities [2]
            second = velocities [1]
            third = velocities [0] 
            players = [first, second, third]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'tres', '1')
                if i == dos.velocity:
                    play (dos, 'tres', '2')
                if i == tres.velocity:
                    play (tres, 'tres', '3')
                if uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                    print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                elif dos.health <= 0 and tres.health <= 0:
                    print ('Jugador 1 WIIIIN')
                elif uno.health <= 0 and tres.health <= 0:
                    print ('Jugador 2 WIIIIN')
                elif uno.health <= 0 and dos.health <= 0:
                    print ('Jugador 3 WIIIIN')


elif cuantosplayers == '4':
    numjuga.numjug = 4
    nah = True
    while nah:
        teams = input ('2v2? (s/n)')
        if teams.lower() == 's':
            teams = True
            print ('Los equipos son 1 & 2, 3 & 4')
            nah = False
        elif teams.lower() == 'n':
            teams = False
            nah = False
        else:
            print ('Eso NO es una opción')
    uno = input('Jugador 1, escoja su personaje: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    if uno.lower() == 'build':
        equipbuild (equipamiento1, uno)
        uno = input('Jugador 1, escoja su personaje:')
    check_personaje(uno)

    while True:
        dos = input('Jugador 2, escoja su personaje: (No repetir)')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break
    if dos.lower() == 'build':
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje: (No repetir)')
            if dos == uno:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(dos)

    while True:
        tres = input('Jugador 3, escoja su personaje:')
        if tres == uno or tres == dos:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if tres.lower() == 'build':
        equipbuild (equipamiento3, tres)
        while True:
            tres = input('Jugador 3, escoja su personaje: (No repetir)')
            if tres == uno or tres == dos:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(tres)

    while True:
        cuatro = input('Jugador 4, escoja su personaje:')
        if cuatro == uno or cuatro == dos or cuatro == tres:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if cuatro.lower() == 'build':
        equipbuild (equipamiento4, cuatro)
        while True:
            cuatro = input('Jugador 4, escoja su personaje: (No repetir)')
            if cuatro == uno or cuatro == dos or cuatro == tres:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(cuatro)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    tres = translate(tres)
    cuatro = translate(cuatro)
    jugadores = [uno, dos, tres, cuatro]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos, tres, cuatro]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos, tres, cuatro]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos, tres, cuatro]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos, tres, cuatro]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos, tres, cuatro]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos, tres, cuatro]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos, tres, cuatro]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            players = [uno, dos, tres, cuatro]
            for i in players:
                i.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
                velocities = list()
                players = [uno, dos, tres, cuatro]
                for i in players:
                    velocities.append (i.velocity)
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                fourth = velocities [3]
                players = [first, second, third, fourth]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'cuatro', '1')
                    if i == dos.velocity:
                        play (dos, 'cuatro', '2')
                    if i == tres.velocity:
                        play (tres, 'cuatro', '3')
                    if i == cuatro.velocity:
                        play (cuatro, 'cuatro', '4')
                    check_dies (teams, 4)

    if escenario != 10:
        uno.hello()
        dos.hello()
        tres.hello()
        cuatro.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
            velocities = list()
            players = [uno, dos, tres, cuatro]
            for i in players:
                velocities.append (i.velocity)
            velocities.sort()
            first = velocities [3]
            second = velocities [2]
            third = velocities [1] 
            fourth = velocities [0]
            players = [first, second, third, fourth]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'cuatro', '1')
                if i == dos.velocity:
                    play (dos, 'cuatro', '2')
                if i == tres.velocity:
                    play (tres, 'cuatro', '3')
                if i == cuatro.velocity:
                    play (cuatro, 'cuatro', '4')
                check_dies (teams, 4)

elif cuantosplayers.find('4') != -1 and cuantosplayers.find ('comp') != -1:
    nah = True
    while nah:
        teams = input ('2v2? (s/n)')
        if teams.lower() == 's':
            teams = True
            print ('Los equipos son 1 & 2, 3 & 4')
            nah = False
        elif teams.lower() == 'n':
            teams = False
            nah = False
        else:
            print ('Eso NO es una opción')
    bloqueo1 = input('Jugador 1, escoja un personaje para bloquear: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    bloqueo2 = input('Jugador 2, escoja un personaje para bloquear:')
    bloqueo3 = input('Jugador 3, escoja un personaje para bloquear:')
    bloqueo4 = input('Jugador 4, escoja un personaje para bloquear:')
    numjuga.numjug = 4
    uno = 'build'
    if uno.lower() == 'build':
        print ('jugador 1 seleccione equipamiento:')
        equipbuild (equipamiento1, uno)
        while True:
            uno = input('Jugador 1, escoja su personaje:')
            if uno == bloqueo1 or uno == bloqueo2 or uno == bloqueo3 or uno == bloqueo4:
                print ('Ese personaje está bloqueado')
            else:
                break
    check_personaje(uno)

    dos = 'build'
    if dos.lower() == 'build':
        print ('jugador 2 seleccione equipamiento:')
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje:')
            if dos == bloqueo1 or dos == bloqueo2 or dos == bloqueo3 or dos == bloqueo4:
                print ('Ese personaje está bloqueado')
            elif dos == uno:
                print ('Ese personaje ya está seleccionado')
            else:
                break
    check_personaje(dos)

    tres = 'build'
    if tres.lower() == 'build':
        print ('jugador 3 seleccione equipamiento:')
        equipbuild (equipamiento3, tres)
        while True:
            tres = input('Jugador 3, escoja su personaje:')
            if tres == bloqueo1 or tres == bloqueo2 or tres == bloqueo3 or tres == bloqueo4:
                print ('Ese personaje está bloqueado')
            elif tres == uno or tres == dos:
                print ('Ese personaje ya está seleccionado')
            else:
                break
    check_personaje(tres)

    cuatro = 'build'
    if cuatro.lower() == 'build':
        print ('jugador 4 seleccione equipamiento:')
        equipbuild (equipamiento4, cuatro)
        while True:
            cuatro = input('Jugador 4, escoja su personaje:')
            if cuatro == bloqueo1 or cuatro == bloqueo2 or cuatro == bloqueo3 or cuatro == bloqueo4:
                print ('Ese personaje está bloqueado')
            elif cuatro == uno or cuatro == dos or cuatro == tres:
                print ('Ese personaje ya está seleccionado')
            else:
                break
    check_personaje(cuatro)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    tres = translate(tres)
    cuatro = translate(cuatro)
    jugadores = [uno, dos, tres, cuatro]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos, tres, cuatro]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos, tres, cuatro]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos, tres, cuatro]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos, tres, cuatro]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos, tres, cuatro]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos, tres, cuatro]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos, tres, cuatro]
        for i in players:
            i.energy += 1000000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            players = [uno, dos, tres, cuatro]
            for i in players:
                i.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
                velocities = list()
                players = [uno, dos, tres, cuatro]
                for i in players:
                    velocities.append (i.velocity)
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                fourth = velocities [3]
                players = [first, second, third, fourth]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'cuatro', '1')
                    if i == dos.velocity:
                        play (dos, 'cuatro', '2')
                    if i == tres.velocity:
                        play (tres, 'cuatro', '3')
                    if i == cuatro.velocity:
                        play (cuatro, 'cuatro', '4')
                    check_dies (teams, 4)
                
    if escenario != 10:
        players = [uno, dos, tres, cuatro]
        for i in players:
            i.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
            velocities = list()
            players = [uno, dos, tres, cuatro]
            for i in players:
                velocities.append (i.velocity)
            velocities.sort()
            first = velocities [3]
            second = velocities [2]
            third = velocities [1] 
            fourth = velocities [0]
            players = [first, second, third, fourth]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'cuatro', '1')
                if i == dos.velocity:
                    play (dos, 'cuatro', '2')
                if i == tres.velocity:
                    play (tres, 'cuatro', '3')
                if i == cuatro.velocity:
                    play (cuatro, 'cuatro', '4')
                check_dies (teams, 4)

elif cuantosplayers.lower() == '6':
    numjuga.numjug = 6
    nah = True
    while nah:
        teams = input ('Todos contra Todos, 2v2v2 o 3v3? (1/2/3)')
        if teams.lower() == '2':
            teams = '2v2v2'
            print ('Los equipos son 1 & 2, 3 & 4, 5 & 6')
            nah = False
        elif teams.lower() == '3':
            teams = '3v3'
            print ('Los equipos son 1 & 2 & 3, 4 & 5 & 6')
            nah = False
        elif teams.lower() == '1':
            teams = True
            nah = False
        else:
            print ('Eso NO es una opción')
    uno = input('Jugador 1, escoja su personaje: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    if uno.lower() == 'build':
        equipbuild (equipamiento1, uno)
        uno = input('Jugador 1, escoja su personaje:')
    check_personaje(uno)

    while True:
        dos = input('Jugador 2, escoja su personaje:')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if dos.lower() == 'build':
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje: (No repetir)')
            if dos == uno:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(dos)

    while True:
        tres = input('Jugador 3, escoja su personaje:')
        if tres == uno or tres == dos:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if tres.lower() == 'build':
        equipbuild (equipamiento3, tres)
        while True:
            tres = input('Jugador 3, escoja su personaje: (No repetir)')
            if tres == uno or tres == dos:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(tres)

    while True:
        cuatro = input('Jugador 4, escoja su personaje: (No repetir)')
        if cuatro == uno or cuatro == dos or cuatro == tres:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if cuatro.lower() == 'build':
        equipbuild (equipamiento4, cuatro)
        while True:
            cuatro = input('Jugador 4, escoja su personaje: (No repetir)')
            if cuatro == uno or cuatro == dos or cuatro == tres:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(cuatro)

    while True:
        cinco = input('Jugador 5, escoja su personaje:')
        if cinco == uno or cinco == dos or cinco == tres or cinco == cuatro:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if cinco.lower() == 'build':
        equipbuild (equipamiento5, cinco)
        while True:
            cinco = input('Jugador 5, escoja su personaje: (No repetir)')
            if cinco == uno or cinco == dos or cinco == tres or cinco == cuatro:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(cinco)
    
    while True:
        seis = input('Jugador 6, escoja su personaje:')
        if seis == uno or seis == dos or seis == cuatro or seis == cinco or seis == tres:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if seis.lower() == 'build':
        equipbuild (equipamiento6, seis)
        while True:
            seis = input('Jugador 6, escoja su personaje: (No repetir)')
            if seis == uno or seis == dos or seis == tres or seis == cuatro or seis == cinco:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(seis)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    tres = translate(tres)
    cuatro = translate(cuatro)
    cinco = translate(cinco)
    seis = translate(seis)
    jugadores = [uno, dos, tres, cuatro, cinco, seis]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero', '\n')
            players = [uno, dos, tres, cuatro, cinco, seis]
            for i in players:
                i.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0 or cinco.health >= 0 or seis.health >= 0:
                velocities = list()
                players = [uno, dos, tres, cuatro, cinco, seis]
                for i in players:
                    velocities.append (i.velocity)
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                fourth = velocities [3]
                fiveth = velocities [4]
                sixth = velocities [5]
                players = [first, second, third, fourth, fiveth, sixth]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'seis', '1')
                    if i == dos.velocity:
                        play (dos, 'seis', '2')
                    if i == tres.velocity:
                        play (tres, 'seis', '3')
                    if i == cuatro.velocity:
                        play (cuatro, 'seis', '4')
                    if i == cinco.velocity:
                        play (cinco, 'seis', '5')
                    if i == seis.velocity:
                        play (seis, 'seis', '6')
                    check_dies (teams, 6)
    if escenario != 10:
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0 or cinco.health >= 0 or seis.health >= 0:
            velocities = list()
            players = [uno, dos, tres, cuatro, cinco, seis]
            for i in players:
                velocities.append (i.velocity)
            velocities.sort()
            first = velocities [5]
            second = velocities [4]
            third = velocities [3] 
            fourth = velocities [2]
            fiveth = velocities [1] 
            sixth = velocities [0]
            players = [first, second, third, fourth, fiveth, sixth]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'seis', '1')
                if i == dos.velocity:
                    play (dos, 'seis', '2')
                if i == tres.velocity:
                    play (tres, 'seis', '3')
                if i == cuatro.velocity:
                    play (cuatro, 'seis', '4')
                if i == cinco.velocity:
                    play (cinco, 'seis', '5')
                if i == seis.velocity:
                    play (seis, 'seis', '6')
                check_dies (teams, 6)

elif cuantosplayers.find('6') != -1 and cuantosplayers.find ('comp') != -1:
    nah = True
    while nah:
        teams = input ('Todos contra Todos, 2v2v2 o 3v3? (1/2/3)')
        if teams.lower() == '2':
            teams = '2v2v2'
            print ('Los equipos son 1 & 2, 3 & 4, 5 & 6')
            nah = False
        elif teams.lower() == '3':
            teams = '3v3'
            print ('Los equipos son 1 & 2 & 3, 4 & 5 & 6')
            nah = False
        elif teams.lower() == '1':
            teams = True
            nah = False
        else:
            print ('Eso NO es una opción')
    numjuga.numjug = 6
    bloqueo1 = input('Jugador 1, escoja un personaje para bloquear: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    bloqueo2 = input('Jugador 2, escoja un personaje para bloquear:')
    bloqueo3 = input('Jugador 3, escoja un personaje para bloquear:')
    bloqueo4 = input('Jugador 4, escoja un personaje para bloquear:')
    bloqueo5 = input('Jugador 5, escoja un personaje para bloquear:')
    bloqueo6 = input('Jugador 6, escoja un personaje para bloquear:')
    uno = 'build'
    if uno.lower() == 'build':
        print ('jugador 1 seleccione equipamiento:')
        equipbuild (equipamiento1, uno)
        while True:
            uno = input('Jugador 1, escoja su personaje:')
            if uno == bloqueo1 or uno == bloqueo2 or uno == bloqueo3 or uno == bloqueo4 or uno == bloqueo5 or uno == bloqueo6:
                print ('Ese personaje está bloqueado')
            else:
                break
    check_personaje(uno)

    dos = 'build'
    if dos.lower() == 'build':
        print ('jugador 2 seleccione equipamiento:')
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje:')
            if dos == bloqueo1 or dos == bloqueo2 or dos == bloqueo3 or dos == bloqueo4 or dos == bloqueo5 or dos == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif dos == uno:
                print ('Ese personaje ya está seleccionado')
            else:
                break
    check_personaje(dos)

    tres = 'build'
    if tres.lower() == 'build':
        print ('jugador 3 seleccione equipamiento:')
        equipbuild (equipamiento3, tres)
        while True:
            tres = input('Jugador 3, escoja su personaje:')
            if tres == bloqueo1 or tres == bloqueo2 or tres == bloqueo3 or tres == bloqueo4 or tres == bloqueo5 or tres == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif tres == uno or tres == dos:
                print ('Ese personaje ya está seleccionado')
            else:
                break
    check_personaje(tres)

    cuatro = 'build'
    if cuatro.lower() == 'build':
        print ('jugador 4 seleccione equipamiento:')
        equipbuild (equipamiento4, cuatro)
        while True:
            cuatro = input('Jugador 4, escoja su personaje:')
            if cuatro == bloqueo1 or cuatro == bloqueo2 or cuatro == bloqueo3 or cuatro == bloqueo4 or cuatro == bloqueo5 or cuatro == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif cuatro == uno or cuatro == dos or cuatro == tres:
                print ('Ese personaje ya está seleccionado')
            else:
                break
    check_personaje(cuatro)

    cinco = 'build'
    if cinco.lower() == 'build':
        print ('jugador 5 seleccione equipamiento:')
        equipbuild (equipamiento5, cinco)
        while True:
            cinco = input('Jugador 5, escoja su personaje:')
            if cinco == bloqueo1 or cinco == bloqueo2 or cinco == bloqueo3 or cinco == bloqueo4 or cinco == bloqueo5 or cinco == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif cinco == uno or cinco == dos or cinco == tres or cinco == cuatro:
                print ('Ese personaje ya está seleccionado')
            else:
                break
    check_personaje(cinco)

    seis = 'build'
    if seis.lower() == 'build':
        print ('jugador 6 seleccione equipamiento:')
        equipbuild (equipamiento6, seis)
        while True:
            seis = input('Jugador 6, escoja su personaje:')
            if seis == bloqueo1 or seis == bloqueo2 or seis == bloqueo3 or seis == bloqueo4 or seis == bloqueo5 or seis == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif seis == uno or seis == dos or seis == tres or seis == cuatro or seis == cinco:
                print ('Ese personaje ya está seleccionado')
            else:
                break
    check_personaje(seis)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    tres = translate(tres)
    cuatro = translate(cuatro)
    cinco = translate(cinco)
    seis = translate(seis)
    jugadores = [uno, dos, tres, cuatro, cinco, seis]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            players = [uno, dos, tres, cuatro, cinco, seis]
            for i in players:
                i.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0 or cinco.health >= 0 or seis.health >= 0:
                velocities = list()
                players = [uno, dos, tres, cuatro, cinco, seis]
                for i in players:
                    velocities.append (i.velocity)
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                fourth = velocities [3]
                fiveth = velocities [4]
                sixth = velocities [5]
                players = [first, second, third, fourth, fiveth, sixth]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'seis', '1')
                    if i == dos.velocity:
                        play (dos, 'seis', '2')
                    if i == tres.velocity:
                        play (tres, 'seis', '3')
                    if i == cuatro.velocity:
                        play (cuatro, 'seis', '4')
                    if i == cinco.velocity:
                        play (cinco, 'seis', '5')
                    if i == seis.velocity:
                        play (seis, 'seis', '6')
                    check_dies (teams, 6)
                
    if escenario != 10:
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0 or cinco.health >= 0 or seis.health >= 0:
            velocities = list()
            players = [uno, dos, tres, cuatro, cinco, seis]
            for i in players:
                velocities.append (i.velocity)
            velocities.sort()
            first = velocities [5]
            second = velocities [4]
            third = velocities [3] 
            fourth = velocities [2]
            fiveth = velocities [1] 
            sixth = velocities [0]
            players = [first, second, third, fourth, fiveth, sixth]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'seis', '1')
                if i == dos.velocity:
                    play (dos, 'seis', '2')
                if i == tres.velocity:
                    play (tres, 'seis', '3')
                if i == cuatro.velocity:
                    play (cuatro, 'seis', '4')
                if i == cinco.velocity:
                    play (cinco, 'seis', '5')
                if i == seis.velocity:
                    play (seis, 'seis', '6')
                check_dies (teams, 6)

elif cuantosplayers.lower() == '10':
    numjuga.numjug = 10
    nah = True
    while nah:
        teams = input ('Todos contra Todos, 2v2v2v2v2 o 5v5? (1/2/3)')
        if teams.lower() == '2':
            teams = '2v2v2v2v2'
            print ('Los equipos son 1 & 2, 3 & 4, 5 & 6, 7 & 8, 9 & 10')
            nah = False
        elif teams.lower() == '3':
            teams = '5v5'
            print ('Los equipos son 1 & 2 & 3 4 & 5, 6 & 7 & 8 & 9 & 10')
            nah = False
        elif teams.lower() == '1':
            teams = True
            nah = False
        else:
            print ('Eso NO es una opción')
    uno = input('Jugador 1, escoja su personaje: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    if uno.lower() == 'build':
        equipbuild (equipamiento1, uno)
        uno = input('Jugador 1, escoja su personaje:')
    check_personaje(uno)
    while True:
        dos = input('Jugador 2, escoja su personaje:')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if dos.lower() == 'build':
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje: (No repetir)')
            if dos == uno:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(dos)
    while True:
        tres = input('Jugador 3, escoja su personaje:')
        if tres == uno or tres == dos:
            print ('No se pueden repetir personajes!!')
        else:
            break
    if tres.lower() == 'build':
        equipbuild (equipamiento3, tres)
        while True:
            tres = input('Jugador 3, escoja su personaje: (No repetir)')
            if tres == uno or tres == dos:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(tres)
    while True:
        cuatro = input('Jugador 4, escoja su personaje: (No repetir)')
        if cuatro == uno or cuatro == dos or cuatro == tres:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if cuatro.lower() == 'build':
        equipbuild (equipamiento4, cuatro)
        while True:
            cuatro = input('Jugador 4, escoja su personaje: (No repetir)')
            if cuatro == uno or cuatro == dos or cuatro == tres:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(cuatro)
    while True:
        cinco = input('Jugador 5, escoja su personaje:')
        if cinco == uno or cinco == dos or cinco == tres or cinco == cuatro:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if cinco.lower() == 'build':
        equipbuild (equipamiento5, cinco)
        while True:
            cinco = input('Jugador 5, escoja su personaje: (No repetir)')
            if cinco == uno or cinco == dos or cinco == tres or cinco == cuatro:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(cinco)
    while True:
        seis = input('Jugador 6, escoja su personaje:')
        if seis == uno or seis == dos or seis == cuatro or seis == cinco or seis == tres:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if seis.lower() == 'build':
        equipbuild (equipamiento6, seis)
        while True:
            seis = input('Jugador 6, escoja su personaje: (No repetir)')
            if seis == uno or seis == dos or seis == tres or seis == cuatro or seis == cinco:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(seis)
    while True:
        siete = input('Jugador 7, escoja su personaje:')
        if siete == uno or siete == dos or siete == cuatro or siete == cinco or siete == tres or siete == seis:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if siete.lower() == 'build':
        equipbuild (equipamiento7)
        while True:
            siete = input('Jugador 7, escoja su personaje: (No repetir)')
            if siete == uno or siete == dos or siete == tres or siete == cuatro or siete == cinco or siete == seis:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(siete)
    while True:
        ocho = input('Jugador 8, escoja su personaje:')
        if ocho == uno or ocho == dos or ocho == cuatro or ocho == cinco or ocho == tres or ocho == seis or ocho == siete:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if ocho.lower() == 'build':
        equipbuild (equipamiento8)
        while True:
            ocho = input('Jugador 8, escoja su personaje: (No repetir)')
            if ocho == uno or ocho == dos or ocho == tres or ocho == cuatro or ocho == cinco or ocho == seis or ocho == siete:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(ocho)
    while True:
        nueve = input('Jugador 9, escoja su personaje:')
        if nueve == uno or nueve == dos or nueve == cuatro or nueve == cinco or nueve == tres or nueve == seis or nueve == siete or nueve == ocho:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if nueve.lower() == 'build':
        equipbuild (equipamiento9)
        while True:
            nueve = input('Jugador 9, escoja su personaje: (No repetir)')
            if nueve == uno or nueve == dos or nueve == tres or nueve == cuatro or nueve == cinco or nueve == seis or nueve == siete or nueve == ocho:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(nueve)
    while True:
        diez = input('Jugador 10, escoja su personaje:')
        if diez == uno or diez == dos or diez == cuatro or diez == cinco or diez == tres or diez == seis or diez == siete or diez == ocho or diez == nueve:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if diez.lower() == 'build':
        equipbuild (equipamiento10)
        while True:
            diez = input('Jugador 10, escoja su personaje: (No repetir)')
            if diez == uno or diez == dos or diez == tres or diez == cuatro or diez == cinco or diez == seis or diez == siete or diez == ocho or diez == nueve:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(diez)
    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    players = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez]
    for i in players:
        i = translate(i)
    aplicar_amuletos(players)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero', '\n')
            for i in players:
                i.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0 or cinco.health >= 0 or seis.health >= 0:
                velocities = list()
                players = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez]
                for i in players:
                    velocities.append (i.velocity)
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                fourth = velocities [3]
                fiveth = velocities [4]
                sixth = velocities [5]
                seventh = velocities [6]
                eighth = velocities [7]
                nineth = velocities [8]
                tenth = velocities [9]
                players = [first, second, third, fourth, fiveth, sixth, seventh, eighth, nineth, tenth]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'diez', '1')
                    if i == dos.velocity:
                        play (dos, 'diez', '2')
                    if i == tres.velocity:
                        play (tres, 'diez', '3')
                    if i == cuatro.velocity:
                        play (cuatro, 'diez', '4')
                    if i == cinco.velocity:
                        play (cinco, 'diez', '5')
                    if i == seis.velocity:
                        play (seis, 'diez', '6')
                    if i == siete.velocity:
                        play (siete, 'diez', '7')
                    if i == ocho.velocity:
                        play (ocho, 'diez', '8')
                    if i == nueve.velocity:
                        play (nueve, 'diez', '9')
                    if i == diez.velocity:
                        play (diez, 'diez', '10')
                    check_dies (teams, 10)
    if escenario != 10:
        for i in players:
            i.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0 or cinco.health >= 0 or seis.health >= 0:
            velocities = list()
            players = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez]
            for i in players:
                velocities.append (i.velocity)
            velocities.sort()
            first = velocities [9]
            second = velocities [8]
            third = velocities [7] 
            fourth = velocities [6]
            fiveth = velocities [5] 
            sixth = velocities [4]
            seventh = velocities [3] 
            eighth = velocities [2]
            nineth = velocities [1] 
            tenth = velocities [0]
            players = [first, second, third, fourth, fiveth, sixth, seventh, eighth, nineth, tenth]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'diez', '1')
                if i == dos.velocity:
                    play (dos, 'diez', '2')
                if i == tres.velocity:
                    play (tres, 'diez', '3')
                if i == cuatro.velocity:
                    play (cuatro, 'diez', '4')
                if i == cinco.velocity:
                    play (cinco, 'diez', '5')
                if i == seis.velocity:
                    play (seis, 'diez', '6')
                if i == siete.velocity:
                    play (siete, 'diez', '7')
                if i == ocho.velocity:
                    play (ocho, 'diez', '8')
                if i == nueve.velocity:
                    play (nueve, 'diez', '9')
                if i == diez.velocity:
                    play (diez, 'diez', '10')
                check_dies (teams, 10)

elif cuantosplayers.lower() == 'atraco':
    numjuga.numjug = 6
    print ('(Para poner de objetivo a una caja escribe "caja roja / caja azul")')
    uno = input('Jugador 1 (Equipo azul), escoja su personaje: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    if uno.lower() == 'build':
        equipbuild (equipamiento1, uno)
        uno = input('Jugador 1, escoja su personaje:')
    check_personaje(uno)
    while True:
        cuatro = input('Jugador 4 (Equipo rojo), escoja su personaje: (No repetir)')
        if cuatro == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if cuatro.lower() == 'build':
        equipbuild (equipamiento4, cuatro)
        while True:
            cuatro = input('Jugador 4, escoja su personaje: (No repetir)')
            if cuatro == uno:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(cuatro)
    while True:
        dos = input('Jugador 2 (Equipo azul), escoja su personaje:')
        if dos == uno or dos == cuatro:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if dos.lower() == 'build':
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje: (No repetir)')
            if dos == uno or dos == cuatro:
                print ('No se pueden repetir personajes!!')
            else:
                break

    check_personaje(dos)
    while True:
        cinco = input('Jugador 5 (Equipo rojo), escoja su personaje:')
        if cinco == uno or cinco == dos or cinco == cuatro:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if cinco.lower() == 'build':
        equipbuild (equipamiento5, cinco)
        while True:
            cinco = input('Jugador 5, escoja su personaje: (No repetir)')
            if cinco == uno or cinco == dos or cinco == cuatro:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(cinco)
    while True:
        tres = input('Jugador 3 (Equipo azul), escoja su personaje:')
        if tres == uno or tres == dos or tres == cuatro or tres == cinco:
            print ('No se pueden repetir personajes!!')
        else:
            break

    if tres.lower() == 'build':
        equipbuild (equipamiento3, tres)
        while True:
            tres = input('Jugador 3, escoja su personaje: (No repetir)')
            if tres == uno or tres == dos or tres == cuatro or tres == cinco:
                print ('No se pueden repetir personajes!!')
            else:
                break  
    check_personaje(tres)
    while True:
        seis = input('Jugador 6 (Equipo rojo), escoja su personaje:')
        if seis == uno or seis == dos or seis == cuatro or seis == cinco or seis == tres:
            print ('No se pueden repetir personajes!!')
        else:
            break
    
    if seis.lower() == 'build':
        equipbuild (equipamiento6, seis)
        while True:
            seis = input('Jugador 6, escoja su personaje: (No repetir)')
            if seis == uno or seis == dos or seis == tres or seis == cuatro or seis == cinco:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(seis)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    tres = translate(tres)
    cuatro = translate(cuatro)
    cinco = translate(cinco)
    seis = translate(seis)
    jugadores = [uno, dos, tres, cuatro, cinco, seis]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            players = [uno, dos, tres, cuatro, cinco, seis]
            for i in players:
                i.hello()
            while boxblue.health >= 0 and boxred >= 0:
                velocities = list()
                players = [uno, dos, tres, cuatro, cinco, seis]
                for i in players:
                    velocities.append (i.velocity)
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                fourth = velocities [3]
                fiveth = velocities [4]
                sixth = velocities [5]
                players = [first, second, third, fourth, fiveth, sixth]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'seis', '1')
                    if i == dos.velocity:
                        play (dos, 'seis', '2')
                    if i == tres.velocity:
                        play (tres, 'seis', '3')
                    if i == cuatro.velocity:
                        play (cuatro, 'seis', '4')
                    if i == cinco.velocity:
                        play (cinco, 'seis', '5')
                    if i == seis.velocity:
                        play (seis, 'seis', '6')
                    if boxblue.health <= 0 and boxred.health <= 0 :
                        print ('Hay empate debido a una destrucción mutua de ambas cajas')
                        break
                    elif boxred.health <= 0:
                        print ('Equipo azul WIIIIN')
                        break
                    elif boxblue.health <= 0:
                        print ('Equipo rojo WIIIIN')
                        break
                boxred.turno()
                boxblue.turno()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break

    if escenario != 10:
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.hello()
        while boxblue.health >= 0 and boxred >= 0:
            velocities = list()
            players = [uno, dos, tres, cuatro, cinco, seis]
            for i in players:
                velocities.append (i.velocity)
            velocities.sort()
            first = velocities [5]
            second = velocities [4]
            third = velocities [3] 
            fourth = velocities [2]
            fiveth = velocities [1] 
            sixth = velocities [0]
            players = [first, second, third, fourth, fiveth, sixth]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'seis', '1')
                if i == dos.velocity:
                    play (dos, 'seis', '2')
                if i == tres.velocity:
                    play (tres, 'seis', '3')
                if i == cuatro.velocity:
                    play (cuatro, 'seis', '4')
                if i == cinco.velocity:
                    play (cinco, 'seis', '5')
                if i == seis.velocity:
                    play (seis, 'seis', '6')

                if boxblue.health <= 0 and boxred.health <= 0 :
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break
                    
            boxred.turno()
            boxblue.turno()
            if boxblue.health <= 0 and boxred.health <= 0:
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break

elif cuantosplayers.find('atraco') != -1 and cuantosplayers.find('comp') != -1:
    numjuga.numjug = 6
    bloqueo1 = input('Jugador 1, escoja un personaje para bloquear: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Healer, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Support, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    bloqueo2 = input('Jugador 2, escoja un personaje para bloquear:')
    bloqueo3 = input('Jugador 3, escoja un personaje para bloquear:')
    bloqueo4 = input('Jugador 4, escoja un personaje para bloquear:')
    bloqueo5 = input('Jugador 5, escoja un personaje para bloquear:')
    bloqueo6 = input('Jugador 6, escoja un personaje para bloquear:')
    print ('(Para poner de objetivo a una caja escribe "caja roja / caja azul")')
    print ('jugador 1 seleccione equipamiento:')
    equipbuild (equipamiento1, uno)
    while True:
        uno = input('Jugador 1 (Equipo azul), escoja su personaje: ')
        if uno == bloqueo1 or uno == bloqueo2 or uno == bloqueo3 or uno == bloqueo4 or uno == bloqueo5 or uno == bloqueo6:
            print ('Ese personaje está bloqueado')
        else:
            break
    
    check_personaje(uno)
    cuatro = 'build'
    if cuatro.lower() == 'build':
        print ('jugador 4 seleccione equipamiento:')
        equipbuild (equipamiento4, cuatro)
        while True:
            cuatro = input('Jugador 4, escoja su personaje: (No repetir)')
            if cuatro == bloqueo1 or cuatro == bloqueo2 or cuatro == bloqueo3 or cuatro == bloqueo4 or cuatro == bloqueo5 or cuatro == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif cuatro == uno:
                print ('Ese personaje ya está escogido')
            else:
                break

    check_personaje(cuatro)
    dos = 'build'
    if dos.lower() == 'build':
        print ('jugador 2 seleccione equipamiento:')
        equipbuild (equipamiento2, dos)
        while True:
            dos = input('Jugador 2, escoja su personaje: (No repetir)')
            if dos == bloqueo1 or dos == bloqueo2 or dos == bloqueo3 or dos == bloqueo4 or dos == bloqueo5 or dos == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif dos == uno or dos == cuatro:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(dos)
    cinco = 'build'
    if cinco.lower() == 'build':
        print ('jugador 5 seleccione equipamiento:')
        equipbuild (equipamiento5, cinco)
        while True:
            cinco = input('Jugador 5, escoja su personaje: (No repetir)')
            if cinco == bloqueo1 or cinco == bloqueo2 or cinco == bloqueo3 or cinco == bloqueo4 or cinco == bloqueo5 or cinco == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif cinco == uno or cinco == dos or cinco == cuatro:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(cinco)
    tres = 'build'
    if tres.lower() == 'build':
        print ('jugador 3 seleccione equipamiento:')
        equipbuild (equipamiento3, tres)
        while True:
            tres = input('Jugador 3, escoja su personaje: (No repetir)')
            if tres == bloqueo1 or tres == bloqueo2 or tres == bloqueo3 or tres == bloqueo4 or tres == bloqueo5 or tres == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif tres == uno or tres == dos or tres == cuatro or tres == cinco:
                print ('No se pueden repetir personajes!!')
            else:
                break  
    check_personaje(tres)
    seis = 'build'
    if seis.lower() == 'build':
        print ('jugador 6 seleccione equipamiento:')
        equipbuild (equipamiento6, seis)
        while True:
            seis = input('Jugador 6, escoja su personaje: (No repetir)')
            if seis == bloqueo1 or seis == bloqueo2 or seis == bloqueo3 or seis == bloqueo4 or seis == bloqueo5 or seis == bloqueo6:
                print ('Ese personaje está bloqueado')
            elif seis == uno or seis == dos or seis == tres or seis == cuatro or seis == cinco:
                print ('No se pueden repetir personajes!!')
            else:
                break
    check_personaje(seis)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    tres = translate(tres)
    cuatro = translate(cuatro)
    cinco = translate(cinco)
    seis = translate(seis)
    jugadores = [uno, dos, tres, cuatro, cinco, seis]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            players = [uno, dos, tres, cuatro, cinco, seis]
            for i in players:
                i.hello()
            while boxblue.health >= 0 and boxred >= 0:
                velocities = list()
                players = [uno, dos, tres, cuatro, cinco, seis]
                for i in players:
                    velocities.append (i.velocity)
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                fourth = velocities [3]
                fiveth = velocities [4]
                sixth = velocities [5]
                players = [first, second, third, fourth, fiveth, sixth]
                for i in players:
                    if i == uno.velocity:
                        play (uno, 'seis', '1')
                    if i == dos.velocity:
                        play (dos, 'seis', '2')
                    if i == tres.velocity:
                        play (tres, 'seis', '3')
                    if i == cuatro.velocity:
                        play (cuatro, 'seis', '4')
                    if i == cinco.velocity:
                        play (cinco, 'seis', '5')
                    if i == seis.velocity:
                        play (seis, 'seis', '6')
                    if boxblue.health <= 0 and boxred.health <= 0 :
                        print ('Hay empate debido a una destrucción mutua de ambas cajas')
                        break
                    elif boxred.health <= 0:
                        print ('Equipo azul WIIIIN')
                        break
                    elif boxblue.health <= 0:
                        print ('Equipo rojo WIIIIN')
                        break
                boxred.turno()
                boxblue.turno()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break

    if escenario != 10:
        players = [uno, dos, tres, cuatro, cinco, seis]
        for i in players:
            i.hello()
        while boxblue.health >= 0 and boxred >= 0:
            velocities = list()
            players = [uno, dos, tres, cuatro, cinco, seis]
            for i in players:
                velocities.append (i.velocity)
            velocities.sort()
            first = velocities [5]
            second = velocities [4]
            third = velocities [3] 
            fourth = velocities [2]
            fiveth = velocities [1] 
            sixth = velocities [0]
            players = [first, second, third, fourth, fiveth, sixth]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'seis', '1')
                if i == dos.velocity:
                    play (dos, 'seis', '2')
                if i == tres.velocity:
                    play (tres, 'seis', '3')
                if i == cuatro.velocity:
                    play (cuatro, 'seis', '4')
                if i == cinco.velocity:
                    play (cinco, 'seis', '5')
                if i == seis.velocity:
                    play (seis, 'seis', '6')
                if boxblue.health <= 0 and boxred.health <= 0 :
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break
            boxred.turno()
            boxblue.turno()
            if boxblue.health <= 0 and boxred.health <= 0:
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break

elif cuantosplayers.lower() == '1':
    numjuga.numjug = 2
    uno = input('Jugador 1, escoja su personaje: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Mace, Fires, Snake Charner, Apostador, Natural, Natural Heal, Diablillo, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge, Serenità')
    if uno.lower() == 'build':
        equipbuild (equipamiento1, uno)
        uno = input('Jugador 1, escoja su personaje:')
    check_personaje(uno)

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    escenario = randint (1, 10)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        uno.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        if uno.tipo == 2:
            print (uno.name, 'recibe 0.25 más de defensa')
            uno.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        if uno.tipo == 3:
            print (uno.name, 'recibe 0.25 más de poder')
            uno.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        if uno.tipo == 1:
            print (uno.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            uno.defense += 0.2
            uno.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        if uno.tipo == 0:
            print (uno.name, 'recibe 60 más de velocidad')
            uno.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        uno.preci1 -= 20
        uno.preci2 -= 20
        uno.preci3 -= 20
        uno.precicura -= 20
        uno.precienergia -= 20
    elif escenario == 10:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        uno.energy += 100000

    uno.hello()
    first = uno
    fase = 1
    enemigos = [uno]
    while fase <= 5:
        play (uno, 'dos', '1')
        bichoprueba.turno (enemigos)
        if fase > 5:
            print ('GANASTE')
            break
        elif uno.health <= 0:
            print ('Perdiste :(')
            break 

if cuantosplayers == '2ia':
    numjuga.numjug = 2
    uno = input('Jugador 1, escoja su personaje: Warrior, Warrior Tank, Magician, Hereje, Maldi, Thief, Shapeshifter, Mace, Fires, Snake Charner, Apostador, Natural, Diablillo, Chiquitin, Guadaña, Crossbow, Loco, Root, Santa Claus, Werewolf, Runeforge')
    if uno.lower() == 'build':
        equipbuild (equipamiento1, uno)
        uno = input('Jugador 1, escoja su personaje:')
    check_personaje(uno)

    dos = 'crossbow'

    mapping = {
    'warrior': guerrero, 'magician': mago, 'hereje': arquero, 'maldi': maldito, 'thief': robador, 'shapeshifter': pantera,
    'healer': curandera, 'mace': maza, 'fires': igneo, 'snake charner': serpientero, 'apostador': poker, 'natural': natural,
    'diablillo': diablillo, 'support': support, 'chiquitin': chiquitin, 'guadaña': guadana, 'crossbow': ballesta, 'loco': locoloco,
    'root': raiz, 'santa claus': papanoel, 'werewolf': werewolf, 'natural heal': natural_heal, 'warrior tank': tank, 'runeforge': herrero, 'serenita' : her, 'serenità' : her
    }

    def translate(value):
        return mapping.get(value.lower(), value)

    uno = translate(uno)
    dos = translate(dos)
    jugadores = [uno, dos]
    aplicar_amuletos(jugadores)
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores aumentando su locura en 20')
        players = [uno, dos]
        for i in players:
            i.locura += 20
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        players = [uno, dos]
        for i in players:
            if i.tipo == 2:
                print (i.name, 'recibe 0.25 más de defensa')
                i.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        players = [uno, dos]
        for i in players:
            if i.tipo == 3:
                print (i.name, 'recibe 0.25 más de poder')
                i.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        players = [uno, dos]
        for i in players:
            if i.tipo == 1:
                print (i.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
                i.defense += 0.2
                i.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        players = [uno, dos]
        for i in players:
            if i.tipo == 0:
                print (i.name, 'recibe 60 más de velocidad')
                i.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        players = [uno, dos]
        for i in players:
            i.preci1 -= 20
            i.preci2 -= 20
            i.preci3 -= 20
            i.precicura -= 20
            i.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        players = [uno, dos]
        for i in players:
            i.energy += 100000
    elif escenario == 10:
        print ('La pelea está patas arriba y los menos veloces atacan primero')
        uno.hello()
        dos.hello()
        while uno.health >= 0 or dos.health >= 0:
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.sort()
            second = velocities [1]
            first = velocities [0]
            players = [first, second]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'dos', '1')
                if i == dos.velocity:
                    playIA (dos, 'dos', '2', False)
                if uno.health <= 0 and dos.health <= 0:
                    print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                elif dos.health <= 0:
                    print ('Jugador 1 WIIIIN')
                elif uno.health <= 0:
                    print ('Jugador 2 WIIIIN')

    if escenario != 10:
        uno.hello()
        dos.hello()
        while uno.health >= 0 or dos.health >= 0:
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.sort()
            first = velocities [1]
            second = velocities [0]
            players = [first, second]
            for i in players:
                if i == uno.velocity:
                    play (uno, 'dos', '1')
                if i == dos.velocity:
                    playIA (dos, 'dos', '2', False)
                if uno.health <= 0 and dos.health <= 0:
                    print ('EMPATE. ¿¿Cómo?? JAJAJAJA')
                elif dos.health <= 0:
                    print ('Jugador 1 WIIIIN')
                elif uno.health <= 0:
                    print ('Jugador 2 WIIIIN')
