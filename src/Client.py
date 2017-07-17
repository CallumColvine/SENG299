import ChatRoom
import select
# import threading
from threading import Thread
from time import gmtime, strftime

# One-to-one relationship with IMClients
# Constantly listening for new messages broadcast by the IMClient
# 	Calls its writeMessage() function when a new message is received 
# 	writeMessage() calls the ChatRoom.newMessage() function
class Client:

	def __init__(self, sock, addr, room):
		# This uses self.sock instead now
		# self.ip = ""
		# self.port = -1
		self.sock = sock
		self.addr = addr
		self.curChat = room # I dont know if this is entirely valid
		self.name = "tempname"
		self.startLoop()

	# TODO Changed name of this as well
	def listenForMessageFromIMClient(self):
		while True:
			receive = select.select([self.sock], [], [])
			message = self.sock.recv(4096)
			print "msg received"
			Thread(target=self.writeMessageToChatRoom, args=(message,)).start()
			# threading._start_new_thread(self.writeMessageToChatRoom, (message,))


	def startLoop(self):
		# queueHandler = threading._start_new_thread(self.listenForMessageFromIMClient(), ())
		queueHandler = Thread(target=self.listenForMessageFromIMClient, args=()).start()


	# TODO I updated the name of this to be clearer
	def writeMessageToChatRoom(self, messageIn):
		self.curChat.newMessage(messageIn, self.name)

	# TODO I updated the name of this as well and it doesn't return anything as well
	def sendMessageUpdateToIMClient(self, newMessage):
		self.sock.send(newMessage)
