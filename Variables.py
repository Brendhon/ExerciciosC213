from numpy import arange

class Variables:

    # Setar valores dos coeficientes da planta de nível
    COEFICIENTE_A1 = 0.99736
    COEFICIENTE_B1 = 0.0019800

    PV = 0
    SP = 1

    ERRO = 0
    TEMPO_AMOSTRAGEM = 0.1
    TEMPO = arange(0,300,TEMPO_AMOSTRAGEM)
        
    # Setar valores dos ganhos
    G_PROPORCIONAL = 4
    G_INTEGRADOR = 0.1
    