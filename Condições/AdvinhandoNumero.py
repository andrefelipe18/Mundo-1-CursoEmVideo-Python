import random;

print('----- Jogo de advinhação -----');
print('----- Tenta acertar o numero -----');

numRandom = random.randint(0, 5);
numEscolhido = int(input('Escolha seu numero: '));

if numEscolhido == numRandom:
    print('VOCE GANHOU!!')
else:
    print('FOI DE F');