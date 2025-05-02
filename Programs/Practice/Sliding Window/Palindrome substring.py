"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""
#Like general liding window but window size must be len(str1)
########################!!!!!!!!!!!!!!!!!!!There are lot problems like this check given string in word(consecutive) then also just keep window size=len(strng)
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        hp={}
        for i in s1:
            if i in hp:
                hp[i]+=1
            else:
                hp[i]=1
        c={}
        i,j=0,0
        while j<len(s2):
            if s2[j] in c:
                c[s2[j]]+=1
            else:
                c[s2[j]]=1
            if (j-i+1)>len(s1):####This is important lengths must be same
                c[s2[i]]-=1
                if c[s2[i]]==0:
                    del c[s2[i]]
                i+=1
            if c==hp:
                return True
            j+=1
        return False
"""
var checkInclusion = function(s1, s2) {
    if(s1.length>s2.length){
        return false;
    }
    let hp={};
    for(var i of s1){
        if(i in hp){
            hp[i]+=1;
        }
        else{
            hp[i]=1;
        }
    }
    let l=0,r=0;
    let c=0;
    while(r<s2.length){
        if(s2[r] in hp){
            hp[s2[r]]--;
            if(hp[s2[r]]>-1){
            c++;
            }
        }
        if(r-l+1>s1.length){
            if(s2[l] in hp){
                hp[s2[l]]++;
                if(hp[s2[l]]>0){
                c--;
                }
            }
            l++;
        }
        if(c==s1.length){
            return true;
        }
        r++;
    }
    return false;
};
"""
