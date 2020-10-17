def main():
    import sys
    N=int(sys.stdin.readline())
    first_N=N
    m=2
    L=[]
    import itertools
    while True:
        if N%m==0:
            while N%m==0:
                N//=m
                L.append(m)
        m+=1
        if m==first_N:
            break
        
    st=set()
    output=[]
    for pat in itertools.product([0,1], repeat=len(L)):
        res=1
        for p,bit in zip(L,pat):
            if bit:
                res*=p
        if res not in  st:
            output.append(res)
            st.add(res)

    output.sort()
    for r in output:
        print(r)

main()