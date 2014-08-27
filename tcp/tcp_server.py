#!/usr/bin/python

import socket

from tcp_tools import set_name, set_conn, log, pp_host, send, receive

HOST_PAIR = ("127.0.0.1", 2001)

set_name("Server")

try:
    log("Listening on {}.".format(pp_host(HOST_PAIR)))
    conn = None
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.settimeout(3)
    listener.bind(HOST_PAIR)
    listener.listen(1)

    conn, sender = listener.accept()
    set_conn(conn)
    log("Got a connection from {}.".format(pp_host(sender)))
    data = True
    while data and data != "FLAGPLS":
        data = receive()
        if data and data != "FLAGPLS":
            log("Ignoring.")
    if data:
        send("><3>")
        log("Sent the flag.")
    else:
        log("Lost client.")
except socket.error, e:
    log("-!- {}".format(str(e)))
except KeyboardInterrupt:
    log("Killed.")
finally:
    log("Closing socket.")
    if conn:
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
