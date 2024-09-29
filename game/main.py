import random


def piedra_papel_tijera():
    while True:
        opciones = ['PIEDRA','PAPEL','TIJERA']
        bot = random.choice(opciones)
        texto = """
        1- Tijera
        2- Papel
        3- Tijera"""
        print(texto)
        user = input("Ingrese la opcion que desea escoger:").upper()
        if user not in opciones:
            print("Dato Ingresado no valido")
        else:
            print(f'El usuario escogio {user}')
            print(f'El bot escogio {bot}')
            if user == bot:
                print("Empate")
            elif user == 'TIJERA' and bot == 'PIEDRA':
                print("Haz perdido")
                continue
            elif user == 'TIJERA' and bot == 'PAPEL':
                print("Haz ganado")
                break
            elif user == 'PIEDRA' and bot == 'TIJERA':
                print('Haz Ganado')
                break
            elif user == 'PIEDRA' and bot == 'PAPEL':
                print('Haz perdido')
                continue
            elif user == 'PAPEL' and bot == 'PIEDRA':
                print('Haz ganado')
                break
            elif user == 'PAPEL' and bot == 'TIJERA':
                print('Haz perdido')
                continue



if __name__ == "__main__":
    piedra_papel_tijera()