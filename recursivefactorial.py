#uma recursão é chamar a função dentro da própia função
def factorial(num):
    if num == 0:#regra do fatorial
        return 1
    else:
        return num*(factorial(num - 1))#exemplo de recursão
    
print(factorial(0))