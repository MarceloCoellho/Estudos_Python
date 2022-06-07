"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é yudo que estiver entre:
- Aspas simples -> 'Marcelo'
- Aspas duplas -> "Marcelo"
- Aspas simples triplas -> '''Marcelo'''
- Aspas duplas triplas -> ""Marcelo""

"""
# Entrada de dados
#print('Qual seu nome?')
#nome = input() # Imput - Entrada

nome = input('Qual seu nome?')
# Exemplo de print 'antigo' 2x
#print('Seja bem-vindo(a) %s' % nome)

#Exemplo de print 'moderno' 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

#print('Qual a sua idade?')
#idade = input()

idade = int(input('Qual a sua idade?'))
# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2x
#print('O %s tem %s anos' % (nome, idade))

#Exemplo de print 'moderno' 3.x
#print("O {0} tem {1} anos".format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O {nome} tem {idade} anos')


"""
# int(idade) => cast
Cast e a 'conversão de um tipo de dado para outro.
"""
print(f'O {nome} nasceu em {2022 - idade}')
