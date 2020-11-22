def main():
    import sys
    a,b=list(map(int,sys.stdin.readline().split()))
    c,d=list(map(int,sys.stdin.readline().split()))
    print(a*d-b*c)

if __name__ == "__main__":
    main()