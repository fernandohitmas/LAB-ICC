# Dados 3 linhas onde a primeira linha temos os nomes do correntistas, na segunda seus respectivos saldos.
# Monte um dicionario vinculando a pessoa com seu saldo atual. Na terceira linha temos alguns nomes de 
# clientes que serão pesquisados pelo gerente, caso o nome seja de um cliente cadastrado mostre 
# seu saldo caso contrário mostre "Nao Cadastrado" na tela.

def cria_correntistas():
    
    correntistas = {}
    
    nomes = input().split(",")
    
    saldos = list(map(int,input().split(",")))
    
    for nome,saldo in zip(nomes,saldos):
        
        correntistas[nome.strip()] = saldo
    
    return correntistas


def verifica_cadastro(correntistas, pesquisados):

    for pesquisado in pesquisados:
        
        if pesquisado in correntistas.keys():
            
            print(correntistas[pesquisado])
            
        else:
            
            print("Nao Cadastrado")


def main():
        
    correntistas = cria_correntistas()

    nomes_pesquisados = input().split(",")
    
    verifica_cadastro(correntistas,nomes_pesquisados)

    
if __name__ == "__main__":
    
    main()