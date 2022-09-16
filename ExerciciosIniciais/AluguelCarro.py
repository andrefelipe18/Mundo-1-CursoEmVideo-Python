import os

#Entrada de dados
diasAlugados = float(input("Quantos dias o carro foi alugado? "));
kmRodados = float(input("Quantos km foram rodados? "));

valorDia = 60;
valorKm = 0.15;

valorFinalDias = diasAlugados * valorDia;
valorFinalKm = valorKm * kmRodados;

valorFinal = valorFinalDias + valorFinalKm;
print("O valor total foi R${}".format(valorFinal));

os.system("PAUSE")
