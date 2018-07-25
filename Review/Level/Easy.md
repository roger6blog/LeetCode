
  
  
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
  
### [257.Binary_Tree_Paths](../../SourceCode/Python/257.Binary_Tree_Paths.py) Level: Easy Tags: [Tree]
  
Time:  O(n * h)，h為樹高  
Space: O(h)  
思路: 要求你印出Binary Tree從root到所有leave的路徑   
Traversal的部分用DFS就可以做到  
問題在於怎麼把每次的路徑都印出來  
我們可以在DFS裡面加上純leave的判斷  
traversal到leave即印出其中一條路徑  
在traversal到leave後我們需要把leave Node pop出來  
不然就會變成一般的DFS traversal了  
   
  
***
  
### [326.Power_of_Three](../../SourceCode/Python/326.Power_of_Three.py) Level: Easy Tags: [Math]
  
Time:  O(1)  
Space: O(1)  
思路: 計算輸入的數字是否為3的n次方  
用遞迴從3的0次方算到大於n的3的k次方      
其中有相等於n的次方數即為答案  
題目的Follow up要求用非遞迴的方法  
因為符合3的n次方的正整數並不多  
我們可以把0~最大正整數符合3的n次方的數字都算出來存到dictionary    
接著看n有沒有在裡面就可以了    
  
  
***
  
### [387.First_Unique_Character_in_a_String](../../SourceCode/Python/387.First_Unique_Character_in_a_String.py) Level: Easy Tags: []
  
Time:  O(2*n)  
Space: O(n)
    
思路:找出一個字串裡第一個單獨出現的字母  
單純地用字串的.count方法會超時(Time Limit Exceed)  
我們可以先遍歷一次字串  
把出現的字母和計數都存到一個dictionary中  
然後再重新遍歷一次  
第一個計數為1的字母就是答案  
  
***
  
### [400.Nth_Digit](../../SourceCode/Python/400.Nth_Digit.py) Level: Easy Tags: [Math]
  
Time:  O(logn)  
Space: O(1)
    
思路:雖然被標為Easy，但如果不懂題意其實是頗難的一題  
題目描述有一個無窮正整數從小到大所組成的數列  
如1, 2, 3, 4, 5, 6, 8, 9, 9, 10, 11 ...  
可以組成 1234567891011 .... 這麼長的數列  
給你任意一個正整數n，找出這數列中位於第n個的數字是什麼  
例如n=11的時候  
對於這個數列就是 1234567891 0 11 ...  
　　　　　　　　　　　　　　^第10個數字  
第10個數字為0  
這是一道數學題，我們先從簡單的開始看  
數字為1~9的時候，這數列可以組成9個數字長度那麼長的數列   
數字為10~99的時候，這數列可以組成180個數字長度那麼長的數列  
數字為100~999的時候，這數列可以組成2700個數字長度那麼長的數列  
...  
..  
依此類推，我們可以發現  
一位數時是 1*9 長度  
二位數時是 2*10*9 長度  
三位數時是 3*100*9 長度  
所以每個區間長度為  i*(10**i)*9 那麼長  
所以首先我們需要確定的就是n落在哪個位數組成的區間裡  
接著找出他在這個區段中的哪一個數字  
最後找出它是屬於這個數字中的哪一個數字即為答案
  
因為光用描述太過抽象  
我們用n為數字1234為例子  
第1234個數字中  
我們去掉1位數的長度 9 => 1234 - 9 = 1225  
去掉2位數的長度 180 => 1225 - 180 = 1045 
去掉3位數的長度 2700 => 1045 - 2700 < 0  
由此可知第1234個數字落在3位數組成的數列中  
而這三位數組成的數字是 100101102103.....  ... 998999
全部由3個位數的數字組成  
所以我們可以用 (n-1) 除以位數  
也就是 1044 / 3 = 348  
別忘記我們扣掉過前面位數的數列  
所以這數列是從100算起的，我們得加回來  
所以精確來說是落在 448 這個數字上  
最後一步是找出他落在 4, 4, 8 三個數字的其中一個  
只要取餘數我們就能知道落在哪一個    
所以是 1044 % 3 = 0，第1位  
於是答案等於 4
  
其實我們也可以直接拿區間內所有的數字組成一個字串  
直接找出index = n的數字即為解答  
但在Leetcode中光組成這樣的字串就會超時(TLE)了  
  
  
***
  
### [408.Valid_Word_Abbreviation](../../SourceCode/Python/408.Valid_Word_Abbreviation.py) Level: Easy Tags: []
    
Time:  O(n)  
Space: O(1)  
  
思路: 這題並不難，難的是了解題目的意思  
給你一個字串 s 和相對應的縮寫 abbr
例如 
```python
s = "internationalization"
abbr = "i12iz4n"
```
其中縮寫 "i12iz4n" 內的數字代表左右兩個字母中間有多少個字元  
例如 i12i -> 開頭的i和下一個i中間夾了12個字元  
依此類推  
而另一個例子
```python
s = "apple"
abbr = "a2e"
```
因為a和e中間夾了3個字元而不是2個
所以這個"a2e"不是 "apple"的縮寫  
  
知道題意之後  
就可以照題目的要求解題  
用雙指針分別遍歷 s 和 abbr是不錯的主意  
不過要注意數字可能會超過10  
所以遍歷時遇到數字別急著馬上處理，應該先把它加總起來  
例如 
```python
count = count*10 + int(abbr[j])
```
等看到下一個字母時就能算出正確的數字了
  
  
***
  
### [448.Find_All_Numbers_Disappeared_in_an_Array](../../SourceCode/Python/448.Find_All_Numbers_Disappeared_in_an_Array.py) Level: Easy Tags: []
     
Time:  O(n)  
Space: O(1)  
  
思路:在一個無序數列中，裡面的數字為1~n之間，n為數列長度  
找出沒有出現在該數列裡的數字  
既然有沒有出現的數字又限制數字在1~n之間  
代表一定有數字是重複的  
雖然排序後找出和index不對齊的數字便是答案  
但這種作法只要遇到長數列Leecode就會吐TLE(Time Limit Exceed)    
這裡用負號標記法  
我們把數列中的每個數字都當作是一個index  
對這個index的數字乘上-1讓他變成負數  
如此一來，數列中缺少的數字的index對應的數字就不會成為負數  
接著重新遍歷整個數列，找出數字為正的index就是答案  

  
***