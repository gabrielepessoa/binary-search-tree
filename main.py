from binary_search_tree import *

def main():
    root = BSTNode(8)
    root.left = BSTNode(6)
    root.left.left = BSTNode(5)
    root.left.right = BSTNode(7)
    root.right = BSTNode(10)
    root.right.right = BSTNode(11)
    root.right.left = BSTNode(9)

    choice = None
    while choice != '0':
        choice = input ("Digite 1 para buscar, 2 para adicionar, 3 para remover um elemento ou 0 para sair: ")
        if choice == '1':
            print('BUSCAR ELEMENTO')
            key = input("Digite o elemento que deseja buscar: ")
            key = int(key)
            print('Procurando key ', key, '...')
            found = root.get(key, 0, 0)
            if found:
                print('Número encontrado: ', found.key, '\n\n')
            else:
                print('Não encontrado.')

        elif choice == '2':
            print('ADICIONAR ELEMENTO')
            key = input("Digite o elemento que deseja adicionar: ")
            key = int(key)
            x = BSTNode(key)
            root.add(x)
            found = root.get(key, 0, 0)
            if found:
                print ('Node adicionado. \n\n')

        elif choice == '3':
            print('REMOVER ELEMENTO')
            key = input("Digite o elemento que deseja remover: ")
            key = int(key)
            root.remove(key)
            print('Node removido. \n\n')

        else:
            print("Escolha uma das opções.")

main()
