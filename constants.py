from numpy import arange
from Modelar.leastSquares import calculate

# # Valores dos coeficientes da planta de nível
# COEFICIENTE_A1 = 0.99736
# COEFICIENTE_B1 = 0.0019800

# # Valores dos coeficientes de teste
# COEFICIENTE_A1 = 0.904837
# COEFICIENTE_B1 = 0.095163

# Valores dos coeficientes baseados nos vetores entrada e saida
COEFICIENTE_A1, COEFICIENTE_B1 = calculate()

print(f'COEFICIENTE_A1 = {COEFICIENTE_A1}')
print(f'COEFICIENTE_B1 = {COEFICIENTE_B1}')

# Entrada e saída
SP = 1
PV = 0

ERRO = 0
TEMPO_AMOSTRAGEM = 0.1
TEMPO = arange(0,200,TEMPO_AMOSTRAGEM)
    
# Valores dos ganhos
G_PROPORCIONAL = 4
G_INTEGRADOR = 0.1
G_DERIVADOR = 5
    