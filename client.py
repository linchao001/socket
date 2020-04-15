import socket

class SocketClient:

	def __init__(self, *ip_port):
		try:
			self.sk = socket.socket()
			self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.sk.connect(ip_port)
			print('连接成功')
		except Exception as e:
			print('连接失败')
			print(e)

	def client_read_write(self):
		plate_number = '蓝川A124B5'
		self.sk.sendall(bytes(plate_number, encoding='GBK'))
		print("发送成功")
		data = self.sk.recv(1024)
		print('服务端返回数据：{}'.format(data))
		self.sk.close()

if __name__ == '__main__':
	socket_client = SocketClient('127.0.0.1',8888)
	socket_client.client_read_write()