# -*- coding: utf-8 -*-
"""Listas e Tuplas - Subsequencias

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O7r7oYDyici857ZmczeS-Ab-_Fj4XS8y
"""

# Uma sequência pode ser interpretada como uma lista finita de termos. Faça um programa que leia um numero N;
# em seguida, na linha debaixo, leia todos os elementos de uma sequência de inteiros, armazene-os numa lista
# e verifique se existe uma subsequência tal que a soma dos termos é N, imprimindo "SIM" em caso positivo e "NAO" em caso negativo.

# Obs: uma subsequência é formada pegando uma parte da sequência original, sem pular nenhum termo; 
# por exemplo, se (2,3,4,11,6,7,8) é a nossa sequência, (4,11,6) e (2) são subsequências dela, enquanto que (3,11,6,7) não é.

# Entrada: Um inteiro N

# Saída: A string SIM, caso haja uma subsequência cuja soma dos termos seja N; caso contrário, imprima a string NAO.

def soma_subsequencia(subseq):

  soma = 0

  for n in subseq:
    soma += n

  return soma

def verifica_soma(N, seq):

  for i in range(1,len(seq)):

    inicio = 0
    fim = i+1
    
    while fim <=len(seq):

      soma_sub = soma_subsequencia(seq[inicio:fim])

      inicio += 1
      fim += 1

      if soma_sub == N:

        return True
  
  return False

def main():

  num = int(input())

  sequencia = list(map(int,input().split()))

  existe_soma = verifica_soma(num, sequencia)

  if existe_soma:
    print('SIM')

  else:
    print('NAO')

if __name__ == "__main__":
  main()