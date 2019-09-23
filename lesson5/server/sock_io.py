def read(client, connections, requests, buffersize):
    try:
        client_bytes = client.recv(buffersize)
    except Exception:
        connections.remove(client)
    else:
        requests.append(client_bytes)

def write(client, connections, request):
    try:
        client.send(request)
    except Exception:
        connections.remove(client)