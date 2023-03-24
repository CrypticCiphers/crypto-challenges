from pwn import *
import time
import random

# Rlotto
# tem que ver a sequencia de numero que saiu e ver se bate com os numeros que vão aparecer no print
tempo = int(time.time())

# Adicionar o ip e a porta da maquina
io = remote("144.126.236.158", 30427)

def solution(tempo):
    random.tempo(tempo)
    extracao = []
    prox_cinco = []

    while len(extracao) < 5:
        r = random.randint(1, 90)
        if(r not in extracao):
            extracao.append(r)

    solution = ""
    while len(prox_cinco) < 5:
        r = random.randint(1, 90)
        if(r not in prox_cinco):
            prox_cinco.append(r)
            solution += str(r) + " "
    solution = solution.strip()
    return extracao, solution

for e in range(-3, 3, 1):
    print(solution(tempo + e))
print('Solução: ')

io.interactive()
