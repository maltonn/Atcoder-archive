def main():
    import sys
    X=int(sys.stdin.readline())
    i=1
    while True:
        if 360*i%X==0:
            print(360*i//X)
            break
        i+=1
main()