import math, sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num))+1,1):
        if num % i == 0:
            return False
    return True


def get_permutations(curr_perm,rem_nums,all_perms):
    all_perms.append(''.join(curr_perm))
    if len(rem_nums) == 0:
        return
    for i in range(len(rem_nums)):
        curr_perm.append(rem_nums.pop(i))
        get_permutations(curr_perm,rem_nums,all_perms)
        rem_nums.insert(i,curr_perm.pop(-1))

def count_primes(num):
    all_perms = []
    get_permutations([],list(num), all_perms)
    all_perms.remove('')
    all_perms = [int(x) for x in all_perms]
    all_perms = set(all_perms)
    count = 0
    for num in all_perms:
        if is_prime(num):
            count += 1
    return count


num_cases = int(sys.stdin.readline().rstrip())
for i in range(num_cases):
    num = sys.stdin.readline().rstrip()
    print(count_primes(num))





