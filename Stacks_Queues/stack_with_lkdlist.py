#implementing stack with linked list.

class Node():
    def __init__(self, data):
        self.data = data #armazena o item
        self.prox = None #inicialmente a lista está vazia, sem proxímo.

class Stack():
    def __init__(self): #lista define o topo e o chão vazios
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, data):
        novo_no = Node(data)
        if self.top == None:# se a lista estiver vazia, ele adiciona o top e bottom como o mesmo
            self.top = novo_no
            self.bottom = novo_no
        else:
            novo_no.prox = self.top
            self.top = novo_no
        self.length += 1

    def pop(self):
        if self.top == None:
            print('lista vazia')
        else:
            self.top = self.top.prox
            self.length -= 1
            if(self.length == 0):
                self.bottom = None

    def print(self):
        if self.top == None:
            print('lista vazia')
        else:
            ponteiro_atual = self.top
            while (ponteiro_atual != None):
                print(ponteiro_atual.data)
                ponteiro_atual = ponteiro_atual.prox


stack = Stack()
stack.push('Hiago')
stack.push('Exercicio feito pelo')
stack.print()
