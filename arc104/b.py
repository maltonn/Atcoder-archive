def main():
    import sys
    N,S=sys.stdin.readline().strip().split()
    dic={
        'A':0,
        'T':1,
        'G':2,
        'C':3,
    }
    L=[dic[x] for x in S]
    N=int(N)

    count=0
    for i in range(N):
        lst=[0]*4
        for j in range(i,N):
            lst[L[j]]+=1
            if lst[0]==lst[1] and lst[2]==lst[3]:
                count+=1

    print(count)
    
main()