import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind to all interfaces on port 12345
    server_socket.listen(1)
    
    print("Waiting for connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            print("Connection closed.")
            break
        print(f"Received: {message}")
        reply = input("Enter your message: ")
        client_socket.send(reply.encode('utf-8'))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
