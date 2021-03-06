# -*- coding: utf-8 -*-
"""Listas e Tuplas - Anagramas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dCC8FVFUQTGZiHbs34AXaEyJAIgyg5mu
"""

# Dadas N strings, determinar quantos anagramas existem para cada uma.

# Entrada: Um inteiro positivo N; em seguida, N linhas, cada uma contendo uma string de carácteres alfabéticos minúsculos, seguidas de uma quebra de linha (‘\n’)

# Saída: N linhas, cada uma contendo um inteiro que representa a quantidade de anagramas; a i-ésima linha impressa é a resposta para a i-ésima string inserida, com i de 1 até n.

def conta_letras(palavra):

  conta_letras = {}

  for letra in tuple(palavra):

    if letra in conta_letras.keys():

      conta_letras[letra] += 1

    else:

      conta_letras[letra] = 1

  return conta_letras

def conta_anagramas(palavra):

  ntotal_letras = len(palavra)

  ncada_letra = conta_letras(palavra)

  n_anagramas = 1

  for i in range(1, ntotal_letras +1):
    n_anagramas = n_anagramas*i

  for n in ncada_letra.values():
    
    for i in range(1,n+1):
      
      n_anagramas = n_anagramas/i
  
  return n_anagramas



def main():

  n_palavras = int(input())

  palavras = []

  for i in range(n_palavras):

    palavras.append(input().strip())

  for palavra in palavras:

    n_anagramas = conta_anagramas(palavra)

    print(int(n_anagramas))
    

if __name__ == "__main__":
  main()