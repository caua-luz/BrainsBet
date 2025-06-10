from Materia import Materias_Eletrica,Materias_Aeroespacial_Civil_Mecanica
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
            #instanciar(Registro)
COLOCAR NO PESSOAS.JSON            

def registrar()->None:
     print("Ola! Bem Vindo ao BrainsBet")
     print("O seu aplicativo de incentivo ao estudo")
     limpar_tela(3)
     Curso="0"
     nome=input("Para começarmos, qual o seu nome? ")
     instituicao=input("Qual a sua instituição? ")
     while(True):
        print("Qual a sua Engenharia? ")
        print("\nResponda com as seguintes opções\nCivil Mecanica Eletrica Aeroespacial")
        Curso=input()
        
        if Curso in ("Civil","Aeroespacial","Mecanica","Eletrica"):
            registrar_no_json(nome,instituicao,Curso)
            break
        else:
            print("Resposta Inválida")
            limpar_tela(1)
    
    
        
                

class Aluno_Engenharia(ABC):
    def __init__(self,nome,instituicao) -> None:
        self.nome=nome
        self.curso=''
        self.instituicao=instituicao
        self._braincoins=float(0)
        self.materias=[]
        self.materias_cursando=set([])

    @property
    def ler_braincoin(self)->float:
        return self._braincoins
    
    @property
    def modificar_braincoin(self)->float:
        return self._braincoins

    @modificar_braincoin.setter
    def modificar_braincoin(self,valor:float,soma:bool,subtracao:bool,multiplicacao:bool,divisao:bool)->None:
        if soma:
            self._braincoins += valor
        elif subtracao:
            self._braincoins -= valor
        elif multiplicacao:
            self._braincoins *= valor
        elif divisao:                
            self._braincoins /= valor                

    def inserir_materias(self)-> None:
        limpar_tela(1)
        print("Qual das materias abaixo deseja inserir?\n")
        for p in self.materias:
                print(p.nome)
        materia=input()
        for p in self.materias:
                #materia existe
                if p.nome==materia:
                    self.materias_cursando.add(p)       

    def remover_materias(self)-> None:
        limpar_tela(1)
        print("Qual das materias abaixo deseja Remover?\n")
        for p in self.materias_cursando:
            print(p.nome)
        materia=input()
        for p in self.materias_cursando:
                #materia existe
                if p.nome==materia:
                    break
        self.materias_cursando.discard(p)
    
    def alterar_materias(self)-> None:
        while True:
            opcao = input("Insira 'I' se deseja Inserir e 'R' se deseja Remover: ").strip().upper()

            if opcao in ('I', 'R'):
                break
            else:
                 print("Opção inválida. Tente novamente.")

        if opcao == "I":
           self.inserir_materias()

        if opcao == "R":
            self.remover_materias()



class AE_Eletrica(Aluno_Engenharia):
    def __init__(self, nome,instituicao):
        super().__init__(nome,instituicao)
        self.curso="Engenharia Eletrica"
        self.materias=Materias_Eletrica
        
        print("Agora insira as 3 primeiras materias que vocÊ irá cursar agora:\n")
        print("Agora insira a primeira:\n")
        limpar_tela(5)
        self.inserir_materias()
        limpar_tela(5)
        print("Agora insira a segunda:\n")
        limpar_tela(5)
        self.inserir_materias()
        
        print("Agora insira a terceira:\n")
        limpar_tela(5)
        self.inserir_materias()
        limpar_tela(0)
        print("Suas materias são: ")
        for i in self.materias_cursando:
            print(f"{i.nome}")
        
class AE_Civil(Aluno_Engenharia):
    def __init__(self, nome,instituicao):
        super().__init__(nome,instituicao)
        self.curso="Engenharia Civl"
        self.materias=Materias_Aeroespacial_Civil_Mecanica
        
        print("Agora insira as 3 primeiras materias que vocÊ irá cursar agora:\n")
        print("Agora insira a primeira:\n")
        limpar_tela(5)
        self.inserir_materias()
        limpar_tela(5)
        print("Agora insira a segunda:\n")
        limpar_tela(5)
        self.inserir_materias()
        
        print("Agora insira a terceira:\n")
        limpar_tela(5)
        self.inserir_materias()
        limpar_tela(0)
        print("Suas materias são: ")
        for i in self.materias_cursando:
            print(f"{i.nome}")        

class AE_Aeroespacial(Aluno_Engenharia):
    def __init__(self, nome,instituicao):
        super().__init__(nome,instituicao)
        self.curso="Engenharia Aeroespacial"
        self.materias=Materias_Aeroespacial_Civil_Mecanica
        
        print("Agora insira as 3 primeiras materias que vocÊ irá cursar agora:\n")
        print("Agora insira a primeira:\n")
        limpar_tela(5)
        self.inserir_materias()
        limpar_tela(5)
        print("Agora insira a segunda:\n")
        limpar_tela(5)
        self.inserir_materias()
        
        print("Agora insira a terceira:\n")
        limpar_tela(5)
        self.inserir_materias()
        limpar_tela(0)
        print("Suas materias são: ")
        for i in self.materias_cursando:
            print(f"{i.nome}")                    

class AE_Mecanica(Aluno_Engenharia):
    def __init__(self, nome,instituicao):
        super().__init__(nome,instituicao)
        self.curso="Engenharia Mecanica"
        self.materias=Materias_Aeroespacial_Civil_Mecanica
        
        print("Agora insira as 3 primeiras materias que vocÊ irá cursar agora:\n")
        print("Agora insira a primeira:\n")
        limpar_tela(5)
        self.inserir_materias()
        limpar_tela(5)
        print("Agora insira a segunda:\n")
        limpar_tela(5)
        self.inserir_materias()
        
        print("Agora insira a terceira:\n")
        limpar_tela(5)
        self.inserir_materias()
        limpar_tela(0)
        print("Suas materias são: ")
        for i in self.materias_cursando:
            print(f"{i.nome}") 
                            
class AE_Desafio(Aluno_Engenharia):
    def __init__(self, nome, instituicao):
        super().__init__(nome, instituicao)
        self._braincoins_torneio=float(0)
        self.campeao=False

    @abstractmethod
    def _Retornar_BrainCoins_Torneio(self)->float:
        pass    

class AE_D_Participante(AE_Desafio):
    def __init__(self, nome, instituicao):
        super().__init__(nome, instituicao)

    def _Retornar_BrainCoins_Torneio(self,posicao_torneio:int,numero_de_participantes:int,peso_materia:float)->float:
        if(self.campeao==True):
            return posicao_torneio*numero_de_participantes*peso_materia
        else:
            return (posicao_torneio*numero_de_participantes*peso_materia)/10

class AE_D_ADM(AE_Desafio):
    def __init__(self, nome, instituicao):
        super().__init__(nome, instituicao)

    def _Retornar_BrainCoins_Torneio(self,posicao_torneio:int,numero_de_participantes:int,peso_materia:float)->float:
        if(self.campeao==True):
            return (posicao_torneio*numero_de_participantes*peso_materia)+5
        else:
            return ((posicao_torneio*numero_de_participantes*peso_materia)/10)+5    

registrar()                    
