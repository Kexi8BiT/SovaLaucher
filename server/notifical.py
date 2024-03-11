import socket
import threading
import json

clients = []
host = 'localhost'
port = 6084

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            json_message = json.loads(message)
            print(f'Received message: {json_message}')
            broadcast(message.encode('ascii'), client)
        except:
            clients.remove(client)
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server is listening...')
receive()