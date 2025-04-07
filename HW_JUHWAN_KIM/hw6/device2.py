# device2.py
import socket
import random

server = socket.socket()
server.bind(('localhost', 9002))
server.listen(1)
print("❤️ Device2 (심박/걸음/칼로리) 서버 실행 중...")

while True:
    client, addr = server.accept()
    msg = client.recv(1024).decode()
    if msg == "Request":
        heart = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        data = f"{heart},{steps},{cal}"
        client.send(data.encode())
    elif msg == "quit":
        client.close()
        break
    client.close()

server.close()
