# Primeiro vou iniciar minha estrutura de árvore vazia
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Aqui iniciamos o construtor da estrutura com o init sendo o nó que dará início à minha árvore
class searchtree():
    def __init__(self):  
        self.root = None
        self.numero_de_nos = 0

    def insert(self, data):
        novo_no = Node(data)
        if self.root == None:
            self.root = novo_no
            self.numero_de_nos += 1
            return
        else:
            no_atual = self.root
            while True:
                if data < no_atual.data:
                    if no_atual.left == None:
                        no_atual.left = novo_no
                        break
                    else:
                        no_atual = no_atual.left
                elif data > no_atual.data:
                    if no_atual.right == None:
                        no_atual.right = novo_no
                        break
                    else:
                        no_atual = no_atual.right
            self.numero_de_nos += 1
            return

    def remove(self, data):
        if self.root == None: 
            return "árvore vazia"
        no_atual = self.root
        no_acima = None
        while no_atual != None: 
            if no_atual.data > data:
                no_acima = no_atual
                no_atual = no_atual.left
            elif no_atual.data < data:
                no_acima = no_atual
                no_atual = no_atual.right
            else:
                if no_atual.right == None:
                    if no_acima == None:
                        self.root = no_atual.left
                        return
                    else:
                        if no_acima.data > no_atual.data:
                            no_acima.left = no_atual.left
                            return
                        else:
                            no_acima.right = no_atual.left
                            return
                elif no_atual.left == None:
                    if no_acima == None:  
                        self.root = no_atual.right
                        return
                    else:
                        if no_acima.data > no_atual.data:
                            no_acima.left = no_atual.right
                            return
                        else:
                            no_acima.right = no_atual.right
                            return
                elif no_atual.left == None and no_atual.right == None:
                    if no_acima == None:
                        self.root = None
                        return
                    if no_acima.data > no_atual.data:
                        no_acima.left = None
                        return
                    else:
                        no_acima.right = None
                        return
                else:
                    del_no = no_atual.right
                    del_no_acima = no_atual.right
                    while del_no.left != None:
                        del_no_acima = del_no
                        del_no = del_no.left
                    no_atual.data = del_no.data
                    if del_no == del_no_acima:
                        no_atual.right = del_no.right
                        return
                    if del_no.right == None:
                        del_no_acima.left = None
                        return
                    else:
                        del_no_acima.left = del_no.right
                        return
        return "não encontrado"

    def search(self, data):
        if self.root == None:
            return "árvore vazia"
        else:
            no_atual = self.root
            while True:
                if no_atual == None:
                    return "não encontrado"
                if no_atual.data == data:
                    return "encontrado"
                elif no_atual.data > data:
                    no_atual = no_atual.left
                elif no_atual.data < data:
                    no_atual = no_atual.right

teste = searchtree()

teste.insert(5)
teste.insert(65)
teste.insert(53)
teste.insert(25)
teste.insert(3)
teste.insert(7)