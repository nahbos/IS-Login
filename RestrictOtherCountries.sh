#!/bin/bash

filename='cidr-IR.txt'


while read p; do 
    if [[ $p != '#'* ]]
    then
	iptables -A INPUT -p tcp -s $p --dport 80 -j ACCEPT
    fi
done < $filename

iptables -A INPUT -p tcp --dport 80 -j REJECT

iptables -nL


