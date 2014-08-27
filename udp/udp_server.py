#!/usr/bin/python

import socket

from udp_tools import set_name, log, pp_host, send, receive

SEND_PAIR = ("127.0.0.1", 2012)
RECV_PAIR = ("127.0.0.1", 2011)

set_name("Server")

try:
    log("Listening on {}.".format(pp_host(RECV_PAIR)))
    listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener.bind(RECV_PAIR)
    data = ""
    while data != "FLAGPLS":
        data, sender = receive(listener)
        if data != "FLAGPLS":
            log("Ignoring.")
    send("><3>", SEND_PAIR)
    log("Sent the flag.")
except socket.error, e:
    log("Couldn't bind socket: {}".format(str(e)))
except KeyboardInterrupt:
    log("Killed.")
finally:
    log("Closing socket.")
    listener.close()
