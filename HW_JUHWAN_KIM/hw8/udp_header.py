# udp_header.py
import struct

class Udphdr:
    def __init__(self, srcPort, dstPort, length, checksum):
        self.srcPort = srcPort
        self.dstPort = dstPort
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        print(" [PACKING] UDP 헤더 생성 중...")
        return struct.pack('!HHHH', self.srcPort, self.dstPort, self.length, self.checksum)

    def unpack_Udphdr(self, rawData):
        print("\n [UNPACKING] 수신된 UDP 헤더 해석")
        fields = struct.unpack('!HHHH', rawData)
        self.srcPort, self.dstPort, self.length, self.checksum = fields

    def getSrcPort(self):
        return self.srcPort

    def getDstPort(self):
        return self.dstPort

    def getLength(self):
        return self.length

    def getChecksum(self):
        return self.checksum

# 테스트 실행
udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed = udp.pack_Udphdr()
print("📨 패킹된 결과 (16진수):", packed.hex())

udp.unpack_Udphdr(packed)
print("Source Port     :", udp.getSrcPort())
print("Destination Port:", udp.getDstPort())
print("Length          :", udp.getLength())
print("Checksum        :", hex(udp.getChecksum()))
