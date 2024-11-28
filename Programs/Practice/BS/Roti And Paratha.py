"""
IEEE is having its AGM next week and the president wants to serve cheese prata after the meeting.
The subcommittee members are asked to go to food connection and get P (P<=1000) pratas packed for the function.
The stall has L cooks (L<=50) and each cook has a rank R (1<=R<=8). A cook with a rank R can cook 1 prata in the first R minutes 1 more prata in the next 2R minutes, 1 more prata in 3R minutes and so on (he can only cook a complete prata)
(For example if a cook is ranked 2, he will cook one prata in 2 minutes one more prata in the next 4 mins an one more in the next 6 minutes hence in total 12 minutes he cooks 3 pratas in 13 minutes also he can cook only 3 pratas as he does not have enough time for the 4th prata).
The webmaster wants to know the minimum time to get the order done.
Please write a program to help him out.
Input
The first line tells the number of test cases. Each test case consist of 2 lines.
In the first line of the test case we have P the number of prata ordered.
In the next line the first integer denotes the number of cooks L and L integers follow in the same line each denoting the rank of a cook.
Output
Print an integer which tells the number of minutes needed to get the order done.

Example
Input:
3
10
4 1 2 3 4
8
1 1
8
8 1 1 1 1 1 1 1 1

Output:
12
36
1
"""
class Object():
    def opt_paratha(self,n,chef):
        def condition(m):
            #BS on time(mins)
            #how many rotis chef rank r can make in time
            k=0
            for rank in chef:
                time=0
                j=1#multiply
                while time+(rank*j)<=m:
                    time+=(rank*j)
                    k+=1
                    j+=1
                    if(k>=n):
                        return True
            return k>=n
        s=0
        """ex:mid(mins)12 chef(rank 3)-1st(roti) 3 mins
                                          -2nd roti (2R more) 6mins
                                          -3rd roti(3R) 9mins
                                mis=12 so 3+6mins=9mins<12 so only 2 can be made
                    for example rank 2 then 2+4+6+8+10...=2(1+2+3+4+5...)=Rank*sumof n numbers==r*(n(n+1)//2)
            """
        e=100000000#max constraint is 1000 no_of_rotis and highest rank is 8 so accord to formula 8(1000*999//2)=3996000
        while s<=e:
            mid=s+(e-s)//2
            if condition(mid):
                e=mid-1
            else:
                s=mid+1
        return s
obj=Object()
for _ in range(int(input())):
    no_paratha=int(input())
    chef=list(map(int,input().split()))
    print(obj.opt_paratha(no_paratha,chef[1:]))
