class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.followee = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId] = self.tweets.get(userId, []) + [(-self.time, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        tweets = self.tweets
        people = self.followee.get(userId, set()) | set([userId])
        for person in people:
            if person in tweets and tweets[person]:
                time, tweet = tweets[person][-1]
                h.append((time, tweet, person, len(tweets[person])-1))
        heapq.heapify(h)
        news = []
        for _ in range(10):
            if h:
                time, tweet, person, idx = heapq.heappop(h)
                news.append(tweet)
                if idx:
                    new_time, new_tweet = tweets[person][idx-1]
                    heapq.heappush(h, (new_time, new_tweet, person, idx - 1))
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId] = self.followee.get(followerId, set()) | set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followee:
            self.followee[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)