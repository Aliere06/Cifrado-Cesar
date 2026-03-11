import os

matrix = [['A', 'B', 'C', 'D', 'E', 'F', 'G'],
          ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
          ['O', 'P', 'Q', 'R', 'S', 'T', 'U'],
          ['V', 'W', 'X', 'Y', 'Z', ' ', 'Ñ']]

def transcode(key, message):
    if key is None:
        key = 1
        print("\nDescifrando por fuerza bruta...\n")

        while key < 28:
            search_range = key + 9
            print(f"Llaves {key} - {search_range-1}:")
            for k in range(key, search_range):
                print(f"{k}. {key_shift(-k, message)}")
            selection = input(
                "\nLlave encontrada? (indique el no.)"
                "\nContinuar (enter)\n")
            
            try:
                key = -int(selection)
                break
            except:
                key = search_range

        if key < 28:
            print(f"\nLlave: {-key}")
        else:
            print("Llave no encontrada\n"
                  "El texto no contiene un mensaje o fue cifrado de otra forma\n")
            return

    output = key_shift(key, message)

    os.system(f'echo -n "{output}" | xclip -selection clipboard')
    print(f"\nMensaje procesado:\n{output}\n")

def key_shift(key, message):
    output = ""
    for character in message:
        for row in range(4):
            for column in range(7):
                if character == matrix[row][column]:
                    target = (row*7 + column + key) % 28
                    output += matrix[target // 7][target % 7]
    return output

while True:
    mode = input("\n"
        "Eliga el modo de operación\n"
        "Cifrar (c)\n"
        "Descifrar (d)\n").lower()
    message = input("\nIngrese el mensaje: ").upper()
    no_key = ("", " (? si no la conoce)")['d' in mode]
    try:
        key = int(input(f"Ingrese la llave{no_key}: "))
        key = (key * (1, -1)['d' in mode]) % 28
    except:
        key = None

    transcode(key, message)

    if 'q' in input("Salir (q) / Continuar (enter)\n").lower():
        break

