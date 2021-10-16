# Dado 4 linhas, onde as duas primeiras são os nomes e telefones de uma agenda.
# E as duas ultimas linhas são os nomes e telefones de uma segunda agenda.
# Monte um dicionario e mostre em tela a primeira agenda, a segunda agenda 
# e a mesclagem (união[Agenda2 + Agenda1]) da segunda agenda com a primeira.

def cria_agenda():
    
    agenda = {}
    
    nomes = input().split(",")
    
    telefones = list(map(int,input().split(",")))
    
    for nome,tel in zip(nomes,telefones):
        
        agenda[nome.strip()] = tel
    
    return agenda

def main():
    
    agenda1 = cria_agenda()
    print("Agenda 1")
    print(agenda1)
    
    agenda2 = cria_agenda()
    print("Agenda 2")
    print(agenda2)
    
    print("Agenda Mesclada")
    agenda2.update(agenda1)
    print(agenda2)
    
if __name__ == "__main__":
    
    main()