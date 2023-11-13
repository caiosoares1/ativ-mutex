import threading
import time

# Prof. Gustavo Wagner, gugawag@gmail.com
# IFPB - Sistemas Operacionais
# Explicacao: programa desenvolvido para demonstrar condicao de disputa. Metodos p1 e p2, indefinidamente, incrementam
#             a variavel global 'numero'. Como nao hah exclusao mutua, pode haver condicao de corrida.

# aluno: CAIO BATISTA DA SILVA SOARES
numero = 0

mutex = threading.Semaphore(1)

def p1():
    global numero
    while True:
        global mutex
        mutex.acquire()
        numero += 1
        print('P1:', numero)
        time.sleep(1)  # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
        mutex.release()


def p2():
    global numero
    while True:
        global mutex
        numero += 1
        print('P2:', numero)
        time.sleep(1)  # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
        mutex.release()


t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)

t_p1.start()
t_p2.start()
