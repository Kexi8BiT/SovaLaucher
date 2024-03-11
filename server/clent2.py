import socket
import json
import threading
def send():
    while True:
        title = input('Enter title: ')
        text = input('Enter text: ')
        json_message = json.dumps({'title': title, 'text': text})
        client.send(json_message.encode('ascii'))

host = 'localhost'
port = 6084

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

send_thread = threading.Thread(target=send)
send_thread.start()