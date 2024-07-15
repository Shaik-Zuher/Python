#Trie is tree which stores alpahbets
#     [is ending=false,dict{}]  every node will have boolean variable which tells if any
#the dict will be in format {charcater and address and of next level node}
#     [_,_,2040(address,_,_]
#      a b     c        d e
#        /
#[_,_,_,_,_] #this is how things are if there address at any alphabet that means alphabet is present and level represents index
#root nodes elements tells that character is presnt at index 0
# during insertion we need to create TrieNode and every and store its address in dict mapped to respective character
#every time we need to keep current which acts as pointer and checks nodes
#during search every index charcter check if prent is dict than moved to address mapped to character (simple like it says)
class TrieNode:
    #skelton For creating empty node
    def __init__(self):
        self.isEnding = False 
        self.store = dict()
 
class Trie:
    def __init__(self):
        #creating new node every time object created
        self.root = TrieNode()
 
    def insertWord(self, word):
        #currRoot which acts like pointer this is not like bst/ll rememeber carefully there are no next
        currRoot = self.root 
        n = len(word)
        for index in range(n):
            ######adding element and changing pointer
            if word[index] not in currRoot.store:
                currRoot.store[word[index]] = TrieNode()#dict={c:4040(address of new created Node)}
            #moving through levels
            currRoot = currRoot.store[word[index]]
        #when word ends mark isEnding+true which tells ya its over
        currRoot.isEnding = True 
        print(word, "inserted successfully in the trie")
 
 
 
    def searchWord(self, word):
        currNode = self.root 
        n = len(word)
        for index in range(n):
            ch = word[index]
            #if even single letter doesnt exist false
            if ch not in currNode.store:
                return False
            #checking levels
            currNode = currNode.store[ch]
        #to check if complete word exitsts not prefix for eaxmple there are 2 words com,comp we have comp in tree and at p ending=true so seraching com must be false
            #if we dont use this com will take comp and return true 
        return currNode.isEnding
 
 
    def startsWith(self, word):
        currNode = self.root 
        n = len(word)
        for index in range(n):
            ch = word[index]
            if ch not in currNode.store:
                return False 
 
            currNode = currNode.store[ch]
        return True
 
obj = Trie()
obj.insertWord("cat")
obj.insertWord("computer")
obj.insertWord("compute")
 
print(obj.startsWith("com"))
print(obj.startsWith("comput"))
print(obj.startsWith("coma"))
 
# if obj.searchWord("cat"):
#     print("cat is present in trie")
# else:
#     print("cat is not present in trie")
 
 
# if obj.searchWord("compute"):
#     print("compute is present in trie")
# else:
#     print("compute is not present in trie")
