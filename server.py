import socket
import threading

# List to store all client connections
clients = []
client_count = 0  # Variable to keep track of client numbers

def handle_client(client_socket, client_number):
    while True:
        try:
            # Receive message from client
            data = client_socket.recv(1024)
            if not data:
                break
            # Decode received data and broadcast message to all clients except the sender
            message = data.decode()
            for client in clients:
                if client[0] != client_socket:
                    try:
                        client[0].sendall(f"Client-{client_number}: {message}".encode())
                    except:
                        # If sending fails, assume client disconnected and remove from list
                        clients.remove(client)
        except Exception as e:
            print(f"Error: {e}")
            break

    # Close client connection
    client_socket.close()

def main():
    # Server configuration
    host = '127.0.0.1'
    port = 9999

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[*] Listening on {host}:{port}")

    global client_count

    while True:
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        # Increment client count and assign client number
        client_count += 1
        current_client_number = client_count

        # Add client socket to list along with client number
        clients.append((client_socket, current_client_number))

        # Handle client in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, current_client_number))
        client_thread.start()

if __name__ == "__main__":
    main()
