#!/usr/bin/env python3
# UDP Ping Client

import sys
import socket
import time

cmdargs = str(sys.argv)

server_name = sys.argv[1] # host/server name from command line arguements
server_port = int(sys.argv[2]) # port number from command line arguements
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(0.6)

rtts = []

sequence_num = 3331;
while sequence_num <= 3345:
	# ping 15 times to server and print rtt response
	try:    
		send_time = time.time()
		timestamp = str(send_time)
		# create ping string
		ping = 'PING ' + str(sequence_num) + ' ' + timestamp + ' \r\n'
		client_socket.sendto(ping, (server_name, server_port))
		reply, server_address = client_socket.recvfrom(2048)
		recv_time = time.time()
		time.sleep(0.6)
	# timeout exception
	except socket.timeout:
		sequence_num += 1
		print 'ping to ' + server_name + ', seq = ' + str(sequence_num) + ', time out'
		continue
	# calculate RTT, print server response with RTT
	RTT = round(recv_time - send_time, 3) * 1000
	rtts.append(RTT)
	print 'ping to ' + server_name + ', seq = ' + str(sequence_num) + ', rtt = ' +  str(RTT) + 'ms'
	sequence_num += 1

print 'min/max/avg rtt ' + str(min(rtts)) + 'ms ' + str(max(rtts)) + 'ms ' + str(round(sum(rtts)/len(rtts))) + 'ms'
client_socket.close()
