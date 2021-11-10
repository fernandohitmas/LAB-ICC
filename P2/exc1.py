def add_registros(n_registros, registros):
    
    # loop para os n registros que serão adicionados
    for i in range(n_registros):
        
        nome = input()
        altura = float(input())
        peso = float(input())
        ident = int(input())
        sexo = input()
        
        registros[ident] = {'nome':nome, 
                            'altura': altura,
                            'peso': peso,
                            'sexo':sexo}
        
    return registros
    

def imc(peso,altura):
#Cálculo do IMC
    return peso/altura**2


def main():

    registros = {}
    
    n_registros = int(input())
    
    registros = add_registros(n_registros,registros)
    
    id_consulta = int(input())
        
    while id_consulta != -1:
    
        ind_massa_corp = imc(registros[id_consulta]['peso'], registros[id_consulta]['altura'])    
        
        print(f' {registros[id_consulta]["sexo"]}\t{registros[id_consulta]["nome"]}\t{ind_massa_corp:.2f}')
        
        id_consulta = int(input())
        
if __name__ == "__main__":
    
    main()