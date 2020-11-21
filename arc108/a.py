def main():
    import sys
    import math

    S,P=list(map(int,sys.stdin.readline().split()))
    B=-S
    C=P

    st=set()
    for i in range(10**6+1):
        st.add(i**2)
    
    t=int(math.sqrt(B**2-4*C))
    if B**2-4*C in st or B**2-4*C in [t**2,(t-1)**2,(t-2)**2,(t+1)**2,(t+2)**2]:
        print('Yes')
    else:
        print('No')

main()