# Carregando pacotes
from matplotlib import pyplot
from Variables import Variables

class Malha:

    def __init__(self):

        self.a1 = Variables.COEFICIENTE_A1
        self.b1 = Variables.COEFICIENTE_B1

        self.PV = Variables.PV
        self.SP = Variables.SP
        self.tempo = Variables.TEMPO

        self.resposta = []
        self.legenda = ''
    
    def plot(self):

        pyplot.plot(self.resposta, label=f'{self.legenda}')
        pyplot.legend()
        pyplot.grid(True)
        


class Aberta(Malha):

    def __init__(self):
        super().__init__()
        self.legenda = 'Malha Aberta'
    
    def execute(self):

        # Malha aberta
        for i in self.tempo:

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*self.SP


class Fechada(Malha):

    def __init__(self):
        super().__init__()
        self.legenda = 'Malha Fechada'
        self.erro = Variables.ERRO
    
    def execute(self):

        # Malha aberta
        for i in self.tempo:

            # Calculo do erro
            self.erro = self.SP - self.PV

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*self.erro

class FechadaComGanho(Malha):

    def __init__(self):
        super().__init__()
        self.legenda = 'Malha Fechada com ganho proporcional'
        self.erro = Variables.ERRO
        self.kp = Variables.G_PROPORCIONAL
    
    def execute(self):

        # Malha aberta
        for i in self.tempo:

            # Calculo do erro
            self.erro = self.kp*(self.SP - self.PV)

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*self.erro

class FechadaComGanhoIntegral(Malha):

    def __init__(self):
        super().__init__()
        self.legenda = 'Malha Fechada com ganho Integral e proporcional'
        self.erro = Variables.ERRO
        self.kp = Variables.G_PROPORCIONAL
        self.ki = Variables.G_INTEGRADOR
        self.ts = Variables.TEMPO_AMOSTRAGEM
    
    def execute(self):

        # Variaveis auxiliares
        proporcional = 0
        integrador = 0
        controlador = 0

        # Malha aberta
        for i in self.tempo:

            # Calculo do erro
            self.erro = self.SP - self.PV

            # Ação Proporcional 
            proporcional = self.kp*self.erro   

            # Ação Integrador 
            integrador = integrador + self.ki*self.ts*self.erro

            # Ação controlador 
            controlador = integrador +  proporcional

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*controlador

def showAll():
    pyplot.title("C213")
    pyplot.show()