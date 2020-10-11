def main():
    import heapq
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    mn=min(A)
    A=[mn+x%mn for x in A]
    A=[-x for x in list(set(A))]

    heapq.heapify(A)
    while True:
        p=heapq.heappop(A)
        p*=-1
        if p==mn:
            print(mn)
            break

        heapq.heappush(A,-(p%mn))
        if p%mn<mn:
            mn=p-mn

        
        
    

main()