#This is pattern of merge k sorted lists.
"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
Implement the Twitter class:
Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
"""
#My approach was storing users(followers) in hashmap and for tweets I use Linked List(use MRU cache)--gives TLE
"""
Hashmap for users(followers) which has sets
Another hashmap for tweets in this recent tweets are appended in last generally but as heap to used I will use timer for tweets
mp={userId=[[-1,tweetId],[-2,tweetId],[-3,tweetId]]} because i dont know on which heap to used
####I will take heap to get recent by using merge k pattern because in question priority is said(most recently used--this says priority so I am using some sort of counter)
"""
from heapq import *
class Twitter(object):

    def __init__(self):
        self.users={}
        self.tweets={}
        self.time=0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time+=1
        if userId in self.tweets:
            self.tweets[userId].append([-self.time,tweetId])
        else:
            self.tweets[userId]=[-self.time,tweetId]

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        ans=[]
        pq=[]
        if userId in self.tweets:#presnt user tweets need to to checked becoz some users wont post anything like me hahahahahah
            heappush(pq,[self.tweets[userId][-1],userId,len(self.tweets[userId])-1])
        """#pq=[[last tweet of userId,userId,len(tweet array)]]"""
        if userId in self.users:
            for i in self.users[userId]:
                heappush(pq,[self.tweets[i][-1],i,len(self.tweets[i])-1])
        while len(ans)<10 and pq:
            a=heappop(pq)
            ans.append(a[0][1])
            a[2]-=1
            if a[2]>-1:
                heappush(pq,[self.tweets[a[1]][a[2]],a[1],a[2]])
        return ans
    #Hashamp-Users(followers) but followers stored in map
    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.users:
            self.users[followerId].add(followerId)
        else:
            self.users[followerId]={followeeId}
    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.users:
            return
        else:
            self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
