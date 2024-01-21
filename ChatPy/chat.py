import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 55555

# TODO: Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO: Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# TODO: Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# List to store connected clients
clients = []

# Function to handle individual client connections
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")

    # TODO: Send a welcome message to the client
    client_socket.send("Welcome to the chat! Type 'exit' to leave.".encode())

    # TODO: Add the client to the list
    clients.append(client_socket)

    while True:
        # TODO: Receive and broadcast messages
        message = client_socket.recv(1024).decode()
        if message.lower() == 'exit':
            break

        # TODO: Broadcast the message to all connected clients
        for client in clients:
            if client != client_socket:
                client.send(f"{client_address[0]}: {message}".encode())

    # TODO: Remove the client from the list
    clients.remove(client_socket)
    client_socket.close()
    print(f"Connection from {client_address} closed")

# TODO: Function to handle sending messages
def send_messages():
    while True:
        message = input()
        # TODO: Broadcast the message to all connected clients
        for client in clients:
            client.send(f"Server: {message}".encode())

# TODO: Start a separate thread for sending messages
send_thread = threading.Thread(target=send_messages)
send_thread.start()

# TODO: Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
