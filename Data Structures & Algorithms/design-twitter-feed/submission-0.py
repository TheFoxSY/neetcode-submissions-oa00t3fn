class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list) #[time, tweetId]
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.counter, tweetId])
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followees in self.followMap[userId]:
            if followees in self.tweetMap:
                index = len(self.tweetMap[followees]) -1
                counter , tweetId = self.tweetMap[followees][index]
                heapq.heappush(minHeap, [counter, tweetId, followees, index - 1])
            
        while minHeap and len(res) < 10:
            counter, tweetId, followees, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                counter , tweetId = self.tweetMap[followees][index]
                heapq.heappush(minHeap, [counter, tweetId, followees, index - 1])
            
        return res
    

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
