import os

matrix = [['A', 'B', 'C', 'D', 'E', 'F', 'G'],
          ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
          ['O', 'P', 'Q', 'R', 'S', 'T', 'U'],
          ['V', 'W', 'X', 'Y', 'Z', ' ', 'Ñ']]

while True:
    mode = input("\n"
        "Eliga el modo de operación\n"
        "Cifrar (c)\n"
        "Descifrar (d)\n").lower()
    message = input("\nIngrese el mensaje: ").upper()
    key = int(input("\nIngrese la llave: "))
    key = (key * (1, -1)['d' in mode]) % 28

    output = ""
    for character in message:
        for row in range(4):
            for column in range(7):
                if character == matrix[row][column]:
                    target = (row*7 + column + key) % 28
                    output += matrix[target // 7][target % 7]

    print(output + '\n')
    os.system(f'echo -n "{output}" | xclip -selection clipboard')

    if 'q' in input("Salir (q) / Continuar (enter)\n").lower():
        break
