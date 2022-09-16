kmViajados = float(input('Quantos Kms deseja viajar: '));
mViagem = 0,50
lViagem = 0,45
if kmViajados <= 200:
    print('O Valor para essa viagem é R${}'.format(kmViajados*mViagem));
else:
     print('O valor com desconto para longas viagens é R${}'.format(kmViajados*lViagem));
