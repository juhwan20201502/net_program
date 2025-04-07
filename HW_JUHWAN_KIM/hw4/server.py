import socket

def calculate(expression):
    try:
        expression = expression.replace(" ", "")
        if '+' in expression:
            a, b = expression.split('+')
            result = int(a) + int(b)
        elif '-' in expression:
            a, b = expression.split('-')
            result = int(a) - int(b)
        elif '*' in expression:
            a, b = expression.split('*')
            result = int(a) * int(b)
        elif '/' in expression:
            a, b = expression.split('/')
            result = round(int(a) / int(b), 1)
        else:
            return "Unsupported operation."
        return str(result)
    except:
        return "Error"

s = socket.socket()
s.bind(('', 9001))
s.listen(1)
print("✅ 서버 실행 중...")

while True:
    client, addr = s.accept()
    print("📡 연결됨:", addr)
    expr = client.recv(1024).decode()
    if expr == 'q':
        print("❌ 클라이언트 종료 요청")
        client.close()
        continue
    result = calculate(expr)
    print(f"📥 수신한 식: {expr} ➡ 결과: {result}")
    client.send(result.encode())
    client.close()
