#taking n sized arry initially true which tells every ele is True
#during traverse when number is prime all its multiples are tagged as false do that it won,t be checked to reduce time complexity
#[t,t,t,t,t,t,t,t,t,t,t,t]
#i is 2 because is neigther prime nor compsite
#[t,t,t,f,t,f,t,f,t,f,t,f]
def primesUsingSieve(n):
    isPrime = [True] * (n + 1)
    i = 2 
    while i * i <= n:
        if isPrime[i]:
            #to reduce time complexity step count instead using multiplication evry time
            for j in range(2 * i, n + 1, i): ##########here using 2*i becuse starting from second mutiple instaed of first as first is alerady prime
            # for 3 range(9,100,3)----j=9 then 12 then 15 
                isPrime[j] = False 
        i += 1
 
    primes = []
    for i in range(2, n + 1):
        if isPrime[i]:
            primes.append(i)
 
    print("Primes less than", n, "are:")
    print(primes)
 
 
n = 100 
primesUsingSieve(n)
