""" 
Questão 1
 Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
 próximo valor sempre será a soma dos 2 valores anteriores 
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa 
 na linguagem que desejar onde, informado um número, ele calcule a 
 sequência de Fibonacci e retorne uma mensagem avisando se o número 
 informado pertence ou não a sequência.
"""
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def pertence(m):
    if(m < 0): return 'não pertence'

    i = 0
    while(1):
        aux = fibonacci(i)
        if aux == m:
            return 'pertence'
        elif aux > m:
            return 'não pertence'
        i += 1

m = int(input("Informe o número: "))
print("Resposta questão 2:")
print(pertence(m))

"""
Questão 2
Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula 
ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência 
ou pode ser previamente definida no código;
"""
def contaAs(palavra):
    contagem = 0
    palavra = palavra.lower()
    for l in palavra:
        if l == 'a':
            contagem += 1
    return contagem

palavra = input("Informa a palavra: ")
print(f'Número de a em {palavra}: {contaAs(palavra)}')

""" 
Questão 3
 Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
"""
indice = 12
soma = 0
k = 1
while(k < indice):
    k += 1
    soma += k
    
print("Resposta questão 1:")
print(soma)

"""
Questão 4
Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
    Ímpares: 1, 3, 5, 7, 9
b) 2, 4, 8, 16, 32, 64, ____
    Duplicando: 2, 4, 8, 16, 32, 64, 128
c) 0, 1, 4, 9, 16, 25, 36, ____
    Somando ímpares: 49
d) 4, 16, 36, 64, ____
    Multiplica ímpar por quatro e soma: 4, 16, 36, 64, 100
e) 1, 1, 2, 3, 5, 8, ____
    Fibonnacci: 1, 1, 2, 3, 5, 8, 13
f) 2, 10, 12, 16, 17, 18, 19, ____
    Soma 12 a posição: 2, 10, 12, 16, 17, 18, 19, 20
"""

"""
Questão 5
Suponha três interruptores: [a, b, c] e três lâmpadas incandescentes [x, y, z].
    Ligue o interruptor a e após alguns minutos, desligue-o e ligue o interruptor b
    Visita sala da lâmpada x:
        Se lâmpada apagada e fria: (c, x)
                Visita sala da lâmpada y:
                    Se lâmpada apagada: (a, y) e (b, z)
                    De modo contrário: (b, y) e (a, z)
        Se lâmpada apagada e quente: (a, x)
            Visita sala da lâmpada y:
                Se lâmpada apagada: (c, y) e (b, z)
                De modo contrário: (b, y) e (a, z)
        Se lâmpada acesa: (b, x)
            Visita sala da lâmpada y:
                Se lâmpada apagada e fria: (c, y) e (a, z)
                De modo contrário: (a, y) e (c, z)
Cada tupla (i, l) significa a associação entre um interruptor "i" a uma lâmpada "l".
                
"""