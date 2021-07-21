class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster: # Mixing - classe com comportamentos comuns entre classes
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster): # Herança múltipla
    pass

paulo = Junior("Paulo")
paulo.busca_perguntas_sem_resposta()

henrique = Pleno("Henrique")
henrique.busca_perguntas_sem_resposta()
henrique.busca_cursos_do_mes()

henrique.mostrar_tarefas() # Method Resolution Order (MRO)

print(henrique)