""" Design twitter problem """


from typing import List
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time, tweetId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        totaluser = list(self.following[userId]) + [userId]
        totalvalue = []
        for user in totaluser:
            totalvalue.extend(self.tweet[user])

        sortedtweet = sorted(totalvalue, key=lambda x:x[0], reverse=True)[:10]

        return [tweetid for time, tweetid in sortedtweet]
       
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

   

twitter = Twitter()
twitter.postTweet(1, 5)
out = twitter.getNewsFeed(1)
print("1")
print(out)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
out = twitter.getNewsFeed(1)
print(out)
twitter.unfollow(1, 2)
out = twitter.getNewsFeed(1)
print(out)

