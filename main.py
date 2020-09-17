import modules.controlers.meshes as malha

def main():

    # Malha Aberta
    malhaAberta = malha.Aberta() # Instanciando classe
    malhaAberta.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaAberta.plot() # Plot a resposta
    malha.save("Malha Aberta") # Salvando figura

    malha.clearPlot() # Limpando a figura

    # Malha Fechada 
    malhaFechada = malha.Fechada()  # Instanciando classe
    malhaFechada.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaFechada.plot() # Plot a resposta
    malha.save("Malha Fechada") # Salvando figura

    malha.clearPlot() # Limpando a figura

    # Malha Fechada com Ganho
    malhaFechadaComGanho = malha.FechadaComGanho()  # Instanciando classe
    malhaFechadaComGanho.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaFechadaComGanho.plot() # Plot a resposta
    malha.save("Malha Fechada com Ganho") # Salvando figura

    malha.clearPlot() # Limpando a figura

    # Malha Fechada com Ganho proporcional e integral
    malhaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Instanciando classe
    malhaComGanhoIntegral.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaComGanhoIntegral.plot() # Plot a resposta
    malha.save("Malha Fechada com Ganho proporcional e integral") # Salvando figura

    malha.clearPlot() # Limpando a figura
    
    # Malha Fechada com Ganho proporcional, integral e derivativo 
    malhaComGanhoIntegralDerivativo = malha.FechadaComGanhoIntegralDerivativo() # Instanciando classe
    malhaComGanhoIntegralDerivativo.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaComGanhoIntegralDerivativo.plot() # Plot a resposta
    malha.save("Malha Fechada com Ganho proporcional, integral e derivativo ") # Salvando figura

    malha.clearPlot() # Limpando a figura

    malhaAberta.plot() # Plot a resposta
    malhaFechada.plot() # Plot a resposta
    malhaFechadaComGanho.plot() # Plot a resposta
    malhaComGanhoIntegral.plot() # Plot a resposta
    malhaComGanhoIntegralDerivativo.plot() # Plot a resposta

    malha.save("Todas as malhas")

    malha.clearPlot()


if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main
