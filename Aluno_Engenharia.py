from Materia import materia,Materias_Eletrica#,Materias_Aeroespacial_Civil_Mecanica
from abc import ABC, abstractmethod
import os
import time

def limpar_tela(tempo:int)->None:
    # Se for Windows, usa 'cls'
    # Se for Linux/macOS, usa 'clear'
    time.sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')

def registrar_no_json(nome:str,instituicao:str,Curso:str)->None:
    match Curso:
        case "Eletrica":
            Registro=AE_Eletrica(nome,instituicao)
            print("Agora insira as 3 primeiras materias que vocÊ irá cursar agora:\n")
            print("Agora insira a primeira:\n")
            Registro.alterar_materias()
            print("Agora insira a segunda:\n")
            Registro.alterar_materias()
            print("Agora insira a terceira:\n")
            Registro.alterar_materias()


def registrar()->None:
     print("Ola! Bem Vindo ao BrainsBet")
     print("O seu aplicativo de incentivo ao estudo")
     limpar_tela(5)
     Curso="0"
     nome=input("Para começarmos, qual o seu nome? ")
     instituicao=input("Qual a sua instituição? ")
     while(True):
        print("Qual a sua Engenharia? ")
        print("\nResponda com as seguintes opções\nCivil Mecanica Eletrica Aeroespacial")
        Curso=input()
        #if Curso == "Civil" or Curso == "Aeroespacial" or Curso == "Mecanica" or Curso == "Eletrica":
        if Curso in ("Civil","Aeroespacial","Mecanica","Eletrica"):
            registrar_no_json(nome,instituicao,Curso)
            break
        else:
            print("Resposta Inválida")
            limpar_tela(1)
    
    
        
                

class Aluno_Engenharia(ABC):
    def __init__(self,nome,instituicao) -> None:
        self.nome=nome
        self.instituicao=instituicao
        self._braincoins=float(0)
        self.materias=[]
        self.materias_cursando=[]

    @abstractmethod
    def alterar_materias(self):
        pass


class AE_Eletrica(Aluno_Engenharia):
    def __init__(self, nome,instituicao) -> None:
        super().__init__(nome,instituicao)
        self.materias=Materias_Eletrica
        
               

    def alterar_materias(self):
        while True:
            opcao = input("Insira 'I' se deseja Inserir e 'R' se deseja Remover: ").strip().upper()

            if opcao in ('I', 'R'):
                break
            else:
                 print("Opção inválida. Tente novamente.")

        if opcao == "I":
            limpar_tela(1)
            print("Qual das materias abaixo deseja inserir?\n")
            for p in self.materias:
                print(p.nome)
            materia=input()
            for p in self.materias:
                #materia existe
                if p.nome==materia:
                    self.materias_cursando.add(p)

registrar()                    
