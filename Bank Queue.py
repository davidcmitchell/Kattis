import sys


line = sys.stdin.readline().split()
nc, max_t = int(line[0]),int(line[1])
custs = {}
for i in range(nc):
    line = sys.stdin.readline().split()
    m,t = int(line[0]),int(line[1])
    custs.setdefault(t,[])
    custs[t].append(m)

amount = 0
for i in range(max_t,-1,-1):
    maxm = 0
    mt = -1
    for j in range(i,max_t+1):
        if j in custs:
            if len(custs[j]) > 0 and max(custs[j]) > maxm:
                maxm = max(custs[j])
                mt = j
    if mt != -1:
        custs[mt].remove(maxm)
    amount += maxm
print(amount)