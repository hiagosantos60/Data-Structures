#exercicio do curso ZTM sobre estrutura de dados 

linha = 'eu sou o hiago'

def reverse(linha):
   
    palavras = linha.split()[::-1]

    reverse_palavras = [letra[::-1] for letra in palavras]

    reverse_linha = ' '.join(reverse_palavras)

    return reverse_linha

linha_reverse = reverse(linha)

print(linha_reverse)
