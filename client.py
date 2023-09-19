from socket import *
import time

PORT = 12000
#SERVER = "enter ip here"
ADDR = (SERVER, PORT)
MAX_BUFFER = 1024
DISCONNECT = 'quit'
log = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

print(f"[CONNECTING] Connecting to {SERVER}")
time.sleep(1)
print("[SUCCESSFUL CONNECTION] Enter 'quit' to disconnect...")

connected = True

while connected:
    message = input("[SEND MESSAGE]... ")
    log.append(message)

    if message == DISCONNECT:
        client_socket.send(message.encode())
        client_socket.close()
        print("[LOG]...")

        for x in log:
            print(x)
        break

    print(f"[SENDING]... Sending message to {SERVER}: {message}")
    client_socket.send(message.encode())

