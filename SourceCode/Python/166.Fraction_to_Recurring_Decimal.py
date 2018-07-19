'''

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

'''


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans = ''
        negativeFlag = numerator * denominator < 0
        loopDec = []  # Loop Decimal
        numerator = abs(numerator)
        denominator = abs(denominator)
        loopDict = dict() # Decide the location of decimal loop
        loopStr = None
        cnt = 0
        while True:
            loopDec.append(str(numerator / denominator))
            cnt += 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break

            # Check if this numerator appeared or not
            loc = loopDict.get(numerator)
            if loc:
                # Loop end
                loopStr = "".join(loopDec[loc:cnt])
                break
            loopDict[numerator] = cnt

        ans = loopDec[0]
        if len(loopDec) > 1:
            ans += "."
        if negativeFlag:
            ans = '-' + ans
        if not loopStr:
            ans = ''.join([ans,''.join(loopDec[1:])])
        else:
            ans += "".join(loopDec[1:len(loopDec) - len(loopStr)]) + "(" + loopStr + ")"
        return ans



print Solution().fractionToDecimal(-2147483648, 1)