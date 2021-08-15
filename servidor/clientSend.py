"""
terminar STM32F767ZI servidor
refazer codigo para melhor escrita HAL
como tornar automatico DMA e outros componentes
"""
import socket
import threading


# tell length of posteriors messages in this SERVER/CLIENT connection
HEADER = 64

PORT = 8888
SERVER = '10.0.0.150'
# SERVER = 'localhost'
ADDR = (SERVER, PORT)
# print(SERVER)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))

send("Hello Word!!!")
send(DISCONNECT_MESSAGE)

client.close()
