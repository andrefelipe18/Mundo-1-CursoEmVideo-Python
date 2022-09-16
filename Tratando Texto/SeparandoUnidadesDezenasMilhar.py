numEscolhido = int(input('Digite um numero de 0 a 9999: '));
milhar = numEscolhido // 1000 % 10
centena = numEscolhido // 100 % 10
dezena = numEscolhido // 10 % 10
unidade = numEscolhido // 1 % 10
print('Milhar: {}'.format(milhar));
print('Centena: {}' .format(centena));
print('Dezena: {}' .format(dezena));
print('Unidade: {}' .format(unidade));