def main():
    import sys
    from collections import deque
    from bisect import bisect_left
    N,A=list(map(int,sys.stdin.readline().split()))
    S=list(sys.stdin.readline().strip())
    revs=[]
    for i,s in enumerate(S):
        if s=='#':
            revs.append(i+1)

    
    tmp=bisect_left(revs,A)
    lefts=deque(reversed(revs[:tmp]))
    rights=deque(revs[tmp:])

    
    res=0
    now=A
    for i in range(max(len(lefts),len(rights))):
        if rights:
            res+=rights[0]-now
            now=rights[0]
            rights.popleft()
        else:
            if lefts:
                res+=len(S)+1-now
                now=len(S)+1
            else:
                break
        
    
        if lefts:
            res+=now-lefts[0]
            now=lefts[0]
            lefts.popleft()        
        else:
            if rights:
                res+=now-0
                now=0
            else:
                break
            

    print(res)

if __name__=='__main__':
    main()