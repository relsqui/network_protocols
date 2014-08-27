#!/bin/bash

./tcp_server.py &
sleep .1 # avoid race condition where client gets going first
./tcp_client.py
