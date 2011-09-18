# Set PYTHONPATH before running!

from chronoslib import *
from socket import *

SERVER_PORT = 8001

def accept_client():
        fd = socket(AF_INET, SOCK_STREAM)
        fd.bind(('', SERVER_PORT))
        fd.listen(5)
        newfd = fd.accept()
        return newfd[0]

def mainloop():
        fd = port_open()
        start_ap(fd)
        sockfd = accept_client()

        r = get_acc_data(fd)
        while (r == []):
                r = get_acc_data(fd)

        prev_y = r[1]
        while True:
                r = get_acc_data(fd)
                if r: 
                        curr_y = r[1]
                        if zerocrossed_up(prev_y, curr_y):
                                print 'CROSSED!!'
                                sockfd.send('CROSSED')
                        prev_y = curr_y
 
if __name__ == '__main__':
        mainloop()


