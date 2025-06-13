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

    print(f"aluno com nome '{nome}' não encontrado.")
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
        if Torneio.get("nome_torneio") == nome:
            return Torneio

    print(f"Torneio com nome '{nome}' não encontrado.")
    return None

#--------------FUNÇÕES QUE AUXILIAM O FUNCIONAMENTO DE TORNEIO----------------------



class torneio():
    # def __init__(self,administrador: Type[AE_D_ADM] ):
    #     self.administrador=administrador
    #     self.participantes=set([])
    #     self.nome_torneio=input("Qual o nome do torneio? ")
    #     while(True):
    #         print("Matérias que o administrador está cursando:")
    #         for mmateria in self.administrador.materias_cursando:
    #             print(mmateria.nome)
    #         maateria=input("Insira qual será a matéria tema do torneio das opcoes acima ")
    #         encontrou_materia=False
    #         for mmateria in self.administrador.materias_cursando:                
    #             if mmateria.nome==maateria:
    #                 self.materia_torneio=maateria
    #                 encontrou_materia=True
    #                 break
    #         if encontrou_materia==True:
    #             break
    #         else:
    #             print("Nome inválido")
    #             limpar_tela(1)
    #             print("Tente novamente")
    #             limpar_tela(1) 
                   
        # self.Dias_passados=0
        # self.Duracao_desafio=input("Qual sera a duracao do torneio em dias? ")
        # salvar_torneio(self)
        

    # @classmethod
    # def from_dict_torneio(cls, dado: dict):
    #     administrador = from_dict(dado["administrador"])
    #     torneio = cls.__new__(cls)
    #     torneio.administrador = administrador
    #     torneio.nome_torneio = dado["nome_torneio"]
    #     torneio.materia_torneio = dado["materia_torneio"]  # Corrigido nome
    #     torneio.Dias_passados = dado.get("Dias_passados", 0)
    #     torneio.Duracao_desafio = dado["Duracao_desafio"]

    #     torneio.participantes = set[()]
    #     for p in dado.get("participantes", []):
    #         participante = from_dict(p)
    #         torneio.participantes.add(participante)

    #     return torneio

    # def exibir_dados(self)->None:
    #     participantes=retornar_participantes_torneio(self.nome)
    #     for i in participantes:

    #         print(f"{i.}")

    def atualizar_no_arquivo(self, arquivo="torneios.json"):
        """
        Atualiza este torneio no arquivo JSON com base no nome do torneio.
        """
        try:
            with open(arquivo, "r") as f:
                torneios = json.load(f)
        except FileNotFoundError:
            print("Arquivo de torneios não encontrado.")
            return
        except json.JSONDecodeError:
            print("Erro ao ler o JSON de torneios.")
            return

        # Converte este torneio para dicionário
        torneio_dict = to_dict_torneio(self)

        atualizado = False
        for i, t in enumerate(torneios):
            if t.get("nome_torneio") == self.nome_torneio:
                torneios[i] = torneio_dict
                atualizado = True
                break

        if not atualizado:
            print(f"Torneio '{self.nome_torneio}' não encontrado no arquivo.")
            return

        with open(arquivo, "w") as f:
            json.dump(torneios, f, indent=4)

        print(f"Torneio '{self.nome_torneio}' atualizado com sucesso no arquivo.")


    def _adicionar_participante(self, nome_aluno: str):
        """
        Adiciona um aluno ao set de participantes do torneio, buscando-o em pessoas.json.
        """

        aluno = buscar_aluno_por_nome(nome_aluno)
        if aluno is None:
            print(f"Aluno '{nome_aluno}' não encontrado em pessoas.json.")
            return

        if aluno in self.participantes:
            print(f"O aluno '{nome_aluno}' já está participando deste torneio.")
            return

        self.participantes.add(aluno)
        print(f"Aluno '{nome_aluno}' adicionado com sucesso ao torneio '{self.nome_torneio}'.")
        self.atualizar_no_arquivo()



    # def registrar_estudo(self)->None:

    

        


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

def salvar_torneio(torneio, arquivo="torneios.json"):
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []
    except json.JSONDecodeError:
        dados = []

    dados.append(to_dict_torneio(torneio))

    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

    print(f"Torneio '{torneio.nome_torneio}' salvo com sucesso em '{arquivo}'.")



def from_dict_torneio(dado: dict):
    # Primeiro, criamos o administrador a partir do dicionário
    administrador = from_dict(dado["administrador"])  # Supondo que você tenha essa função de conversão para o administrador
    
    # Cria uma nova instância de Torneio
    torneio = Torneio.__new__(Torneio)
    
    # Preenche os atributos do torneio com os dados do dicionário
    torneio.administrador = administrador
    torneio.nome_torneio = dado["nome_torneio"]
    torneio.materia_torneio = dado["materia_torneio"]
    torneio.Dias_passados = dado.get("Dias_passados", 0)
    torneio.Duracao_desafio = dado["Duracao_desafio"]

    # Converte os participantes para um set de objetos
    torneio.participantes = set()
    for p in dado.get("participantes", []):
        participante = from_dict(p)  # Supondo que você tenha uma função `from_dict` para participantes
        torneio.participantes.add(participante)

    return torneio

def retornar_participantes_torneio(nome_torneio)->set:

    torneioo= buscar_torneio_por_nome(nome_torneio)
    participantes=set([])
    for i in torneioo["participantes"]:
        participantes.add(AE_D_Participante(from_dict(i)))
    return participantes

#--------------FUNÇÕES QUE AUXILIAM O FUNCIONAMENTO DE TORNEIO----------------------

# lili=AE_Civil("Lili","UFMG")
# lili.inserir_materias()
# torneioo=torneio(AE_D_ADM(lili))

# print(to_dict_torneio(torneioo))
# limpar_tela(0)
# torneioo._adicionar_participante("caua")
# print(to_dict_torneio(torneioo))
# print('')
# print('')
# asc=input()
# torneioo._adicionar_participante("Lili")
# print(to_dict_torneio(torneioo))
# asc=input()
# print('')
# print('')


# print(buscar_aluno_por_nome("c").nome)
# for i in buscar_aluno_por_nome("c").materias_cursando:
#     print(i.nome)
# print("\n")
# print(buscar_aluno_por_nome("C").nome)
# for i in buscar_aluno_por_nome("C").materias_cursando:
#     print(i.nome)    



# def retornar_um_participante_torneio(nome_torneio,nome)->AE_D_Participante:
#     participantes=retornar_participantes_torneio(nome_torneio)
#     retorno is AE_D_Participante
#     for i in participantes:
#         if i.nome==nome:
#             retorno=i
#             break
#         return retorno

participantes=retornar_participantes_torneio("tht")
for i in participantes:
     if i.nome=="caua":
         i._BrainCoins_Torneio=0
     if i.nome=="Lili":
         i._BrainCoins_Torneio=1

for i in participantes:
    print(f"{i.nome} tem {i._BrainCoins_Torneio}")


participantes_ordenados = sorted(participantes, key=lambda p: p.Get_braincoins_torneio, reverse=True)

for i in participantes:
    print(f"Final\t{i.nome} tem {i.Get_braincoins_torneio}")

# for i in participantes:
#     if i.nome==nome:
#         retorno=i
#         break
# print(i)
# print(i.nome) 
# print(i._braincoins) 
# print(i.Get_braincoins_torneio)


# print(torneioo.administrador)
