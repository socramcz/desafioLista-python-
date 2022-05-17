lista = []


def empilhar(cadeira):

    # Se a lista estiver vazia, vai criar uma nova pilha
    if len(lista) == 0:

        # E criar uma pilha dentro da lista
        pilha = []
        pilha.append(cadeira)
        lista.append(pilha)

    # Caso contrario vai criar uma nova pilha e verificar se ja existe alguma pilha com o tipo da cadeira
    else:
        adicionar = False

        # O programa verifica a lista
        for i in lista:

            # Se caso existir uma pilha com o modelo da cadeira, ela so vai ser adicionada
            if i[0] == cadeira and len(i) < 10:
                i.append(cadeira)
                adicionar = True
                break

        # Caso não existir uma pilha com este modelo, ele vai criar uma nova pilha
        if not adicionar:
            pilha2 = []
            pilha2.append(cadeira)
            lista.append(pilha2)

    return 'Cadeira adicionada'

# Função para retirar uma cadeira da pilha


def tirar(cadeira):
    for i in lista:
        if i[0] == cadeira:
            i.pop()

            return 'Cadeira removida da pilha'

    return 'Não existe nenhuma cadeira com esse modelo'

# Somente para exibir as pilhas de cadeira dentro da lista


def imprimir():
    for i in lista:
        print(i)


while True:
    print('-=' * 20)
    print('Empilhador de cadeiras')

    print('-=' * 20)
    print('Para empilhar uma cadeira digite "1"\nPara remover uma cadeira digite "2"\nPara ver a lista digite "3"\nPara sair digite "0"')
    decisao = int(input())

    if decisao == 1:
        cadeira = input('Digite o modelo da cadeira: ')

        print(empilhar(cadeira))
        print(' ')

    elif decisao == 2:
        cadeira = input('Digite o modelo da cadeira: ')

        print(tirar(cadeira))
        print(' ')

    elif decisao == 3:
        imprimir()

    elif decisao == 0:
        print('PROGRAMA ENCERRADO')
        break

    else:
        print('OPÇÃO INVALIDA')
