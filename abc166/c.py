def main():
    import sys
    N,M=list(map(int,sys.stdin.readline().split()))
    H=list(map(int,sys.stdin.readline().split()))
    lsts=[[] for _ in range(N)]
    st=set()
    for i in range(M):
        A,B=list(map(int,sys.stdin.readline().split()))
        if (A,B) not in st:
            lsts[A-1].append(H[B-1])
            lsts[B-1].append(H[A-1])
            st.add((A,B))
            
    output=0
    for i,lst in enumerate(lsts):
        if len(lst)==0:
            output+=1
        elif max(lst)<H[i]:
            output+=1
    print(output)


    

main()