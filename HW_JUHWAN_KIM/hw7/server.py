# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 9999))
print("📡 UDP 서버 실행 중... (포트 9999)")

mailboxes = {}

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()

    print(f"📥 받은 메시지: {message}")
    parts = message.split(maxsplit=2)

    if parts[0] == "send" and len(parts) == 3:
        mbox_id, content = parts[1], parts[2]
        mailboxes.setdefault(mbox_id, []).append(content)
        server_socket.sendto("OK".encode(), addr)

    elif parts[0] == "receive" and len(parts) == 2:
        mbox_id = parts[1]
        if mbox_id in mailboxes and mailboxes[mbox_id]:
            msg = mailboxes[mbox_id].pop(0)
            server_socket.sendto(msg.encode(), addr)
        else:
            server_socket.sendto("No messages".encode(), addr)

    elif parts[0] == "quit":
        print("👋 서버 종료됨.")
        break

    else:
        server_socket.sendto("Invalid command".encode(), addr)

server_socket.close()
