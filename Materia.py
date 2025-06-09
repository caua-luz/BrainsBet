class materia:
    def __init__(self,nome:str,peso:float,horas:int):
        self.nome=nome
        self._peso=peso
        self._horas=horas

# ------------------------ Físicas ------------------------
fund_mec = materia("Fundamentos de Mecanica", 4, 60)
fund_elmg = materia("Fundamentos de Eletromagnetismo", 3, 60)
fund_mecflu = materia("Fundamentos de Mecanica dos Fluidos", 3, 60)
fund_termo = materia("Fundamentos de Termodinâmica", 3, 60)
fund_mecso = materia("Fundamentos de Mecanica dos Solidos", 3, 60)
fund_mecflu_termo = materia("Fundamentos de Mecanica dos Fluidos e Termodinâmica", 3, 60)
fund_ooo = materia("Fundamentos de Ondas, Oscilações e Óptica", 4, 60)

# ------------------------ Cálculos ------------------------
c1 = materia("Calculo 1", 5, 90)
c2 = materia("Calculo 2", 2, 60)
c3 = materia("Calculo 3", 2, 60)
gaal = materia("Geometria Analitica e Algebra Linear", 3, 60)
eda = materia("Equacoes Diferenciais", 3, 60)

# --------------------- Programação -----------------------
pds1 = materia("Programacao e Desenvolvimento de Software 1", 3, 60)
pds2 = materia("Programacao e Desenvolvimento de Software 2", 3, 60)
prog_comp = materia("Programacao de Computadores", 2, 60)

Materias_Aeroespacial={c1,c2,c3,eda,fund_elmg,fund_mec,fund_mecflu,fund_mecso,prog_comp}

Materias_Civil={c1,c2,c3,eda,fund_elmg,fund_mec,fund_mecflu,prog_comp}

Materias_Mecanica={c1,c2,c3,eda,fund_elmg,fund_mec,fund_mecflu,fund_mecso,prog_comp}

#Diferencial fooo e pds1 e pds2
Materias_Eletrica={c1,c2,c3,eda,pds1,pds2,fund_elmg,fund_mec,fund_mecflu_termo,fund_ooo}
