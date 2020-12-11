from os import system
system("clear")

"""
Python - Tipos de Variáveis
    As variáveis são espaço na memoria para guardar valores
> Atribuição de valores a variáveis
    A declaração acontece automaticamente quando é atribuido um valor
    a variável.
"""

counter = 100
miles = 1000.0
name = 'Lucas'

print(counter)
print(miles)
print(name)

"""
> Atribuiçaõ múltipla
    Python permite que você atribua um único valor a várias variáveis
    simultaneamente.
"""
a = b = c = 1

"Pode ser atribuido varios objetos a varias variáveis"

a, b, c = 1, 2, "John"

"""
> Tipos de dados padrão
    Python tem cinco tipos de dados padrão
        - Números
            -> int
            -> long
            -> float
            -> complexo
        - String
            Conjunto continue de caractere entre aspas
            + operador de concatenação
            * operador de repetição
        - Lista
            + operador de concatenação
            * operador de repetição
            Aceitam qualquer valor
            podem ser mudadas
        - Tupla
            aceita qualquer valor
            são imutaveis
        - Dicionário
            São do tipo tabela hash
"""

print("===== STRING =====")
# String
nome = "Lucas"
Sobrenome = "de Souza Santos"

## concatenação
print(nome + Sobrenome)

## Repetição
print(nome * 2)

print("===== LISTA =====")
# lista [nome, peso, idade]
lista1 = ['Lucas', 82.2, 28]
lista2 = ['nancy', 55.6, 54]

## concatenação
cadastro = lista1 + lista2
print(cadastro)

# repetição
print(lista1 * 2)

print("===== TUPLA ====")
tupla1 = ('lucas', 34, 89.2)
tupla2 = ('nancy', 67, 68.9)

## concatenação
print(tupla1 + tupla2)

## repetição
print(tupla1 * 2)

print("===== Dicionário =====")
# Dicionário
dicionario1 = {"nome": "Lucas", "idade": 28, "peso": 82.1}
dicionario2 = {"nome": "nancy", "idade": 54, "peso": 54.6}

print(dicionario1)
print(dicionario2)
print(dicionario1["nome"])

"""
> Conversão de tipo de dados
    x -> dados 
    int(x)
    long(x)
    float(x)
    str(x)
    
"""
