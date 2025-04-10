# client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("💬 클라이언트 실행 중. 명령어: send [mboxID] [msg], receive [mboxID], quit")

while True:
    cmd = input(">> ")

    client_socket.sendto(cmd.encode(), ('localhost', 9999))
    if cmd.startswith("quit"):
        print("👋 클라이언트 종료")
        break

    data, _ = client_socket.recvfrom(1024)
    print("📨 서버 응답:", data.decode())

client_socket.close()
