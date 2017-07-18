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

	def __init__(self, sock, addr, room, chatRoomHandler):
		# This uses self.sock instead now
		# self.ip = ""
		# self.port = -1
		self.sock = sock
		self.addr = addr
		self.curChat = room # I dont know if this is entirely valid
		self.name = "tempname"
		self.chatRoomHandler = chatRoomHandler
		self.startLoop()
		self.helpMessage = "/help - will provide the possible command | /switch chatroomName - switch to given chatroomName | Chat Rooms Available : General and Random"

	# TODO Changed name of this as well
	def listenForMessageFromIMClient(self):
		while True:
			receive = select.select([self.sock], [], [])
			message = self.sock.recv(4096)
			Thread(target=self.writeMessageToChatRoom, args=(message,)).start()

	def startLoop(self):
		queueHandler = Thread(target=self.listenForMessageFromIMClient, args=()).start()

	# TODO I updated the name of this to be clearer
	def writeMessageToChatRoom(self, messageIn):
		self.newMessage(messageIn, self.name)

	# TODO I updated the name of this as well and it doesn't return anything as well
	def sendMessageUpdateToIMClient(self, newMessage):
		self.sock.send(newMessage)

	def changeChatRoom(self, newRoomName):
		newRoom = self.chatRoomHandler.changeChatRoom(newRoomName, self.curChat.name, self)
		self.curChat = newRoom
		return
	
	def specialMessage(self, message):
		if message[0] is '/':
			return True

	def ignoreFirstWord(self, message):
		return message.split(' ', 1)[1]
		
	def switchCommand(self, message):
		if message.split(" ")[0] == "/switch":
			return True
			
	def helpCommand(self, message):
		if message.split(" ")[0] == "/help":
			return True
	
	def userJoining(self, message):
		if message.split(" ")[0] == "/announce":
			return True

	def newMessage(self, messageIn, clientName):
		''' called by the Client object '''
		newMessage = ""
		if self.specialMessage(messageIn):
			if self.userJoining(messageIn):
				newMessage = clientName + self.ignoreFirstWord(messageIn)
			elif self.switchCommand(messageIn):
				chat = messageIn.split(" ")[1]
				if self.chatRoomHandler.findChatRoom(chat).name == chat:
					self.changeChatRoom(chat)
			elif self.helpCommand(messageIn):
				self.sendMessageUpdateToIMClient(self.helpMessage)
				#send user help specs
		else:
			newMessage = clientName + " : " + messageIn
			self.curChat.messageQueue.put(newMessage)
			print "(%s) %s" % (self.curChat.name, newMessage)

