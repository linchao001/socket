import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import configparser
import os
import time
from tkinter import ttk
from datetime import datetime
import tkinter.font as tkFont
import operator

from server import SocketServer
import socket
from threading import Thread

class StrFindGUI:

	def __init__(self):
		'类的构造函数 主要用于绘制应用程序的界面'
		
		self.root = Tk()
		self.root.title(u"数据解析工具")
		self.root.geometry('800x600')
		self.root.resizable(FALSE,FALSE)


		self.search_button_01 = Button(self.root, text=u"启动socket server", padx=3, pady=6,width=15,cursor='hand2',command=self.paass)
		self.search_button_01.grid(row=1,column=10,sticky=W)

		self.search_button_02 = Button(self.root, text=u"退出socket server", padx=3, pady=6,width=15,cursor='hand2',command=self.close)
		self.search_button_02.grid(row=1,column=50,sticky=W)


		self.data = ScrolledText(self.root,width=110,height=15)
		self.data.grid(row=2,column=0,columnspan=200)

		self.result = ScrolledText(self.root,width=110,height=22,spacing1=3)
		self.result.grid(row=4,columnspan=200)


		self.root.mainloop()

	def paass(self):
		getini = GetINI()
		getini.Read('socket.ini')
		ip = getini.Get('ip_port', 'ip')
		port = getini.Get('ip_port', 'port')
		port = int(port)
		self.socket_server = SocketServer(ip,port)
		self.result.insert(END,'server启动\n\n')
		self.result.insert(END,'{}、{}\n\n'.format(ip,port))
		t1 = Thread(target = self.server_read_write)
		#t1 = subThread(self.server_read_write,())
		t1.start()
		

	def close(self):
		self.socket_server.close()
		self.result.insert(END,'退出成功！！！\n\n\n')




	def server_read_write(self):
		while 1:
			conn,addr = self.socket_server.sk.accept()
			#print('客户端{}连接成功，开始通讯...'.format(addr))
			data = conn.recv(1024)
			#a_str,size = struct.unpack('15sq', data)
			#print('接收数据：{}'.format(data.decode(encoding='GBK').strip('\x00')))
			self.result.insert(END,'客户端{}连接成功，开始通讯...\n\n'.format(addr))
			self.result.insert(END,'接收数据：{}\n\n'.format(data.decode(encoding='GBK').strip('\x00')))
			conn.sendall(b'It is OK')

		
		
	











class GetINI:
	'提供读写ini类型文件和读取值得一些方法'
	def __init__(self):
		'实例化ConfigParser()对象'
		self.conf = configparser.ConfigParser()

	def Read(self, inifilename):
		'读取ini文件'
		#self.conf.read(inifilename)
		self.conf.read(inifilename,encoding="utf-8-sig")
		#self.conf.read(inifilename,encoding="ANSI")

	#获取ini文件内所有的section，以列表形式返回['path', 'keyword']
	def GetSections(self):
		return self.conf.sections()

	#'获取指定section下所有options ，以列表形式返回['Keyword_1', 'Keyword_2']'
	def GetOptions(self,section):	
		return self.conf.options(section)

	#'获取指定section下所有的键值对，以元祖列表形式返回[('Keyword_1', 'F_PAN'), ('Keyword_2', 'F_VALIDDATE')]'
	def GetItems(self,section):	
		return self.conf.items(section)

	#'获取指定section中option的值，返回为string类型'
	def Get(self,section,option):
		return self.conf.get(section,option)

	#判断是否存在指定section
	def HasSection(self,section):
		return self.conf.has_section(section)


	#删除指定section
	def DelSection(self,section):
		self.conf.remove_section(section)

	#删除指定section下的option
	def DelOption(self,section,option):
		self.conf.remove_section(section,option)

	#增加指定section
	def AddSection(self,section):
		self.conf.add_section(section)

	#增加指定section下的key和value
	def AddOption(self,section,key,value):
		self.conf.set(section,key,value)

	#写指令，对配置文件进行修改后，一定要执行写指令
	def Write(self,inifilename):
		with open(inifilename,'w') as configfile:
			self.conf.write(configfile)


#创建一个类，继承自Thread对象
class subThread(Thread):
	#重载构造函数
	def __init__(self,func,args):
		#调用基类的构造函数，必要的一步
		Thread.__init__(self)
		self.func = func
		self.args = args

	#重载Thread.run()方法
	def run(self):
		#带一个*号的参数，代表可以收集位置参数
		#若是带两个*号的参数，代表可以收集关键字参数
		self.func(*self.args)



def main():
	show=StrFindGUI()


if __name__ == '__main__':
	if os.path.exists('Sensitive_log_01.txt'):
		os.remove('Sensitive_log_01.txt')
	if os.path.exists('Sensitive_log_02.txt'):
		os.remove('Sensitive_log_02.txt')
	main()
