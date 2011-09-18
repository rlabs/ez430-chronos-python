from socket import *
import serial

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8001
LAUNCHPAD_PORT = '/dev/ttyACM1'
BAUDRATE = 2400

def connect_to_server(ip_addr, port):
        fd = socket(AF_INET, SOCK_STREAM)
        fd.connect((ip_addr, port))
        return fd
       
def launchpad_open(port, baudrate):
        fd = serial.Serial(port, baudrate=baudrate)
        return fd

def mainloop():
        sockfd = connect_to_server(SERVER_IP, SERVER_PORT)
        fd = launchpad_open(LAUNCHPAD_PORT, BAUDRATE)
        while True:
                sockfd.recv(1000)
                fd.write('A')
        

mainloop()


