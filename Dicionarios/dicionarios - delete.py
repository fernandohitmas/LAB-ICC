# Dados 3 linhas onde a primeira contem os nomes, a segunda os números de telefones respectivos.
# Crie uma agenda(dicionário) que relacione o Nome com seu respectivo telefone. Na terceira linha
# temos nomes de contatos que serão excluídos da agenda. Mostre a agenda(dicionário) resultante após as remoções.

def main():
    
    contatos = {}
    
    nomes = input().split(",")
    
    telefones = list(map(int,input().split(",")))
    
    for nome,tel in zip(nomes,telefones):
        
        contatos[nome.strip()] = tel
    
    nomes_excluidos = input().split(",")
    
    for excluido in nomes_excluidos:
        
        contatos.pop(excluido)
        
    print(contatos)
    
if __name__ == "__main__":
    
    main()