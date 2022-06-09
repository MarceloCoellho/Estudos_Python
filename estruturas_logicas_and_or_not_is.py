"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not;
Operadores binários:
    - and, or, is;

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True

"""
ativo = False
logado = False


if ativo and logado:
    print('Bem-vindo, usuário!')
elif ativo or logado:
    print('Ainda falta uma etapa, você precisa ativar seu cadastro no e-mail ou logar com sua conta!')
elif not ativo:
    print('Você não possui cadastro!')

print(ativo is False)






