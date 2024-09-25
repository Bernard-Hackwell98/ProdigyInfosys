#!/bin/bash

if ! command -v tcpdump &> /dev/null
then
    echo "tcpdump not found, install it first"
    exit
fi

interface = "eth0"

echo "Starting Tcpdump on $interface"
sudo tcpdump -i $interface -n -c 10 | while read -r line; do
    echo "______________________________________________________"
    echo "Packet: $line"

    source_ip = $(echo $line | awk '{print$3}' | cut -d'.' -f1-4)
    dest_ip = $(echo $line| awk '{print$5}' | cut -d'.' -f1-4)
    protocol = $(echo $line | awk '{print$2}')


    echo "Source IP address is: $source_ip"
    echo "Destanation IP address is: $dest_ip"
    echo "The protocol is: $protocol"

done