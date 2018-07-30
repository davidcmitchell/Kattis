import sys

def msd_sort(nums,digit):
    #print("On digit",digit)
    #print(nums)
    if len(nums) == 1:
        return True
    bucket = [[] for i in range(10)]
    for word in nums:
        if digit > len(word)-1:
            return False
        else:
            bucket[int(word[digit])].append(word)
    for i in range(10):
        if len(bucket[i]) != 0:
            if not msd_sort(bucket[i],digit+1):
                return False
    return True


nc = int(sys.stdin.readline().rstrip())
for i in range(nc):
    npn = int(sys.stdin.readline().rstrip())
    nums = [];
    for j in range(npn):
        nums.append(sys.stdin.readline().rstrip())
    if msd_sort(nums,0):
        print("YES")
    else:
        print("NO")
