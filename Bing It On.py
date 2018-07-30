import sys

nc = int(sys.stdin.readline().rstrip())
words = {}
for i in range(nc):
    word = sys.stdin.readline().rstrip()
    if word in words:
        print(words[word])
    else:
        print(0)
    for j in range(1,len(word)+1):
        add_word = word[:j]
        if add_word not in words:
            words[add_word] = 1
        else:
            words[add_word] += 1
