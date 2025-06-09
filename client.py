import socket
import threading

#Public Ip Address: 76.187.205.244
# My pc ip address: 192.168.0.209

class GameClient:
    def __init__(self, host='192.168.0.209', port=25565):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send_data(self, data):
        self.client.send(data.encode('utf-8'))

    def receive_data(self):
        while True:
            try:
                data = self.client.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"Received: {data}")
            except:
                break

    def start(self):
        receive_thread = threading.Thread(target=self.receive_data)
        receive_thread.start()

if __name__ == "__main__":
    client = GameClient()
    client.start()
    while True:
        message = input("Enter message: ")
        client.send_data(message)