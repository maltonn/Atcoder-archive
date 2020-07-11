def main():
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    count=0
    for i,a in enumerate(A):
        if a%2 and (i+1)%2:
            count+=1
    print(count)
main()