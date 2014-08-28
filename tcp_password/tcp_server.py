#!/usr/bin/python

import socket
import random

from tcp_tools import set_name, set_conn, close_conn, log, pp_host, send, receive

HOST_PAIR = ("127.0.0.1", 2005)
PASSWORDS = ["red", "blue", "gray", "purple", "elephant", "monkey", "lion",
             "tiger", "bear", "password", "hunter", "dog", "cat", "swordfish"]

set_name("Server")

try:
    log("Listening on {}.".format(pp_host(HOST_PAIR)))
    conn = None
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.settimeout(3)
    listener.bind(HOST_PAIR)
    listener.listen(1)

    password = random.choice(PASSWORDS)
    log("Set password to '{}'.".format(password))

    while True:
        conn, sender = listener.accept()
        set_conn(conn)
        log("Got a connection from {}.".format(pp_host(sender)))
        send("PASSWORDPLS")
        data = receive()
        if data == password:
            send("OK")
            data = receive()
            if data == "FLAGPLS":
                send("<3><")
        else:
            send("BAD PASSWORD")
        close_conn()
except socket.error, e:
    log("-!- {}".format(str(e)))
except KeyboardInterrupt:
    log("Killed.")
finally:
    close_conn()
