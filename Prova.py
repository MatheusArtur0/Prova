import random #Importando o random

trocaBubble = 0
compBubble = 0

trocaQuick = 0
compQuick = 0

trocaSelection = 0
compSelection = 0


def main(): #Inicio do programa.
    tamanhoLista = 100
    lista = [random.randint(1, tamanhoLista) for _ in range(tamanhoLista)] #Criando uma lista random delimitando seu quantitativo até 100

    listaQuick = lista.copy()
    listaBubble = lista.copy()
    listaSelection = lista.copy()

    print("Listagem original:", listaQuick) #Pegando o a cópia da lista original para mostrar ela antes da ordenação

    quickSort(listaQuick, 0, len(listaQuick) - 1)
    bubbleSort(listaBubble)
    selectionSort(listaSelection)

    print("Listagem organizada:", listaQuick)

    print("Total de trocas (Bubble):", trocaBubble)
    print("Total de comparações (Bubble):", compBubble)

    print("Total de trocas (Selection):", trocaSelection)
    print("Total de comparações (Selection):", compSelection)

    print("Total de trocas (Quick):", trocaQuick)
    print("Total de comparações (Quick):", compQuick)


def bubbleSort(array): #Ordenação do Bubble Sort
    global trocaBubble, compBubble
    len_array = len(array)
    for i in range(len_array):
        totalTrocas = 0
        for j in range(len_array - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                trocaBubble += 1
                totalTrocas += 1
            compBubble += 1
        compBubble += 1
        if totalTrocas == 0:
            return


def selectionSort(array): #Ordenação com o Selection Sort
    global trocaSelection, compSelection
    len_array = len(array)
    for i in range(len_array):
        smallest = i
        for j in range(i, len_array):
            if array[j] < array[smallest]:
                smallest = j
            compSelection += 1
        array[i], array[smallest] = array[smallest], array[i]
        trocaSelection += 1


def quickSort(array, start, end): #Ordenação com o QuickSort
    global trocaQuick, compQuick
    compQuick += 1
    if end <= start:
        return

    pivot = reparticoes(array, start, end)

    quickSort(array, start, pivot - 1)
    quickSort(array, pivot + 1, end)


def reparticoes(array, start, end): #Função criada para auxiliar o QuickSort, visto que o mesmo precisa de um elemento "pivô", para alocar números menores a sua esquerda e maiores a sua direita.
    global trocaQuick, compQuick
    pivot = array[end]

    i = start - 1
    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            trocaQuick += 1
            array[i], array[j] = array[j], array[i]
        compQuick += 1
    i += 1
    trocaQuick += 1
    array[i], array[end] = array[end], array[i]

    return i


if __name__ == "__main__": #Para verificar se o script está sendo rodado como um programa
    main()