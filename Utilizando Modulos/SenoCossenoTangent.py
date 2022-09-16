import math

angulo = float(input("Digite um angulo: "))

seno = math.sin(math.radians(angulo));
coseno = math.cos(math.radians(angulo));
tangente = math.tan(math.radians(angulo));

print("O Angulo de {} tem o SENO de {:.2f}" .format(angulo, seno));
print("O Angulo de {} tem o COSENO de {:.2f}" .format(angulo, coseno));
print("O Angulo de {} tem a TANGENTE de {:.2f}" .format(angulo, tangente));

