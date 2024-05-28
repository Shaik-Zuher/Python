lisy,lis=[],[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lisy.append([name,score])
        lis.append(score)
lisy.sort()       
lis.sort()
lis=list(set(lis))
min=lis[1]
for i in range(len(lisy)):
    if lisy[i][1]==min:
        print(lisy[i][0])
