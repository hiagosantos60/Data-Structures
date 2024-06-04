#exercicio do curso ZTM sobre estrutura de dados 

#Google Question
#Given an array, return the first recurring character
#Example1 : array = [2,1,4,2,6,5,1,4]
#It should return 2

array = [2,1,4,2,6,5,1,4]

def rcr(array):
    dicionario = {}
    for item in array:
        if item in dicionario:
            return item
        else:
            dicionario[item] = True
    return None

print(rcr(array)) 
