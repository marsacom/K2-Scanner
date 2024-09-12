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

def main():
    scan(args.target)

def get_args():
    parser = argparse.ArgumentParser(prog='K2-Scanner', description='An accurate, fast, in depth network scanning tool')

    parser.add_argument('-t', '--target', dest='target', required=True, help='The target IP Address/Addresses...')

    args = parser.parse_args()

    return args

def scan(ip):
    ps = n.PortScanner()
    ps.scan(hosts=ip)

args = get_args()
main()