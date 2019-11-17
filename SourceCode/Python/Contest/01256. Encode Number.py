'''

5108->1256. Encode Number
Difficulty: Medium
Given a non-negative integer num, Return its encoding string.

The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:



Example 1:

Input: num = 23
Output: "1000"
Example 2:

Input: num = 107
Output: "101100"


Constraints:

0 <= num <= 10^9

'''


class Solution(object):
    def __init__(self):
        self.n = [2,4]
        self.n.extend([0]*28)
        self.ans = [2,6]
        self.ans.extend([0]*28)
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        for i in range(1, 30):
            self.n[i] = self.n[i-1] * 2

        for i in range(1, 30):
            self.n[i] += self.n[i-1]

        if num == 0:
            return ""

        elif num == 1:
            return "0"

        elif num == 2:
            return "1"

        s = ""

        for i in range(1, 30):
            if num >= self.n[i-1] and num <= self.n[i]:
                num -= self.n[i-1]
                num -= 1
                while num > 0:
                    s += str(num & 1)
                    num >>= 1

                m = i + 1
                l = len(s)
                for _ in range(l, m):
                    s += '0'
                break
        s = list(s)
        for i in range(len(s)/2):

            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

        return ''.join(s)
print(Solution().encode(23))
'''
int n[30]={2,4};
int ans[30]={2,6};
       for(int i=1;i<30;i++)
       {
           n[i]=n[i-1]*2;

       }
        for(int i=1;i<30;i++)
            n[i]+=n[i-1];
      //  for(int i=0;i<10;i++)
       //     printf("%d ",n[i]);
        if(num==0)
            return "";
        else if(num==1){
            return "0";
        }else if(num==2){
            return "1";
        }
        string s="";
        for(int i=1;i<30;i++){
            if(num>=n[i-1]&&num<=n[i])
            {
                num-=n[i-1];
                num--;
                while(num>0){
                    s+=(num&1)+'0';
                    num>>=1;
                }
                int l=i+1;
                for(int j=s.length();j<l;j++)
                {
                    s+='0';
                }
                break;
            }
        }
        for(int i=0;i<s.length()/2;i++)
            swap(s[i],s[s.length()-i-1]);
        return s;
    }
'''