"""
Exemplo de classe
Aluno - matricula, nome, curso, nota

1 - João, Python, 10
2 - Manoela, Javascript, 9.9
"""
from dataclasses import dataclass #Nova forma de declarar classes

#Criando uma classe
class Aluno: #Classe sempre letra maiuscula

    #Função/método construtor
    def __init__(self, matricula:int, nome: str, curso: str,
                 nota: float): # self, parâmetros da função

        # Definição de atributos
        self.matricula = matricula  #self.atributo = valor
        self.nome = nome
        self.curso = curso
        self.nota = nota
        self.qtd_faltas = 0
        print(f"Bem vindo, {self.nome}")

    def atribuirFaltas(self):
        print(f"Falta atribuída ao aluno {self.nome}")
        self.qtd_faltas +=1


# Declaração de objeto
aluno1 = Aluno(matricula=1,nome="Daniel",curso="Python",nota=10.0)
aluno2 = Aluno(matricula= 2,nome="Joanilda",curso="NodeJs",nota= 4.3)

# Como acessar/alterar um atributo de um objeto
print(f"\nNome: {aluno1.nome}")
print(f"Nome: {aluno2.nome}\n")

aluno2.nome = "Joana Silva"
print(f"""Aluno 2: {aluno2.nome}
Curso:   {aluno2.curso}\n""")

# Como chamar uma função de um objeto?
aluno1.atribuirFaltas()
aluno1.atribuirFaltas()
aluno1.atribuirFaltas()

aluno2.atribuirFaltas()
print(f"""\nFaltas aluno 01: {aluno1.qtd_faltas} faltas
Faltas Aluno 02: {aluno2.qtd_faltas} faltas""")


# Classe para representar um carro
class Carro:
    def __init__(self, marca: str, modelo: str, cor: str, status: bool):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.status = status
        self.velocidade = 0

    def ligarCarro(self):
        self.status = True
    def desligarCarro(self):
        self.status = False

    def acelerarCarro(self):
        if self.status:
            print("Velocidade Aumentada")
            self.velocidade+=20


# Acrescente novo atributo booleano para indicar se o carro está ligado ou desligado

# Crie 2 carros e imprima todas as info dos carros
carro1 = Carro(cor="Branco",marca="Volkswagem",modelo="Golzin",status=False)
print(f"""
      Marca: {carro1.marca}
      Modelo: {carro1.modelo}
      Cor: {carro1.cor}
      Status: {carro1.status}\n""")

carro2 = Carro(marca="Renault",modelo="Sandero Authentique",cor="Prata",status=True)
print(f"""Marca:{carro2.marca}
Modelo: {carro2.modelo}
Cor: {carro2.cor}
Status: {carro2.status}""")

carro1.acelerarCarro()
carro1.ligarCarro()

print(f"""
      Marca: {carro1.marca}
      Modelo: {carro1.modelo}
      Cor: {carro1.cor}
      Status: {carro1.status}
      Velocidade: {carro1.velocidade}Km/h\n""")

carro1.acelerarCarro()

print(f"""
      Marca: {carro1.marca}
      Modelo: {carro1.modelo}
      Cor: {carro1.cor}
      Status: {carro1.status}
      Velocidade: {carro1.velocidade}Km/h\n""")


carro1.desligarCarro()

print(f"""    Marca: {carro1.marca}
    Modelo: {carro1.modelo}
    Cor: {carro1.cor}
    Status: {carro1.status}\n""")


#------------------------------ Nova forma de declarar classes ------------------------------#
@dataclass
class Alunos:
    matricula: int
    nome: str
    curso: str
    nota: float
    qtd_faltas: int=0

    def alterarNota(self,nova_nota:float):
        self.nota = nova_nota

alunos = Aluno(matricula=1,nome="Daniel",nota=100.0,curso="Python")
print(alunos.nome)