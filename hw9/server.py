# server.py - 멀티스레드 채팅 서버
from socket import *
import threading

clients = []
port = 3333
BUFFSIZE = 1024

def handle_client(conn, addr):
    print(f"✔️ {addr} 연결됨")
    while True:
        try:
            data = conn.recv(BUFFSIZE)
            if not data:
                break
            print(f"[{addr}] {data.decode()}")

            # 모든 클라이언트에게 메시지 전송
            for c in clients:
                if c != conn:
                    c.send(data)
        except:
            break

    print(f"❌ {addr} 연결 종료")
    clients.remove(conn)
    conn.close()

# 서버 시작
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)
print(f"✅ 서버 시작 (포트 {port})...")

while True:
    conn, addr = sock.accept()
    clients.append(conn)
    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()
