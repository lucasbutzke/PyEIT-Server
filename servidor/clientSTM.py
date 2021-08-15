"""fazer codigo para receber dados do servidor 
raspberry, para isso deve mandar executar o script
no dispositivo
"""
import asyncio
import numpy as np
import time
import paramiko
import os

# comando para retornar ip publico
# curl "http://myexternalip.com/raw"
os.system('curl "http://myexternalip.com/raw"')

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost, vetor):
        self.message = message
        self.on_con_lost = on_con_lost
        self.vetor = vetor

    def connection_made(self, transport):
        transport.write(self.message.encode())
        # print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        data = data.decode()
        print(data)
        # exit()
        data = data.split()
        index = int(data[0])
        self.vetor[index] = data[1]
        # print(f'Data received: {self.vetor[0]}')

    def connection_lost(self, exc):
        # print('The server closed the connection')
        self.on_con_lost.set_result(True)


async def main(message, vetor):
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost, vetor),
        '0.0.0.0', 8888)

    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    finally:
        transport.close()


if __name__ == '__main__':
    message_getADC = "GET /ADC"
    vetor = np.array(np.zeros(208), dtype=int)
    print(vetor)
    tempo = time.time()
    while 1:
        asyncio.run(main(message_getADC, vetor))
        # time.sleep(1)
        if(vetor[208-1] != 0):
            print(vetor)
            print(time.time() - tempo)
            break

