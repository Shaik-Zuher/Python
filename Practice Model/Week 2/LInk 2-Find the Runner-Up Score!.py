if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis=[int(i) for i in arr]
    lis=list(set(lis))
    lis.sort(reverse=True)
    print(lis[1])
