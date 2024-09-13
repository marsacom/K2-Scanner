# K2 - Scanner 
# V.1.0.0
# Author : Brayden Kukla

import os
import sys
import socket
import datetime
import argparse
import requests
import threading
import nmap as n 
import subprocess

#Define the needed vars
ps = n.PortScanner()

def main():
    scan(args.target)
    print(args.target)

def get_args():
    parser = argparse.ArgumentParser(prog='K2-Scanner', description='An accurate, fast, in depth network scanning tool')

    parser.add_argument('-t', '--target', dest='target', required=True, help='The target IP Address/Addresses...')

    args = parser.parse_args()

    return args

def scan(ip):
    ps.scan(ip, sudo=True)

    # Print out results
    for host in ps.all_hosts():
        print("Host: ", host)
        print("State: ", ps[host].state())
        for protocol in ps[host].all_protocols():
            print("Protocol: ", protocol)
            ports = ps[host][protocol].keys()
            for port in ports:
                print("Port: ", port, "State: ", ps[host][protocol][port]['state'])

args = get_args()
main()