import random
import time


def best_of(x, y):
    if x == melhor:
        print("\nParábens Jogador, voce venceu a melhor de", melhor, "partidas\n")
        init()
    elif y == melhor:
        print("\nInfelizemente o Computador venceu a melhor de", melhor, "partidas"\n)
        init()
    else:
        return start(x, y)


def victory(choice, comp_choice, placar_player, placar_comp):

    print(f"\nEmbate: {choice} x {comp_choice}")
    time.sleep(1)
    if choice == "PEDRA" and comp_choice == "PAPEL":
        print("Vencedor: computador")
        placar_comp += 1
    elif choice == "PEDRA" and comp_choice == "TESOURA":
        print("Vencedor: jogador")
        placar_player += 1
    elif choice == "PAPEL" and comp_choice == "PEDRA":
        print("Vencedor: jogador")
        placar_player += 1
    elif choice == "PAPEL" and comp_choice == "TESOURA":
        print("Vencedor: computador")
        placar_comp += 1
    elif choice == "TESOURA" and comp_choice == "PEDRA":
        print("Vencedor: computador")
        placar_comp += 1
    elif choice == "TESOURA" and comp_choice == "PAPEL":
        print("Vencedor: jogador")
        placar_player += 1
    else:
        print("empate")
    time.sleep(2)
    return best_of(placar_player, placar_comp)


def escolhas(escolha, placar_player, placar_comp):

    choose = ""
    if escolha == 1:
        choose = "PEDRA"
    elif escolha == 2:
        choose = "PAPEL"
    elif escolha == 3:
        choose = "TESOURA"
    else:
        print("escolha invalida, retomando...")
        time.sleep(1)
        start(placar_player, placar_comp)
    L = ["PEDRA", "PAPEL", "TESOURA"]
    comp_choose = random.choice(L)

    return victory(choose, comp_choose, placar_player, placar_comp)


def start(placar_player, placar_comp):
    print("\nJOKEN PO")
    print("1 - PEDRA,2 - PAPEL,3 - TESOURA")
    print(f"\nPlacar - Jogador {placar_player} x {placar_comp} Computador")
    esc = int(input("escolha: "))
    escolhas(esc, placar_player, placar_comp)


def init():
    global melhor, cont

    placar_player = 0
    placar_comp = 0
    while True:
        print("Olá jogador, bem vindo ao Joken-PO.\n")
        melhor = int(input("Será melhor de quantas partidas? "))
        start(placar_player, placar_comp)


init()
