#Uma linked list é uma estrutura onde um item aponta para o seu próximo. Cada item é chamado de nó

class Nozes():# classe que define os nós
    def __init__(self, data):
        self.data = data #este comando atribui o valor passado como argumento ao atributo 'data' do nó
        self.prox = None #indica que o próximo nó é nulo, assim começo minha lista.

class LikendList():
    def __init__(self):
        self.head = None #diz que o head (primeiro nó)da lista está vazio
        self.tail = self.head #bem como o tail(último nó) da lista também
        self.length = 0 #a lista está inicialmente vazia

    def adicionar_final(self, data):#método para add nós. Esse seria um append
        novo_no = Nozes(data)#chama a classe primeiro_no para armazenar o valor passado e esse valor fica armazenado na variavel novo_no
        if self.head == None:#se a lista nao tem nós... 
            self.head = novo_no #esse será o primeiro nó da lista
            self.tail = self.head #também será o último nó
            self.length += 1 #o comprimento da lista passa a ser 1
        else:# caso contrário...
            self.tail.prox = novo_no #o nó atual tem seu tail atualizado
            self.tail = novo_no #o tail se tornará esse
            self.length += 1 # o comprimento da lista é atualizado

    def adicionar_inicio(self, data):#esse seria um prepend. adiona no início da lista
        novo_no = Nozes(data)
        if self.head == None:
            self.head = novo_no
            self.tail = self.head
            self.length += 1
        else:
            novo_no.prox = self.head
            self.head = novo_no
            self.length += 1

    def print_lista(self):# função para printar a lista atual.
        if self.head == None:#verificar se a lista está vazia
            print('lista vazia')
        else:
            no_atual = self.head
            while no_atual != None:#loop sobre a lista qunado o no_atual for difente de None, o loop vai até quando o no_atual for none.
                print(no_atual.data, end=' ')
                no_atual = no_atual.prox# atualiza para o próximo no da lista.              

        def inserir(self, posicao, data):#para quando queremos adicionar um item em uma posição específica
            if posicao >= self.length:
                if posicao > self.length:
                    print('posição inválida.')
                novo_no = Nozes(data)
                self.tail.prox = novo_no
                self.tail = novo_no
                self.length += 1
            
            elif posicao == 0:
                novo_no = Nozes(data)
                novo_no.prox = self.head
                self.head = novo_no
                self.length += 1
            
            else:
                novo_no = Nozes(data)
                no_atual = self.head
                for i in range(posicao - 1):
                    no_atual = no_atual.prox
                novo_no.prox = no_atual.prox
                no_atual.prox = novo_no
                self.length += 1

        def delete_por_valor(self, data):#método para quando queremos excluir um valor especifico da lista, se ele aparecer mais de uma vez, o valor só será excluido uma vez.
            if self.head == None:
                print('lista vazia')
                return
            
            if no_atual.data == data:
                self.head = self.head.prox
                if self.head == None or self.head.prox == None:
                    self.tail = self.head
                self.length -= 1
                return
            
            while no_atual.prox != None and no_atual.prox.data != data:
                if no_atual.data == data:
                    prox_no = no_atual.prox
                    return
            
            if no_atual.prox != None:
                no_atual.prox == no_atual.prox.prox
                if no_atual.prox == None:
                    self.tail = no_atual
                    self.length -= 1
                    return
                
            else:
                print('valor não encontrado')

        def delete_por_posicao(self, posicao):
            if self.head == None:
                print('lista vazia')
                return
            
            if posicao == 0:
                self.head = self.head.prox
                if self.head == None or self.head.prox == None:
                    self.tail = self.head
                self.length -= 1
                return
            
            if posicao >= self.length:
                posicao = self.length-1
            no_atual = self.head
            for i in range(posicao - 1):
                no_atual = no_atual.prox
            no_atual.prox =no_atual.prox.prox
            self.length -= 1
            if no_atual.prox == None:
                self.tail = no_atual
            return
        

teste = LikendList()
teste.adicionar_final(4)
teste.adicionar_final(5)
teste.adicionar_final(7)
teste.adicionar_inicio(2)

teste.print_lista()