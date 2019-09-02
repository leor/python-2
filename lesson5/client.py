import socket
import json
from datetime import datetime
from argparse import ArgumentParser
import hashlib
import zlib


READ_MODE = 'r'
WRITE_MODE = 'w'


def make_request(action, data, token=None):
    return {
        'action': action,
        'data': data,
        'time': datetime.now().timestamp(),
        'token': token
    }


config = {
    'server': '127.0.0.1',
    'port': 7777,
    'buffersize': 1024
}

arg_parser = ArgumentParser()

arg_parser.add_argument(
    '-a', '--addr', type=str, required=True,
    help='Sets server IP address'
)
arg_parser.add_argument(
    '-p', '--port', type=int, required=False,
    help=f'Sets server port ({config["port"]} by default)'
)
arg_parser.add_argument(
    '-m', '--mode', type=str, default=READ_MODE,
    help=f'Sets client mode ("read" by default)'
)

args = arg_parser.parse_args()

if args.addr:
    config['host'] = args.addr

if args.port:
    config['port'] = args.port


if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((config['host'], config['port']))

        print(f'Client started (press Ctrl+C to stop)...')

        while True:
            if args.mode == WRITE_MODE:
                action = input('Enter server action: ')
                data = input('Enter data to pass to server: ')
                
                hash_object = hashlib.sha256()
                hash_object.update(
                    str(datetime.now().timestamp()).encode()
                )

                print('Sending data...')
                sock.send(zlib.compress(json.dumps(make_request(
                    action, data, hash_object.hexdigest()
                )).encode()))

            else:
                print('Recieving data...')
                bytes_response = sock.recv(config.get('buffersize'))
                print(f'Server message: {json.loads(zlib.decompress(bytes_response).decode())}')
    except KeyboardInterrupt:
        sock.close()
        print('Client shutdown')
