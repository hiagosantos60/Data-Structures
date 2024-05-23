x = [1, 2, 3, 4, 5, 6]
y = [3, 5, 2, 6, 8, 7]

def mergearr(x,y):
    #confirmando se nenhum array é vazio
    if len(x)==0 or len(y)==0:
        return x+y
    #criando um array novo 
    array = []
    i = 0
    j = 0

    while i < len(x) and j < len(y):
        #se o elemento de x for <= ao de y, no momento, ele será add ao novo array e o índice de x aponta para o próximo
        if x[i] <= y[j]:
            array.append(x[i])
            i += 1
        #mesma lógica do primeiro, mas agora para o y
        else:
            array.append(y[j])
            j += 1
    #retornando o array concatenando com os de x por isso x[i:] e de y[j:]
    return array+x[i:]+y[j:]

k = mergearr(x,y)
print(k)
