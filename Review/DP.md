
動態規劃表面上很難，其實存在很簡單的準則  
當求解的問題滿足以下兩個條件時， 就應該使用動態規劃：　　
1. 主問題的答案 包含了 可分解的子問題答案  
  （也就是說，問題可以被遞歸的思想求解）
2. 遞歸求解時， 很多子問題的答案會被多次重覆利用  
  
動態規劃的本質思想就是遞歸  
但如果直接應用遞歸方法，子問題的答案會被重覆計算產生浪費    
同時遞歸更加耗費堆疊記憶體    
所以通常用一個二維矩陣（表格）來表示不同子問題的答案  
以實現更加高效的求解。  


***

### [139.Word_Break](../SourceCode/Python/139.Word_Break.py) Level: Medium Tags: [DP, Sequence DP]

給一個String word, 和一个字典, 檢查是否word可以被分開, 而所有substring都應該是dictionary裡面的words.  
  
思路: 從第一個字元開始依次向後尋找，直到找到一個可以分開的地方(斷句)，這時代表目前的substing在dictionary中  
如果找到最後都沒找到，傳回False  
  
找到第一個斷句後，接下來找下一個斷句處，就是從第一個斷句後的字元開始找連續的字串  
但此時和第一次尋找稍微不同，例如說 word = 'ab', dict= {'a', 'ab', ...}
在從word裡找到a之後，接下來要處理的是b，我們發現b不再dict中  
但b可以和a相結合形成ab，而ab在dict中  
所以這裡的每個字串有三個選擇  

+ 自己單獨為個體到dict中尋找
+ 和前面的string合併起來一起找
+ 等後面的新字元，構成更長的substring  

以第二項來說，我們需要跟前面的string合併起來找，所以我們需要紀錄訊息來代表前面的substring  
是從哪裡分開而滿足條件的  
如此我們就能一次從離前一個substring近的部分進行結合  
例如 word = 'aab', dict= {'a', 'aab'}  
處理a時在dict中，處理下一個a也在dict中  
但再下一個b就不在dict中了  
此時就和前面的b結合形成 ab ，但發現也不再dict中  
於是繼續跟前面的substring結合形成aab，此時在dict中了  
於是word便滿足條件

這個紀錄狀態的情況便適合用Dynamic Programming (DP) 來解決

![Alt text](Res/dp.png)


_Initialization_: dp\[0]  
_function_: 
***
  
  
### [140.Word_Break II](../SourceCode/Python/140.Word_Break_II.py) Level: Hard Tags: [DP, Sequence DP, DFS]
  
  
***
  
### [279.Perfect_Squares](../SourceCode/Python/279.Perfect_Squares.py) Level: Medium Tags: [DP]
  
  
思路:這題雖然可以用數學定理的四平方和解題  
( Lagrange's four-square theorem，每個正整數均可表示為4個整數的平方和 )  
但我們在面試中不太可能碰到剛好能用數學定理解題的情況，還是考慮一般解吧。  
此題需要使用的是Dynamic Programming  
而且屬於重疊子問題 (自上而下 ): 每個子問題只解一次，把解保存在一個需要時就可以查看的表中  
每次查表的時間為常數  
  
首先把輸入的正整數所有的完全平方數都找出來並在dp紀錄上填上1  
它是我們之後dynamic programming的依據  
接著從1開始找每個整數(x)加另一個從1開始整數的平方(y)  
例如 x+y*y  
看他們的和是否小於等於n  
是的話就能加入我們的dp筆記     
如果沒寫過的話，就能直接從dp[x]加1(這個1是找到的y給的)  
如果寫過的話，就比較目前筆記裡寫過的值+1有沒有小於目前值  
比較小的話當然採用dp[x]+1  
如此走完整個迴圈，則dp[n]即為答案
  
  
  
  
