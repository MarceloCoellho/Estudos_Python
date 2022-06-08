"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre áspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
#- Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

"""
nome = 'Marcelo Henrique'
print(nome)
print(type(nome))

nome = "Gina's Bar"  #Para incluir as àspas simples numa string tem que colocar em àspas duplas
print(nome)
print(type(nome))

nome = "Marcelo \nHenrique"  #Podemos utilizar àspas duplas triplas para dar enter no meio das strings nao utilizando o \n
print(nome)
print(type(nome))

nome = "Marcelo \" Henrique"
print(nome)
print(type(nome))
"""

nome = 'Marcelo Henrique'
print(nome.upper())  # Transforma todos os caracteres em MAIUSCULA
print(nome.lower())  # Transdorma todos os caracteres em minuscula
print(nome.split())  # Transforma em uma lista de strings
print(nome.split()[0])  # Imprime o iten da lista relacionado entre []
"""
[ 0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15 ]
['M', 'a', 'r', 'c', 'e', 'l', 'o', ' ', 'H', 'e', 'n', 'r', 'i', 'q', 'u', 'e']
"""
print(nome[0:7])  # Imprime os caracteres relacionados entre []
print(nome[8:16])  # Chamamos essa função de Slice de String
print(nome[::-1])  # [::-1] -> Começe do primeiro elemento, vá ate o último elemento e inverta
print(nome.replace('M', 'H'))  # Troca os elementos


