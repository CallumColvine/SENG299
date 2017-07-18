from ChatRoom import ChatRoom


class ChatRoomHandler(object):

	def __init__(self):	
		self.chatRoomList = []
		self.initChatRooms()

	def initChatRooms(self):
		self.createChatRoom("General")
		self.createChatRoom("Random")	
		return

	def addClient(self, roomName, clientObj):
		''' Returns the ChatRoom obj so the Client can keep reference to it '''
		room = self.findChatRoom(roomName)
		room.newClient(clientObj)
		return room

	def removeClient(self, roomName, clientObj):
		room = self.findChatRoom(roomName)
		room.removeClient(clientObj)		
		return

	def createChatRoom(self, roomName):
		# Avoid duplicates
		for room in self.chatRoomList:
			if room.name == roomName:
				return
		print "Appending lists"
		tempRoom = ChatRoom(roomName)
		self.chatRoomList.append(tempRoom)
		return

	def findChatRoom(self, roomName):
		for room in self.chatRoomList:
			if room.name == roomName:
				return room
		print "ChatRoomHandler: unable to find specified ChatRoom", roomName
		return None

	def changeChatRoom(self, newRoomName, oldRoomName, clientObj):
		self.removeClient(oldRoomName, clientObj)
		room = self.addClient(newRoomName, clientObj)
		return room

