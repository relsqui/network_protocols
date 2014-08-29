#!/usr/bin/python

import socket

from tcp_tools import set_name, set_conn, close_conn, log, pp_host, send, receive

HOST_PAIR = ("127.0.0.1", 2001)

set_name("Client")

try:
    log("Connecting on {}.".format(pp_host(HOST_PAIR)))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    set_conn(sock)
    sock.connect(HOST_PAIR)
    data = receive()
    if data.startswith("CHALLENGE"):
        operands = [None, None]
        challenge, operands[0], operator, operands[1] = data.split()
        operands = map(int, operands)
        if operator == '+':
            answer = operands[0] + operands[1]
        elif operator == '-':
            answer = operands[0] - operands[1]
        elif operator == '*':
            answer = operands[0] * operands[1]
        else:
            answer = operands[0] / operands[1]
        send(answer)
        data = receive()
        if data == "OK":
            send("FLAGPLS")
            data = receive()
            if data:
                log("Got the flag!")
    close_conn()
except socket.error, e:
    log("-!- {}".format(str(e)))
except KeyboardInterrupt:
    log("Killed.")
finally:
    close_conn()
