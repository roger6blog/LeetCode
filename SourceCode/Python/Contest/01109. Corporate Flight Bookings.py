'''

There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.

The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.



Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]


Constraints:

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000


'''

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """


        result = [0] * n
        booking_count = 0
        for b in bookings:
            if booking_count > 20000:
                break
            else:
                booking_count += 1
            for l in xrange(b[0], b[1] + 1):
                if 1 <= b[0] <= 20000 and \
                        1 <= b[1] <= 20000 and \
                        1 <= n <= 20000 and \
                        b[0] <= b[1] <= n and \
                        1 <= b[2] <= 10000:
                    result[l - 1] += b[2]
                else:
                    break

        return result


bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
sol = Solution()
print(sol.corpFlightBookings(bookings, n))
