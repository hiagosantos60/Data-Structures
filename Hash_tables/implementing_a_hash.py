#no python, uma hash table é um dicionario {} basicamente. É um O(1), ou seja, tem lookups, insetion e deletes muito rápidos.

class HashTable():
    def __init__(self, size):
        self.size = size 
        self.data = [None]*self.size #aqui inicializamos com o array em zero

    def __str__(self): #este método retorna strings com os atributos da instância em formato de dicionário
        return str(self.__dict__)
    
    def _hash(self, key):  #'_hahs'indica que não usamos fora da classe
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i])*i) % self.size  # ord(key[i]) transforma em unicode, que faz com que evite colisões.
        return hash_value

    def get(self, key):
        hash_value = self._hash(key) #o método hash vai calcular o valor hash
        if self.data[hash_value]: #verifica se existe algum item naquela posição da tabela, caso não, a função retorna None
            for i in range(len(self.data[hash_value])):
                if self.data[hash_value][i][0] == key:  #verifica se a posição do par chave-valor é igual a chave fornecida pelo usuário
                    return self.data[hash_value][i][1]
        return None
    
    def set(self, key, value):
        hash_value = self._hash(key) #pega o valor hash da chave
        if not self.data[hash_value]: #verifica se a posição está vazia
            self.data[hash_value] = [[key, value]]
        else:
            self.data[hash_value].append([key, value])
        print(self.data) #imprime para depuração

    def keys(self):
        keys_array = []  # Lista vazia para armazenar as chaves
        for i in range(self.size): #loop sobre a tabela hash
            if self.data[i]:
                if len(self.data[i]) > 1: #verifica se há mais de um item na posição
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0]) #add chave ao keys_array
        return keys_array

    def values(self): #função para retornar todos os valores, mesma lógica da função keys
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])
        return values_array

minha_hash = HashTable(2)

print(minha_hash)
