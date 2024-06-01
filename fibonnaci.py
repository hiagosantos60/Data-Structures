#um fibonnaci é uma sequencia que soma os dois ultimos e soma formando o terceiro: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def fibonnaci(num):
    sequencia = [] #define uma lista para armazenar a sequencia   
    a,b = 0,1 #primeiro elemento é 0 o segundo é 1
    for i in range(num): #looping num range que o usuário pediu para a sequencia
        sequencia.append(a)#add a lista o valor calculado
        a, b = b, a+b #calcula o próximo valor
    return sequencia #retorna o calculo

print(fibonnaci(5))#chama a função e o range do tamanho da lista