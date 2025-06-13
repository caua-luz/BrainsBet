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
        "BrainCoins_Torneio": float(classe.Get_braincoins_torneio),
        "materias_cursando": [m for m in classe.materias_cursando]  # apenas nomes
    }

def to_dict_adm(classe) -> dict:
    return {
        "classe": classe.__class__.__name__,
        "nome": classe.nome,
        "instituicao": classe.instituicao,
        "curso": classe.curso,
        "braincoins": classe._braincoins,
        "materias_cursando": [m for m in classe.materias_cursando]  # apenas nomes
    }

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
        salvar_torneio(self)
        self.atualizar_no_arquivo(self)


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
        
        torneio_dict = to_dict_torneio(self)  # Aqui chamamos a função que converte o torneio em um dicionário
        print(torneio_dict)
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


    def Registrar_Estudo(self) -> None:
        limpar_tela(0)
        participantes = self.participantes  # Pega a lista de participantes
        while True:
            print("Os participantes são estes: ")
            for i in participantes:
                print(i.nome)
            nome = input("Qual o participante está estudando?\t")
            nome_set = False
            for i in participantes:
                if nome == i.nome:
                    nome_set = True
            if not nome_set:
                print("Nome não encontrado")
                print("Coloque outro")
                limpar_tela(3)
            else:
                peso_materia_torneio = 0
                tempo = float(input("Por quantas horas?\t"))
                for i in self.administrador.materias:
                    if i.nome == self.materia_torneio:
                        peso_materia_torneio = i._peso
                        break
                for i in participantes:
                    if i.nome == nome:
                        incremento = tempo * peso_materia_torneio / 10
                        print(incremento)
                        
                        # Atualizando o valor com o setter
                        i.Set_braincoins_torneio += incremento  # Usa o setter corretamente
                        
                        print("par")
                        print(i.Set_braincoins_torneio)
                        break
                    else:
                        continue
        
                self.participantes = participantes  # Atualiza o set de participantes
                for i in self.participantes:
                    print(i.Set_braincoins_torneio)
        
                # Atualiza o arquivo após a alteração
                self.atualizar_no_arquivo()  # Agora isso vai garantir que o arquivo seja atualizado corretamente
                break

    def Mostrar_Dados_Torneio(self)->None:
        participantes=retornar_participantes_torneio(self.nome_torneio)
        participantes = sorted(participantes, key=lambda p: p.Get_braincoins_torneio, reverse=True)
        print(f"O torneio {self.nome_torneio} tem os seguintes dados: ")
        print(f"Administrador {self.administrador.nome}")
        print(f"E da materia {self.materia_torneio}")
        print("Tem os participantes: ")
        for i in participantes:
            print(f"\t{i.nome} tem {i.Get_braincoins_torneio}")

    @classmethod
    def from_dict_torneio(cls, dado: dict):
        administrador = from_dict(dado["administrador"])
        torneio = cls.__new__(cls)
        torneio.administrador = administrador
        torneio.nome_torneio = dado["nome_torneio"]
        torneio.materia_torneio = dado["materia_torneio"]  # Corrigido nome
        torneio.Dias_passados = dado.get("Dias_passados", 0)
        torneio.Duracao_desafio = dado["Duracao_desafio"]

        torneio.participantes = set[()]
        for p in dado.get("participantes", []):
            participante = from_dict(p)
            torneio.participantes.add(participante)

        return torneio


    def _adicionar_participante(self, nome_aluno: str):
        """
        Adiciona um aluno ao set de participantes do torneio, buscando-o em pessoas.json.
        """

        aluno = AE_D_Participante(buscar_aluno_por_nome(nome_aluno))
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
        "administrador": to_dict_adm(torneio.administrador),
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
    torneioo = torneio.__new__(torneio)
    
    # Preenche os atributos do torneio com os dados do dicionário
    torneioo.administrador = administrador
    torneioo.nome_torneio = dado["nome_torneio"]
    torneioo.materia_torneio = dado["materia_torneio"]
    torneioo.Dias_passados = dado.get("Dias_passados", 0)
    torneioo.Duracao_desafio = dado["Duracao_desafio"]

    # Converte os participantes para um set de objetos
    torneioo.participantes = set()
    for p in dado.get("participantes", []):
        participante = from_dict(p)  # Supondo que você tenha uma função `from_dict` para participantes
        torneioo.participantes.add(participante)

    return torneioo

def retornar_participantes_torneio(nome_torneio)->set:

    torneioo= buscar_torneio_por_nome(nome_torneio)
    participantes=set([])
    for i in torneioo["participantes"]:
        participantes.add(AE_D_Participante(from_dict(i)))
    return participantes

#--------------FUNÇÕES QUE AUXILIAM O FUNCIONAMENTO DE TORNEIO----------------------

# torneioo= from_dict_torneio(buscar_torneio_por_nome("tht"))
# torneioo.Mostrar_Dados_Torneio()
# torneioo.Registrar_Estudo()
# for i in torneioo.participantes:
#     print(i.nome)
#     print(i.Set_braincoins_torneio)

# for i in torneioo.participantes:

#     print(i.nome)
#     i.Set_braincoins_torneio=1+i.Set_braincoins_torneio
#     print(i.Set_braincoins_torneio)    
# print(to_dict_torneio(torneioo))
# torneioo.atualizar_no_arquivo()







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




    
            

# participantes=retornar_participantes_torneio("tht")
# participantes = sorted(participantes, key=lambda p: p.Get_braincoins_torneio, reverse=True)
# win
# for i in participantes:
#     print(f"O vencedor é \t{i.nome} com {i.Get_braincoins_torneio} BrainCoins do Torneio")
#     win=i
#     win._campeao=True
# win._Retornar_BrainCoins_Torneio(1,len(self.participantes),self.materia_torneio.peso) 
# for i in participantes:
#     if not i._campeao:
#         i._Retornar_BrainCoins_Torneio(1,len(self.participantes),self.materia_torneio.peso) 


# for i in participantes:
#     if i.nome==nome:
#         retorno=i
#         break
# print(i)
# print(i.nome) 
# print(i._braincoins) 
# print(i.Get_braincoins_torneio)


# print(torneioo.administrador)
