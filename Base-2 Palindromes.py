import sys

def get_nth_pal(nth):
    if nth == 1:
        return [1]
    count = [1,1]
    total = 2
    i = 2
    while total < nth:
        count.append(count[i-2]*2)
        total += count[-1]
        i += 1
    if total == nth:
        digs = [1]*len(count)
        return digs
    elif len(count) % 2 != 0:
        total = total-count[-1]
        digs = [1] +[0]*(len(count)-2) + [1]
        return get_nth_odd_pal(nth-total,digs)
    else:
        total = total-count[-1]
        digs = [1] +[0]*(len(count)-2) + [1]
        return get_nth_even_pal(nth-total,digs)


def get_nth_odd_pal(nth,digs):
    if nth == 1:
        return digs
    mid = int(len(digs)/2)
    if nth == 2:
        digs[mid] = 1
        return digs
    count = [1]
    total = 2
    i = 1
    while total < nth:
        if (i+1) % 2 == 0:
            count.append(0)
        else:
            count.append(count[i-2]*2)
            total += count[-1]
        i += 1
    dist = int((len(count) - 1) / 2)
    digs[mid + dist] = 1
    digs[mid - dist] = 1
    total = total-count[-1]
    return get_nth_odd_pal(nth-total,digs)



def get_nth_even_pal(nth,digs):
    if nth == 1:
        return digs
    midl = int(len(digs)/2)-1
    midh = int(len(digs)/2)
    if nth == 2:
        digs[midl] = 1
        digs[midh] = 1
        return digs
    count = [0,1]
    total = 2
    i = 2
    while total < nth:
        if (i+1) % 2 != 0:
            count.append(0)
        else:
            count.append(count[i-2]*2)
            total += count[-1]
        i += 1
    dist = int((len(count)) / 2)-1
    digs[midh + dist] = 1
    digs[midl - dist] = 1
    total = total-count[-1]
    return get_nth_even_pal(nth-total,digs)

num = int(sys.stdin.readline())
digs = get_nth_pal(num)
digs = [str(x) for x in digs]
digs = ''.join(digs)
digs = int(digs, 2)
print(digs)

'''
1   1
2   11
3   101
4   111
5   1001
6   1111
7   10001
8   10101
9   11011
10  11111
11  100001
12  101101
13  110011
14  111111
15  1000001
16  1001001
17  1010101
18  1011101
19  1100011
20  1101011
21  1110111
22  1111111
23  10000001
24  10011001

1
1
2
2
4
4

'''