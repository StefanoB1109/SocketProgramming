from socket import *
import time
import threading

PORT = 12000
#SERVER = "enter server ip here"
ADDR = (SERVER, PORT)
MAX_BUFFER = 1024
DISCONNECT = 'quit'

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen(1)

print("[STARTING] Server is starting...")
time.sleep(1)
print(f"[READY] Server is ready to recieve at {SERVER}...")

def connect_client():
    while True:
        connection, addr = server_socket.accept()
        thread = threading.Thread(target = client_message, args = (connection, addr))
        thread.start()
        
def client_message(connection, addr):
    print(f"[SUCCESSFUL CONNECTION] {addr}")

    connected =  True
    while connected:
        message = connection.recv(MAX_BUFFER).decode()
        if message == DISCONNECT:
            connected = False
            print(f"[DISCONNECTED] {addr} has been disconnected...")
            connection.close()
        else: 
            print(f"[MESSAGE RECIEVED] {addr}: {message}")

connect_client()

