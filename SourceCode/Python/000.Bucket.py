import sys
import collections
class Testcase(object):
    def rearrange(self, testcase, limitTime):

        testcase.sort()
        slot = sum(testcase)/limitTime
        average = sum(testcase)/slot

        print testcase

        bucket = []
        dq = collections.deque(testcase)
        while True:
            if len(dq) == 0:
                break
            if len(dq) == 1:
                minBucket = self.minBucket(bucket)
                minBucket.extend(dq)
                break
            t = []
            t.append(dq.pop())

            if sum(t) > average:
                bucket.append(t)
                continue

            i = 0
            while i < len(dq):
                temp = sum(t) + dq[i]
                if temp > average:
                    temp -= dq[i]
                    break
                else:
                    t.append(dq[i])
                    dq.remove(dq[i])
                i += 1
            bucket.append(t)

        self.printSum(bucket, average)


    def rearrange2(self, testcase, limitTime):

        testcase.sort()
        slot = sum(testcase)/limitTime
        average = sum(testcase)/slot

        print testcase

        bucket = []

        while testcase != []:
            t = []
            t.append(testcase.pop())

            if sum(t) > average:
                bucket.append(t)
                continue
            i = len(testcase)-1
            if i < 0:
                minBucket = self.minBucket(bucket)
                minBucket.extend(t)
                break
            while i != 0:
                if i < 0:
                    print "!!!"
                temp = sum(t) + testcase[i]
                if temp > average:
                    temp -= testcase[i]
                else:
                    t.append(testcase[i])
                    testcase.pop(i)
                i -= 1

            bucket.append(t)
        # print bucket
        self.printSum(bucket, average)


    def minBucket(self, buckets):
        minBucket = sys.maxint
        rtn = None
        for b in buckets:
            minBucket = min(minBucket, sum(b))
            if sum(b) == minBucket:
                rtn = b
        return rtn


    def printSum(self, bucket, average):
        maxTime = 0
        print
        for c, b in enumerate(bucket):
            print("Bucket[{}]: {}".format(c, b))
            print("Sum of bucket[{}]: {}".format(c, sum(b)))
            print
            maxTime = max(maxTime, sum(b))
        print("Average: {}".format(average))
        print("MAX running time: {}".format(maxTime))


testcase =[64,95,285,93,94,380,102,122,67,119,68,100,68,120,214,218,213,253,70,82,71,201,71,59,59,54,74,54,78,51]

limitTime = 600
print
print("Total {}, hope be able to run in {} seconds".format(sum(testcase), limitTime))
print
Testcase().rearrange(testcase, limitTime)
# Testcase().rearrange2(testcase, limitTime)

