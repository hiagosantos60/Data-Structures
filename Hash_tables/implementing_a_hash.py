#no python, uma hash table é um dicionario {} basicamente. É um O(1), ou seja, tem lookups, insetion e deletes muito rápidos.

class HashTable():
    def __init__(self, size):
        size.self = size
        self.data = [None]*self.data #Aqui inicializamos com o array em zero

    def __str__(self):#Este método retorna strings com os atributos da instânica em formato de dicionário
        return str(self.__dict__)
    
    def _hash(self, key):#'_hahs' indica que não usamos fora da class
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size #ord(key[i]) transforma em unicode, que faz com que evite colisões.
            return hash

    def get(self, key):
        hash = self._hash(key)#o metodo hash vai calcular o valor hash
        if self.data[hash]:#verifica se existe algum item naquela posição da tabela, caso não, a função retorna None
            for i in range (len(self.data[hash])):
                if self.data[hash][i][0] == key:#verifica se a posiçao do par chave-valor é igual a chave fornecida pelo usuário
                    return self.data[hash][i][1]
        return None
    
    #estudar daqui pra baixo e revisar o get
    
    def set (self, key, value):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data.[hash].append([key, value])
        print(self.data)

    def keys(self):
        keys_array = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i] > 1):
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][0][0])
                        return keys_array
                
    def values(self):
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i][j][1])):
                    values_array.append(self.data[i][j][1])
        return values_array
    

    