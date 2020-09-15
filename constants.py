from numpy import arange

# # Valores dos coeficientes da planta de nível
# COEFICIENTE_A1 = 0.99736
# COEFICIENTE_B1 = 0.0019800

# Valores dos coeficientes de teste
COEFICIENTE_A1 = 0.904837
COEFICIENTE_B1 = 0.095163

# Entrada e saída
SP = 1
PV = 0

ERRO = 0
TEMPO_AMOSTRAGEM = 0.1
TEMPO = arange(0,6,TEMPO_AMOSTRAGEM)
    
# Valores dos ganhos
G_PROPORCIONAL = 5
G_INTEGRADOR = 5
G_DERIVADOR = 0.25
    