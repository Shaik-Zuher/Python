"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        positive, negative = [], []
        result = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                positive.append(asteroid)
            else:
                value = abs(asteroid)
                shouldInsertAsteroid = True
                while True:
                    if len(positive) == 0:
                        break 
                    
                    if positive[-1] == value:
                        positive.pop()
                        shouldInsertAsteroid = False
                        break 
                    
                    if positive[-1] < value:
                        positive.pop()
                    else:
                        shouldInsertAsteroid = False
                        break
                    
                if shouldInsertAsteroid:
                    negative.append(value)
                    
        for ele in negative:
            result.append(-1 * ele)
            
        for ele in positive:
            result.append(ele)
        return result
"""
'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
'''
#Approach
#There are 2types of asterids on ewith positive values(right direction) and one with negative(left direction)
#They should not collide if collided they will be blasted based upon cases
#for example case 1:-25,-10,-9,6,-5,6,7
#     directions  <--------<- -> <- --> only 6 and -5 will collide
#     take  2 arrys onw which has positive and one for negative
#     here neg=[-25,-10,-9] becoz they never collided
#     positive=[6] when ever posoitve follwed by negative  there is collision if collided value is larger then smaller values than neg in array positive must be popped
#Cas2:  6,-7
#first 6 is added and 7 is opposite so smaller 6 blastes now as there is no more asteroids so -7 keeps travelling so it is added to negative array
#case 3: 8,6,-7
# positive=[8,6] -7 collided with 6 so 6 blasted,pos=[8]now 6 collided wth 8 this time 6 poffff
#fina res must be neg+pos becuse if viceversa [8,-25,-6] once again collison can happen
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        p=[]
        n=[]
        for asteroid in asteroids:
            #if positive
            if asteroid>0:
                p.append(asteroid)
            else:
                #if negative
                check=abs(asteroid)
                #first check if p is empty
                if(len(p)==0):
                    n.append(asteroid)
                #collision time
                while p and p[-1]<check:
                    p.pop()
                    #no more collisions and neg still prevails adding it
                    if(len(p)==0):
                        n.append(asteroid)
                #if both eqals both blasted
                if(p and p[-1]==check):
                    p.pop()
        return n+p
'''
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        p=[]
        n=[]
        for asteroid in asteroids:
            #if positive
            if asteroid>0:
                p.append(asteroid)
            else:
                #if negative
                check=abs(asteroid)
                #first check if p is empty
                if(len(p)==0):
                    n.append(asteroid)
                #if both eqals both blasted   if placed here it wont work for some cases like [-2,2,1,2] becuse after while loop it becomes[-2,2] but correct is [-2]
                if(p and p[-1]==check):
                    p.pop()
                #collision time
                while p and p[-1]<check:
                    p.pop()
                    #no more collisions and neg still prevails adding it
                    if(len(p)==0):
                        n.append(asteroid)
                
        return n+p
'''
                    
