######## max->new array len mx+1->store freq->prefix- from freq>use prefix and store
####It has problems with negative numbers

def performCountingSort(nums):
    n = len(nums)
    temp = [-1] * n
    # step-1: finding max 
    mx = max(nums)
 
    # step-2: creating (max + 1) length list with zeroes 
    store = [0] * (mx + 1)
 
    # step-3: finding each element frequency 
    for ele in nums:
        store[ele] += 1 
    print(store)
 
    # step-4: calculating prefix sum 
    for index in range(1, mx + 1):
        store[index] += store[index - 1]
    print("s",store)
 
 
    # step-5: traverse from right to left and place the element at appropriate index 
    for index in range(n - 1, -1, -1):
        ele = nums[index]
        store[ele] -= 1 
        temp[store[ele]] = ele
        print(temp)
 
 
    # step-6: (optional) copy the temp output list to main list
    for index in range(n):
        nums[index] = temp[index]
 
 
 
 
 
 
nums = [8, 1, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 4, 4, 4, 4, 6]
 
print("Before sorting:", nums)
performCountingSort(nums)
print("After sorting:", nums)
##when neg [3,-1]  we usually create array mx+1 [0,0,0,0]
#                                                0 1 2 3
#want to store -1 so ill add onw more [0 0 0 0 0] if -2 is there ill add 2 so basically mx+min+1 i.e mx-mn+1 remember min is neg right
###now about storing
#lets say i want to store 3  i will have to store next index(due to -1) so basically 3+min=3-(-1)
#it can be properly accessed this will be offset
#so for -1 stored in -1-(-1)=0 proper place
"""
negative numbers count sort in JS
var sortArray = function(nums) {
    let mn=Math.min(...nums);  ----this is changed
    let off=0;
    let mx=0
    if (mn<0){
     mx=Math.max(...nums)-mn;
    off=0-mn;--------------------------------------------
    }
    else{
    mx=Math.max(...nums);
    }
    let ans=[];
    let store=[];
    for(var i=0;i<=mx+1;i++){
        store.push(0);
    };
    for(var i of nums){
        ans.push(-1);
        store[i+off]+=1;
    };
    let s=0;
    for(i=0;i<store.length;i++){
        s+=store[i];
        store[i]=s;
    };
    for(i=nums.length-1;i>-1;i--){
        store[nums[i]+off]-=1;
        ans[store[nums[i]+off]]=nums[i];
    };
    return ans;
};
"""
