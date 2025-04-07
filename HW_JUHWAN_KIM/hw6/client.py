# client.py (사용자)
import socket
import time

def save_data(device, values):
    now = time.ctime()
    if device == 1:
        temp, humid, illum = values.split(',')
        line = f"{now}: Device1: Temp={temp}, Humid={humid}, Illum={illum}\n"
    else:
        heart, steps, cal = values.split(',')
        line = f"{now}: Device2: Heartbeat={heart}, Steps={steps}, Cal={cal}\n"

    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(line)
    print("✅ 저장 완료:", line.strip())

while True:
    cmd = input("📥 디바이스 선택 (1, 2 또는 quit): ")
    if cmd == "1":
        sock = socket.socket()
        sock.connect(('localhost', 9001))
        sock.send("Request".encode())
        data = sock.recv(1024).decode()
        save_data(1, data)
        sock.close()
    elif cmd == "2":
        sock = socket.socket()
        sock.connect(('localhost', 9002))
        sock.send("Request".encode())
        data = sock.recv(1024).decode()
        save_data(2, data)
        sock.close()
    elif cmd == "quit":
        for port in [9001, 9002]:
            sock = socket.socket()
            sock.connect(('localhost', port))
            sock.send("quit".encode())
            sock.close()
        print("👋 종료합니다.")
        break
    else:
        print("❗ 1, 2, quit 중에서 입력하세요.")
1