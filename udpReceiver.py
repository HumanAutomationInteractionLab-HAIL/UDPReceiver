from enum import Enum

import struct
import socket

class MessageType(Enum):
	TIMESTAMP = 0x01

host = '127.0.0.1'
port = 1234

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((host, port))

print('Listening...')
while True:
	data, addr = serverSock.recvfrom(1024)

	messageType = data[0]
	payload = data[1:]

	if messageType == MessageType.TIMESTAMP.value:
		timestamp = struct.unpack('>q', payload)[0]
		print('Received timestamp:', timestamp)
	else:
		print('UNRECOGNIZED MESSAGE TYPE:', messageType, payload)
