import socket
import struct

class SocketServer:

	def __init__(self,*ip_port):
		try:
			self.sk =  socket.socket()
			self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.sk.bind(ip_port)
			self.sk.listen()
			self.a =1
			#print("socket server启动成功，等待客户端连接...")
			
		except Exception as e:
			print(e)

	def server_read_write(self):
		while True:
			conn,addr = self.sk.accept()
			print('客户端{}连接成功，开始通讯...'.format(addr))
			data = conn.recv(1024)
			#a_str,size = struct.unpack('15sq', data)
			print('接收数据：{}'.format(data.decode(encoding='GBK').strip('\x00')))
			conn.sendall(b'It is OK')

	def close(self):
		self.sk.close()

if __name__ == '__main__':
	socket_server = SocketServer('127.0.0.1',8888)
	socket_server.server_read_write()
	socket_server.sk.close()


