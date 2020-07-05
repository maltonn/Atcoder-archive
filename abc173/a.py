def main():
    import sys
    N=int(sys.stdin.readline())
    if N%1000:
        print(1000-N%1000)
    else:
        print(0)

        
main()