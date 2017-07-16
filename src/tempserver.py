import Queue
import select
import socket
import sys
import threading
from time import gmtime, strftime

HOST = ''
PORT = 12345


def bind(sock):
	try:
		sock.bind((HOST, PORT))
	except socket.error, msg:
		print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()

# Create the socket and make sure to make it reusable and non-blocking
# AF_INET is IPv4 and IIRC SOCK_STREAM is TCP
base = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Make it so that sockets can be reused
base.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# We don't want it blocking
base.setblocking(0)

# Bind the sock
bind(base)

base.listen(5)

# inputs is what's coming into our program
inputs = [base]
outputs = []
# Each connection gets its own message queue
message_queues = {}

while inputs:
	# Select monitors inputs and puts them into three categories
	readable, writable, errors = select.select(inputs, outputs, inputs)

	for sock in readable:
		# The base socket has to keep listening for things that want to connect
		if sock is base:
			# accept the connection
			conn, addr = sock.accept()
			conn.setblocking(0)
			inputs.append(conn)

			message_queues[conn] = Queue.Queue()
		# For incoming information that isn't from the base socket
		else:
			# get the message
			message = sock.recv(4096)
			if message:
				print '(%s)%s' % (strftime("%H:%M:%S", gmtime()), message)
				# print '%s:%s' % (sock.getpeername(), message)
				message_queues[sock].put(message)
				if sock not in outputs:
					outputs.append(sock)

			else:
				if sock in outputs:
					outputs.remove(sock)
				inputs.remove(sock)
				sock.close()

				del message_queues[sock]

	for sock in writable:
		try:
			message = message_queues[sock].get_nowait()
		except Queue.Empty:
			outputs.remove(sock)
		else:
			for s in inputs:
				if s is not base:
					s.send(message)

	for sock in errors:
		print "Error for %s" % (sock)
		inputs.remove(sock)
		if sock in outputs:
			outputs.remove(sock)
		sock.close()

		del message_queues[sock]


