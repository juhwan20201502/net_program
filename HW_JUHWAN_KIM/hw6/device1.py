# device1.py
import socket
import random

server = socket.socket()
server.bind(('localhost', 9001))
server.listen(1)
print("🌡️ Device1 (온습조도) 서버 실행 중...")

while True:
    client, addr = server.accept()
    msg = client.recv(1024).decode()
    if msg == "Request":
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)
        data = f"{temp},{humid},{illum}"
        client.send(data.encode())
    elif msg == "quit":
        client.close()
        break
    client.close()

server.close()
