def minion_game(string):
    # your code goes here
    con="BCDFGHJKLMNPQRSTVWXYZ"
    vo="AEIOU"
    ss,ks=0,0
    for i in range(len(string)):
        if string[i] in con:
            ss+=len(string)-i
        if string[i] in vo:
            ks+=len(string)-i
    if ss>ks:
        print("Stuart",ss)
    elif ks>ss:
        print("Kevin",ks)
    else:
        print("Draw")
