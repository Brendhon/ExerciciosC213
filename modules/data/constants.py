from modules.data.fileRead import readJson
from numpy import arange
from modules.modelar.leastSquares import calculate

# Lendo arquivo JSON
var = readJson()

# Constantes escolhidas
SP = var['SP']
PV = var['PV']
KP = var['KP']
KI = var['KI']
KD = var['KD']
TEMPO_INICIAL = var['TEMPO_INICIAL']
TEMPO_FINAL = var['TEMPO_FINAL']
TEMPO_AMOSTRAGEM = var['TEMPO_AMOSTRAGEM']

# Calculando intervalo de tempo
TEMPO = arange(TEMPO_INICIAL,TEMPO_FINAL,TEMPO_AMOSTRAGEM)

# Calculando coeficientes
COEFICIENTE_A1, COEFICIENTE_B1 = calculate()

print(f'COEFICIENTE_A1 = {COEFICIENTE_A1}')
print(f'COEFICIENTE_B1 = {COEFICIENTE_B1}')

# # Valores dos coeficientes da planta de nível
# COEFICIENTE_A1 = 0.99736
# COEFICIENTE_B1 = 0.0019800

# # Valores dos coeficientes de teste
# COEFICIENTE_A1 = 0.904837
# COEFICIENTE_B1 = 0.095163

