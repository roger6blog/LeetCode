'''
Level: Medium  Tag: [String]

Given two integers representing the numerator and denominator of a fraction,

return the fraction in string format.

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

Input: numerator = 4, denominator = 333
Output: "0.(012)"

Constraints:

-2^31 <= numerator, denominator <= 2^31 - 1
denominator != 0

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


    def fractionToDecimal2(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)

        if numerator * denominator < 0:
            sign = "-"
        else:
            sign = ""

        num = abs(numerator)
        den = abs(denominator)

        quotient = num / den
        remain = num % den

        ans = sign + str(quotient) + "."
        offset = {}
        while remain != 0 and remain not in offset:
            offset[remain] = len(ans)
            num = remain * 10
            quotient = num / den
            remain = num % den
            ans += str(quotient)

        if remain in offset:
            i = offset[remain]
            ans = ans[:i] + "(" + ans[i:] + ")"

        print(ans)

        return ans


# print Solution().fractionToDecimal(-2147483648, 1)
print(Solution().fractionToDecimal(1, 333))
print(Solution().fractionToDecimal2(1, 333))
print(Solution().fractionToDecimal2(1, 7))