from Aluno_Engenharia import AE_D_Participante,AE_Aeroespacial,AE_Civil,AE_D_ADM,AE_Eletrica,AE_Mecanica,limpar_tela
from typing import Type
from Materia import Materias_Eletrica,Materias_Aeroespacial_Civil_Mecanica

import json

#--------------FUNÇÕES QUE AUXILIAM O FUNCIONAMENTO DE TORNEIO----------------------
def to_dict(classe) -> dict:
    return {
        "classe": classe.__class__.__name__,
        "nome": classe.nome,
        "instituicao": classe.instituicao,
        "curso": classe.curso,
        "braincoins": classe._braincoins,
        "BrainCoins_Torneio": classe._BrainCoins_Torneio,
        "materias_cursando": [m.nome for m in classe.materias_cursando]  # apenas nomes
    }

def from_dict(dado: dict):
 
    # Mapeamento de nomes para classes
    CLASSES = {
        "AE_D_ADM": AE_D_ADM,
        "AE_D_Participante": AE_D_Participante,
        "AE_Eletrica": AE_Eletrica,
        "AE_Civil": AE_Civil,
        "AE_Aeroespacial": AE_Aeroespacial,
        "AE_Mecanica": AE_Mecanica
    }

    # Mapeamento de curso para lista de matérias
    MATERIAS = {
        "Engenharia Eletrica": Materias_Eletrica,
        "Engenharia Civl": Materias_Aeroespacial_Civil_Mecanica,
        "Engenharia Aeroespacial": Materias_Aeroespacial_Civil_Mecanica,
        "Engenharia Mecanica": Materias_Aeroespacial_Civil_Mecanica
    }

    # Criar a instância da classe correta
    cls = CLASSES[dado["classe"]]
    aluno = cls(dado["nome"], dado["instituicao"])

    # Atribuir manualmente os atributos que não são passados no construtor
    aluno._braincoins = dado["braincoins"]
    aluno._BrainCoins_Torneio = dado.get("BrainCoins_Torneio", 0)

    # Reconstruir as matérias cursando
    materias_disponiveis = MATERIAS[dado["curso"]]
    aluno.materias_cursando = set(
        [m for m in materias_disponiveis if m.nome in dado["materias_cursando"]]
    )

    return aluno

def remover_aluno_por_nome(nome: str, arquivo="torneio.json"):
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    novos_dados = [aluno for aluno in dados if aluno["nome"] != nome]

    with open(arquivo, "w") as f:
        json.dump(novos_dados, f, indent=4)

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

    print(f"Torneio com nome '{nome}' não encontrado.")
    return None

def buscar_torneio_por_nome(nome: str, arquivo="torneios.json"):
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro ao ler o conteúdo do arquivo JSON.")
        return None

    for Torneio in dados:
        if Torneio["nome"] == nome:
            return Torneio

    print(f"Torneio com nome '{nome}' não encontrado.")
    return None

#--------------FUNÇÕES QUE AUXILIAM O FUNCIONAMENTO DE TORNEIO----------------------



