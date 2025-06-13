from abc import ABC, abstractmethod
import os
import time
import json

from Materia import Materias_Eletrica,Materias_Aeroespacial_Civil_Mecanica



def to_dict(classe) -> dict:
    return {
        "classe": classe.__class__.__name__,
        "nome": classe.nome,
        "instituicao": classe.instituicao,
        "curso": classe.curso,
        "braincoins": classe._braincoins,
        "materias_cursando": [m.nome for m in classe.materias_cursando]  # apenas nomes
    }

def remover_aluno_por_nome(nome: str, arquivo="pessoas.json"):
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    novos_dados = [aluno for aluno in dados if aluno["nome"] != nome]

    with open(arquivo, "w") as f:
        json.dump(novos_dados, f, indent=4)


def salvar_aluno(aluno):
    try:
        with open("pessoas.json", "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []

    dados.append(to_dict(aluno))

    with open("pessoas.json", "w") as f:
        json.dump(dados, f, indent=4)


def limpar_tela(tempo:int)->None:
    # Se for Windows, usa 'cls'
    # Se for Linux/macOS, usa 'clear'
    time.sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')


def registrar_no_json(nome:str,instituicao:str,Curso:str)->None:
    match Curso:
        case "Eletrica":
            Registro=AE_Eletrica(nome,instituicao)
            Registro.inserir_materias()
            Registro.inserir_materias()
            Registro.inserir_materias()
            salvar_aluno(Registro)
        case "Civil":
            Registro=AE_Civil(nome,instituicao)
            Registro.inserir_materias()
            Registro.inserir_materias()
            Registro.inserir_materias()
            salvar_aluno(Registro)
        case "Mecanica":
            Registro=AE_Mecanica(nome,instituicao)
            Registro.inserir_materias()
            Registro.inserir_materias()
            Registro.inserir_materias()
            salvar_aluno(Registro)
        case "Aeroespacial":
            Registro=AE_Aeroespacial(nome,instituicao)
            Registro.inserir_materias()
            Registro.inserir_materias()
            Registro.inserir_materias()
            salvar_aluno(Registro)

def registrar()->None:
     print("Ola! Bem Vindo ao BrainsBet")
     print("O seu aplicativo de incentivo ao estudo")
     limpar_tela(3)
     Curso="0"
     nome=input("Para começarmos, qual o seu nome? ")
     instituicao=input("Qual a sua instituição? ")
     while(True):
        print("Qual a sua Engenharia? ")
        print("\nResponda com as seguintes opções\nCivil     Mecanica    Eletrica    Aeroespacial")
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
        while(True):
            limpar_tela(1)
            print("Qual das materias abaixo deseja inserir?\n")
            for p in self.materias:
                    print(p.nome)
            materia=input()

            quebra=False
            for p in self.materias:
                    #materia existe
                    if p.nome==materia:
                        self.materias_cursando.add(p)
                        quebra=True
            if quebra:
                break
            else:
                print("Nome invalido! insira novamente")       

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
        

        
class AE_Civil(Aluno_Engenharia):
    def __init__(self, nome,instituicao):
        super().__init__(nome,instituicao)
        self.curso="Engenharia Civil"
        self.materias=Materias_Aeroespacial_Civil_Mecanica
        
        

class AE_Aeroespacial(Aluno_Engenharia):
    def __init__(self, nome,instituicao):
        super().__init__(nome,instituicao)
        self.curso="Engenharia Aeroespacial"
        self.materias=Materias_Aeroespacial_Civil_Mecanica
        
                    

class AE_Mecanica(Aluno_Engenharia):
    def __init__(self, nome,instituicao):
        super().__init__(nome,instituicao)
        self.curso="Engenharia Mecanica"
        self.materias=Materias_Aeroespacial_Civil_Mecanica
        
 

#Esta classe parte do principio que                             
class AE_Desafio(AE_Aeroespacial,AE_Civil,AE_Eletrica,AE_Mecanica):
    def __init__(self,Aluno_Eng):
        self.nome=Aluno_Eng.nome
        self.curso=Aluno_Eng.curso
        self.instituicao=Aluno_Eng.instituicao
        self._braincoins=Aluno_Eng._braincoins
        self.materias=Aluno_Eng.materias
        self.materias_cursando=Aluno_Eng.materias_cursando

        
        

    @abstractmethod
    def _Retornar_BrainCoins_Torneio(self)->float:
        pass 

  


class AE_D_Participante(AE_Desafio):
    def __init__(self,Aluno_Eng):
        super().__init__(Aluno_Eng)
        self._BrainCoins_Torneio=0
        self._campeao=False
        self._braincoins_torneio=float(0)

    @property
    def Get_braincoins_torneio(self)->float:
        return self._braincoins_torneio 

    @property
    def Set_braincoins_torneio(self)->float:
        return self._braincoins_torneio   
    
    @Set_braincoins_torneio.setter
    def Set_braincoins_torneio(self,valor:float)->None:
        self._braincoins_torneio=float(valor)

    def _Retornar_BrainCoins_Torneio(self,posicao_torneio:int,numero_de_participantes:int,peso_materia:float)->float:
        if(self.campeao==True):
            return 10*numero_de_participantes*peso_materia
        else:
            return (numero_de_participantes*peso_materia-posicao_torneio)/10

class AE_D_ADM(AE_Desafio):
    def __init__(self,Aluno_Eng):
        super().__init__(Aluno_Eng)
        

    def _Retornar_BrainCoins_Torneio(self)->float:
        return 10    

# registrar()
