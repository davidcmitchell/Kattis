import sys

def low_frac(a,b):
    if b == 1:
        return [a,b]
    else:
        hi = max(a,b)
        for i in range(hi,1,-1):
            if b % i == 0 and a % i == 0:
                return low_frac(int(a/i),int(b/i))
        return [a,b]

frac = sys.stdin.readline().rstrip().split("/")
frac = [int(f) for f in frac]
thirtytwo = [32*frac[1],1*frac[1]]
frac[0] = frac[0]-thirtytwo[0]
celc = [frac[0]*5,frac[1]*9]
ans = low_frac(celc[0],celc[1])
print(ans[0],"/",ans[1],sep="")