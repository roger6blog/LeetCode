

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
