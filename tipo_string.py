"""
Tipo String
Em Python um dado é considerado do tipo String sempre que:

- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Ola'
- Aspas duplas -> "Ola"
- Aspas simples triplas -> '''Ola'''
- Aspas duplas triplas -> Ola

nome = "Fabio 1 Kavlac"
print(nome)
print(type(nome))
"""

# [0,    1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11]
# ['F', 'a', 'b', 'i', 'o', '',  'K', 'a', 'v', 'l', 'a', 'c']

nome = 'Fabio Kavlac'
print(nome[0:5])   #Slice de string

print(nome.split())

print(nome.split()[0])

print(nome[11])

# [::-1] -> Comece do primeiro elemento, va ate o ultimo elemento e inverta
print(nome[::-1])

print(nome.replace('a', 'i')[::-1])
