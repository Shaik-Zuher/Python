#gcd follow euler theorem
# if a=b:retun a
#if a>b return gcd(a-b,b)
#else return gcd(a,b-a)
class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        def gcd(a,b):
            if a==0:
                return b
            if b==0:
                return a
            if a==b:
                return a
            if a>b:
                return gcd(a-b,b)
            return gcd(a,b-a)
        return gcd(A,B)

 # lcm can be calculated by lcm=(A*B)//gcd(A,B)
#find gcd of array can be tricky so loop and take every 2 elements.dont forget to insert gcd of previous 2 in front
