'''Use python-nmap library to scan ports and find closed ones, then manually use python to restart them'''
import nmap
import socket
import socketserver
from server import MyTCPSocketHandler

nmscan = nmap.PortScanner()

nmscan.scan('127.0.0.1', '9999')

def port_scanner():
    '''scan for open or closed ports'''
    for host in nmscan.all_hosts():
        print("-"*60)
        print('Host: %s (%s)' % (host, nmscan[host].hostname()))
        print('State: %s' % (nmscan[host].state()))

        for proto in nmscan[host].all_protocols():
            print("-"*60)
            print('Protocol : %s' % proto)
            print("-"*60)

            lport = nmscan[host][proto].keys()
            lport = list(lport)
            lport.sort()

            for port in lport:
                state_of_port = nmscan[host][proto][port]['state']
                print('port: %s \tstate: %s\t\t' %(port, state_of_port))
    return state_of_port

def open_closed_server(state_of_port):
    '''Open closed server'''
    if state_of_port == 'closed':
        print('\n\nRestarting port...')

        HOST, PORT = "localhost", 9999

        print("-"*60)
        print('\n\nport: %d successfully restarted' %PORT)

        server = socketserver.TCPServer((HOST, PORT), MyTCPSocketHandler)
        server.serve_forever()

state_of_port = port_scanner()
open_closed_server(state_of_port)
port_scanner()