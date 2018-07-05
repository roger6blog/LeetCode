
  
  
***
  
### [001.Two_Sum](../../SourceCode/Python/001.Two_Sum.py) Level: Easy Tags: []
  
Time:  O(n)
Space: O(n)
思路: 檢查一個List中的兩個元素相加是否等於目標的數字   
雖然看起來可用兩個for迴圈  
前一個元素和後一個元素不斷試著相加就能得出答案  
但這O(n^2)的解法在元素太多時會超出Leetcode的時間限制  
可以用另一個方式，就是既然是其中兩個元素相加會等於target  
那我們便可以得知Target減其中一個元素就等於另一個元素  
如此便可用一個暫存的dict來存放目前已經找過的元素  
另一個元素用target相減後的值能在dict中找到的話便為答案

***
  
### [157.Read_N_Characters_Given_Read4](../../SourceCode/Python/157.[Locked]Read_N_Characters_Given_Read4.py) Level: Easy Tags: [Locked]
  
  
首先要明白題意的Read4是什麼意思  
實際上你給 Read4(buf) 的buf 必須要是一個有4個空字元的list  
如:  
temp = [''] * 4  # 即為['', '', '', '']
  
接著輸入的buf也是一堆空字元組成的list  
我們要做的就是利用每一次的Read4 把讀到的4個字元放到buf中  
注意每次Read4只能讀取4個字元，如果發現讀不出來了就要break  
  
***
