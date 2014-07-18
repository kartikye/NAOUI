import socket
import sys
import os
import threading

import proxy
import posture
import datacontroller

server_address = '/tmp/socket'

#MAIN METHOD

try:
	os.unlink(server_address)
except OSError:
	if os.path.exists(server_address):
		raise
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print >>sys.stderr, 'starting up on %s' % server_address
sock.bind(server_address)

sock.listen(1)

threads = []

while True:
	# Wait for a connection
	#print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()
	try:
		#print >>sys.stderr, 'connection from', client_address
		while True:
			data = connection.recv(16)
			print >>sys.stderr, '%s' % data
			if data:
				dataShort = data[:3]
				if len(data) > 3:
					dataContent = data[3:]
				
				print >>sys.stderr, 'received "%s"' % data
				
				if len(data) > 3:
					t = threading.Thread(target=datacontroller.dataController, args=(dataShort,dataContent))
				else:
					t = threading.Thread(target=datacontroller.dataController, args=(dataShort,""))	
				
				t.start()
				print >>sys.stderr, 'starting thread'

				threads.append(t)

				break
				#connection.sendall(dataShort)
	      
	finally:
        # Clean up the connection
		connection.close()
		