class torneio():
    def __init__(self,administrador: Type[AE_D_ADM] ):
        self.administrador=administrador
        self.participantes=set([])
        self.nome_torneio=input("Qual o nome do torneio? ")
        while(True):
            print("Matérias que o administrador está cursando:")
            for mmateria in self.administrador.materias_cursando:
                print(mmateria.nome)
            maateria=input("Insira qual será a matéria tema do torneio das opcoes acima ")
            encontrou_materia=False
            for mmateria in self.administrador.materias_cursando:                
                if mmateria.nome==maateria:
                    self.materia_torneio=maateria
                    encontrou_materia=True
                    break
            if encontrou_materia==True:
                break
            else:
                print("Nome inválido")
                limpar_tela(1)
                print("Tente novamente")
                limpar_tela(1) 
                   
        self.Dias_passados=0
        self.Duracao_desafio=input("Qual sera a duracao do torneio em dias? ")
        
        #Função auxiliar de adicionar participante
    def from_dict_torneio(dado: dict):

        # Reconstruir o administrador com from_dict
        administrador = from_dict(dado["administrador"])  # Usa a função inversa que você já tem

        # Criar uma instância "vazia" do torneio
        torneio = torneio.__new__(torneio)  # Cria sem chamar __init__

        # Atribuir atributos manualmente
        torneio.administrador = administrador
        torneio.nome_torneio = dado["nome_torneio"]
        torneio.Materia = dado["Materia"]
        torneio.Dias_passados = dado.get("Dias_passados", 0)
        torneio.Duracao_desafio = dado["Duracao_desafio"]

        # Participantes (opcional)
        torneio.participantes = set()
        if "participantes" in dado:
            for participante_dict in dado["participantes"]:
                participante = from_dict(participante_dict)
                torneio.participantes.add(participante)

        return torneio
    
    def _adicionar_participante(self,nome:str)->None:
        #BUsca o nome no arquivo
        if buscar_aluno_por_nome(nome)==None:
            return print("Este aluno não existe em pessoas.json")
        #se existir ele retorna esse objeto
        aluno=buscar_aluno_por_nome(nome)
        #busca instancia o proprio torneio armazanado em torneios.json
        torneioo=self.from_dict_torneio(buscar_torneio_por_nome(self.nome_torneio))
        #adiciona o aluno buscado no set participantes
        torneioo.participantes.add(aluno)
        atualizar_torneio_por_nome(self.nome_torneio,torneioo)

    def _remover_participante(self,nome:str)->None:
        #BUsca o nome no arquivo
        if buscar_aluno_por_nome(nome)==None:
            return print("Este aluno não existe em pessoas.json")
        #se existir ele retorna esse objeto
        aluno=buscar_aluno_por_nome(nome)
        #busca instancia o proprio torneio armazanado em torneios.json
        torneioo=self.from_dict_torneio(buscar_torneio_por_nome(self.nome_torneio))
        #adiciona o aluno buscado no set participantes
        torneioo.participantes.discard(aluno)
        atualizar_torneio_por_nome(self.nome_torneio,torneioo)    
    

        


#--------------FUNÇÕES QUE AUXILIAM O FUNCIONAMENTO DE TORNEIO----------------------
def to_dict_torneio(torneio):  # conversão do objeto Torneio para dicionário
    return {
        "administrador": to_dict(torneio.administrador),
        "nome_torneio": torneio.nome_torneio,
        "materia_torneio": torneio.materia_torneio,
        "Dias_passados": torneio.Dias_passados,
        "Duracao_desafio": torneio.Duracao_desafio,
        "participantes": [to_dict(p) for p in torneio.participantes]
    }

def atualizar_torneio_por_nome(nome_torneio: str, novo_torneio, arquivo="torneios.json"):
    try:
        with open(arquivo, "r") as f:
            torneios = json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro ao ler o JSON.")
        return

    # Atualiza ou substitui o torneio existente
    atualizado = False
    for i, torneio in enumerate(torneios):
        if torneio.get("nome_torneio") == nome_torneio:
            torneios[i] = to_dict_torneio(novo_torneio)
            atualizado = True
            break

    if not atualizado:
        print(f"Torneio '{nome_torneio}' não encontrado. Nenhuma alteração feita.")
        return

    # Salva o arquivo atualizado
    with open(arquivo, "w") as f:
        json.dump(torneios, f, indent=4)
    print(f"Torneio '{nome_torneio}' atualizado com sucesso.")
#--------------FUNÇÕES QUE AUXILIAM O FUNCIONAMENTO DE TORNEIO----------------------

lili=AE_Civil("Lili","UFMG")
torneioo=torneio(AE_D_ADM(lili))
print(to_dict_torneio(torneioo))
