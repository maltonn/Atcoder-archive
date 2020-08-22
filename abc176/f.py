def main():#WA
    from collections import deque,Counter
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    A=deque(A)
    print(A)
    score=0
    for _ in range(N-1):
        lst=[0]*5
        for i in range(5):
            lst[i]=A.popleft()
        
        flag=False
        C=Counter(lst)
        for key,val in C.items():
            if val==3:
                score+=1
                for a in lst:
                    if a!=key:
                        A.appendleft(a)
                flag=True
                break
        
        if not flag:
            k1=0
            for a in A:
                if a in C:
                    C[a]+=1
                    if C[a]==3:
                        k1=a
                        break
                    
            if k1 and lst.count(k1)==2:
                A.appendleft(k1)
                A.appendleft(k1)#2ついれる

            elif k1:
                A.appendleft(k1)
                for a in C:
                    if C[a]==2:
                        C[a]=1
                
                k2=0
                for a in A:
                    if a in C:
                        C[a]+=1
                        if C[a]==3 and a!=k1:
                            k2=a
                            break
                if k2:
                    A.appendleft(k2)
                else:
                    A.appendleft(lst[0])       
                    
            else:
                A.extend(lst[:2])
        print(A)


    if A[0]==A[1]==A[2]:
        print(score+1)
    else:
        print(score)

main()