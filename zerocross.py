from chronoslib import *

def mainloop():
        fd = port_open()
        start_ap(fd)
        r = get_acc_data(fd)
        while (r == []):
                r = get_acc_data(fd)

        prev_y = r[1]
        while True:
                r = get_acc_data(fd)
                if r: 
                        curr_y = r[1]
                        if zerocrossed_down(prev_y, curr_y):
                                print 'CROSSED!!'
                        prev_y = curr_y
 
mainloop()


