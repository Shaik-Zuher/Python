def print_rangoli(size):
    # your code goes here
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in range(1,size+1):
        bet=[alpha[size-1-j] for j in range(i)]
        rev=bet[::-1]
        print(("-".join(bet)+"-"+"-".join(rev[1:])).center(((size+size-1)*2)-1,"-"))
    for i in range(size-1,0,-1):
        bet=[alpha[size-1-j] for j in range(i)]
        rev=bet[::-1]
        print(("-".join(bet)+"-"+"-".join(rev[1:])).center(((size+size-1)*2)-1,"-"))
