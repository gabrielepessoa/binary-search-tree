from binary_search_tree import *

def main():
    tree = BSTNode(8)
    tree.left = BSTNode(6)
    tree.left.left = BSTNode(5)
    tree.left.right = BSTNode(7)
    tree.right = BSTNode(10)
    tree.right.right = BSTNode(11)
    tree.right.left = BSTNode(9)

    print("TESTANDO BUSCAR ELEMENTO")
    key = 5
    print('Procurando key ', key, '...')
    found = tree.get(key, 0, 0)

    if found:
        print('Número encontrado: ', found.key)

    print("")
    print("")

    print("TESTANDO ADICIONAR ELEMENTO")
    x = 12
    found = tree.add(x)

    if found:
        print ("Número add", x)

    print("")
    print("")

    print("TESTANDO REMOVER ELEMENTO")

main()
