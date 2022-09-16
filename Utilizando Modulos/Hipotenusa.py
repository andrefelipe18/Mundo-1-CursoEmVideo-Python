import math

CatetoOposto = float(input("Comprimento do Cateto Oposto: "))
CatetoAdjacente = float(input("Comprimento do Cateto Adjacente: "))

hipotenusa = math.hypot(CatetoOposto, CatetoAdjacente);

print("A hipotenusa é: {:2}".format(hipotenusa))
