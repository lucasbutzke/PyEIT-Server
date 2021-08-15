# asyncio already comes eith sockets and simplify code
# understand and make a simple client to test
# better code to run multiple applications besides only connection
import asyncio

clients = []
SERVER = '192.168.0.10'

class SimpleChatClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.peername = transport.get_extra_info("peername")
        print("connection_made: {}".format(self.peername))
        clients.append(self)

    def data_received(self, data):
        print("data_received: {}".format(data.decode()))
        for client in clients:
            if client is not self:
                client.transport.write("{}: {}".format(self.peername, data.decode()).encode())

    def connection_lost(self, ex):
        print("connection_lost: {}".format(self.peername))
        clients.remove(self)

if __name__ == '__main__':
    print("starting up..")

    loop = asyncio.get_event_loop()
    coro = loop.create_server(SimpleChatClientProtocol, SERVER, port=80, family=socket.AF_INET, flags=socket.SOCK_STREAM)
    server = loop.run_until_complete(coro)

    for socket in server.sockets:
        print(f"serving on {socket.getsockname()}")

    loop.run_forever()
