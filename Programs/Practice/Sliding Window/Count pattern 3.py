#somewhat different count pattern
#Usually it will be count(k)-count(k-1)
"""
3306. Count of Substrings Containing Every Vowel and K Consonants II
You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0
Explanation:
There is no substring with every vowel.

Example 2:
Input: word = "aeiou", k = 0
Output: 1
Explanation:
The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
Explanation:
The substrings with every vowel and one consonant are:
word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:
5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5
"""
#Hint
#work = "iqeaouqi"
#sliding window gives you two but if you look close enough the entire string is also a valid substring!
class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def count(l):
            v={"a","e","i","o","u"}
            hp={}
            i=j=0
            c=0
            cons=0
            while j<len(word):
                if word[j] in v:
                    if word[j] in hp:
                        hp[word[j]]+=1
                    else:
                        hp[word[j]]=1
                else:
                    cons+=1
                while len(hp)==5 and cons>k:
                    if word[i] in hp:
                        hp[word[i]]-=1
                        if hp[word[i]]==0:
                            del hp[word[i]]
                    else:
                        cons-=1
                    i+=1
                if len(hp)==5 and cons<=k:
                    #c=(j-i+1) orignally but not whole subarray so may be no
                    c+=1
                j+=1
            #Actually here is trick for example take word "iqeaouqi" and k=2
            """
            valids are iqeaouq,qeaouqi  but whole string is also valid one.
            So actually our logic(striver) will fail here
            Observe something  the question says exactly k consonents so lets find cons>=k
            Another thing say in iqeaouqi  I took iqeaouq is one answer and another thing is all strings which conatins this as my substring is also my answer
            """
            """
            take example 3:
            word = ieaouqqieaouqq, k = 1

            with l = 0 and r = 5, the window "ieaouq" meets the requirement of all vowels and 1 consonant. Therefore, all other substrings extending to the end of word will also have all vowels and at least 1 consonant, so count n - r + 1 to include all these.

            ieaouqq
            ieaouqqi
            ieaouqqie
            ieaouqqiea
            ieaouqqieao
            ieaouqqieaou
            ieaouqqieaouq
            ieaouqqieaouqq
            """
            #So i will add this and start shrink window so i can find smaller ones
        #Actually might be so different
        return count(k)-count(k-1)
class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        #actual logic
        def count(l):
            v={"a","e","i","o","u"}
            hp={}
            i=j=0
            c=0
            cons=0
            while j<len(word):
                if word[j] in v:
                    if word[j] in hp:
                        hp[word[j]]+=1
                    else:
                        hp[word[j]]=1
                else:
                    cons+=1
                #As long as cons< i will keep adding
                while len(hp)==5 and cons>=l:
                    c+=(len(word)-j)#Adding all substrings
                    if word[i] in hp:
                        hp[word[i]]-=1
                        if hp[word[i]]==0:
                            del hp[word[i]]
                    else:
                        cons-=1
                    i+=1
                j+=1
            return c
        #Actually needs to be changed for <=k  we tend to find count of exactly(count(k)-count(k-1))
        #This is >=k so may be count(k)-(count(k+1))
        """
        return count(k)-count(k-1)
        We have two types atmost(k)-atmost(k-1) and atleast(k)-atleast(k+1)
        """
        return count(k)-count(k+1)
#################Actually our first approach works like seriusly what the HELL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Remember when while loop used never use a if condition actually do this
#First try if and if works ok
# else remove if condition                     FOLLOW TEMPLATE
class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def count(l):
            cons=0
            c=i=j=0
            hp={}
            v={"a","e","i","o","u"}
            while j<len(word):
                if word[j] in v:
                    if word[j] in hp:
                        hp[word[j]]+=1
                    else:
                        hp[word[j]]=1
                else:
                    cons+=1
                while len(hp)==5 and cons>l:
                    if word[i] in hp:
                        hp[word[i]]-=1
                        if hp[word[i]]==0:
                            del hp[word[i]]
                    else:
                        cons-=1
                #if len(hp)==5 and cons<=l:   remove
                c+=(j-i+1)    #dont care add all subarrays works 
                j+=1
            return c
        return count(k)-count(k-1)
