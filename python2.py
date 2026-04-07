#        Condicionais aninhadas

nome = str(input('Qual seu nome?'))
if nome == 'Larissa':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Clara, Laura, Luiza, Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
    print(f'Tenha um bom dia, {nome}!')
