def main():
    import sys
    from collections import deque
    deq=deque()

    N,M=list(map(int,sys.stdin.readline().split()))
    dic={}
    for i in range(M):
        A,B=list(map(int,sys.stdin.readline().split()))
        if A in dic:
            dic[A].append(B)
        else:
            dic[A]=[B]
        
        if B in dic:
            dic[B].append(A)
        else:
            dic[B]=[A]
        
    K=int(sys.stdin.readline())
    C=list(map(int,sys.stdin.readline().split()))
    Cst=set(C)

    for start in C:
        deq.append((start,))
        while deq:
            tup=deq.popleft()
            for nxt in dic[tup[-1]]:
                
                deq.append(tup+(nxt,))



if __name__ == "__main__":
    main()