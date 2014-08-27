#!/usr/bin/python

import socket
import time

BUF_SIZE = 1024
NAME = ""
CONN = None

def set_name(name):
    global NAME
    NAME = name

def set_conn(conn):
    global CONN
    CONN = conn

def log(message):
    print "[{}] {}".format(NAME, message)

def pp_host(host_pair):
    return ":".join(map(str, host_pair))

def send(data):
    if CONN:
        log("Sending: {}".format(data))
        CONN.send(data)
    else:
        log("Not sending ({}) because I have no connection.".format(data))

def receive():
    if CONN:
        try:
            data = CONN.recv(BUF_SIZE)
            if data:
                log("Received: {}".format(data))
                return data
            else:
                raise socket.timeout
        except socket.timeout:
            log("Timed out waiting to receive.")
            return ""
    log("Not trying to receive, because I have no connection.")
    return None
