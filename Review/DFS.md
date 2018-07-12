  
  
  
***
  
### [017.Letter_Combinations_of_a_Phone_Number](../SourceCode/Python/017.Letter_Combinations_of_a_Phone_Number.py) Level: Medium Tags: [DFS]
   
思路: 用DFS窮舉所有可能的字串
  
***
  
  
### [133.Clone_Graph](../SourceCode/Python/133.Clone_Graph.py) Level: Medium Tags: [Graph, Sequence DFS]
  
思路:用DFS遍歷所有節點
差別在於接觸到相鄰節點時要做複製的動作
  
  

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
  
  
### [200.Number_of_Islands](../SourceCode/Python/200.Number_of_Islands.py) Level: Medium Tags: []
  
Time:  O(m * n)  
Space: O(m * n)  
思路: 本題是找出與周圍被0包圍的1  
可以使用DFS，利用四個方向去取得每個元素的周圍是否還有0  
已經走過 (visited) 的元素我們用0標示，如此便不會再去走它
  
  
***
 
### [212.Word_Search_II](../../SourceCode/Python/212.Word_Search_II.py) Level: Hard Tags: [DFS, Tree]
  
思路: 題目給了你一個2D陣列，要求你找出給予的單字中是能讓這陣列中的相鄰字元成為該單字  
例如  
words = ["oath","pea","eat","rain"]  
board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
因為e, a, t能在陣列中找出相鄰的字元    
看到2D陣列的traversal便能很自然想到用DFS或BFS解題  
而題目限制字元是a~z的組合也暗示了我們能用 Tries來拆解單字和搜尋  
因為自己寫的code一直敗在其中一個test case  
這裡附上能被Accept的版本  
[212.Word_Search_II_Accept](../../SourceCode/Python/212.Word_Search_II_Accept.py)

***
  
### [329.Longest_Increasing_Path_in_a_Matrix](../../SourceCode/Python/329.Longest_Increasing_Path_in_a_Matrix.py) Level: Hard Tags: [DFS, DP]
  
Time:  O(m * n)  
Space: O(m * n)  

思路:找出2D陣列裡所能排出最長的遞增序列  
這題非常的難，除了要會用DFS Traversal所有可能的元素外  
還要會運用Dynamic Programming  
不然就會敗在題目給的超大2D陣列下吐出Time Limit Exceeded  
  
首先我們先造出全部為0的2D陣列  
這陣列用來記錄曾經找出過的最長序列元素個數  
接著逐行逐列，用DFS找出每個元素所能形成的最長序列個數  
DFS相關的步驟可以寫成另一個函式  
這函式一開始就要先檢查dp陣列裡是否已經紀錄過找過的最長序列元素數  
找過的話就可以直接給遞回中呼叫的 sub function答案以節省時間  
沒有找過的話，我們定出四個方向的tuple  
分別代表目前元素的上下左右方  
然後依次去比較(上下左右)方的元素是否大於目前元素  
是的話深度就+1  
並且遞回呼叫DFS繼續往深處找  
該元素所能達到的最大深度找完後，把它紀錄在dp上  
就能在Leetcode給的時間限制內把所有元素所能到達的最大深度全部算完  
最後只要看dp陣列中的最大值  
就是題目要的答案了  
  
  
***

