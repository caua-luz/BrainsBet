from Aluno_Engenharia import AE_D_Participante,AE_Aeroespacial,AE_Civil,AE_D_ADM,AE_Eletrica,AE_Mecanica,limpar_tela,registrar
from typing import Type
from Materia import Materias_Eletrica,Materias_Aeroespacial_Civil_Mecanica
from Torneio import torneio

import json

def encerrar()->None:
    print("Muito obrigado volte sempre!")

def login()->None:
    pass

# def registrar()->None:
#     pass

def Inicio()->None:
    while(True):
        entrada=input("Você já possui conta?\nResponda com 'Sim' ou 'Não'\t")
        if entrada=="Sim":
            login()
            break
        elif entrada=="Não":    
            registrar()
            break
        else:
            "Nome Inválido tente novamente"

def mostradisplay_lobby():
    pass
                                                                        
                                                                        
                                                                                                                                                
def looby():
    mostradisplay_lobby()

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def encerramento():
    pass

def mostradisplay_lobby():
    opcoes = [
        "Solo",
        "Multiplayer",
        "Alterar Materia",
        "Ajuda",
        "Sair"
    ]
    
    while True:
        limpar_tela()
        print("\033[1;34m" + "="*30 + "\033[0m")  # linha azul em negrito
        print("\033[1;33m   Bem-Vindo ao \n    Brains Bet \n\n ESCOLHA UMA OPÇÃO\033[0m")
        print("\033[1;34m" + "="*30 + "\033[0m\n")
        
        for i, opcao in enumerate(opcoes, 1):
            print(f"\033[1;32m[{i}]\033[0m \033[1;37m{opcao}\033[0m")
        
        print("\nDigite o número da opção desejada:")
        escolha = input("> ").strip()
        
        if escolha in [str(i) for i in range(1, len(opcoes)+1)]:
            
            match escolha:
                case "Ajuda":
                    print('')
                case "Multiplayer":
                    print('')
                case "Solo":
                    print('')
                case "Alterar Materia":
                    print('')
                case "Sair":    
                    print('')
                case _:
                    break
            input("Pressione ENTER para voltar ao menu...")
        else:
            print("\n\033[1;31mOpção inválida! Tente novamente.\033[0m")
            input("Pressione ENTER para tentar de novo...")


def tela_ajuda():
    limpar_tela()
    print("\033[1;35m" + "="*40 + "\033[0m")  # linha roxa negrito
    print("\033[1;33m📚  TELA DE AJUDA - COMO USAR O JOGO 📚\033[0m")
    print("\033[1;35m" + "="*40 + "\033[0m\n")
    
    print("\033[1;36m🎮 Intuito do jogo:\033[0m")
    print("  Este jogo tem como objetico incentivar as pessoas a estudarem através da competição")
    print("  O jeito de ranquear")
    print("  ⏸️  Para pausar o jogo, pressione Ctrl+C.\n")
    
    print("\033[1;36m🧠 Dicas para melhorar:\033[0m")
    print("  💡 Estude um pouco todo dia para acumular Brain Coins.")
    print("  🏆 Participe dos torneios com as materias mais dificeis para ganhar mais pontos.")
    print("  📝 Seja administrador de torneios\n")    
    
    print("\033[1;34m" + "="*40 + "\033[0m")
    input("Pressione ENTER para voltar...")
    mostradisplay_lobby()    

mostradisplay_lobby()
