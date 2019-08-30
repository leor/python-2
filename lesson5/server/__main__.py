import socket
import logging
from logging.handlers import TimedRotatingFileHandler
from select import select

from argparse import ArgumentParser
from handlers import handle_tcp_request

config = {
    'host': '127.0.0.1',
    'port': 7777,
    'buffersize': 1024
}

arg_parser = ArgumentParser()

arg_parser.add_argument(
    '-a', '--addr', type=str, required=False,
    help='Sets server IP address'
)
arg_parser.add_argument(
    '-p', '--port', type=int, required=False,
    help=f'Sets server port ({config["port"]} by default)'
)

args = arg_parser.parse_args()

if args.addr:
    config['host'] = args.addr

if args.port:
    config['port'] = args.port


logging.basicConfig(
    level = logging.DEBUG,
    handlers=(
        TimedRotatingFileHandler(f'logs/server.log', when='D'),
        logging.StreamHandler()
    ),
    format='%(asctime)s - %(levelname)s - %(message)s'
)

connections = []
requests = []

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((config['host'], config['port']))
        sock.setblocking(False)
        sock.settimeout(0)
        sock.listen(5)

        logging.info(f'Server started on {config["host"]}:{config["port"]} (press Ctrl+C to stop)...')

        while True:
            try:
                client, address = sock.accept()
                client_host, client_port = address

                logging.info(f'Client connected at {client_host}:{client_port}')

                connections.append(client)
            except:
                pass


            rlist, wlist, xlist = select(connections, connections, connections, 0)

            for r_client in rlist:
                requests.append(r_client.recv(config['buffersize']))

            if requests:
                client_bytes = requests.pop()
                response = handle_tcp_request(client_bytes)

                for w_client in wlist:
                    w_client.send(response)
    except KeyboardInterrupt:
        if connections:
            for client in connections:
                sock.close(client)

        logging.info('Server shutdown')
