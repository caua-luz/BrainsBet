from abc import ABC, abstractmethod
import os
import time
import json
from typing import List

from Materia import materia,Materias_Eletrica,Materias_Aeroespacial_Civil_Mecanica


def atualizar_somando_braincoins(aluno_novo, arquivo="pessoas.json"):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []

    nome_novo = aluno_novo.nome
    curso_novo = aluno_novo.curso
    instituicao_nova = aluno_novo.instituicao
    braincoins_novo = aluno_novo.ler_braincoin

    total_braincoins = braincoins_novo
    novos_dados = []
    atualizado = False

    for aluno in dados:
        if (
            aluno["nome"] == nome_novo and
            aluno["curso"] == curso_novo and
            aluno["instituicao"] == instituicao_nova
        ):
            total_braincoins += aluno.get("braincoins", 0.0)
            atualizado = True
        else:
            novos_dados.append(aluno)

    # Atualiza ou cria a entrada consolidada
    aluno_dict = to_dict(aluno_novo)
    aluno_dict["braincoins"] = total_braincoins
    novos_dados.append(aluno_dict)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(novos_dados, f, indent=4, ensure_ascii=False)

def from_dict(dado: dict):
    # Mapeamento de classes
    CLASSES = {
        "AE_D_ADM": AE_D_ADM,
        "AE_D_Participante": AE_D_Participante,
        "AE_Eletrica": AE_Eletrica,
        "AE_Civil": AE_Civil,
        "AE_Aeroespacial": AE_Aeroespacial,
        "AE_Mecanica": AE_Mecanica
    }

    # Criar a instância de aluno com os dados do dicionário
    nome = dado.get("nome", "")
    instituicao = dado.get("instituicao", "")
    curso = dado.get("curso", "")
    materias_cursando = dado.get("materias_cursando", [])

    # Supondo que as subclasses de Aluno_Eng sejam instanciadas aqui
    # Aqui você cria a instância correta de acordo com o curso do aluno
    if curso == "Engenharia Eletrica":
        aluno = AE_Eletrica(nome, instituicao)
    elif curso == "Engenharia Civil":
        aluno = AE_Civil(nome, instituicao)
    elif curso == "Engenharia Aeroespacial":
        aluno = AE_Aeroespacial(nome, instituicao)
    elif curso == "Engenharia Mecanica":
        aluno = AE_Mecanica(nome, instituicao)
    else:
        raise ValueError(f"Curso desconhecido: {curso}")

    # Atribuir dados extras que não são passados no construtor
    aluno._braincoins = dado.get("braincoins", 0)
    aluno._BrainCoins_Torneio = dado.get("BrainCoins_Torneio", 0)
    aluno.materias_cursando = set(materias_cursando)
    aluno.campeao = dado.get("campeao")

    # Verifica a classe do administrador ou participante e instancia corretamente
    classe = dado.get("classe", None)
    cls = CLASSES.get(classe, None)
    
    if not cls:
        raise ValueError(f"Classe não encontrada: {classe}")
    
    # Agora passamos a instância de aluno para a classe de administrador ou participante
    if classe == "AE_D_Participante":
        return AE_D_Participante(aluno)
    elif classe == "AE_D_ADM":
        return AE_D_ADM(aluno)
    
    return aluno


def buscar_aluno_por_nome(nome: str, arquivo="pessoas.json"):
    try:

        with open(arquivo, "r") as f:
            dados = json.load(f)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro ao ler o conteúdo do arquivo JSON.")
        return None

    for aluno in dados:

        if aluno["nome"] == nome:

            return from_dict(aluno)

    print(f"aluno com nome '{nome}' não encontrado.")
    return None


def to_dict(classe) -> dict:
    return {
        "classe": classe.__class__.__name__,
        "nome": classe.nome,
        "instituicao": classe.instituicao,
        "curso": classe.curso,
        "braincoins": float(classe._braincoins),
        "materias_cursando": [m.nome for m in classe.materias_cursando]  # apenas nomes
    }

def to_dict(classe) -> dict:
    return {
        "classe": classe.__class__.__name__,
        "nome": classe.nome,
        "instituicao": classe.instituicao,
        "curso": classe.curso,
        "braincoins": float(classe._braincoins),
        "materias_cursando": [m for m in classe.materias_cursando]  # apenas nomes
    }




