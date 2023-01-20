"""
Estruturas condicionais
if(Se), else, elif
"""

idade = 18

"""
Estrutura condicional if, em C

if(idade < 18) {
    printf("Menor de idade");
}
"""

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')