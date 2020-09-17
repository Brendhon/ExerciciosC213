import scipy.io as sio

def load():

    # # Teste
    # x = sio.loadmat('Modelar/Variables/relatorio3_variaveis_exemplo.mat')
    # return x['u'], x['y']

    # carregando o arquivo matlab
    x = sio.loadmat('Modelar/Variables/variaveis_planta_de_nivel.mat')
    return x['potencia'], x['nivel']