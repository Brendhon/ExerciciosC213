import scipy.io as sio

def load():

    # # Teste
    # x = sio.loadmat('modules/modelar/variables/relatorio3_variaveis_exemplo.mat')
    # return x['u'], x['y']

    # Carregando o arquivo matlab
    x = sio.loadmat('modules/modelar/variables/variaveis_planta_de_nivel.mat')
    return x['potencia'], x['nivel']