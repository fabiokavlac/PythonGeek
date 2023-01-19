"""
Escopo de variaveis

Dois casos de escopo:

1 - Variaveis globais;
    - Variaveis globais são reconhecidas, ou seja seu escopo compreende, todo o programa.

2 - Variaveis locais;
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está
    limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de prototipagem dinamica.
Isso significa que ao declararmos uma variável, nós não vamos colocar o tipo de dado dela.
Este tipo é indeferido ao atribuirmos o valor a mesma.
"""

numero = 42
print(numero)
print(type(numero))

numero = 100
if numero > 99:
    novo = numero + 11 # A variavel 'novo' esta declarada localmente dentro do bloco if. Portanto é local.
    print(novo)
