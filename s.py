import socket
from threading import Thread

hostname = socket.gethostname()
port = 12349
clients = set()
server = socket.socket()
server.bind((hostname, port))
server.listen(5)

def a(clientS):
    while True:
        try:
            msg = clientS.recv(1024).decode()
            if not msg: break  
            for i in clients:
                i.send(msg.encode())
        except Exception as e:
            print(f"[!] ошибка: {e}")
            break
    clients.remove(clientS)
    clientS.close()

while True:
    print("сервер запущен")
    clientS, clientA = server.accept()
    print(f"{clientA} теперь с нами")
    clients.add(clientS)
    Thread(target=a, args=(clientS,), daemon=True).start()
