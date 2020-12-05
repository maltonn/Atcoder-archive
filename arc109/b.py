def main():
    import sys
    import math
    n=int(sys.stdin.readline())
    K=int((math.sqrt(1+8*(n+1))-1)/2)
    K-=1
    while True:
        if K*(K+1)>2*(n+1):
            K-=1
            break
        K+=1

    
    print(n-K+1)

if __name__=='__main__':
    main()