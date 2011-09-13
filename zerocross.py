from chronoslib import *

def zero_crossed(prev, curr):
        if (prev < 100) and (curr > 200):
                return True
        if (prev > 200) and (curr < 100):
                return True
                

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
                        if zero_crossed(prev_y, curr_y):
                                print 'CROSSED!!'
                        prev_y = curr_y
 
mainloop()

mainloop()

