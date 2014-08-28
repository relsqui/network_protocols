#!/usr/bin/python

import socket

from tcp_tools import set_name, set_conn, close_conn, log, pp_host, send, receive

HOST_PAIR = ("127.0.0.1", 2005)
PASSWORDS = ["red", "blue", "gray", "purple", "elephant", "monkey", "lion",
             "tiger", "bear", "password", "hunter", "dog", "cat", "swordfish"]

set_name("Client")

try:
    for password in PASSWORDS:
        log("Connecting on {}.".format(pp_host(HOST_PAIR)))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        set_conn(sock)
        sock.connect(HOST_PAIR)
        data = receive()
        if data == "PASSWORDPLS":
            send(password)
            data = receive()
            if data == "OK":
                send("FLAGPLS")
                data = receive()
                if data:
                    log("Got the flag!")
                    break
        close_conn()
except socket.error, e:
    log("-!- {}".format(str(e)))
except KeyboardInterrupt:
    log("Killed.")
finally:
    close_conn()
