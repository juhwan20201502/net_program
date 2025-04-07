import socket

while True:
    expr = input("📝 계산식 입력 (또는 q 입력시 종료): ")
    if expr == 'q':
        break
    sock = socket.socket()
    sock.connect(('localhost', 9001))
    sock.send(expr.encode())
    result = sock.recv(1024).decode()
    print("📤 결과:", result)
    sock.close()
