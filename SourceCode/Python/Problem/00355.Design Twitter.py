'''
Level: Medium   Tag: [Design]

Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
    Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
    Each item in the news feed must be posted by users who the user followed or by the user themself.
    Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId)
    The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId,
    int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


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
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
                            id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5],
                            since user 1 is no longer following user 2.


Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 10^4
All the tweets have unique IDs.
At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

'''

from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        self.time_stamp = 0
        self.tweets = defaultdict(list)
        self.friendship = defaultdict(set)


    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        #紀錄tweet info
        tweet_info = self.time_stamp, tweetId, userId, len(self.tweets[userId])
        self.tweets[userId].append(tweet_info)
        self.time_stamp -= 1


    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        ret = []

        # 放入自己的最新tweets資訊
        if self.tweets[userId]:
            heapq.heappush(heap, self.tweets[userId][-1])

        # 放入自己follow的最新tweets資訊
        for followee_id in self.friendship[userId]:
            if self.tweets[followee_id]:
                heapq.heappush(heap, self.tweets[followee_id][-1])

        count = 10

        while heap and count > 0:
            time_stamp, tweet_id, user_id, index = heapq.heappop(heap)
            ret.append(tweet_id)
            # 如果index大於0, 說明這user還有更舊的tweet,放入heap中排序
            if index > 0:
                heapq.heappush(heap, self.tweets[user_id][index-1])

            count -= 1

        return ret


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId == followerId:
            return

        self.friendship[followerId] |= {followeeId}
        pass

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId == followerId:
            return
        self.friendship[followerId] -= {followeeId}



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

obj = Twitter()
obj.postTweet(1, 5)
obj.getNewsFeed(1)
obj.follow(1, 2)
obj.postTweet(2, 6)
obj.getNewsFeed(1)
obj.unfollow(1, 2)
obj.getNewsFeed(1)