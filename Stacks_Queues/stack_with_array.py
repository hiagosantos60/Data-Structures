#Implementing a stack with an array
#Stack seria uma pilha, imagine uma pilha de pratos onde você só pode colocar e tirar prato pelo topo.

class Stack():
    def __init__(self):
        self.array = [] #aqui eu inicio minha stack vazia

    def peek(self): #esse método me permite verificar qual o elemento no topo da minha pilha
        return self.array[len(self.array)-1] #se referindo ao atributo que está armazenando os itens, pega seu comprimento e diminui em 1, pois é ali onde está o topo da lista verdadeiramente.
    
    def pop(self): #esse metódo remove o último elemento da lista
        if len(self.array) != 0:#verifica se a stack está vazia, se não estiver usa o método pop do python para remover.
            self.array.pop()
            return
        else:
            print('pilha vazia')

    def push(self, data): #esse método serve para adicionar itens na pilha, usa o método append do python para isso.
        self.data.append(data)
        return
    
    def print(self): #esse for loop é para percorrer a pilha do final para o início
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])
        return
    #len(self.array)-1 -> para começar o loop logo em baixo do último da fila
    #-1 -> para garantir que vá até o antepenultimo
    #-1 -> define o tamanho do passo, ou seja, ele diz para ir de um em um no loop.
    