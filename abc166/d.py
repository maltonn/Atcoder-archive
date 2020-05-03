def main():
    import sys
    X=int(sys.stdin.readline())
    for i in range(-1000,1000):
        for j in range(-1000,1000):
            if i**5-j**5==X:
                print("{} {}".format(i,j))
                return
            

main()