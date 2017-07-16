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
		self.input = ""
		self.port = 12345
		self.sock = None # TODO Update design documents to show this variable

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
			sys.exit()
		s.connect((remote_ip, self.port))

		print 'Socket Connected to ' + self.host #+ ' on ip ' + remote_ip
	
	def updateChat(self, newMessage):
		raise NotImplementedError 
	
	def listenForInput(self):
		message_ready = False 
		input, message_ready 
		input = raw_input("> ")
		message_ready = True
	
	def sendInput(self, messtoSend):
		try: 
			self.sock.sendall(self.username + ':' + messtoSend)
		except socket.error:
			print 'Send failed'
		return true




















