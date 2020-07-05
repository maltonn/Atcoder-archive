# lossがつらいので、全コンテストで26日以上の間があかないようにする。
# 26日サイクルで全部回すとして、残ってるコンテストの中で一番点数の高いものから順に選んでいく
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
    already=set()
    for d in range(D):
        argSS=np.argsort(S[d])
        for c in argSS[::-1]:
            if c not in already:
                already.add(c)
                out=c+1
                break

        if DEBUG_MODE:
            fo.write(str(out)+'\n')
        else:
            print(out)

        now+=1
        if now==26:
            now=0
            already=set()

    if DEBUG_MODE:
        f.close()
        fo.close()
main()
