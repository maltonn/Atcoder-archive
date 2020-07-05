# 各日について満足度の一番高いコンテストを選択する貪欲
def main():
    import sys
    import numpy as np
    D = int(sys.stdin.readline())
    S = np.zeros((D, 26))
    C = np.array(map(int, sys.stdin.readline().split()))
    for i in range(D):
        S[i] = list(map(int, sys.stdin.readline().split()))

    for i in range(D):
        print(np.argmax(S[i])+1)


main()
