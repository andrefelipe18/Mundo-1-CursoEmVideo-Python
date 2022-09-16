salario = float(input('Digite seu salario: '));
if salario > 1250.00:
    novoSalario = (10/100) * salario;
    print('Seu novo salario será R${:2}'.format(salario+novoSalario));
else:
    novoSalario = (15/100) * salario;    
    print('Seu novo salario será R${:2}'.format(salario+novoSalario));