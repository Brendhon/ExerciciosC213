import Controlers.meshes as malha

def main():

    # Malha Aberta
    malhaAberta = malha.Aberta() # Instanciando classe
    malhaAberta.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaAberta.plot() # Plot a resposta

    # Malha Fechada 
    malhaFechada = malha.Fechada()  # Instanciando classe
    malhaFechada.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaFechada.plot() # Plot a resposta

    # Malha Fechada com Ganho
    malhaFechadaComGanho = malha.FechadaComGanho()  # Instanciando classe
    malhaFechadaComGanho.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaFechadaComGanho.plot() # Plot a resposta

    # Malha Fechada com Ganho Integral e proporcional
    malhaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Instanciando classe
    malhaComGanhoIntegral.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaComGanhoIntegral.plot() # Plot a resposta
    
    # Malha Fechada com Ganho proporcional, integral e derivativo 
    malhaComGanhoIntegralDerivativo = malha.FechadaComGanhoIntegralDerivativo() # Instanciando classe
    malhaComGanhoIntegralDerivativo.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaComGanhoIntegralDerivativo.plot() # Plot a resposta

    # Salvar figura com todos os Plots
    malha.save("C213")

    # Mostrar figura
    malha.show()

if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main
