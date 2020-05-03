def main():
    import sys
    from collections import Counter
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    C=Counter([i+x for i,x in enumerate(A)])
    output=0
    for key,val in Counter([i-x for i,x in enumerate(A)]).items():
        if key in C.keys():
            output+=val*C[key]
    print(output)

main()