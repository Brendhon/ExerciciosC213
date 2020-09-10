from Malhas import Aberta, Fechada, FechadaComGanho, FechadaComGanhoIntegral, showAll

def main():

    # Malha Aberta
    malhaAberta = Aberta() # Instanciando classe
    malhaAberta.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaAberta.plot() # Plot a resposta
    
    # Malha Fechada 
    malhaFechada = Fechada()  # Instanciando classe
    malhaFechada.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaFechada.plot() # Plot a resposta
    
    # Malha Fechada com Ganho
    malhaFechadaComGanho = FechadaComGanho()  # Instanciando classe
    malhaFechadaComGanho.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaFechadaComGanho.plot() # Plot a resposta

    # Malha Fechada com Ganho Integral e proporcional
    malhaComGanhoIntegral = FechadaComGanhoIntegral()  # Instanciando classe
    malhaComGanhoIntegral.execute() # Executando as operações baseadas nas esquações a diferenças
    malhaComGanhoIntegral.plot() # Plot a resposta
    
    # Mostrar figura
    showAll()
    


if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main
