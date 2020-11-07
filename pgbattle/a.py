def main():
    import sys
    N=int(sys.stdin.readline())
    lst=[0]*N
    for i in range(N-1):
        a,b=list(map(int,sys.stdin.readline().split()))
        lst[a-1]+=1
        lst[b-1]+=1
            
    res=0
    for c in lst:
        if c==1:
            res+=1
    if lst[0]==1:
        res-=1
    
    print(res)

main()