##radix sort has same mechanism as counting sort
#here main difference instead of using count sort on number we use it on digits(i.e places)
#for example [12,1,5,23,670]
# counting sort in done on digits on ones place on every number
#[670,1,12,23,5] 1st iteration.
#   - -  -  - -
#second  time on ones place
#if no number there considered 0
#[1,5,12,23,670] 2nd iteration
#now on thousnads place  ########no of digits in max number that many times
#[1,5,12,23,670] 3rd iteration -----done
nums=[12,1,5,23,670]
def radix(nums):
    def cs(nums,exp):#normal count sort but need to use exp that all
        temp=[-1]*len(nums)
        store=[0]*10#as there are only 0-9 digits no need of extra
        #freq count on index
        for i in range(len(nums)):
            index=nums[i]//exp
            store[index%10]+=1#we get proper indexes
        #prfix sum
        ps=0
        for i in range(len(store)):
            ps+=store[i]
            store[i]=ps
        #placing in ans
        for i in range(len(nums)-1,-1,-1):
            index=nums[i]//exp
            store[index%10]-=1
            temp[store[index%10]]=nums[i]
        #coping to main array
        for i in range(len(nums)):
            nums[i]=temp[i]
    mx=max(nums)
    exp=1####positions    #say 503 to get one place %10 to get to get second place need to use %100->03 not good
    while exp<=mx:        # so lets divide it with 10 503//10=50 now 50%10
        cs(nums,exp)      #so we can say exp tracks how many places must be removed
        exp*=10
radix(nums)
print(nums)
