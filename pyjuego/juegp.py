#Librerias necesarias para el juego
import os
import time
import random

# Variable para controlar el bucle principal
ini = True

while ini:
    # Portada del juego con un menu de opciones
    print("      _______________________________________________________________________________________________")
    print("""
    |    ___ ___                ___         _________    _                      ___                  |
    |    | \ | |                | |         / ____| |   (_)                     | |           _      |
    |    |  \| | __ _ _ __ _   _| |_ ___   | (___ | |__  _ _ __  _ __  _   _  __| | ___ _ __ (_)     |
    |    | . ` |/ _` | '__| | | | __/ _ \   \___ \| '_ \| | '_ \| '_ \| | | |/ _` |/ _ \ '_ \        |
    |    | |\  | (_| | |  | |_| | || (_) |  ____) | | | | | |_) | |_) | |_| | (_| |  __/ | | |_      |
    |    |_| \_|\__,_|_|   \__,_|\__\___/  |_____/|_| |_|_| .__/| .__/ \__,_|\__,_|\___|_| |_(_)     |
    |    ___  ___ __   _                    ______        | |   | |                                  |
    |    | |  | | | | (_)                  / ____|        |_|   |_|                                  |
    |    | |  | | | |_ _ _ __ ___   ___   | |  __ _   _  ___ _ __ _ __ ___ _ __ ___                  |
    |    | |  | | | __| | '_ ` _ \ / _ \  | | |_ | | | |/ _ \ '__| '__/ _ \ '__/ _ \                 |
    |    | |__| | | |_| | | | | | | (_) | | |__| | |_| |  __/ |  | | |  __/ | | (_) |                |
    |     \____/|_|\__|_|_| |_| |_|\___/   \_____|\__,_|\___|_|  |_|  \___|_|  \___/                 |
    """)
    print("    __________________________________________________________________________________________________")
    print("|------------------------------------------------------------------------------------------------------|")
    print("|                                1. Lectura de la Historia                                             |")
    print("|                                2. Instrucciones para jugar                                           |")
    print("|                                        3. Inicio                                                     |")
    print("|                                        4. Salir                                                      |")
    print("|------------------------------------------------------------------------------------------------------|")

    # Validar entrada del usuario
    try:
        opcion = int(input("Opción: "))  # Opción que se guarda en la variable
    except ValueError: # Si la entrada no es un número entero  y no es una letra
        print("Por favor, ingresa un número válido.") #por favor ingresalo bien
        continue

    # Opcion de leer la historia al presionar el 1
    if opcion == 1:

        print("|------------------------------------------------------------------------------|")
        print("")
        print("Después de muchos años de que Uchiha Sasuke fuera de la aldea de la hoja,")
        print("")
        print(" y abandona al equipo 7, Naruto Uzumaki se siente triste y decepcionado.")
        print("")
        print("Uzumaki Naruto entrena día y noche para encontrarlo y dar la pelea final")
        print("")
        print("para que este vuelva a casa y con el equipo 7.")
        print("")
        print("Una noche se lo encuentra en la Villa del Fin,donde pelearon Grandes")
        print("")
        print("Guerreros del pasado: Hashirama Senju y Madara Uchiha.")
        print("")
        print("Naruto se da cuenta que Sasuke ha cambiado y que ya no es el mismo.")
        print("")
        print("|-------------------------------------------------------------------------------|")
        print("")
        print("Naruto (sorprendido): Sasuke, te he estado buscando por mucho tiempo.")
        print("")
        print("Sasuke (frío): No pienses que estoy aqui por ti, Naruto.")
        print("")
        print("Naruto (determinado): No me importa por qué estás aquí. Solo quiero que vuelvas.")
        print("")   
        print("Sasuke (frio): No tengo nada que ver con la aldea, ni contigo, ni con el equipo 7.")
        print("")   
        print("Naruto (enojado): No puedo dejar que te vayas así. Te necesito, somos tu y yo.")
        print("")   
        print("Sasuke (desafiante): Entonces ven y pégame si puedes. Demuéstrame que eres más fuerte.")
        print("")   
        print("Naruto (determinado): Lo haré. No me detendré hasta que te traiga de vuelta conmigo.")
        print("")   
        print("Sasuke (desafiante): Entonces ven, Naruto. Vamos a pelear.")
        print("")
        print("Naruto (determinado): ¡Sí! ¡Vamos a pelear!")
        print("")
        print("|-------------------------------------------------------------------------------|")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    #Opcion de instrucciones al presionar el 2
    elif opcion == 2:

        print("|------------------------------------------------------------------------------------|")
        print("")
        print("Bienvenido a la sección de instrucciones.Donde solamente se debe escribir bien la accion a realizar.")
        print("En este juego, tendrás que tomar decisiones que afectarán el resultado de la historia.")
        print("Menu de opciones:")
        print("1. atacar")
        print("2. defender")
        print("")
        print("|-------------------------------------------------------------------------------------|")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    #Opcion de iniciar el juego al presionar el 3 de la batalla
    elif opcion == 3:

        print("|------------------------------------------------------------------------------------------|")
        print("")
        print("¡Bienvenido a la batalla final entre Naruto y Sasuke!")
        
        # diccionario de personajes y con sus respectivos atributos
        personajes = {
            "Naruto": [200, 100, 50],  # vida, ataque, defensa
            "Sasuke": [200, 100, 50],
        }
        #dicionario de acciones
        acciones = ["atacar", "defender"]

        # Elección del personaje
        print("Elige tu personaje:")
        
        #recorre la lista de personajes y los imprime de acuerdo a su nombre
        for nombre in personajes.keys():
            print(nombre)
        jugador_nombre = ""

        # Se asegura que el nombre del jugador sea válido dentro de los personajes existentes y disponibles
        while jugador_nombre not in personajes:
            jugador_nombre = input("Escribe el nombre de tu personaje: ").strip() #strip elimina los espacios en blanco al inicio y al final
            #si el nombre no es correcto, se vuelve a pedir
            if jugador_nombre not in personajes:
                print("Personaje no disponible, intenta de nuevo.")

        # Elección del oponente diferente al jugador de acuerdo a los personajes disponibles
        oponente_nombre = [p for p in personajes if p != jugador_nombre][0]

        #a las variables se les asigna el nombre del jugador y el oponente 
        jugador_stats = personajes[jugador_nombre]
        oponente_stats = personajes[oponente_nombre]

        #Muestra el nombre del jugador y el oponente
        print("")
        print(f"\nHas elegido a {jugador_nombre}. Tu oponente es {oponente_nombre}.\n")

        # Bucle de combate del juego
        while jugador_stats[0] > 0 and oponente_stats[0] > 0:
            # Mostrar estadísticas de vida del jugador y oponente
            print(f"Vida de {jugador_nombre}: {jugador_stats[0]} | Vida de {oponente_nombre}: {oponente_stats[0]}")
            # Mostrar acciones disponibles
            accion_jugador = input("Elige tu acción (atacar/defender): ").strip().lower()

            #si la accion no se encuentra en la lista de acciones, se vuelve a pedir
            while accion_jugador not in acciones:
                print("Acción no válida. Elige 'atacar' o 'defender'.")
                accion_jugador = input("Elige tu acción (atacar/defender): ").strip().lower()

            #si existe la accion se le resta vida del oponente de acuerdo a su ataque
            if accion_jugador == "atacar":
                dano = max(jugador_stats[1] - oponente_stats[2], 0)
                oponente_stats[0] -= dano
                print(f"{jugador_nombre} ataca a {oponente_nombre} y causa {dano} de daño.")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print(f"{jugador_nombre} se defiende.")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

            #En caso de que el jugador gane, se imprime un mensaje de victoria y la continuacion de la historia
            # de acuerdo al personaje que eligio el jugador
            if oponente_stats[0] <= 0 and jugador_nombre == "Naruto":
                print("|------------------------------------------------------------------------------------------------------------------------------|")
                print("")
                print(f"¡Felicidades! {jugador_nombre} ha ganado la batalla.")
                print("")
                print("Sasuke (sorprendido): No puedo creer que me hayas vencido...")
                print("")
                print("Naruto (sonriendo): Siempre he creído en ti que no cambiaste, Sasuke.")
                print("")
                print("Sasuke (reflexionando): Quizás haya algo más en la vida que solo venganza.")
                print("")
                print("Naruto (sonriendo): Siempre estaré aquí para ti, Sasuke.")
                print("")
                print("Sasuke (sonriendo): Gracias, Naruto. Quizás podamos encontrar un camino juntos.")
                print("")
                print("Naruto (sonriendo): Sí, juntos podemos lograrlo.")
                print("")
                print("Luego de una larga batalla, Naruto y Sasuke regresan a la aldea de la hoja juntos en donde, ")
                print("sus amigos y Kakashi sensei los estaban esperando.Sasuke se da cuenta de su error y cambia de opinion.")
                print("Naruto y Sasuke se reconcilian")
                print("")
                print("                                                  FINAL BUENO")
                print("|------------------------------------------------------------------------------------------------------------------------------|")
                time.sleep(13)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif oponente_stats[0] <= 0 and jugador_nombre == "Sasuke":
                print("|------------------------------------------------------------------------------------------------------------------------------|")
                print("")
                print(f"¡Felicidades! {jugador_nombre} ha ganado la batalla.")
                print("")
                print("Sasuke (frio): lo sabía, siempre he sido más fuerte que tú.")
                print("")
                print("Naruto (tristeza): Sasuke...")
                print("")
                print("Sasuke (serio): En mi cuerpo solo es venganza.. No me busques mas.")
                print("")
                print("Naruto (sorprendido que se esta yendo): SASUKE, NO TE VAYAS.")
                print("")
                print("Sasuke (sonriendo): Adios Naruto, siempre serás mi rival.")
                print("")
                print("Naruto (tristeza): Adios Sasuke, siempre serás mi amigo.")
                print("")
                print("""Sasuke luego de una larga batalla de vencer a Naruto, lo deja en el suelo malherido y lo cubre con su
con una capa de su chakra, para que no muera y lo deja abandonado en la Villa del Fin. Sakura y Kakashi 
sensei lo encuentran y lo llevan a la aldea de la hoja, donde se recupera. Naruto se da cuenta que Sasuke 
no volverá y decide mejorar sus habilidades para volverlo a intentar para recuperar a su amigo y rival.
Kakashi sensei lo ayuda a mejorar sus habilidades y mejorar su chakra, para que no vuelva a perder.
                      """)
                print("")
                print("                                                 FINAL NEUTRO")
                print("|------------------------------------------------------------------------------------------------------------------------------|")
                time.sleep(13)
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            #aqui las acciones del oponente, elige una accion al azar de la lista de acciones al azar
            accion_oponente = random.choice(acciones)
            print(f"\n{oponente_nombre} elige {accion_oponente}.")
            if accion_oponente == "atacar":
                dano = max(oponente_stats[1] - jugador_stats[2], 0)
                jugador_stats[0] -= dano
                print(f"{oponente_nombre} ataca a {jugador_nombre} y causa {dano} de daño.")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print(f"{oponente_nombre} se defiende.")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

            #En caso de que el jugador gane, se imprime un mensaje de derrota y la continuacion de la historia
            # de acuerdo al personaje que eligio el jugador
            if jugador_stats[0] <= 0 and jugador_nombre == "Naruto":
                print("|-------------------------------------------------------------------------------------------------------------------------------|")
                print("")
                print(f"Has perdido. {oponente_nombre} ha ganado la batalla.")
                print("")
                print("Naruto (tristeza): No puedo creer que haya perdido...")
                print("")
                print("""Sasuke con su propia espada mata a Naruto.Sin piedad y sin compasion, viendo como su amigo y rival
Naruto muere en sus brazos, Sasuke se da cuenta que no tiene sentido seguir con su venganza y decide irse de la villa
del fin, para nunca volver. Sakura y Kakashi sensei lo encuentran y se llevan la sopresa de que Naruto ha muerto.
Sakura llora la muerte de su amigo, mientras que Kakashi sensei se siente culpable por no haberlo podido salvar.    
La aldea de la hoja llora la muerte de su héroe y su amigo, Naruto Uzumaki.
                      """)
                print("")
                print("                                                 FINAL MALO 1")
                print("|------------------------------------------------------------------------------------------------------------------------------|")
                time.sleep(13)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif jugador_stats[0] <= 0 and jugador_nombre == "Sasuke":
                print("|-----------------------------------------------------------------------------------------------------------------------------------|")
                print("")
                print("")
                print(f"Has perdido. {oponente_nombre} ha ganado la batalla.")
                print("")
                print("Sasuke (odio): No puedo creer que haya perdido...")
                print("")
                print("""Sasuke se desmaya y cae al suelo, mientras que Naruto lo mira y se da cuenta que su amigo y rival ha caído.
Naruto no mide su fuerza y mata a este con un rasengan, ya cuando se da cuenta que lo ha matado, era demasiado tarde.
Naruto grita a los cielos por perder a alguien importante para el, su vida entera se habia ido para siempre..
La aldea de la hoja le hacen un funeral al ultimo Uchiha, Sasuke Uchiha.
 Naruto se siente culpable por haberlo matado y decide irse de la aldea de la hoja, para nunca volver.
Uzumaki Naruto desaparece y nunca se vuelve a saber de el.
                      """)
                print("")
                print("                                                 FINAL MALO 2")
                print("|------------------------------------------------------------------------------------------------------------------------------------|")
                time.sleep(13)
                os.system('cls' if os.name == 'nt' else 'clear')
                break

        os.system('cls' if os.name == 'nt' else 'clear')
    
    #opcion para salir del juego al presionar el 4
    elif opcion == 4:
                    print("_______________________________________________________________________________________________________________")
                    print("""                                                                                                       
 |     _   _    _____                _                                  _                          _   _         |
 |    (_) (_)  / ____|              (_)                                (_)                        | | | |        |
 |    | | | | | |  __ _ __ __ _  ___ _  __ _ ___   _ __   ___  _ __     _ _   _  __ _  __ _ _ __  | | | |        |
 |    | | | | | | |_ | '__/ _` |/ __| |/ _` / __| | '_ \ / _ \| '__|   | | | | |/ _` |/ _` | '__| | | | |        |
 |    | | | | | |__| | | | (_| | (__| | (_| \__ \ | |_) | (_) | |      | | |_| | (_| | (_| | |    |_| |_|        |
 |    |_| |_|  \_____|_|  \__,_|\___|_|\__,_|___/ | .__/ \___/|_|      | |\__,_|\__, |\__,_|_|    (_) (_)        |
 |                                                | |                 _/ |       __/ |                           |
 |                                                |_|                |__/       |___/                            |
                    """)
                    print("________________________________________________________________________________________________________________")
                    print("")
                    print("Atentamente: El creador del juego y la laptop de nombre MiMi <3 .")
                    print("")
                    print("Espero que te haya gustado el juego y la historia.")
                    print("________________________________________________________________________________________________________________")
                    ini = False
    else:
     #mensaje en caso de que el numero de opcion no exista
     print("Opción inexistente. Vuelve a intentarlo.")
