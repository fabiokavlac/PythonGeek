"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.
Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:
num = 5
num < 5

#Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

#OBS: Em sum loop while é importante que cuidemos do critétio de parada para não causar um loop infinito.

#Exemplo 2

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
"""


"""
Saindo de loops com break
Utilizamos o break para sair de loops de maneira projetada.

#Exemplo 1
for numero in range(1, 10):
     if numero == 6:
         break
     else:
         print(numero)
print('Sai do loop')

"""

#Exemplo2

while True:
    comando = input("Digite '1' para sair: ")
    if comando == '1':
        break