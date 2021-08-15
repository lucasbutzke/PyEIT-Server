"""
terminar STM32F767ZI servidor
refazer codigo para melhor escrita HAL
como tornar automatico DMA e outros componentes
"""
import socket
import threading
import time

# tell length of posteriors messages in this SERVER/CLIENT connection
HEADER = 64

PORT = 8888
# SERVER = '10.0.0.180'
# SERVER = '192.168.0.10'
# SERVER = '169.254.143.8'
SERVER = '169.254.153.67'
# SERVER = 'localhost'
ADDR = (SERVER, PORT)
# print(SERVER)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


def send(msg):
    while 1:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect(ADDR)
            print("conectou")
        except:
            print("nao deu")
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        # send_length += b' ' * (HEADER - len(send_length))
        # client.send(send_length)
        client.send(message)
        print(client.recv(10))
        time.sleep(1)
        client.close()

send("GET /STM32F7xx_files/ST.gif")
# send(DISCONNECT_MESSAGE)


