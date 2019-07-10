

***
  
### [00263.Ugly_Number](../../SourceCode/Python/Problem/00263.Ugly_Number.py) Level: Easy Tags: [Math]
  
Time:  O(logn)    
Space: O(1)    
  
思路:要我們判斷一個數字是否為醜數(Ugly number)  
醜數的定義是只能被[2,3,5]整除的數  
雖然可以用質因數分解後去看對應的質因數是否為2,3,5的組合    
但本題有時間要求，所以遇到太大的數字會超時  
其中一個解法是拿題目給的數字不斷去除2或3或5  
整除的話就把商塞給原本的數字，繼續除下去  
一旦除到有餘數就換下一個數字  
直到三個數字都除完後看題目最後給的數字是否為1  
是的話就代表是醜數  
反之則一定還有其他數字為題目給的數字的因數  
因此不是醜數  
  
  
***
  
### [00264.Ugly_Number_II](../../SourceCode/Python/Problem/00264.Ugly_Number_II.py) Level: Medium Tags: [Math]  

Time:  O(n)  
Space: O(1)
    
思路: 是 [00263.Ugly_Number](../../SourceCode/Python/Problem/00263.Ugly_Number.py) 的衍伸題  
要知道醜數的定義請看之前的題目   
本題要你找出從1開始排起，排行位於第n個的醜數  
我們當然可以從1開始每個數都挑出來看他是不是醜數  
但這做法非常的慢  
這裡用題目提示給的方法  
仔細觀察一開始的醜數數列  [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]...  
可以發現他們是從大到小的 2 或 3 或 5 相乘的結果  
所以我們可以把他們想成是這樣:  

**1x2**, 2x2, **2x2**, 3x2, **3x2**, **4x2**, 5x2, ....  
1x3, **1x3**, 2x3, 2x3, 2x3, 3x3, **3x3**...  
1x5, 1x5, 1x5, 1x5, **2x5**, 2x5, 2x5...  
  
我們用三個從1開始的index去分別乘上每個醜數的因子 (2,3,5)    
然後去取他們相乘後的最小值  
這時就一定是我們目前能取到最小的醜數  
粗體代表每一次index增加時索取的醜數  
如果該醜數的因子被選中了，他的index就會遞增  
這樣下一輪要取時該因子的數字就可能因為變得比較大  
而讓其他index沒有增加的因子被選為當前最小醜數  
如此一來只要重複n次就能知道第n個醜數是多少了  
  
  
***
  
### [00313.Super_Ugly_Number](../../SourceCode/Python/Problem/00313.Super_Ugly_Number.py) Level: Medium Tags: [Math]
  
思路:思路: 是 [00263.Ugly_Number](../../SourceCode/Python/Problem/00263.Ugly_Number.py)   
和 [00264.Ugly_Number_II](../../SourceCode/Python/Problem/00264.Ugly_Number_II.py) 的衍伸題  
給你一組全新的醜數因子，要你找出第n個醜數  
其實只是把264題的內建醜數因子改成題目給的而已  
所以把264題的解答改成用動態給因子的方式就可以了  
具體思路請參考264題  
    
      
***
