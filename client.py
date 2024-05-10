import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    # Server configuration
    host = '127.0.0.1'
    port = 9999

    # Connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Start receiving messages in a separate thread
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send messages to server
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())

    # Close connection
    client_socket.close()

if __name__ == "__main__":
    main()
