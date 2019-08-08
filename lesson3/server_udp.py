import json
import socket
from argparse import ArgumentParser


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


if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        sock.bind((config['host'], config['port']))

        print(f'Server started on {config["host"]}:{config["port"]} (press Ctrl+C to stop)...')

        while True:
            client_bytes, client = sock.recvfrom(config['buffersize'])
            client_host, client_port = client

            print(f'Client connected at {client_host}:{client_port}')

            client_data = json.loads(client_bytes.decode())
            print(f'Client message: {client_data}')

            sock.sendto(json.dumps({
                'status': 200,
                'alert': f'{client_data["user"]["account"]} typed: {client_data["user"]["status"]}!'
            }).encode(), client)

    except KeyboardInterrupt:
        # todo: close all the connections
        # client.close()
        print('Server shutdown')
