def main():
    import sys
    a,b,x,y=list(map(int,sys.stdin.readline().split()))
    if a==b:
        print(x)
    elif a>b:
        if 2*x<y:
            print(((a-b)*2-1)*x)
        else:
            print(((a-b)-1)*y+x)
    else:
        if 2*x<y:
            print(((b-a)*2+1)*x)
        else:
            print((b-a)*y+x)



if __name__=='__main__':
    main()
