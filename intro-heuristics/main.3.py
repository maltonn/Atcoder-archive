# lossがつらいので、全コンテストで26日以上の間があかないようにする。
# とりあえず1番目のコンテストから順番にあてる
import sys
import numpy as np
def main():
    DEBUG_MODE=False

    if DEBUG_MODE:
        f = open('tester/example/sample2.in')
        fo=open('tester/example/sample2.out','w')
    
    if DEBUG_MODE:
        D = int(f.readline())
    else:
        D = int(sys.stdin.readline())
    Dur = np.zeros(26)
    S = np.zeros((D, 26))
    if DEBUG_MODE:
        C = np.array(list(map(int, f.readline().split())))
    else:
        C = np.array(list(map(int, sys.stdin.readline().split())))

    for i in range(D):
        if DEBUG_MODE:
            S[i] = list(map(int, f.readline().split()))
        else:
            S[i] = list(map(int, sys.stdin.readline().split()))
    now=0
    for d in range(D):
        print(now+1)
        if DEBUG_MODE:
            fo.write(str(now+1)+'\n')

        now+=1
        now%=26

    if DEBUG_MODE:
        f.close()
        fo.close()
main()
