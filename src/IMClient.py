#!/usr/bin/env python3 

""" Initializes connections with IMServer with initConnection()
These connections are passed on to a Client object which is managed by IMServer  """
import Queue
import select 
import socket 
import sys 
import threading 

class IMClient: 

	def __init__(self):
		self.username = ""
		self.curChatRoom = ""
		self.host = '127.0.0.1' # TODO Update design documents to show this variable
		self.input = Queue() # TODO Update design to make variable equal Queue
		self.port = 12345
		self.sock = None # TODO Update design documents to show this variable
		self.startLoop()

	def initConnection(self):
		# TODO Update document to remove ip from method header
		try: 
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# socket.AF_INET IPV4 and socket.SOCK_STREAM is TCP
		except socket.error, msg: 
			print 'Failed to create socket: ' + str(msg[1])
		try: 
			remote_ip = socket.gethostbyname(self.host)
		except socket.gaierror:
			print 'Hosetname could not be resolved. Exiting'
			return False
		s.connect((remote_ip, self.port))

		print 'Socket Connected to ' + self.host #+ ' on ip ' + remote_ip
		return True
	
	def updateChat(self, newMessage):
		raise NotImplementedError 
	
	def listenForInput(self):
		input.put(raw_input("> "))
	
	def sendInput(self):
		# TODO Update method header
		try: 
			self.sock.sendall(self.username + ':' + self.input.get())
		except socket.error:
			print 'Send failed'
		return true
	
	def startLoop(self):
		queueHandler = threading._start_new_thread(mainLoop, ())
		return
	
	def mainLoop(self):
		while True:
			# message = str(raw_input("Type something: "))
			# send_message(message, sock)
			if self.input.empty() is not True:
				# global input, message_ready
				listener = threading._start_new_thread(get_input, ())
				sendInput()
			receive = select.select([sock], [], [], 0.005)
			# Only check the rlist
			if receive[0]:
				message = sock.recv(4096) # TODO update this
				print message



















