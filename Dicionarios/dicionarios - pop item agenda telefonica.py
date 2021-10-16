# Dado um número de contatos N e N tuplas de linha onde o primeiro termo é o nome
# e o segundo o telefone. Crie um dicionario e mostre seu desempilhamento.

def cria_agenda():
    
    n_contatos = int(input())
    
    agenda = {}
    
    for n in range(n_contatos):
        
        nome,tel = input().split()
        
        agenda[nome] = tel
        
    return agenda

def main():
    
    agenda = cria_agenda()
    
    for n in range(len(agenda)):
        
        print(agenda.popitem())
        
if __name__ == "__main__":
    
    main()