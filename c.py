import socket
from threading import Thread
from datetime import datetime

hostname = socket.gethostname()
port = 12349
s = socket.socket()
s.connect((hostname, port))

print("вы подключились к серверу")
print("для отключения введите: й")
name = input("ваш ник: ")

def a():
    while True:
        message = s.recv(1024).decode()
        print(message)

Thread(target=a, daemon=True).start()

while True:
    message = input()
    if message.lower() == 'й':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M%S')
    message = f"[{date_now}] {name}: {message}"
    s.send(message.encode())
s.close()
