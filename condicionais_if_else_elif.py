"""
Estruturas condicionais
if(se), else(senão), elif(else if)
"""

idade = 26

"""
# Estrutura condicional if, else em C
if(idade < 10){
    printf("Menor de idade");
}else{
    printf("Maior de idade");
}
"""
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')


