"Adivinhe se Puder"
import random

pontosJogador = 0
pontosComputador = 0

for tentativa in range(0, 3):
	aleatorio = random.randint(0, 5)
	#print(aleatorio)# Temporario

	print("Digite um número entre 0 e 5: ")
	numero = int(input())

	if numero == aleatorio:
		pontosJogador += 1
		print("Parabéns. Você Acertou!!!")
	else:
		pontosComputador += 1
		print("Que triste. Você Errou!!!")

if pontosJogador > pontosComputador:
	print(f"Incrivel. Você ganhou, acertou {pontosJogador} vezes.")
else:
	print(f"Que pena. Você perdeu, acretou somente {pontosJogador} vezes.")
