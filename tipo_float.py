"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula.
 - Errado
valor = 1,44
 - Certo
valor = 1.44
"""

valor = 1, 44 # Com a vírgula gera uma tupla
print(valor)
print(type(valor))


valor = 1.44
print(valor)
print(type(valor))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com númeres complexos
variavel = 5j
print(variavel)
print(type(variavel))
