#exercicio do curso ZTM sobre estrutura de dados 

#Uma linked list é uma estrutura onde um item aponta para o seu próximo. Cada item é chamado de nó

class Nozes(): #classe que define os nós
    def __init__(self, data):
        self.data = data #este comando atribui o valor passado como argumento ao atributo 'data' do nó
        self.prox = None #indica que o próximo nó é nulo, assim começo minha lista.

class LikendList():
    def __init__(self):
        self.head = None #diz que o head (primeiro nó) da lista está vazio
        self.tail = self.head  # bem como o tail (último nó) da lista também
        self.length = 0 #a lista está inicialmente vazia

    def adicionar_final(self, data): #método para add nós. Esse seria um append
        novo_no = Nozes(data) #chama a classe primeiro_no para armazenar o valor passado e esse valor fica armazenado na variavel novo_no
        if self.head is None: #se a lista não tem nós...
            self.head = novo_no #esse será o primeiro nó da lista
            self.tail = self.head #também será o último nó
            self.length += 1 #o comprimento da lista passa a ser 1
        else: #caso contrário...
            self.tail.prox = novo_no #o nó atual tem seu tail atualizado
            self.tail = novo_no #o tail se tornará esse
            self.length += 1 #o comprimento da lista é atualizado

    def adicionar_inicio(self, data): #esse seria um prepend. adiciona no início da lista
        novo_no = Nozes(data) #aqui cria um novo nó
        if self.head is None: #verifica se o head está vazio
            self.head = novo_no #caso esteja, o head passa a ser o novo_no
            self.tail = self.head #se a lista estiver vazia, o head e o tail são o mesmo
            self.length += 1 #aumenta o tamanho da lista
        else: #se não estiver vazia
            novo_no.prox = self.head #faz com que o novo_no aponte para o próximo
            self.head = novo_no #novo_no vira o head
            self.length += 1


    def inserir(self, posicao, data): #para quando queremos adicionar um item em uma posição específica
        if posicao >= self.length: #verifica se a posição passada é >= ao atual comprimento 
            if posicao > self.length: #caso for, a posição é inválida
                print('posição inválida.')
                return
            novo_no = Nozes(data) #o novo_no é criado com o valor fornecido
            self.tail.prox = novo_no #o tail é atualizado para apontar para esse novo_no
            self.tail = novo_no #e por fim o tail é atualizado
            self.length += 1

        elif posicao == 0: #caso a posição for 0
            novo_no = Nozes(data) #novo_no é criado
            novo_no.prox = self.head #ele atualiza o head atual
            self.head = novo_no #por fim novo_no vira o head da lista
            self.length += 1

        else:
            novo_no = Nozes(data) #novo_no é criado na classe Nozes
            no_atual = self.head #no_atual se torna o head
            for i in range(posicao - 1):#esse loop levará no_atual até o que vamos inserir
                no_atual = no_atual.prox #no_atual se trasformara no proximo nó
            novo_no.prox = no_atual.prox #o novo nó se trasformara no no_atual
            no_atual.prox = novo_no #no_atual agora aponta para o novo_no
            self.length += 1

    def delete_por_valor(self, data): #método para quando queremos excluir um valor especifico da lista, se ele aparecer mais de uma vez, o valor só será excluído uma vez.
        if self.head == None: # se o nao tiver head, nao tem lista
            print('lista vazia')
            return

        no_atual = self.head #inicia com o no_atual sendo o head
        if no_atual.data == data: #verifica se o no_atual é igual ao valor que será excluido
            self.head = self.head.prox #caso seja, faz com que aponte para o próximo nó
            if self.head == None or self.head.prox == None: #verifica se a lista ficou vazia ou se tem so um nó
                self.tail = self.head #caso sim, o tail vira head ao mesmo tempo
            self.length -= 1
            return

        while no_atual.prox != None and no_atual.prox.data != data: #loop que funicona enquanto o proximo nó não seja none e não for igual ao valor a ser excluído
            no_atual = no_atual.prox #dentro do loop, o no_atual é atualiazado 

        if no_atual.prox != None: #verifica se o proximo nó é difente de none
            no_atual.prox = no_atual.prox.prox #ajusta o ponteiro da lista, pulando aquele que será excluido
            if no_atual.prox == None: 
                self.tail = no_atual #se o nó que foi excluido era o ultimo da listam essa variavel atualiza a lista
            self.length -= 1
        else:
            print('valor não encontrado')

    def delete_por_posicao(self, posicao):
        if self.head == None:
            print('lista vazia') #caso a lista seja vazia
            return

        if posicao == 0: #caso seja a primeira posição
            self.head = self.head.prox #caso sim, atualiza o head para a proxima posição 
            if self.head == None or self.head.prox == None: #basicamente varifica se a lista ficou vazia ou se restou apenas um nó
                self.tail = self.head #tail e head viram iguais
            self.length -= 1
            return

        if posicao >= self.length:
            posicao = self.length - 1 #caso a posição indicada seja maior que o comprimento, a posicao é atualizada para que esteja dentro do range da lista
        no_atual = self.head # dá o no_atual como se fosse o head
        for i in range(posicao - 1): #percorre toda a lista do 'tail' (que é head para a função) até o 'head' (para a função é o tail)
            no_atual = no_atual.prox # faz o ponteiro ir para o próximo
        no_atual.prox = no_atual.prox.prox #faz o ponteiro ir para o item que será excluído
        self.length -= 1
        if no_atual.prox == None: #verifica se oq foi excluido era o ultimo.
            self.tail = no_atual #caso sim, ele é atualizado.

    def print_lista(self): #função para printar a lista atual.
        if self.head is None: #verificar se a lista está vazia
            print('lista vazia')
        else:
            no_atual = self.head
            while no_atual is not None: #loop sobre a lista quando o no_atual for diferente de None, o loop vai até quando o no_atual for none.
                print(no_atual.data, end=' ')
                no_atual = no_atual.prox #atualiza para o próximo no da lista.
        print()

teste = LikendList()

teste.adicionar_final(3)
teste.adicionar_final(6)
teste.adicionar_inicio(9)

teste.print_lista()