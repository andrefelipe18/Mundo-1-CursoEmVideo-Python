a = float(input('Digite um numero: '));
b = float(input('Digite um numero: '));
c = float(input('Digite um numero: '));

if a < b + c and b < a + c and c < a + b:
    print('Com esses tres numeros pode ser formado um triangulo');
else:
    print('Nao pode formar um triangulo');