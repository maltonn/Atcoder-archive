def main():
    import sys
    import math
    from collections import Counter
    N=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    A.sort()

    A_counter=Counter(A)

    L=[]
    count=0
    for a in A:
        if a==0:
            continue
        flag=True
        for s in L:
            if a%s==0:
                flag=False
                break
        if flag:
            L.append(a)
            if A_counter[a]==1:
                count+=1
    
    print(count)

main()