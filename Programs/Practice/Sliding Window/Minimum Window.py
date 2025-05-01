#Minimum window substring
#mininum window subsequence
#Substring---s1=abcdfsypay  s2=ysa  substring is sypa In substring no need to maitain order
#Subsequnec --s1=abcdfsyay  s2=ysa  no subsequnce becuse it maintains a particular order
"""
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
#As substring doesnt maintain any order lets take hashmap and calculate counts
#################If there is need for 2 hashmaps only use one and decremnt the values in it....
class Solution(object):
    def minWindow(self, s, t):
        i,j,cnt=0,0,0
        ml=0
        hp={}
        start,end=-1,-1
        for i in t:
            if i in hp:
                hp[t]+=1
            else:
                hp[t]=1
        while j<len(s):
            if s[j] in hp:
                hp[s[j]]-=1#decrease the values as we find matched elements
                if hp[s[j]]>-1:
                    cnt+=1
            else:
                hp[s[j]]=-1 ###other elemnts its not needed
            """
            hp={A:1 B:2 c:3} when s[j] is c then hp={A:1 B:2 c:2},cnt=1 so we keep trac of counts
            """
            while cnt==len(t):#when cnt matches "Sdabc" lets remove the start alphabets
                if cnt==len(t) and ml>(j-1+1):
                    ml=(j-i+1)
                    start=i#start index
                    end=j #last index
                    hp[s[i]]+=1
                    if hp[s[i]]>0:
                        cnt-=1
                i+=1
            j+=1
        if start==-1:
            return -1
        return s[start:end+1]
"""
Minimum Window Subsequence
Given strings str1 and str2 containing lowercase English letters, find the minimum (contiguous) substring w of str1, so that str2 is a subsequence of w. If there is no such window in str1 that covers all characters in str2, return the empty string. If there are multiple such minimum-length windows, return the one with the left-most starting index.

Examples:
Input: str1: geeksforgeeks  str2: eksrg
Output: eksforg
Explanation: "eksforg" satisfies all required conditions. str2 is its subsequence and it is longest and leftmost among all possible valid substrings of str1.
Input: 
Input: str1: abcdebdde str2: bde 
Output:  bcde 
Explanation:  "bcde" is the answer and "deb" is not a smaller window because the elements in the window must occur in order.
"""
#Example 
# geeksforgeeks   eksrg
# i               k
# j
# geeksforgeeks   eksrg
# i               k        when matched k+=1
#   j
# geeksforgeeks   eksrg
# i                k
#   j
##Like this
# geeksforgeeks   eksrg
# i                   k
#         j
# geeksforgeeks   eksrg
#         i             k     i==k and k-=1 to keep it back track now decremnt to find start
#         j
# geeksforgeeks   eksrg
#  i             k        my start is i+1 and k=0 must be in track
#         j                 impotnat j=i#once again start from there maybe you can find even smaller answer
#example
#dgfbkfibbkihjkaediegihhdjfaaedhdffaedcehhagedfjg         dgjhfh
#first time you get dgfbkfibbkihjkaediegihhdjfaaedh
#                   i here
#second you get dgfbkfibbkihjkae diegihhdjfaaedhdffaedceh
#                               i will be here
 #this is subsequnec so take 3 pointers to keep track of second string(order to be maintained)
class Solution:
    def minWindow(self, str1, str2):
        i=j=k=0
        start,end,ml=-1,-1,10**9
        while j<len(str1):
            #matching str1,str2
            if(str1[j]==str2[k]):
                k+=1
            if k==len(str2):#k out of bounds
                k-=1 #back in bounds
                i=j #find start
                while k>=0:
                    if(str1[i]==str2[k]):
                        k-=1
                    i-=1
                i+=1#as to check even str2[0] the next index is start
                if ml>(j-i+1): ##Condition
                    ml=j-i+1
                    start=i
                    end=j
                j=i  #make j=i again to find even more small one
                k=0 #k back to zero becoz previously -1
            j+=1
        if start==-1:
            return ""
        return str1[start:end+1]
