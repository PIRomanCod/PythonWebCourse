import asyncio
import logging
from datetime import datetime

import websockets
import names
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK

from exchanger import exchanger_run


logging.basicConfig(level=logging.INFO, handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ])
fh = logging.FileHandler("app.log")
fh.setLevel(logging.INFO)

class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{datetime.now()} {ws.remote_address} connects')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{datetime.now()} {ws.remote_address} disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            if message.startswith('exchange'):
                income = message.split()
                if len(income) == 3:
                    r = await exchanger_run(income[1], income[2])
                elif len(income) == 2:
                    r = await exchanger_run(income[1])
                else:
                    r = await exchanger_run()
                logging.info(f'user: "{datetime.now()} {ws.name}" used exchanger func with args: {income[1:]}"')
                await self.send_to_clients(r)
                # await self.send_to_client(r, ws)
            else:
                logging.info(f'user: "{datetime.now()} {ws.name}" wrote: "{message}"')
                await self.send_to_clients(f"{ws.name}: {message}")


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())