def salvar_aluno(aluno):
    try:
        with open("pessoas.json", "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []

    aluno_dict = to_dict(aluno)

    # Verifica se já existe um aluno com mesmo nome, curso e instituição
    for existente in dados:
        if (
            existente["nome"] == aluno_dict["nome"] and
            existente["curso"] == aluno_dict["curso"] and
            existente["instituicao"] == aluno_dict["instituicao"]
        ):
            print(f"Aluno '{aluno_dict['nome']}' já está salvo. Ignorando duplicata.")
            return

    dados.append(aluno_dict)

    with open("pessoas.json", "w") as f:
        json.dump(dados, f, indent=4)

    print(f"Aluno '{aluno_dict['nome']}' salvo com sucesso.")

def atualizar_aluno(aluno, arquivo="pessoas.json"):
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []

    aluno_dict = to_dict(aluno)
    nome = aluno_dict.get("nome")
    curso = aluno_dict.get("curso")
    instituicao = aluno_dict.get("instituicao")

    atualizado = False
    novos_dados = []

    for a in dados:
        if a.get("nome") == nome and a.get("curso") == curso and a.get("instituicao") == instituicao:
            novos_dados.append(aluno_dict)  # Substitui o antigo
            atualizado = True
        else:
            novos_dados.append(a)

    if not atualizado:
        novos_dados.append(aluno_dict)  # Se não achou, adiciona como novo

    with open(arquivo, "w") as f:
        json.dump(novos_dados, f, indent=4)


def limpar_tela(tempo:int)->None:
    # Se for Windows, usa 'cls'
    # Se for Linux/macOS, usa 'clear'
    time.sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')

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

def registrar_no_json(nome:str,instituicao:str,Curso:str)->None:
    match Curso:
        case "Eletrica":
            Registro=AE_Eletrica(nome,instituicao)
            Registro._inserir_materias()
            Registro._inserir_materias()
            Registro._inserir_materias()
            salvar_aluno(Registro)
        case "Civil":
            Registro=AE_Civil(nome,instituicao)
            Registro._inserir_materias()
            Registro._inserir_materias()
            Registro._inserir_materias()
            salvar_aluno(Registro)
        case "Mecanica":
            Registro=AE_Mecanica(nome,instituicao)
            Registro._inserir_materias()
            Registro._inserir_materias()
            Registro._inserir_materias()
            salvar_aluno(Registro)
        case "Aeroespacial":
            Registro=AE_Aeroespacial(nome,instituicao)
            Registro._inserir_materias()
            Registro._inserir_materias()
            Registro._inserir_materias()
            salvar_aluno(Registro)
    

def registrar()->None:
     limpar_tela(0)
     print("Ola! Bem Vindo ao BrainsBet")
     print("O seu aplicativo de incentivo ao estudo")
     limpar_tela(3)
     Curso=""
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
    def modificar_braincoin(self):
        return self._braincoins

    @modificar_braincoin.setter
    def modificar_braincoin(self,valor)->None:
        self._braincoins=valor#+self.ler_braincoin


    def buscar_torneios_administrados_por(self, arquivo="torneios.json") -> List[str]:
        instancia_ae= self
        nome_aluno = instancia_ae.nome
        curso_aluno = instancia_ae.curso
        instituicao_aluno = instancia_ae.instituicao
        torneios_administrados = []

        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o JSON em '{arquivo}'.")
            return []

        for torneio in dados:
            adm = torneio.get("administrador", {})
            if (
                adm.get("nome") == nome_aluno and
                adm.get("curso") == curso_aluno and
                adm.get("instituicao") == instituicao_aluno
            ):
                torneios_administrados.append(torneio.get("nome_torneio"))

        return torneios_administrados
                    

    def _inserir_materias(self)->None:
        limpar_tela(0)
        p=''
        materia=''
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
                        quebra=True
            if quebra:
                print(f"A materia é {materia}")
                self.materias_cursando.add(materia)
                print("Agora voce esta cursando:")
                for i in self.materias_cursando:
                    print(i)
                
                atualizar_aluno(self)
                input("\n\nInsira qualquer coisa para continuar")                 
                break
            else:
                    print("Nome invalido! insira novamente")
    def _remover_materias(self)->None:
        limpar_tela(0)
        p=''
        materia=''
        while(True):
            limpar_tela(1)
            print("Qual das materias abaixo deseja remover?\n")
            for p in self.materias_cursando:
                    print(p)
            materia=input()

            quebra=False
            for p in self.materias_cursando:
                    #materia existe
                    if p==materia:
                        quebra=True
            if quebra:
                print(f"A materia é {materia}")
                self.materias_cursando.discard(materia)
                print("Agora voce esta cursando:")
                for i in self.materias_cursando:
                    print(i)
                
                atualizar_aluno(self)
                input("\n\nInsira qualquer coisa para continuar")                 
                break
            else:
                    print("Nome invalido! insira novamente")      

    
    def _alterar_materias(self)->None:
        limpar_tela(0)
        while True:
            opcao = input("Deseja 'Inserir' ou 'Remover'?\t")

            if opcao in ("Inserir", "Remover"):
                break
            else:
                 print("Opção inválida. Tente novamente.")

        if opcao == "Inserir":
           self._inserir_materias()

        if opcao == "Remover":
            self._remover_materias()
        

    def estudar(self)->None:
        while(True):
            limpar_tela(0)
            loop=False
            print("Você está cursando:")
            for i in self.materias_cursando:
                print(i)
            nome=input("Qual o nome da materia que deseja estudar? \t")
            for i in self.materias_cursando:
                if nome==i:
                   loop=True
                   break
            if loop:
                break                    
            else:
                print("Esta materia não está sendo cursada insira outra")
                limpar_tela(2)
                
        tempo=float(input("Por quantas horas?\t"))
        self.modificar_braincoin=float(0.01*tempo)+self.ler_braincoin
        print(f"O estudo rendeu {float(0.01*tempo)+self.ler_braincoin} BrainCoins")
        salvar_aluno(self)
        input("Pressione qualquer coisa para continuar...")
        limpar_tela(0)
        atualizar_somando_braincoins(buscar_aluno_por_nome(self.nome))
                
    def buscar_torneios_do_aluno(self, arquivo="torneios.json")->None:
        """
        Retorna uma lista com os nomes dos torneios em que o aluno especificado participa.
        
        :param nome_aluno: Nome do aluno a ser buscado.
        :param arquivo: Caminho para o arquivo JSON com os torneios.
        :return: Lista de nomes de torneios.
        """
        nome_aluno=self.nome
        try:
            with open(arquivo, "r") as f:
                torneios = json.load(f)
        except FileNotFoundError:
            print("Arquivo de torneios não encontrado.")
            return []
        except json.JSONDecodeError:
            print("Erro ao ler o JSON de torneios.")
            return []

        torneios_do_aluno = []

        for torneio in torneios:
            for participante in torneio.get("participantes", []):
                if participante.get("nome", "").lower() == nome_aluno.lower():
                    torneios_do_aluno.append(torneio.get("nome_torneio"))
                    break  # Não precisa verificar mais participantes

        return torneios_do_aluno


                



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
    def Retornar_BrainCoins_Torneio(self)->float:
        pass 

  


class AE_D_Participante(AE_Desafio):
    def __init__(self,Aluno_Eng):
        super().__init__(Aluno_Eng)
        
        self.campeao=False
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

    def Retornar_BrainCoins_Torneio(self,posicao_torneio:int,numero_de_participantes:int,peso_materia:float)->float:
        
        if(self.campeao==True):
            self.Set_braincoins_torneio=10*numero_de_participantes*peso_materia
            print(f"O torneio rendeu a {self.nome} o total de {self.Get_braincoins_torneio} BrainCoins\n")
            return 10*numero_de_participantes*peso_materia
        else:
            self.Set_braincoins_torneio= (numero_de_participantes*peso_materia-posicao_torneio)/10
            return (numero_de_participantes*peso_materia-posicao_torneio)/10

class AE_D_ADM(AE_Desafio):
    def __init__(self,Aluno_Eng):
        super().__init__(Aluno_Eng)
        

    def Retornar_BrainCoins_Torneio(self)->float:
        self._braincoins+=10
        print(f"O torneio rendeu a {self.nome} o total de {self.Get_braincoins_torneio} BrainCoins\n")
        return 10    

# registrar()
# remover_aluno_por_nome("Lili")
