"""
Fazer cliente que envie continuamente algum dado e
receba mensagens de comando para START/STOP ou ate
STATUS atual. Como executar de maneira que o servidor
entenda todos parametros, enviar STRINGS e INTEIROS.
"""
from socket import *
from threading import Thread

host = 'localhost'
port = 1234
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))

def Listener():
    try:
        while True:
            message = input('')
            s.send(message.encode('utf-8'))
    except EOFError:
        pass

    try:
        while True:
            data = s.recv(1024).decode('utf-8')
            print('', data)
    except ConnectionAbortedError:
        pass

    finally:
        s.close()

t = Thread(target=Listener)
t.start()
