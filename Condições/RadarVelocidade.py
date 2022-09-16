vel = float(input('Qual a velocidade que o carro estava: '));
velMaxima = 80;
valorMulta = (vel - velMaxima) * 7
if vel > velMaxima:
    print('Sua velocidade está acima do permitido');
    print('Está devendo R${:2} em multa'.format(valorMulta));
else:
    print('Tudo certo!!');