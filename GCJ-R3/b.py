try:
    f=open('input.txt')
    lines=list(f.readlines())
except:
    pass
from collections import defaultdict
def solve():
    st=set()
    S=[""]*10
    S2=""
    already=set()
    non_zero_cand=set()
    U=int(input())
    L=[0]*10**4
    for i in range(10**4):
        try:
            m,r=lines[i].split()
        except:
            m,r=input().split()
        L[i]=(m,r)
        
    if +[0][0]=="-1":
        L.sort(key=lambda x: x[0])
        
        cands=[set() for _ in range(10)]

        dic=defaultdict(int)

        for m,r in L:#m:1 -> 10 -> 11 -> .. -> 2
            dic[r[0]]+=1
            st=st|set(list(r))

        
        for key,val in sorted(dic.items(),key=lambda x: x[1]):
            S2+=key
        
        f=tuple(st-set(dic.keys()))[0]
        
        return f+S2
    else:
        cands=[set() for _ in range(10)]
        for m,r in L:#m:1 -> 10 -> 11 -> .. -> 2
            if len(m)==len(r):
                cands[int(m[0])].add(r[0])
                cands[9]=cands[9] | set(list(r))

            non_zero_cand.add(r[0])
        
        for i,cand in enumerate(cands):
            if i and i!=9:
                s=tuple(cand-already)[0]
                S[i]=s
                already.add(s)
            elif i==9:
                cand=cand-already
                S[0]=tuple(cand-non_zero_cand)[0]
                S[9]=tuple(cand & non_zero_cand)[0]

                
        return "".join(S)


def main():
    T=int(input())
    for case in range(1,T+1):
         print('Case #{}: {}'.format(case,solve()))

main()
try:
    f.close()
except:
    pass