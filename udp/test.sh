#!/bin/bash

./udp_server.py &
sleep .1 # avoid race condition where client gets going first
./udp_client.py
