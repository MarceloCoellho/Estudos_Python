"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    esta limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguatem de tipagem dinâmica. isso significa que ao declarar uma variável, nos não precisamos
colocar o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;
# não e possivel fazer uma re-atribuição

"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Marcelo'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10  # Exemplo de variável local, a variável 'novo' foi declarada localmente dentro do bloco do if.
    print(novo)

