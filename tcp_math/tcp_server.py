#!/usr/bin/python

import socket
import random

from tcp_tools import set_name, set_conn, close_conn, log, pp_host, send, receive

HOST_PAIR = ("127.0.0.1", 2001)

set_name("Server")

try:
    log("Listening on {}.".format(pp_host(HOST_PAIR)))
    conn = None
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(HOST_PAIR)
    listener.listen(1)

    operands = [None, None]
    operands[0] = random.randrange(100)
    operands[1] = random.randrange(100)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = operands[0] + operands[1]
    elif operator == '-':
        answer = operands[0] - operands[1]
    elif operator == '*':
        answer = operands[0] * operands[1]
    else:
        answer = operands[0] / operands[1]
    challenge = "{} {} {}".format(operands[0], operator, operands[1])
    log("Set challenge to '{}' (answer is {}).".format(challenge, answer))

    conn, sender = listener.accept()
    set_conn(conn)
    log("Got a connection from {}.".format(pp_host(sender)))
    send("CHALLENGE {}".format(challenge))
    data = receive()
    if int(data) == answer:
        send("OK")
        data = receive()
        if data == "FLAGPLS":
            send("<3><")
    else:
        send("NO")
except socket.error, e:
    log("-!- {}".format(str(e)))
except KeyboardInterrupt:
    log("Killed.")
finally:
    close_conn()
