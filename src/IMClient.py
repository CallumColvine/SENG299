#!/usr/bin/env python3 

""" Initializes connections with IMServer with initConnection()
These connections are passed on to a Client object which is managed by IMServer  """
import select
import socket
import sys 
from Queue import Queue
from threading import Thread

class IMClient: 

	def __init__(self):
		self.username = ""
		self.curChatRoom = ""
		self.host = '127.0.0.1' # TODO Update design documents to show this variable
		self.input = Queue() # TODO Update design to make variable equal Queue
		self.port = 12345
		self.sock = None # TODO Update design documents to show this variable
		self.initConnection()
		self.startLoop()

	def initConnection(self):
		# TODO Update document to remove ip from method header
		try: 
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# socket.AF_INET is IPV4 and socket.SOCK_STREAM is TCP
		except socket.error, msg: 
			print 'Failed to create socket: ' + str(msg[1])
		try: 
			remote_ip = socket.gethostbyname(self.host)
		except socket.gaierror:
			print 'Hostname could not be resolved. Exiting'
			return False
		self.sock.connect((remote_ip, self.port))

		print 'Socket Connected to ' + self.host #+ ' on ip ' + remote_ip
		return True
	
	def updateChat(self, newMessage):
		print newMessage
	
	def listenForInput(self):
		while True:
			input = raw_input("> ")
			self.input.put(input)
	
	def sendInput(self):
		# TODO Update method header
		try: 
			self.sock.sendall(self.username + ':' + self.input.get())
		except socket.error:
			print 'Send failed'
			return False
		return True

	def startLoop(self):
		# queueHandler = threading._start_new_thread(self.mainLoop, ())
		Thread(target=self.mainLoop).start()
		# test = threading._start_new_thread(self.listenForInput(), ())
		Thread(target=self.listenForInput).start()

	def mainLoop(self):
		while True:
			# message = str(raw_input("Type something: "))
			# send_message(message, sock)
			if self.input.empty() is not True:
				# global input, message_ready
				# listener = threading._start_new_thread(self.listenForInput(), ())

				self.sendInput()
			receive = select.select([self.sock], [], [], 0.005)
			# Only check the rlist
			if receive[0]:
				message = self.sock.recv(4096) # TODO update this
				updateChat(message)

if __name__ == "__main__":
	IMClient()