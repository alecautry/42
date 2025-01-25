import socket
import threading

#Public Ip Address: 76.187.205.244
# My pc ip address: 192.168.0.209

class GameServer:
    def __init__(self, host='0.0.0.0', port=25565):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(4)  # Listen for up to 4 connections
        self.clients = []
        self.lock = threading.Lock()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                self.broadcast(data, client_socket)
            except:
                break
        client_socket.close()
        with self.lock:
            self.clients.remove(client_socket)

    def broadcast(self, message, client_socket):
        with self.lock:
            for client in self.clients:
                if client != client_socket:
                    try:
                        client.send(message.encode('utf-8'))
                    except:
                        client.close()
                        self.clients.remove(client)

    def start(self):
        print("Server started...")
        while True:
            client_socket, addr = self.server.accept()
            print(f"Connection from {addr}")
            with self.lock:
                self.clients.append(client_socket)
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    server = GameServer()
    server.start()