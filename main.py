from Aluno_Engenharia import AE_D_Participante,AE_Aeroespacial,AE_Civil,AE_D_ADM,AE_Eletrica,AE_Mecanica
from Aluno_Engenharia import limpar_tela,registrar
from typing import Type
from Materia import Materias_Eletrica,Materias_Aeroespacial_Civil_Mecanica
from Torneio import torneio,buscar_torneio_por_nome,buscar_aluno_por_nome,from_dict_torneio

import json

import sys



    

def login(nome:str)->None:
    while(True):
        nome=input("Qual o seu nome? ")
        if buscar_aluno_por_nome(nome)==None:
            print("Insira novamente")
            limpar_tela(2)
        else:
            break
    looby(nome)
    pass

# def registrar()->None:
#     pass

def Inicio()->None:
    while(True):
        nome=''
        entrada=input("Você já possui conta?\nResponda com 'Sim' ou 'Não'\t")
        if entrada=="Sim":
            login(nome)
            break
        elif entrada=="Não":    
            registrar()
            login(nome)
            break
        else:
            print("Nome Inválido tente novamente")
            limpar_tela(2)

def mostradisplay_lobby():
    pass
                                                                        
                                                                                                                                                                                                              
def looby(nome:str)->None:
    mostradisplay_lobby(nome)
    

def encerramento():
    pass

def alterar_materia(nome: str):
    aluno=buscar_aluno_por_nome(nome)
    aluno._alterar_materias()
    looby(nome)

def multiplayer(nome:str):
    pass
def solo(nome:str):
    pass

def mostradisplay_lobby(nome:str):
    opcoes = [
        "Solo",
        "Multiplayer",
        "Alterar Materia",
        "Ajuda",
        "Sair"
    ]
    
    while True:
        aluno=buscar_aluno_por_nome(nome)
        limpar_tela(0)
        print("\033[1;34m" + "="*40 + "\033[0m")  # linha azul em negrito
        print("\033[1;33m\t  Bem-Vindo  ao \n\t    Brains Bet\033[0m")
        print(f"\033[1;33mUsuário: {aluno.nome}      BrainCoins: {aluno.ler_braincoin}\n\n ESCOLHA UMA OPÇÃO\n\033[0m")
        print("\033[1;34m" + "="*40 + "\033[0m\n")
        
        for i, opcao in enumerate(opcoes, 1):
            print(f"\033[1;32m[{i}]\033[0m \033[1;37m{opcao}\033[0m")
        
        print("\nDigite a ação desejada:")
        escolha = input()
                    
        match escolha:
            case "Ajuda":
                tela_ajuda(nome)
            case "Multiplayer":
                multiplayer()
            case "Solo":
                solo(nome)
            case "Alterar Materia":
                alterar_materia(nome)
            case "Sair":    
                print("Muito obrigado volte sempre!\n\n")
                sys.exit(0)
                break
            case _:
                print("Insira novamente\nDica: Não insira o número, insira a ação")
                input("Pressione ENTER para voltar ao menu...")



def tela_ajuda(nome:str):
    limpar_tela(0)
    print("\033[1;35m" + "="*40 + "\033[0m")  # linha roxa negrito
    print("\033[1;33m📚  TELA DE AJUDA - COMO USAR O JOGO 📚\033[0m")
    print("\033[1;35m" + "="*40 + "\033[0m\n")
    
    print("\033[1;36m🎮 Intuito do jogo:\033[0m")
    print("  Este jogo tem como objetico incentivar as pessoas a estudarem através da competição")
    
    
    
    print("\033[1;36m🧠 Dicas para melhorar:\033[0m")
    print("  💡 Estude um pouco todo dia para acumular Brain Coins.")
    print("  🏆 Participe dos torneios com as materias mais dificeis para ganhar mais pontos.")
    print("  📝 Seja administrador de torneios\n")    
    
    print("\033[1;34m" + "="*40 + "\033[0m")
    input("Pressione ENTER para voltar...")
    looby(nome)    

def solo(nome:str)->None:
    limpar_tela(0)
    aluno=buscar_aluno_por_nome(nome)
    while(True):
        escolha=input("O que deseja fazer?\n Estudar ou Voltar ao Looby?\t")
        if escolha=="Estudar" or escolha=="Looby":
            break
        else:
            print("Entrada inválida!\nInsira novamente\n Caso queira só voltar ao looby insira 'Looby'")
            limpar_tela(2)
    match escolha:
        case "Estudar":
            aluno.estudar()
            looby(nome)
        case "Looby":
            looby(nome)

def exibir_torneio_usuario(nome):
    aluno=buscar_aluno_por_nome(nome)
    torneios_do_aluno=aluno.buscar_torneios_do_aluno(nome)
    limpar_tela(0)
    while(True):
        print("Os seus torneios são:")
        for i in torneios_do_aluno:
            print(i)    

def acessar_torneio(nome:str)->None:
    pass

def criar_torneio(nome:str)->None:
    pass

def multiplayer(nome:str):

    acessar='Acessar Torneios'
    criar='Criar Torneio'
    voltar='Voltar ao Looby'

    escolhas=[acessar,voltar,criar]


    limpar_tela(0)
    while(True):
        escolha=input("O que deseja fazer?\n 'Acessar Torneios', 'Criar Torneios' ou 'Voltar ao Looby'?")
        if escolha in escolhas:
            break
        else:
            print("Entrada inválida!\nInsira novamente")
            limpar_tela(2)

    match escolha:
        case 'Acessar Torneios':
            acessar_torneio(nome)
        case 'Criar Torneio':
            criar_torneio(nome)
        case 'Voltar ao Looby':
            looby(nome)
        
def acessar_torneio(nome:str)->None:
    aluno=buscar_aluno_por_nome(nome)
    torneios_do_aluno=aluno.buscar_torneios_do_aluno(nome)
    while(True):
        aluno.buscar_torneios_do_aluno()
        nome_torneio=input("Insira o nome do torneio: ")
        if not (nome_torneio  in torneios_do_aluno):
            print("Não existe este torneio\nInsira Outro:")
            limpar_tela(3)
        else:
            break
    limpar_tela(0)
    while(True):
        escolha=input("O que deseja fazer?\n'Estudar' 'Exibir dados'?")
        if escolha=='Estudar' or escolha=='Exibir dados':
            break
        else:
            print("Entrada inválida!\nInsira novamente")
            limpar_tela(2)
    torneioo=from_dict_torneio(buscar_torneio_por_nome(nome_torneio))
    match escolha:
        case 'Estudar':
            torneioo.Registrar_Estudo()
            looby(nome)
        case 'Exibir dados':
            torneioo.Mostrar_Dados_Torneio()
            looby(nome)


def criar_torneio(nome:str)->None:
    aluno=buscar_aluno_por_nome(nome)
    torneioo=torneio(AE_D_ADM(aluno))
    while(True):
        
        escolha=input("Deseja dicionar mais participantes?\n'Sim'\t'Nao")
        if escolha=='Sim' or escolha == 'Nao':
            if escolha=='Sim':
                torneioo._adicionar_participante()
                continue
            break
                
        else:
            print("Entrada invalida\nInsira outra coisa")
            limpar_tela(2)
        looby(nome)
    

Inicio()
