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
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((config['host'], config['port']))
        sock.listen(5)

        print(f'Server started on {config["host"]}:{config["port"]} (press Ctrl+C to stop)...')

        while True:
            client, address = sock.accept()
            client_host, client_port = address

            print(f'Client connected at {client_host}:{client_port}')

            client_bytes = client.recv(config['buffersize'])
            client_data = json.loads(client_bytes.decode())

            print(f'Client message: {client_data}')

            client.send(json.dumps({
                'status': 200,
                'alert': f'Hi, {client_data["user"]["account"]}!'
            }).encode())
    except KeyboardInterrupt:
        # todo: close all the connections
        client.close()
        print('Server shutdown')
