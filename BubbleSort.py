import random #Importa uma lista de números aleatória  

def criar_lista_random(): 
    lista_random = [random.randint(1, 1000) for _ in range(100)]
    return lista_random

def bubble_sort(lista) #Comandos para criar o algoritmo Bubble Sort
    n = len(lista)
    for i in range(n):
      trocou = False 
      for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
          lista[j], lista[j+1] = lista[j+1], lista[j]
          trocou = True 
      if not trocou: 
        break 

lista_random = criar_lista_random()

print ("Lista desordenada:" + lista_random)

bubble_sort(lista_random) #Processo de ordenação da listagem aleatória utilizando o Bubble Sort

print ("Lista ordenada com o Bubble Sort:" + lista_random)




