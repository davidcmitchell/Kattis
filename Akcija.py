import sys

num_cases = int(sys.stdin.readline().rstrip())
prices = []

for i in range(num_cases):
    prices.append(int(sys.stdin.readline().rstrip()))
prices = sorted(prices)
cost = 0
group_num = 1
for i in range(len(prices)-1,-1,-1):
    if (group_num == 1 or group_num == 2):
        cost += prices[i]
        group_num += 1
    else:
        group_num = 1
print(cost)
