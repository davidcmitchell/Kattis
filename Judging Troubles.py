import sys

nc = int(sys.stdin.readline().rstrip())
counts1 = {}
for i in range(nc):
    result = sys.stdin.readline().rstrip()
    if result in counts1:
        counts1[result] += 1
    else:
        counts1[result] = 1

counts2 = {}
for i in range(nc):
    result = sys.stdin.readline().rstrip()
    if result in counts2:
        counts2[result] += 1
    else:
        counts2[result] = 1

max_corr = 0
for i in counts1:
    if i in counts2:
        max_corr += min(counts1[i],counts2[i])

print(max_corr)