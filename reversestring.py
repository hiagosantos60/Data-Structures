#essa função vai reverter uma string. Por exemplo: revertido -> oditrever

def reverse(string):#função criada para reverter a string
    reverse_string = '' #cria uma variável para armazenar a string
    for i in range(len(string)): #esse loop vai percorrer todas as letras da string
        reverse_string = reverse_string + string[len(string) - i - 1] #a variável começa vazia no looping e concatena com uma outra string. i é onde está o looping e -1 vai diminuindo o tamanho da string.
    return reverse_string #retorna a string reversa 

print(reverse('blablabla'))