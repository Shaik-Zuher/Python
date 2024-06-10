def average(array):
    # your code goes here
    array=set(array)
    avg=sum(array)/len(array)
    return round(avg,3)
