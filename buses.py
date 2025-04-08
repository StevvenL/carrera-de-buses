import os
import time
import random


# Función para limpiar la pantalla
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Dibujar el bus en una posición específica
def draw_bus(position, track_length):
    bus = [
        "  ____________________",
        " |                    )___",
        "| [] [] [] [] [] [] []    |",
        "|_________________________|",
        "  O                  O",
    ]
    for line in bus:
        print(" " * position + line)
    ground = " " * position + "-" * (track_length - position) + "| META"
    print(ground)


# Mostrar el estado de la carrera
def print_race(bus1_pos, bus2_pos, track_length, bus1_name, bus2_name):
    clear_screen()
    print(f"{bus1_name} (Carril 1):")
    draw_bus(bus1_pos, track_length)
    print("\n" * 2)
    print(f"{bus2_name} (Carril 2):")
    draw_bus(bus2_pos, track_length)

    # Mostrar quién va ganando
    print("\n")
    if bus1_pos > bus2_pos:
        print(f"🏁 ¡{bus1_name} va ganando!")
    elif bus2_pos > bus1_pos:
        print(f"🏁 ¡{bus2_name} va ganando!")
    else:
        print("🏁 ¡Van empatados!")


# Mostrar mensaje de amor
def show_love_message():
    clear_screen()
    love_message = [
        "",
        "**********************************************",
        "*                                            *",
        "*  ¡Gracias por jugar esta carrera divertida! *",
        "*        Esperamos que lo hayas disfrutado   *",
        "*                                            *",
        "**********************************************",
        "",
        "                 🚍🏁🏁🚍",
    ]
    for line in love_message:
        print(line)
    time.sleep(6)


# Configuración de la carrera
track_length = 110
bus1_pos = 0
bus2_pos = 0
goal = track_length - 1

# Nombres personalizados
bus1_name = input("Ingresa el nombre del Bus 1: ")
bus2_name = input("Ingresa el nombre del Bus 2: ")

# Iniciar la carrera
while bus1_pos < goal and bus2_pos < goal:
    bus1_pos += random.randint(1, 3)
    bus2_pos += random.randint(1, 3)

    bus1_pos = min(bus1_pos, goal)
    bus2_pos = min(bus2_pos, goal)

    print_race(bus1_pos, bus2_pos, track_length, bus1_name, bus2_name)
    time.sleep(0.2)

# Mostrar resultado
clear_screen()
print_race(bus1_pos, bus2_pos, track_length, bus1_name, bus2_name)

print("\n" + "=" * 60)
if bus1_pos >= goal and bus2_pos >= goal:
    print("¡Empate!")
elif bus1_pos >= goal:
    print(f"🎉 ¡{bus1_name} ha ganado!")
else:
    print(f"🎉 ¡{bus2_name} ha ganado!")

time.sleep(2)
show_love_message()
