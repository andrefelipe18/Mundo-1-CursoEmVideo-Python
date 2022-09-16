import os;

largura = float(input("Digite a largura da parede"));
altura = float(input("Digite a altura da parede"));
area = largura * altura
litro = 2;
qtdNecessaria = area / litro

print("A Quantidade de baldes necessario para pintar sua parede é {}".format(qtdNecessaria));
os.system("PAUSE")
