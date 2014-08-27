#!/usr/bin/python

import socket

BUF_SIZE = 1024
NAME = ""

def set_name(name):
    global NAME
    NAME = name

def log(message):
    print "[{}] {}".format(NAME, message)

def pp_host(host_pair):
    return ":".join(map(str, host_pair))

def send(data, dest):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    log(" ".join(["Sending to", pp_host(dest), "--", data]))
    sock.sendto(data, dest)
    sock.close()

def receive(sock):
    data, sender = sock.recvfrom(BUF_SIZE)
    log(" ".join(["Received from", pp_host(sender), "--", data]))
    return data, sender
