#!/usr/bin/python

import socket

from udp_tools import set_name, log, pp_host, send, receive

SEND_PAIR = ("127.0.0.1", 2011)
RECV_PAIR = ("127.0.0.1", 2012)

set_name("Client")

try:
    log("Listening on {}.".format(pp_host(RECV_PAIR)))
    listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener.bind(RECV_PAIR)
    send("Hi!", SEND_PAIR)
    send("FLAGPLS", SEND_PAIR)
    data = ""
    while not data:
        data, sender = receive(listener)
    log("Got the flag!")
except socket.error, e:
    log("Couldn't bind socket: {}".format(str(e)))
except KeyboardInterrupt:
    log("Killed.")
finally:
    log("Closing socket.")
    listener.close()
