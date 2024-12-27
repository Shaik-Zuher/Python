"""
30. Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
"acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s.
You can return the answer in any order.

 Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"]
"""
#barfoobarthethfoobar first checking every letter will give tle bad it is said that every word in words has same length
#So will check in that intervals and use hashmap hp={foo:1,bar:1}(words)
#barfoobarthethfoobar   empty map={}
#j(slice and check) prenst added to map={bar:1}
#   j  added to map={bar:1,foo:1}
#map==hp so add index start index j-len(words-1)*len(words[0])   ans=[0]
#      j now I am here but map={bar:1,foo:1} but i missed foobar at pos=4 so i will keep track of number of words count==len(words)
#So whenever my count exceeded i will shrink window basically you can use new pointer as k or you can use slice(math) 
# s[j-len(words)*len(words[0]):j-len(words-1)*len(words[0])] //This will give us  check first elemnt sliced until length of first element
#barfoobarthethfoobar
#         j(the)        map=(bar:1,foo:1) by removing first  ans=[0,3]
#This is not present so empty map ans reset count=0 becuse our anagrams must be concated so when not matched then not coonacted
#            j(thf)
#               j(oob) like this but we missed one more at index 14
#Orinally in brute one we checked everything so about checking at every index of until len(word[0])
#barfoobarthethfoobar                   => barfoobarthethfoobar => barfoobarthethfoobar
# j(like this once more whole process)       j(once more)             j(repeated so stop)
"""#######I might think because 2 loops 0(n^2) but for used wisely it wont run for n^2"""
import collections
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n=len(words[0])
        j=0
        ans=[]
        hp=collections.Counter(words)
        for i in range(n):
            cnt=0
            mp={}#not oustide becuse everytime not refreshed
            for j in range(i,len(s),n):#step skip counter
                check=s[j:j+n]#slice check every word
                if check in hp:
                    if check in mp:
                        mp[check]+=1
                    else:
                        mp[check]=1
                    cnt+=1
                    if cnt>len(words): #barfoobar case to get foobar thing
                        text=s[j-(len(words)*n):j-((len(words)-1)*n)]
                        mp[text]-=1
                        if mp[text]==0:
                            del mp[text]
                        cnt-=1
                    if mp==hp and cnt==len(words):
                        ans.append(j-((len(words)-1)*n)) #-1 used because at this point j is at start of last word so remove that word from total anagram length
                else:#Reset everything becuse anagram concate broke
                    mp={}
                    cnt=0
        return ans
        
