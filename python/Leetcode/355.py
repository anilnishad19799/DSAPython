""" Design twitter problem """


from typing import List
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # pass      
        self.tweet[userId].append([[],tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        # return self.tweet[userId]
        allvalue = []
        print(self.tweet[userId])
        allvalue.append(self.tweet[userId][0][1])
        followvalue = self.tweet[userId][0][0]
        if followvalue:
            for i in followvalue:
                allvalue.extend(self.tweet[i][0][1])
        return allvalue

    def follow(self, followerId: int, followeeId: int) -> None:
        # pass
        # self.tweet[followerId].extend(self.tweet[followeeId])
        self.tweet[followerId] = self.tweet[followerId][0][0].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.tweet[followerId] = self.tweet[followerId][0][0].remove(followeeId)

twitter = Twitter()
out = twitter.postTweet(1, 5)
print(out)
out = twitter.getNewsFeed(1)
print(out)

out = twitter.follow(1, 2)
print(out)

out = twitter.postTweet(2, 6)
print(out)

out = twitter.getNewsFeed(1)
print(out)
