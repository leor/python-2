import json
import socket
import logging
from logging.handlers import TimedRotatingFileHandler

from argparse import ArgumentParser
from protocol import validate_request, make_response
from settings import INSTALLED_APPS
from resolver import resolve


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


if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((config['host'], config['port']))
        sock.listen(5)

        logging.info(f'Server started on {config["host"]}:{config["port"]} (press Ctrl+C to stop)...')

        while True:
            client, address = sock.accept()
            client_host, client_port = address

            logging.info(f'Client connected at {client_host}:{client_port}')

            client_bytes = client.recv(config['buffersize'])
            request = json.loads(client_bytes.decode())

            if(validate_request(request)):
                action = request.get('action')
                controller = resolve(action, INSTALLED_APPS)

                if controller:
                    try:
                        response = controller(request)
                        logging.info(f'Sending server response {response}')
                    except Exception as err:
                        response = make_response(request, 500, 'Internal server error')
                        logging.critical(f'Exception - {err}')    
                else:
                    response = make_response(request, 404, f'Action {action} not found')
                    logging.error(f'Client {client_host}:{client_port} call unknown action {action}')
            else:
                response = make_response(request, 400, 'Wrong request')
                logging.error(f'Client {client_host}:{client_port} sent wrong request {request}')

            client.send(json.dumps(response).encode())

            client.close()
    except KeyboardInterrupt:
        client.close()
        logging.info('Server shutdown')
