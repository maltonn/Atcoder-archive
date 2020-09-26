def main():
    import sys
    from collections import deque

    N,M=list(map(int,sys.stdin.readline().split()))
    dic=[[] for _ in range(100001)]
    sys.setrecursionlimit(100001)
    mark=[0]*N
    for i in range(M):
        A,B=list(map(int,sys.stdin.readline().split()))
        dic[A-1].append(B-1)
        dic[B-1].append(A-1)


    i=0
    count=0
    while True:
        if not mark[i]:
            count+=1
            d=deque()
            d.appendleft(i)
            while d:
                a=d.popleft()
                mark[a]=1
                for j in dic[a]:
                    if mark[j]:
                        continue
                    
                    d.appendleft(j)
        i+=1
        if i==N:
            break
    
    print(count-1)
main()