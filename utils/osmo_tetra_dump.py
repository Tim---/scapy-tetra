#!/usr/bin/env python

# This snippet listens to GSMTAP datagrams sent by osmo-tetra and dumps
# dissected packets.
# For more informations on osmo-tetra : http://tetra.osmocom.org/trac/

from scapy.all import *
from scapy_tetra import *
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4729

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    pkt = GSMTAP(data)
    pkt.show()
