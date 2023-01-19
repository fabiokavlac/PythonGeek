"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Ola'
- Aspas duplas -> "Ola"
- Aspas simples triplas -> '''Ola'''
- Aspas duplas triplas -> Ola
"""
#print("Qual seu nome? ")
#nome = input()

nome = input('Qual seu nome? ')

#Exemplo de print antigo 2.x
#print('Seja bem-vindo(a) %s' % nome)

#Exemplo de print moderno 3.x
#print('Seja bem vinfo(a) {0}'.format(nome))

#Exemplo de print moderno 3.7
print(f'Seja bem vindo(a) {nome}')

#print("Qual sua idade? ")
#idade = input()

idade = input('Qual sua idade? ')

#Processamento

#Saida de dados
#Exemplo de print antigo 2.x
#print('O(a) %s tem %s anos' % (nome, idade))

#exemplo de print moderno 3.x
#print('A(o) tem {0} {1} anos'.format(nome, idade))


#Exemplo de print moderno 3.7
print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2022 - int(idade)}')


