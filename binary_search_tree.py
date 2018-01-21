class BSTNode(object):
    #left e right são referências a outros nós
    #key guarda a chave utilizada p identificar o nó
    #value representa o valor a ser guardado
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    #Busca de Elemento da árvore
    def get(self, key, i, j):
        if key < self.key:
            i = i+1
            print('Procurando pela esquerda ', i)
            return self.left.get(key, i, j) if self.left else None
        elif key > self.key:
            j = j+1
            print('Procurando pela direita ', j)
            return self.right.get(key, i, j) if self.right else None
        else:
            return self

    #Adicionar um elemento na árvore
    def add(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)
        print("Node adicionado: ", node)

    #Remover um elemento da árvore
    def remove(self, key):
        #Percorre a árvore até achar a key desejada
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            #o elemento foi encontrado, da-se início ao processo de remoção
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            #tmp recebe o valor mínimo da subárvore a direita
            tmp = self.right._min()
            #quando o _min() achar e retornar o mínimo
            #key e value agora adquirem os valores de tmp
            self.key, self.value = tmp.key, tmp.value
            #agora é removido o mínimo da subárvore da direita
            self.right._remove_min()
        return self

    #retorna o menor elemento da subárvore da direita
    def _min(self):
        if self.left is None:
            return self
        else:
            return self.left._min()

    #remove o menor elemento da subárvore que tem self como raiz
    def _remove_min(self):
        #se encontrou o mínimo
        if self.left is None:
            return self.right
        self.left = self.left._remove_min
        return self
