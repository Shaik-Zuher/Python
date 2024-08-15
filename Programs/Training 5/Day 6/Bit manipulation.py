# & opeartor  but it uses mutiply bu tit doesn't give multipy of numbers!!!!!!!!!!!
# | opeartor used as add
#^ opeartor( bitwise xor) (fifferent bits will be 1)
#<< left shift shifts bits to left
#           n<<1 means 2*n (if one then multiply else power)
#           1<<n means 2**n
#>> right shifts bits to right n>>2 === n//2
# if binary 001 the bit at last psoition is 1 this one is called set bit
#if 0 then no set bit
#Observe carefully  3-- 0001     for odd numbers last bit is 1
#                   4-- 1000     for even last bit is 1
# to check if number is odd or even  and with 1
# if number & 1 is 1 thn odd
# if number &1 is 0 then even for example  111&001=001 so odd, 100*001=000 so even
#BIT MASKING
''' In this concept
let say we have number n=1010000 set(n,i)=set(n,5) which means set 5th position bit to 1
we can create array for loop array and cahnge it but not optimal
so we use new bit called as bit mask(craeting new bit)
1)set bit
For example if 0|1==1 and 1|0==1 so lets use or opeartor betwen number and mask
index 6 5 4 3 2 1 0 set(n,4)
      1 0 1 0 0 0 0
  (|) 0 0 0 0 0 0 1 we want 1 to be in 5th position so left shift that many times i.e 1<<i
  ------------------
index 6 5 4 3 2 1 0 set(n,4)
      1 0 1 0 0 0 0
  (|) 0 0 1 0 0 0 0  now we will get it so n|(1<<i) is used for set bit
  ------------------
2)clear bit always set to 0
For example if 0|1==1 and 1|0==1 so cant use or opeartor betwen number and mask
   0&1==0 1&1==0 so works
index 6 5 4 3 2 1 0 clear(n,4)
      1 0 1 0 0 0 0
  (|) 0 0 0 0 0 0 1 we want 1 to be in 5th position so left shift that many times i.e 1<<i
  ------------------
index 6 5 4 3 2 1 0 clear(n,4)
      1 0 1 0 0 0 0
  (|) 0 0 1 0 0 0 0  now we will get it so n&(1<<i) is used for set bit
  ------------------
3)toggle bit change 0 to 1 and 1 to 0
For example if 0|1==1 and 1|0==1 so can't use or opeartor betwen number and mask
  if 0^1==1 and 1^0==0 yea works so xor used 
index 6 5 4 3 2 1 0 toggle(n,4) wwhich is(n,i)
      1 0 1 0 0 0 0
  (^) 0 0 0 0 0 0 1 we want 1 to be in 5th position so left shift that many times i.e 1<<i
  ------------------
index 6 5 4 3 2 1 0 toggle(n,4)
      1 0 1 0 0 0 0
  (^) 0 0 1 0 0 0 0  now we will get it so n^(1<<i) is used for set bit
  ------------------
'''
################IF 2 same numbers are xored you gonna get 0 wohoooooooooooooo
#leetcode 286
nums=[0,1]
n=len(nums)
mask=0
for i in range(n+1):
    mask^=i
#first adding possible elements by ^
for ele in nums:
    #duplicates get out
    mask^=ele
print(mask)
