import sys

def find_min(num_printers,printed_statues,curr_days, num_statues):
    global curr_min
    if (curr_days+1) >= curr_min:
        return
    if (num_printers+printed_statues) >= num_statues:
        curr_min = curr_days+1
        return
    find_min(num_printers+num_printers,printed_statues,curr_days+1,num_statues)
    find_min(num_printers,printed_statues+num_printers,curr_days+1,num_statues)

num_statues = int(sys.stdin.readline().rstrip())
#num_statues = 5
curr_min = num_statues
find_min(1,0,0, num_statues)
print(curr_min)