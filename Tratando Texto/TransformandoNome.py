nome = str(input('Digite seu nome completo: '));

print('Seu nome todo em maisculo: {}'.format(nome.upper()));
print('Seu nome todo em minusculo: {}'.format(nome.lower()));
qtdSemEspaco = len(nome.strip());
print('Seu nome sem espaços: {}'.format(qtdSemEspaco));
nomeCortado = nome.split();
qtdLetras = len(nomeCortado[0]);
print('Quantas letras tem seu primeiro nome: {}'.format(qtdLetras));