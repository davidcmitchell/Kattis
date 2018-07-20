import math, sys

def count_anagrams(word):
    word_list = list(word)
    word_set = set(word_list)
    anagrams = math.factorial(len(word))
    divisor = 1
    for letter in word_set:
        divisor = divisor*math.factorial(word_list.count(letter))
    print(int(anagrams//divisor))

for line in sys.stdin.readlines():
    word = line.rstrip()
    count_anagrams(word)
