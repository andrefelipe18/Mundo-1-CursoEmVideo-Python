frase = 'Curso em Video Python';

print('A quarta letra da frase é: {}'.format(frase[3]));
print('Da quarta letra a 14 fica: {}'.format(frase[3:14]));
print('Do inicio até a 14 fica: {}'.format(frase[:14]))
print('Do 14 até o final fica: {}'.format(frase[14:]))
print('Do inicio ao final com espaçamento de 2 em 2 fica: {}'.format(frase[::2]))
print('O Comprimento da frase é: {}'.format(len(frase)));
print('Usando replace em Python fica: {}'.format(frase.replace('Python', 'Android')));
print('Separando as palavras com split: {}'.format(frase.split()));
fraseSeparada = frase.split();
print('Juntando a frase novamente com Join: {}'.format('-'.join(frase)))
