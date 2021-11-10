def maior_elemento(lista):
    maior = lista[0]
    
    for n in range(1,len(lista)):
        
        maior = lista[n] if lista[n] > maior else maior
        
    return maior

def menor_elemento(lista):
    menor = lista[0]
    
    for n in range(1,len(lista)):
        
        menor = lista[n] if lista[n] < menor else menor
        
    return menor
    
def intersecao_elementos(lista1,lista2):
    
    intersecao = []
    
    for ele1 in lista1:
        
        if ele1 in lista2:
            
            intersecao.append(ele1)
    
    return intersecao
    
def imprime_lista(lista):
    
    print(*lista)
    
def main():
    
    tamanho_l1 = int(input())
    tamanho_l2 = int(input())
    
    l1 = list(map(int, input().split(' ')))
    l2 = list(map(int, input().split(' ')))
    
    intersecao = intersecao_elementos(l1,l2)
    print("Intersecao:")
    imprime_lista(intersecao)
    
    l1_maior = maior_elemento(l1)
    l2_maior = maior_elemento(l2)
        
    l1_menor = menor_elemento(l1)
    l2_menor = menor_elemento(l2)
    
    print("Menor:")
    print(l1_menor) if l1_menor < l2_menor else print(l2_menor)
    
    print("Maior:")
    print(l1_maior) if l1_maior > l2_maior else print(l2_maior)
    

if __name__ == "__main__":
    main()