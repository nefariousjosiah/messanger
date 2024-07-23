import socket

def start_client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 12345))  # Connect to the server IP on port 12345
    
    print("Connected to the server")

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            print("Connection closed.")
            break
        reply = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {reply}")

    client_socket.close()

if __name__ == "__main__":
    server_ip = input("Enter the server IP address: ")
    start_client(server_ip)
