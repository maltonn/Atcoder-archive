def Func(s):
    s+='0000'
    s=s[:s.find('.')+4]
    s=s.replace('.','')
    return int(s)

def main():
    import sys
    X,Y,R=list(map(Func,sys.stdin.readline().split()))

    print(X,Y,R)

if __name__ == "__main__":
    main()