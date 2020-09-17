# Carregando pacotes
from matplotlib import pyplot
import constants as const

class Malha:

    def __init__(self, legend):

        self.a1 = const.COEFICIENTE_A1
        self.b1 = const.COEFICIENTE_B1

        self.PV = const.PV
        self.SP = const.SP
        self.tempo = const.TEMPO

        self.resposta = []
        self.legenda = legend
    
    def plot(self):

        pyplot.plot(self.resposta, label=f'{self.legenda}')
        pyplot.legend()
        pyplot.grid(True)
        

class Aberta(Malha):

    def __init__(self):
        super().__init__('Malha Aberta')
    
    def execute(self):

        # Malha aberta
        for i in self.tempo:

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*self.SP


class Fechada(Malha):

    def __init__(self):
        super().__init__('Malha Fechada')
        self.erro = const.ERRO
    
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
        super().__init__('Malha Fechada com ganho proporcional')
        self.erro = const.ERRO
        self.kp = const.G_PROPORCIONAL
    
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
        super().__init__('Malha Fechada com ganho proporcional e integral')
        self.erro = const.ERRO
        self.kp = const.G_PROPORCIONAL
        self.ki = const.G_INTEGRADOR
        self.ts = const.TEMPO_AMOSTRAGEM
    
    def execute(self):

        # Variáveis auxiliares
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


class FechadaComGanhoIntegralDerivativo(Malha):

    def __init__(self):
        super().__init__('Malha Fechada com ganho proporcional, integral e derivativo')
        self.erro = const.ERRO
        self.kp = const.G_PROPORCIONAL
        self.ki = const.G_INTEGRADOR
        self.kd = const.G_DERIVADOR
        self.ts = const.TEMPO_AMOSTRAGEM
    
    def execute(self):

        # Variaveis auxiliares
        proporcional = 0
        integrador = 0
        controlador = 0
        derivador = 0

        # Calculo do erro anterior
        erroAnterior = self.SP - self.PV

        # Malha aberta
        for i in self.tempo:

            # Calculo do erro
            self.erro = self.SP - self.PV

            # Ação Proporcional 
            proporcional = self.kp*self.erro   

            # Ação Integrador 
            integrador = integrador + self.ki*self.ts*self.erro
            
            # Ação Derivador 
            derivador = ((self.erro - erroAnterior)/self.ts)*self.kd

            # Ação controlador 
            controlador = integrador + proporcional + derivador
            
            # Atualizando erro
            erroAnterior = self.erro

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*controlador


def show():
    pyplot.show()

def save(fileName):
    pyplot.savefig(f'{fileName}.png')