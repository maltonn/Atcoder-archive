def main():
    import sys
    N,K=list(map(int,sys.stdin.readline().split()))
    P=list(map(int,sys.stdin.readline().split()))
    C=list(map(int,sys.stdin.readline().split()))

    output=-10**20

    lst=[[0]*(N+1) for _ in range(N)]
    for i in range(N):
        st=set()
        now=i
        count=0
        score=0
        if K==1:
            output=max(output,C[P[i]-1])
            continue

        while True:
            count+=1
            now=P[now]-1

            if now in st:
                count-=1
                break
    
            lst[i][count]=lst[i][count-1]+C[now]
            st.add(now)
            
            if count==K:
                break


        if lst[i][count]>0:
            m=max(lst[i][1:count+1])
            
            if K%count:
                p=max(lst[i][1:K%count+1])
                if p>0:
                    s=lst[i][count]*(K//count)+p
                else:
                    s=lst[i][count]*(K//count-1)+m
            else:
                s=lst[i][count]*(K//count-1)+m
        else:
            s=max(lst[i][1:count+1])
        
        output=max(output,s)

    print(output)

main()