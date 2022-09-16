nome = str(input('Digite seu nome: ')).strip();
nome = nome.split();
print('Seu primeiro nome é: {}'.format(nome[0]));
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]));
