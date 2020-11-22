def main():
    import sys
    a,b=list(map(int,sys.stdin.readline().split()))
    c,d=list(map(int,sys.stdin.readline().split()))
    
    if a==c and b==d:
        print(0)
    elif a+b==c+d or a-b==c-d or abs(a-c)+abs(b-d)<=3:
        print(1)
    elif (a+b)%2==(c+d)%2:
        print(2)
    else:
        for t1 in [-3,-2,-1,0,1,2,3]:
            for t2 in [-3,-2,-1,0,1,2,3]:
                ct=c+t1
                dt=d+t2
                if abs(c-ct)+abs(d-dt)<=3:
                    if a+b==ct+dt or a-b==ct-dt or abs(a-ct)+abs(b-dt)<=3:
                        print(2)
                        return

        print(3)

if __name__ == "__main__":
    main()