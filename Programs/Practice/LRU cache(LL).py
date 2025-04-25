"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put"""
#Lru least recently used  there is length when new value is inserted,least recntly is used is removed we also need to keep tarck of recntly used and moved to front at most recently used like linked list
class Lnode():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class LRUCache(object):
#so instead of travesring link we keep address in hashmap thats how it works
#when you get adress you directly get node
#"""
#->MRU                       LRU<-
#  -1 (values inserted here) -1 
#"""
#hashmap is something like this
#{
#key=address(the node address) without traverse to can access pretty much
#}
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.cache={}  
        self.mru=Lnode(-1,-1)
        self.lru=Lnode(-1,-1)
        self.mru.next=self.lru
        self.lru.prev=self.mru
    def remove(self,node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p
        node.next=None
        node.prev=None#####important to remove whole relation
    def insert(self,node):
        nx=self.mru.next
        self.mru.next=node
        node.prev=self.mru
        node.next=nx
        nx.prev=node
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val#be carefull at what you return
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val=value
            return
        new=Lnode(key,value)
        self.insert(new)
        self.cache[key]=new
        if len(self.cache)>self.cap:
            toremove=self.lru.prev
            self.remove(toremove)
            del self.cache[toremove.key]
            return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
###We similarly have LFU cache
