from typing import Deque


def main():
    import sys
    from bisect import bisect_right
    from collections import deque
    N,T=list(map(int,sys.stdin.readline().split()))
    L=list(map(int,sys.stdin.readline().split()))
    
    A=L[:N//2]
    B=L[N//2:]
    AS=set()
    BS=set()

    deqA=deque()
    deqB=Deque()

    deqA.appendleft((0,0))
    deqB.appendleft((0,0))
    
    while deqA:
        i,total=deqA.popleft()
        if i<N//2:
            deqA.appendleft((i+1,total+A[i]))
            deqA.appendleft((i+1,total))
        else:
            AS.add(total)
    
    while deqB:
        i,total=deqB.popleft()
        if i<N-N//2:
            deqB.appendleft((i+1,total+B[i]))
            deqB.appendleft((i+1,total))
        else:
            BS.add(total)
    

    BL=sorted(BS)
    mx=0
    for a in AS:
        idx=bisect_right(BL,T-a)
        if idx!=0:
            mx=max(mx,a+BL[idx-1])

    print(mx)

if __name__ == "__main__":
    main()