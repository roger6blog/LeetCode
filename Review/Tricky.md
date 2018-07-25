

***

### [031.Next_Permutation](../../SourceCode/Python/031.Next_Permutation.py) Level: Medium Tags: [Tricky]  
  
Time:  O(n)  
Space: O(1)
    
思路: 給你一個數字組成的數列  
要你找出他的下一個排列比他大的數字  
例如[1,4,5,3,2] =>  [1,5,2,3,4]  
如果找不到比他大的數，就找最小的數  
如[3,2,1] => [1,2,3]  
這題的解法非常巧妙，據說是STL的演算法  
可以見圖解說  
![Alt text](../Res/Picture4.png)
  
我們這裡拿上面的數列做例子  
1. 從右往左找出兩個數字為升序排列的  
這裡是4和5，我們稱4為partition number  
2. 從右找出第一個比partition number大的數字  
這裡是5，我們叫他change number  
3. 把partition number和change number做交換
所以數列變成[1,5,4,3,2]
4. 從原本partition number在的index後面開始  
把其後的數列做反轉  
[1,5,4,3,2] => [1,5,2,3,4]
5. 此數列即為題目要求的答案  
  
  
***

## [042.Trapping_Rain_Water](../SourceCode/Python/042.Trapping_Rain_Water.py) Level: Hard Tags: []
   
思路: 
he following idea is in fact from the last answer in this link, which leads to a clean code. I just reorganize it and add some explanations. I hope it is Ok.

The following are four solutions in C/C++/Java/Python respectively.  
The basic idea is that we set two pointers l and r to the left and right end of height.  
Then we get the minimum height (minHeight) of these pointers  
(similar to Container with Most Water due to the Leaking Bucket Effect) since the level of the water cannot be higher than it.  
Then we move the two pointers towards the center.  
If the coming level is less than minHeight, then it will hold some water.  
Fill the water until we meet some "barrier"  
(with height larger than minHeight) and update left and right to repeat this process in a new interval
  
  
***  
  
### [421.Maximum_XOR_of_Two_Numbers_in_an_Array](../../SourceCode/Python/421.Maximum_XOR_of_Two_Numbers_in_an_Array.py) Level: Medium Tags: [Tricky]
    
Time:  O(n)  
Space: O(n)   
  
思路: 給你一個整數組成的數列  
要你找出用XOR能達到最大值的兩個數  
最直觀的解法是暴力解法，分頭找兩個數來配對，時間複雜度為O(n^2)  
但題目要求在O(n)的時間內解出來  
在這裡引入一個XOR的定律:
```
if  a ^ b = x, then b ^ x = a
# 此^為XOR
```  
我們把所有數字的最高bit放到一個set裡  
然後使用同樣高的bit來對裡面的數字做XOR  
如果XOR過的數字仍在這個set裡的話  
說明這個最高位的bit存在兩個數字的最高位XOR的結果
即 a ^ 1 = b，此b存在於set中  
代表 a ^ b = 1，所以此最高位bit是能找到1的XOR組合的  
依此類推，從高位到低位一直算下去　　
我們就能找到所有讓該位為1的組合，此即為能達到的最大結果　　
　　
我們用題目的範例　[3, 10, 5, 25, 2, 8]　做說明　　
雖然題目寫最大數字可以到2^31(此^為次方)  
但我們不用從31個bit開始算起  
因為25 = 11001 最多五個bit，所以我們從5個bit開始算起  
用mask 0b10000 和 所有數字做AND然後放進set中  
得到 [00000, 00000, 00000, 10000, 00000, 00000]  
set去除重複元素後為 [00000, 10000]  
  
我們用最高位為 10000 來對此set的每個元素做XOR
其中 00000 XOR 10000 = 10000
10000也存在於這個Set中  
所以這個bit是可以被湊出來的，目前的max就是10000  
  
接下來我們看第4個bit的mask，0b01000  
得到 [00000, 01000, 00000, 11000, 00000, 01000]  
剔除重複元素得到 [00000, 01000, 11000]    
我們用目前的max 10000 和第四個bit做 OR 得到 11000  
用11000和此Set裡所有的元素做XOR  
其中，00000 XOR 11000  = 11000  
而11000存在於這個Set中  
所以max為 11000  
  
  
接下來看第3個bit的mask，0b00100  
得到 [00000, 01000, 00100, 11000, 00000, 01000]  
剔除重複元素得到 [00000, 01000, 11000]  
我們用目前的max 11000 和第三個bit做 OR 得到 11100  
用11000和此Set裡所有的元素做XOR  
其中，  
00000 XOR 11100 = 11100 該Set無此元素  
01000 XOR 11100 = 10100 該Set無此元素
11000 XOR 11100 = 00100 00100能在此Set中找到
所以max為 11100  
  
接下來看第2個bit的mask，0b00010  
得到 [00010, 01010, 00100, 11000, 00010, 01000]
剔除重複元素得到 [00010, 01010, 00100, 11000, 01000]
我們用目前的max 11100 和第二個bit做 OR 得到 11110 
其中，  
00010 XOR 11110 = 11100 該Set無此元素  
01010 XOR 11110 = 10100 該Set無此元素  
00100 XOR 11110 = 11010 該Set無此元素  
11000 XOR 11110 = 00110 該Set無此元素  
01000 XIR 11110 = 10110 該Set無此元素  
在此bit中找不到能配對的組合  
所以第2位bit為0  
  
接下來看最後1個bit的mask，0b00001  
得到 [00011, 01010, 00101, 11001, 00010, 01000]  
至此已經不會有重複的元素了  
我們用目前的max 11100 和第一個bit做 OR 得到 11101  
其中  
00011 XOR 11101 = 11110 該Set無此元素  
01010 XOR 11101 = 10111 該Set無此元素  
00101 XOR 11101 = 11000 該Set無此元素  
11001 XOR 11101 = 00100 該Set無此元素  
00010 XOR 11101 = 11111 該Set無此元素  
01000 XOR 11101 = 10101 該Set無此元素  
在此bit中找不到能配對的組合  
所以第1位bit為0  
  
所以我們找到的max就是 11100 = 28  
此為最後的答案  
  
***
