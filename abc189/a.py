def main():
    import sys
    s=sys.stdin.readline().strip()
    if s[0]==s[1]==s[2]:
        print('Won')
    else:
        print('Lost')

if __name__ == "__main__":
    main()