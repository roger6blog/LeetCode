  
  
***

### [003.Longest_Substring_Without_Repeating_Characters](../../SourceCode/Python/003.Longest_Substring_Without_Repeating_Characters.py) Level: Medium Tags: [String, Sliding Window]  
  
Time:  O(n)  
Space: O(1)    
  
思路:給你一個字串  
要你求最大長度的不重複字元子字串的長度  
解題的核心觀念就是題目告訴你的:  
不重複字元子字串，代表這個字串不能存在兩個相同的字元  
所以我們可以用一個Sliding Window來計算這字串的長度  
加上一個dictoionary來儲存目前字串擁有的字元和位置  
一開始這Window的左右邊界都在最左邊  
然後我們讓右邊界的值不斷增加  
在他們兩個中間的字串就是當前最長的不重複子字串  
在右邊界增加的同時，我們把右邊界指向的新字元和dictionary裡的內容比較  
如果dictionary裡不存在這個新字元  
就把他加入裡面並賦值為當前位置
```python
wordDict[char] = index
```
反之如果能在dictionary裡找到這個字元  
說明這個字串已經有字元重複了  
我們應該把左邊界移動到這個重複字元位置的右邊一位  
然後把該字元的位置更新成當前字元所在位置  
```python
if char in wordDict and wordDict[char] >= begin:
    begin = wordDict[char] + 1
```
這裡有一個額外的判斷是wordDict[char] >= begin  
他是為了避免begin會因為某個重複字元出現在begin的前面過  
造成begin往回指的狀況
  
每一次的新增字元都能判斷一次當前最長不重複子字串是否為最大  
整個字元都掃描完後這個當前最長子字串就是答案了    

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

### [056.Merge_Intervals](../../SourceCode/Python/056.Merge_Intervals.py) Level: Medium Tags: [List]  
  
思路: 對Python來說不難，因為Python就有內建List排序  
把題目給的List照start值得順序排好後  
用以下的方式來判斷兩個Interal:  
1. 如果新的List裡面沒Interval，直接加入新List  
2. 如果有的話，比較新List最後一個Interval和要加入的Interval是否有重疊    
  重疊的規則: 新Interval的start值落在最後一個Interval的區間裡(相同值也算)    
  如此不斷iterate所有元素  
  新List即為答案  
  
***

### [074.Search_a_2D_Matrix](../../SourceCode/Python/074.Search_a_2D_Matrix.py) Level: Medium Tags: []
  
Time:  O(logm + logn)  
Space: O(1)  
  
思路:在一個已排序的2D List中找出某個元素  
最直觀的解法當然是用for去找，不過此解法只能得到O(n)  
既然這List已經被排序，就算它分成幾個小List  
我們還是能用BinarySearch來找出我們要的元素  
```python
while left < right:
    mid = left + (right - left) / 2
    if matrix[mid / col][mid % col] >= target:
        right = mid
    else:
        left = mid + 1
```
所以最佳解為O(nlog(n))  
  
  
***

### [079.Word_Search](../../SourceCode/Python/079.Word_Search.py) Level: Medium Tags: [DFS]
  
Time:  O(m * n * k)  
Space: O(k)  
k is length of word
  
思路: 給你一個由字母組成的2維陣列和一個單字  
要你判斷這個單字能不能在這陣列中找到   
這是個典型的深度搜索(DFS)問題  
我們可以把每一個端點都當作起點  
然後從這端點進行上下左右的DFS  
下一個端點如果是我們預期的字母就繼續同樣的動作  
反之如果超過邊界，或是不是我們預期的字母就返回False  
返回True的條件看要怎麼寫  
我這裡是如果現在搜尋到的是我們預期的字母  
就把這個字母從目前的單字裡移除  
如此一來返回True的條件就是這個單字變數變為空字串  
  
在搜尋過程中我們要防止自己走過的地方又走回來  
這裡有很多種方式，只要和原本走過的字母不同就可以  
例如改為'.'、'#' 等等  
Python的話可以用swapcase變換字母大小  
寫起來稍微優雅些  
  
  
***
  
### [179.Largest_Number](../../SourceCode/Python/179.Largest_Number.py) Level: Medium Tags: [Sort]

Time:  O(nlogn)  
Space: O(1)
      
思路:在一串數字中找出所能排列的最大數字  
Python雖然有內建排序  
但是我們在排序時還需要確認兩個數字接起來時誰比較大
如 201和9 單比數字時是201大
但接起來時很明顯9201比2019大  
python sort的cmp函式在這裡可以派上用場  
cmp函式:
```python
if str(a)+str(b) > str(b) + str(a):
    return 1
else:
    return -1
```

這裡要知道Python的數字string是可以比大小的  
  
***
  
### [133.Clone_Graph](../../SourceCode/Python/133.Clone_Graph.py) Level: Medium Tags: [Graph, DFS]
  
Time:  O(n)  
Space: O(n)  
  
思路：題目要求你clone一個無向圖  
就是把整個圖走一遍然後順便把圖的節點加進去而已  
DFS或BFS皆可  
  
  
***
  
### [139.Word_Break](../../SourceCode/Python/139.Word_Break.py) Level: Medium Tags: [DP, Backtracking]
  
Time:  O(n * j), worst case is O(n^2)  
Space: O(n)    
  
思路: 給你一個用任意字母片段的List  
要你判斷用這些片段是否能湊出輸入的英文片段  
例如
```python
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
```
s可被字典裡的字串拼出來，所以結果為True  

第一個方法是從第一個字元開始依次向後尋找，直到找到一個可以分開的地方(斷句)，這時代表目前的substing在dictionary中    
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
此時就和前面的b結合形成 ab ，但發現也不在dict中  
於是繼續跟前面的substring結合形成aab，此時在dict中了  
於是word便滿足條件

第二個方法是  
在拼湊的過程中，我們會需要不斷檢查之前拼湊的結果
所以可以用Dynamic Programming解題  

首先我們先宣告一個長度比輸入字串多1的一維陣列  
除了第一個是True外，其他內容全為False，如:

|   | c | a | t | s | a | n | d | o | g |
|---|---|---|---|---|---|---|---|---|---|
| T |   |   |   |   |   |   |   |   |   |

接著我們從第一個字元c來開始掃描他們有沒有在預設的字典中  
c我們可以看到字典裡沒有這個字，所以是False
第二個字起比較複雜  
我們比較的順序會是這樣:   
ca=>a  
第三個字加入後會是:
cat=>at=>t
我們發現cat有符合字典中的字了  
所以在t的位置把False改成True  

|   | c | a | t | s | a | n | d | o | g |
|---|---|---|---|---|---|---|---|---|---|
| T |   |   | T |   |   |   |   |   |   |


第四個字母加入後會是:  
cats=>ats=>ts=>s  
和上面一樣，字典裡有cats這個字  
所以在s的位置改成True

|   | c | a | t | s | a | n | d | o | g |
|---|---|---|---|---|---|---|---|---|---|
| T |   |   | T | T |   |   |   |   |   |

第五個字母加入後是catsa  
catsa=>asta=>sta=>ta=>a  
沒什麼好說的
    
第六個字母加入後事catsan  
catsan=>astan=>tsan=>san=>an=>n  
在比到san的時候，因為san是在字典裡的字  
我們除了看san本身外，也要回頭去看扣掉san的字串比對的結果  
而扣掉san的字串是cat，之前的比對結果是True  
所以這裡我們也能填上True    

|   | c | a | t | s | a | n | d | o | g |
|---|---|---|---|---|---|---|---|---|---|
| T |   |   | T | T |   | T |   |   |   |
  
  
第七個字母加入後為 catsand，省略
第八個字母加入後為 catsando，省略
第九個字母加入後為 catsandog
catsandog=>atsandog=>tsandog=>sandog  
=>andog=>ndog=>dog=>og=>g  
在dog時，我們會去參考剩下的字串的比對結果，就是catsan
這在剛才的比對中已經證明為True了  
所以dog這裡也可以寫為True  

|   | c | a | t | s | a | n | d | o | g |
|---|---|---|---|---|---|---|---|---|---|
| T |   |   | T | T |   | T |   |   | T |

全部比完後我們看最後面的比對結果  
就是題目要的答案  
  
下圖是另一個用DP的範例  
![Alt text](../Res/dp.png)
  
***
  
### [163.Missing_Ranges](../../SourceCode/Python/163.Missing_Ranges.py) Level: Medium Tags: []
  
Time:  O(n)  
Space: O(n)
    
思路: 題目給你一組排序過的數列  
要你找個每個元素間漏掉的數字，用 a->b表示  
我們可以使用雙指標  
pre指標指向前一個元素、curr指標指向後面一個元素  
不斷的比較前一個元素和後一個元素是否有大於2的差距  
如果有的話代表有Missing range  
把這兩個元素的區間逐個印出來就大功告成  
需注意判斷lower和upper的區間
  
***
  
### [166.Fraction_to_Recurring_Decimal](../../SourceCode/Python/166.Fraction_to_Recurring_Decimal.py) Level: Medium Tags: []
  
Time:  O(logn), 
where logn is the length of result strings    
Space: O(1)    
  
思路: 題目要求你找出不同數字相除後的小數，如果有循環則在循環的數字中括號  
除了最基本的兩數相除取模和找商之外  
我們需要一個dictionary來記錄該小數點數字出現的位置  
不能直接把小數點數字加入list再去搜尋該list  
否則會無法處理小數點數字重複的情況如: 1/333=0.(003)  
  
***
  
### [200.Number_of_Islands](../../SourceCode/Python/200.Number_of_Islands.py) Level: Medium Tags: []
  
思路: 本題是找出與周圍被0包圍的1  
可以使用DFS，利用四個方向去取得每個元素的周圍是否還有0  
已經走過 (visited) 的元素我們用0標示，如此便不會再去走它  
  
***
  
### [208.Implement_Trie_(Prefix_Tree)](../../SourceCode/Python/208.Implement_Trie_(Prefix_Tree).py) Level: Medium Tags: []
  
Time:  O(n), per operation
Space: O(1)
思路:本題要求你實作一個字典樹(Trie)的insert, search和startWith  
在此之前你必須先了解字典樹是什麼  
  
![一個保存了8個鍵的trie結構，"A", "to", "tea", "ted", "ten", "i", "in", and "inn".](../Res/1200px-Trie_example.svg.png)
  
簡單來說就是一個方便搜尋同樣Prefix單字的樹  
有同樣prefix字的單字會被插到同一條Trie  
roo節點通常為空，底下有a~z 26個子Trie  
好處是用空間換取時間  
搜尋速度比未最佳化的Hash快，只要O(n)    
壞處就是浪費空間和比不上最佳化的Hash  
雖然圖裡沒提到  
不過通常建構Trie時都會加上isword屬性  
題目有三個function要實作:    
insert、search、startwith  
比較特別的是startwith  
只要隨著輸入的字母不斷往下traversal  
在輸入的字母全跑完之前這條Trie還沒有走到底部  
就代表能找到startwith 輸入的單字  
  
***
  
### [228.Summary_Ranges](../../SourceCode/Python/228.Summary_Ranges.py) Level: Medium Tags: []
  
Time:  O(n)  
Space: O(1)  
  
思路:要你印出一個排序的正整數陣列的Range  
例如 [0,1,2,4,5,7] => ["0->2","4->5","7"]  
最簡單的方式是用兩個while  
一個while遍歷所有元素  
內層的while則是判斷遍歷的前後元素是否為連續  
連續的話則外層while的變數+1  
如此便可和進入內圈while前的變數做對照找出前後範圍  
  
  
***
  
  
  
### [230.Kth_Smallest_Element_in_a_BST](../../SourceCode/Python/230.Kth_Smallest_Element_in_a_BST.py) Level: Medium Tags: [Recursive]
  
Time:  O(max(h, k))  
h is height of tree  
Space: O(h)  
  
思路: 在一個二元樹中找出第K小的元素  
Python的話可以先traversal整個二元樹(BFS或DFS都行)    
然後對traversal後的list做sort  
如此便知道第K個元素是誰了  
一般的遞迴方法則是從左子樹走起  
遞迴尋找此二元樹的child  
每找到一個就把k減去1   
當k減到0時該元素即為答案  
  
  
***

### [240.Search_a_2D_Matrix_II](../../SourceCode/Python/240.Search_a_2D_Matrix_II.py) Level: Medium Tags: [Recursive]
  
Time:  O(row + col)  
Space: O(1)
  
思路:   
是[074.Search_a_2D_Matrix](../../SourceCode/Python/074.Search_a_2D_Matrix.py) 的衍伸題    
不同的是這次的2D Matrix是呈螺旋狀遞減，但基本還是西高東低  
所以同樣也能用遞迴解題，甚至可能用同樣的解法來解題  
只有效率的差別  
我們這次在這裡採用非遞迴的解法  
我們從該2D Matrix的最右上角開始比對  
如果比target大的話說明元素在我們的左手邊，所以目標col-1  
如果比target小的話說明元素在我們的下面，所以目標row+1    
終止條件為超過matrix的邊界  
這種搜尋方式稱為階梯式搜尋  
  
  
***
  

### [246.[Locked]Strobogrammatic_Number](../../SourceCode/Python/246.[Locked]Strobogrammatic_Number.py) Level: Medium Tags: []
  
Time:  O(n)  
Space: O(1)  
  
思路:Strobogrammatic Number是對稱數，亦即左右上下翻轉都能維持原狀的數  
本題只要求上下翻轉，不過都差不多  
解法為預設一個dictionary，上面寫好應該要對應的key-value pair  
例如 1:1, 6:9, 8:8  
然後從中間切半，不斷比對左右兩邊的元素是否是dictionary預期的即可  
  
  
***

### [247.[Locked]Strobogrammatic_Number_II](../../SourceCode/Python/247.[Locked]Strobogrammatic_Number_II.py) Level: Medium Tags: [Recursive]
  
Time:  O(n^2 * 5^(n/2))
Space: O(n)
  
思路:[246.[Locked]Strobogrammatic_Number](../../SourceCode/Python/246.[Locked]Strobogrammatic_Number.py) 的衍伸題目  
這次是要求你組出一個n長度的所有對稱數  
但題目也好心的提示你要用遞迴來做，還告訴你要用n-2來當遞迴條件(因為是對稱數)  
重點就在於遞迴的參數，我們一開始呼叫帶兩個n的遞迴function  
每呼叫一次其中一個n就減2並組合可能的字串  
如此一直到減去的n為1或0即為終止條件  
最後要注意一點，最外層的數不能是0，所以需要加判斷條件去掉  

  
***

### [249.[Locked]Group_Shifted_Strings](../../SourceCode/Python/249.[Locked]Group_Shifted_Strings.py) Level: Medium Tags: []
  
Time:  O(nlogn)  
Space: O(n)  
  
思路: 題目要你把[字元間隔]一樣的字串歸類  
例如 abc 他們的字元間隔就是1，但a和z的字元間隔也是1  
所以歸類時需要有循環的觀念  
我們可以用 % 運算子做到循環的效果，來算出每個字串的字元間隔  
例如 abc就是 [1,1] xyz也是[1,1]  
由此可得這兩個字串的字元間隔相同，便可將他們歸在同一類  
我們可以把 [1,1]當作索引存到一個dictionary  
value即為歸類於此的各個字串組成的List  
  
  
***
  
### [251.[Locked]Flatten_2D_Vector](../../SourceCode/Python/251.[Locked]Flatten_2D_Vector.py) Level: Medium Tags: []
  
Time:  O(1)  
Space: O(1)  
  
思路: 題目很難弄懂  
他的要求是要你把一個2D List壓平後用2個iterator把裡面的元素印出來  
因為有iterator的要求所以其他方法都不能用  
這兩個iterator，第一個iterator疊代最外面的List  
第二個iterator疊代裡面List的元素
首先用Python內建的iter把輸入的Vector疊代化，名為x  
在hasNext方法中，檢查有沒有第二個疊代器y  
有的話就把之後next要返回的值塞入第二個疊代器指向的元素值  
對於StopIteration的處理，因為第二個疊代器已經沒有元素了  
所以需要把當前的第二個疊代器刪除，重新產生一個新的  
  
如果一開始就沒有第二個疊代器  
那就把第一個疊代器的下一個List拿來疊代化，產生一個新的  
對於StopIteration的處理，就是告訴caller下面沒有了  
  
  
***
  
### [264.Ugly_Number_II](../../SourceCode/Python/264.Ugly_Number_II.py) Level: Medium Tags: [Math]  

Time:  O(n)  
Space: O(1)
    
思路: 是 [263.Ugly_Number](../../SourceCode/Python/263.Ugly_Number.py) 的衍伸題  
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
  
### [279.Perfect_Squares](../../SourceCode/Python/279.Perfect_Squares.py) Level: Medium Tags: [DP]
  
  
思路:檢查所給的數字能被多少個完美平方數相加  
例如 13 可以分成4和9 所以答案為2  
這題雖然可以用數學定理的四平方和解題  
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
  
  
***
  
### [280.[Locked]Wiggle_Sort](../../SourceCode/Python/280.[Locked]Wiggle_Sort.py) Level: Medium Tags: [Sort]
  
Time:  O(n)  
Space: O(1)  
  
思路:把輸入的陣列元素按照山峰的形狀排列  
nums[0] <= nums[1] >= nums[2] <= nums[3]....  
對於Python來說很簡單的一題  
先用sort排序後，每隔2個元素互相交換其值  
便能達到搖擺排序的效果了  
  
  
***
  
### [284.Peeking_Iterator](../../SourceCode/Python/284.Peeking_Iterator.py) Level: Medium Tags: [Iterator]
   
Time:  O(1) per peek(), next(), hasNext()  
Space: O(1)   
  
思路:要你在一個為Iterator基礎的iterator建立其相關method  
例如next、hasNext,peek等  
因為Python沒有內建hasNext，所以這method建立稍麻煩點  
peek也是題目特別要求的method  
關於hasNext的部分，我們可以用題目已經提供的hasNext method  
(有興趣的話可以看Soruce code裡題目提供的hasNext())  
peek的要求是告訴我們下一個元素的值  
因為內建的next會自動疊代到下一個元素  
所以我們需要設一個peekflag，預設為False  
當peek被呼叫時把next得到的元素存到另一個全域變數去
然後把peekflag設為True  
如此當之後呼叫該class的next()時  
我們可以看peekflag查之前有沒有呼叫過peek()  
有的話就直接return全域變數內存的值  
並把相關的變數重設回預設值  
反之的話就能直接呼叫該iterator的next來取值  
    
    
***
  
### [289.Game_of_Life](../../SourceCode/Python/289.Game_of_Life.py) Level: Medium Tags: [List, Bit manipulation]
  
Time:  O(m * n)  
Space: O(m * n)  Follow up: O(1)    
  
思路:題目非常的長，大部分的篇幅在講解有名的生命遊戲 (Game of Life)    
如果你寫過的話便能很快上手  
簡單來說，給你一個0與1構成的多維陣列，每個元素代表一個元素的狀態    
1代表活、0代表死  
對任何細胞來說，他的鄰居有2~3個都是活的，他下一次的狀態就是活的  
反之則代表下一次狀態細胞會死亡    
因為題目要求直接對輸入的陣列做in-place操作  
我們需要多拷貝一個陣列來記錄原本的狀態  
然後寫另外一個函式來比較每個元素的周圍八個方向有多少個活細胞  
計算出來後我們便能得知每個細胞下一個狀態的生死了  
  
Follow up要求我們在不能使用額外空間的情況下得出陣列的下一個狀態  
此時需要使用 Bit manipulation　來統計細胞的狀態　　
1. 00 : Dead -> Dead  

2. 01 : Live -> Live  

3. 10 : Live -> Dead  

4. 11 : Dead -> Live  
最關鍵的Bit為 2(10) 和 3(11)  
把之前的程式碼判斷"生轉死"或"死轉生"的部分改成bit標示    
你會得到一個由0~3組成的新陣列  
接著用 1做and運算便可得知下一個陣列的狀態  
然而計算鄰居個數的部分此時也需要做相對應的修改    
因為你統計鄰居時可能會統計到生轉死(2)的細胞  
統計到此細胞的時候需要把它改成3，也就是翻盤的狀態  
  
  
***
  
### [309.Best_Time_to_Buy_and_Sell_Stock_with_Cooldown](../../SourceCode/Python/309.Best_Time_to_Buy_and_Sell_Stock_with_Cooldown.py) Level: Medium Tags: [DP]
  
Time:  O(n)  
Space: O(n)  
  
思路: 是[122.Best_Time_to_Buy_and_Sell_Stock_II](../../SourceCode/Python/122.Best_Time_to_Buy_and_Sell_Stock_II.py)   
     和[121.Best_Time_to_Buy_and_Sell_Stock_II](../../SourceCode/Python/121.Best_Time_to_Buy_and_Sell_Stock.py) 的延伸  
如果不熟動態規劃()Dynamic Programming)的話  
這題可以算是Hard了  
題目和之前幾題一樣都要求買低賣高，但多了冷卻期  
也就是賣出後的那一天不能買進股票  
如果你第一天買入，第二天賣出的話  
你得等第四天後才能買進第二筆  
  
這裡用動態規劃需要令兩個List  
分別是buy和sell，長度為prices長度  
buy[i]和sell[i]分別代表第i天持股股票的最大利潤  
和第i天賣出股票時的最大利潤  
這裡我們要寫出他們的狀態轉移方程  
對於buy[i]，最大利潤有兩種可能:  
1. 前一天的持股buy[i-1]，到今天仍未賣出  
2. 之前賣出股票後今天買了股票，花掉了prices[i]
因為有一天的冷卻期，所以是sell[i-2]-prices[i]  
第i天的買進最大利潤就為  
```python
buy[i] = max(buy[i-1], sell[i-2] - prices[i]
```
  
對於sell[i]，最大利潤有兩種可能:  
1. 前一天賣出後，今天仍然沒買進股票  
所以最大利潤是sell[i-1]  
2. 前一天買進後，今天賣出持股得到了今天股價prices[i]  
所以是buy[i-1] + prices[i]  
所以我們可以知道sell[i]的最大利潤為:  
```python
sell[i] = max(sell[i-1], buy[i-1] + prices[i])
```
  
不斷轉移狀態到最後一天賣出持股 (sell[len(prices)-1])  
就是我們所能達到的最大利潤了  
  
  
***
  
### [313.Super_Ugly_Number](../../SourceCode/Python/313.Super_Ugly_Number.py) Level: Medium Tags: [Math]
  
思路:思路: 是 [263.Ugly_Number](../../SourceCode/Python/263.Ugly_Number.py)   
和 [264.Ugly_Number_II](../../SourceCode/Python/264.Ugly_Number_II.py) 的衍伸題  
給你一組全新的醜數因子，要你找出第n個醜數  
其實只是把264題的內建醜數因子改成題目給的而已  
所以把264題的解答改成用動態給因子的方式就可以了  
具體思路請參考264題  
  
  
***
  
### [318.Maximum_Product_of_Word_Lengths](../../SourceCode/Python/318.Maximum_Product_of_Word_Lengths.py) Level: Medium Tags: [Bit Manipulation]
  
Time:  O(n^2)  
Space: O(n)  (用Bit可再降低點空間複雜度)  
  
思路: 給你一組由不同單字組成的陣列  
要你找出每兩個單字所能組成的最大乘積  
這兩個單字必須要沒有共同字母才能相乘  
例如 ["abcw","baz","foo","bar","xtfn","abcdef"]  
因為"abcw" 和 "abcdef"有共同字母，所以不能相乘  
因為有共同字母的限制，所以我們在找最大乘積前得先解決這個問題  
單純的相互比對字串會造成超時 (Time Limit Exceed)  
所以我們要用其他方式來加速比對  
網路上推薦使用Bit操作，因為題目描述限制字母只有小寫  
一個32bit的整數就能囊括26個英文字母  
不過也能使用Python的Set來操作  
先把每個單字分別儲存到不同的Set中，再交叉比對作聯集  
如果是空集合就代表符合題目要求  
不斷循環找出最大乘積即為答案  
  
  
***
  
### [324.Wiggle_Sort_II](../../SourceCode/Python/324.Wiggle_Sort_II.py) Level: Medium Tags: [Sort]
  
Time:  O(nlogn)  
Space: O(n)  
  
思路:是[280.[Locked]Wiggle_Sort](../../SourceCode/Python/280.[Locked]Wiggle_Sort.py) 的衍伸  
和280不同的是peak間的元素不能相等，所以原本的方法不能用了  
但解法其實也不難  
把原本的陣列先排序好之後存到另一個陣列  
然後在新陣列中找出最中間的元素  
依照這中位數元素把新陣列分成左右半邊  
由此可知左邊一定是小元素，右邊一定是大元素    
接著使用一套準則來填充新元素到舊陣列裡(因為題目要求return為原本的陣列):  
1. 把較小半邊的小陣列取最後一個，較大元素的小陣列取最後一個  
2. 把舊陣列的第一、二元素分別填上小陣列取的值和大陣列取的值
3. 重複1和2，把舊陣列的值填完    
照上述步驟便可排序完成     
  
  
Follow up是挺難的題目  
思路如下:  
1. 使用Quick排序，從未經排序的nums中挑選出mid  
2. 參考一開始的思路，把nums陣列的下標從  
[0, 1, 2, ... , n-1, n] mapping到  
[1, 3, 5, ...., 0, 2, 4,...]得到新的下標  
3. 以中位數mid為界，將大於mid的元素排列在新下標的較小部分  
而將小於mid的元素排列在新下標的較大部分  
  
  
***
  
### [325.[Locked]Maximum_Size_Subarray_Sum_Equals_k](../../SourceCode/Python/325.[Locked]Maximum_Size_Subarray_Sum_Equals_k.py) Level: Medium Tags: [String]
    
Time:  O(n)  
Space: O(n)  
  
思路: 是[560.Subarray_Sum_Equals_K](../../SourceCode/Python/560.Subarray_Sum_Equals_K.py)的類似題  
差別只在於560是求總和為K的數列數量  
本題是求最長的總和為K的子數列長度  
所以解題思路也類似，都用到sum - (sum - k) == k 的原理  
處理條件則有所差別  
如果sum不在當前hash中的話，就把當前index存到hash  
如果sum剛好等於k的話，那最大長度就是index + 1   
另外當sum-k (之前出現過的sum)在has中的話  
最大長度就是目前最大長度和當前index減去之前出現過的sum的index
```python
maxLen = max(maxLen, x - prefixSum[sum - k])
```
  
***
  
### [332.Reconstruct_Itinerary](../../SourceCode/Python/332.Reconstruct_Itinerary.py) Level: Medium Tags: [Graph, DFS]
  
Time:  O(t! / (n1! * n2! * ... nk!)),   
t is the total number of tickets,  
ni is the number of the ticket which from is city i,  
k is the total number of cities.  
Space: O(t)  
      
思路: 給你幾張飛機票組成的List  
上面由 [起點->終點] 組成  
要你求出順路而且用掉所有機票的順序，且順序要照字母排序  
看到機票、路徑，很容易可以想到是Graph問題  
而Graph的Traversal就是用DFS  
然而因為目標可能會重複，所以建立圖時一開始就要注意這裡  
可以用defaultdict，或是用自己用if else來判斷  
如此我們可以建立一個以list為值的字典  
list內為這個key能夠飛到的地點  
  
我們另外寫一個dfs函式  
函式內一開始用for迴圈把所有起點能飛到的點都做疊代  
也就是一個個計算他們所能飛到的路徑  
在這過程中我們需要把要飛過去的路徑從字典中暫時刪除
```python
ans.append(spot)
travel[spot].remove(dst)            
if len(travel[spot]) == 0:
    travel.pop(spot)
```  
然後再用DFS繼續搜索剩下能飛的點
```python
valid = self.dfs(travel, ans, dst, tickets)
```  
如果過程中發現沒有能飛的點了，就直接返回
```python
if travel == {}:
    return
```    
如果過程發現沒有能走的點了，也直接返回  
```python
if spot not in travel:
    return
```    
這樣的返回結果會是None，我們用valid這變數來接dfs的結果  
如果valid有值，代表這條路走得通  
我們就能在遞迴裡返回結果valid  
```python
if valid:
    return valid
```    
不要忘記結束該次遞迴後要把原本扣掉的點再加回去  
才能繼續下一次的dfs搜尋  
```python
key = spot
..
..
ans.pop()
if key not in travel:
    travel[key] = [dst]
else:
    travel[key].append(dst)
``` 
還有一點很重要的是題目要求照字母順序來選點  
所以我們在for迴圈時就要先把能走的List做排序  
```python
for dst in sorted(travel[spot]):
```       
最後一個最重要的判斷條件  
只要ans List的元素數量已經到了我們的預期  
就要中斷dfs搜尋並返回結果
```python
if len(ans) == len(tickets) + 1:
    return ans
```
這結果就是題目要求的答案 
      
    
***
  
### [341.Flatten_Nested_List_Iterator](../../SourceCode/Python/341.Flatten_Nested_List_Iterator.py) Level: Medium Tags: [Iterator]
  
Time:  O(n), n is the number of the integers.  
Space: O(h), h is the depth of the nested lists.  
  
思路:本題要你用iterator把所有巢狀List中的元素疊代出來  
和  [251.[Locked]Flatten_2D_Vector](../../SourceCode/Python/251.[Locked]Flatten_2D_Vector.py) 有點相似    
可是251題的Input全部都是List而這題有時Input會有數字    
因為iter有個條件是要疊代的元素需要全部屬於同一種type  
所以我們不能用251題的解法來解此題  
我們可以用一個List代表要疊代的元素，依次把原本List中的元素倒給他    
之後的next方法就只是pop這List裡的第一個元素了  
hasNext方法中，有一個很重要的步驟是當我們的List接到元素時    
需要判斷接到的是數字或是List  
List的話還需要對他做進一步的處理才能給next方法用    
  
如果Input的List和我們的List都空了  
說明後面已經沒有東西能疊代了  
此時就能return False  
  
   
***  
  
### [357.Count_Numbers_with_Unique_Digits](../../SourceCode/Python/357.Count_Numbers_with_Unique_Digits.py) Level: Medium Tags: [Math]
  
Time: O(n)   
Space: O(1)
    
思路: 給你一個x，0 <= x < 10^n  
要你求在這範圍內所有不重複數字的數字  
例如x = 2時，11,22,33....99就不能算，如此共有100-19=81個數字  
直覺的作法是把每個數字挑出來去檢查是否有重複數字的數字  
但此法很明顯的在n越大時他的時間複雜度會是指數級的O(10^n)  
所以不可能用此解法  
這裡我們用簡單的排列組合來解題  
n = 1 時，可以有0~9個數字的排列組合共10個數字  
n = 2 時，十位數不能用0所以只能用1~9  
個位數則從10個少了1個數字  
所以有 9*9 共81個組合  
n = 3 時，只剩8個數字可選  
所以是 9*9*8的組合  
n繼續往上加可以很容易地發現能使用的數字持續減少  
到n=11時已經完全不可能有不重複的數字  
我們可以用一個陣列存使用的數字  
即  [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]  
接著看題目給的n多少就從這陣列拿多少進去算  
不過這種算法只能算 n 個數字的組合  
我們要從1算到n然後全部作加總  
如此便為題目所求  

其實這題根本是數學題  
甚至你可以先算出來每個n的組合直接return結果  
所以這題的差評很多
     
   
***  
  
### [375.Guess_Number_Higher_or_Lower_II](../../SourceCode/Python/375.Guess_Number_Higher_or_Lower_II.py) Level: Medium Tags: [DP]
  
Time:  O(n^2)  
Space: O(n^2)  
    
思路: 是[374.Guess_Number_Higher_or_Lower](../../SourceCode/Python/374.Guess_Number_Higher_or_Lower.py) 的衍伸題  
但解法完全不同  
雖然一樣是猜數字，但這次每猜一個數字你就要多花該數字的錢  
給你一個數字為n的範圍，如果n=10的話  
就要你找出猜1~10範圍內數字猜中所需花費的最小金錢  
這是一個Dynamic Programming的題目 (DP) 
因為每個範圍內的結果都是之前範圍可以推得的  
我們在這裡宣告一個 (n+1) * (n+1) 的2維DP陣列  
每行每列分別代表猜[行~列]範圍內的數字  
例如[第一行, 第十列] 就是 1~10內的猜數字    
所以算出 dp[1][10]就是答案  
  
底下我們用n=5來作範例   
當我們在猜範圍1~5的數字時  
如果今天答案是5而我們猜4，會得到太小的結果  
這時下一次就一定能猜到答案就是5了  
但我們並不能預期題目會主動告訴我們太大還是太小  
所以我們不論太大的結果或太小的結果都要算  
然後取他們的最小值  
假如我們猜了一個數字k  
這時會產生三種成本:  
1. 猜中了，那成本就是這個k的大小  
2. k太大，那成本就是k加上猜 (1, k-1) 的範圍內保證能贏所需的錢    
3. k太小，那成本就是k加上猜 (k+1, n) 的範圍內保證能贏所需的錢  
  
上面這三個情況可以寫成  
1. guess = k
2. guess = k + dp[1][k-1]  
3. guess = k + dp[k+1][n]  
  
我們每猜一個K最高就是需要花上  
max(k, dp[1][k-1], dp[k+1][n])
因為k是非得花下去的金錢，我們可以把他抽出來  
變成 max(dp[1][k-1], dp[k+1][n]) + k    
所以我們要求的最小成本就是  
依次求出猜每個數所得到的最大成本  
然後取他們的最小值  
即為題目要求的最低成本  

n為5的動態表格如下表，初始值都是0  

|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   |   |   |   |
| 3 |   |   |   |   |   |   |
| 4 |   |   |   |   |   |   |
| 5 |   |   |   |   |   |   |
      
  
這裡計算的範圍和一般的印象有點不同，大體上是這樣的:
我們先從最右邊的範圍找起，如下圖
```
         guess -->
1  2  3    4     5
           i <-> j
```
```
       guess -->
1  2     3    4     5
         i   <--->  j
```
```
  guess ----->
1  2     3    4     5
   i    <-------->  j
```
也就是每次先界定好要猜數字的範圍  
然後從左邊猜到右邊來算出最小成本  
  
照上圖找法
我們從i->left=4、j->right=5的範圍先找起  
在這範圍內很明顯你的最低成本只可能是4  
所以我們先在這裡填上4
    

|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   |   |   |   |
| 3 |   |   |   |   |   |   |
| 4 |   |   |   |   |   | 4 |
| 5 |   |   |   |   |   |   |      
      
下一個要填的是left=3、right=5的範圍  
如果範圍縮小到3~4的話，很容易得出最高成本為3
所以我們在dp[3][4]填入3

|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   |   |   |   |
| 3 |   |   |   |   | 3 |   |
| 4 |   |   |   |   |   | 4 |
| 5 |   |   |   |   |   |   |      
  
那麼dp[3][5]，我們猜3時又是如何呢?  
照我們剛才推導出的公式  
max(dp[left][guess-1], dp[guess+1][right])  
我們可以得知他的最大成本應該是  
max(dp[3][2], dp[4][5]) + 3  
其中dp[3][2]為0 (事實上根本不可能存在這種猜測方式，因為左邊界大於右邊界)  
dp[4][5]是我們已經找出的最小成本  
於是dp[3][5]的最小成本就是 4+3 = 7
   
|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   |   |   |   |
| 3 |   |   |   |   | 3 | 7 |
| 4 |   |   |   |   |   | 4 |
| 5 |   |   |   |   |   |   |  
  
但這並不是dp[3][5]的最終最小成本  
因為我們在猜4的時候可以發現  
dp[3][5] = max(dp[3][3], dp[5][5]) + 4
可以得到最小成本為 4，這小於我們剛才找到的7    
所以dp[3][5]的最終最小成本應該為4
  
|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   |   |   |   |
| 3 |   |   |   |   | 3 | 4 |
| 4 |   |   |   |   |   | 4 |
| 5 |   |   |   |   |   |   |  
  
繼續猜dp[2][3]  
我們從之前例子可以先知道 dp[2][3]的最小成本必定為 2  
 
|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   | 2 |   |   |
| 3 |   |   |   |   | 3 | 4 |
| 4 |   |   |   |   |   | 4 |
| 5 |   |   |   |   |   |   |  
   
   
dp[2][4] 則和之前的dp[3][5]一樣  
一開始我們會因為先猜2而得到最小成本為5  
但改成先猜3後我們就會發現最小成本應該是 3  
於是會變成下表  

|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   | 2 | 3 |   |
| 3 |   |   |   |   | 3 | 4 |
| 4 |   |   |   |   |   | 4 |
| 5 |   |   |   |   |   |   |  
   
考慮d[2][5]的情況  
一開始我們先猜2，會得到  
dp[2][5] = max(dp[2][1], dp[3][5]) + 2  
dp[2][5] = 6 這樣的答案  
先猜3的話則是
dp[2][5] = max(dp[2][2], dp[4][5]) + 3  
dp[2][5] = 7
先猜4的話則是  
dp[2][5] = max(dp[2][3], dp[5][5]) + 4  
dp[2][5] = 6  
所以最後的最小成本為6 
  
|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   | 2 | 3 | 6 |
| 3 |   |   |   |   | 3 | 4 |
| 4 |   |   |   |   |   | 4 |
| 5 |   |   |   |   |   |   |  


最後幾行的計算我們就省略了，可以得到  

  
|   |   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|   |   |   | 1 | 2 | 4 | 6 |
| 1 |   |   | 1 | 2 | 4 | 6 |
| 2 |   |   |   | 2 | 3 | 6 |
| 3 |   |   |   |   | 3 | 4 |
| 4 |   |   |   |   |   | 4 |
| 5 |   |   |   |   |   |   |  

其中dp[1][5] 就是範例所要的範圍  
故最終最小成本為6  

本題也可以用遞迴解  
但因為時間複雜度最差可高達O(n^3)，速度會差疊代非常多  


***  
  
### [378.Kth_Smallest_Element_in_a_Sorted_Matrix](../../SourceCode/Python/378.Kth_Smallest_Element_in_a_Sorted_Matrix.py) Level: Medium Tags: [Binary Search]
  
Time:  O(k * log(min(n, m, k))), with n x m matrix  
Space: O(min(n, m, k))  
  
思路: 給你一個行和列都有排序的整數二維陣列  
要你找出第k小的元素是什麼  
直觀的作法是把所有元素倒到一個陣列後排序  
然後找出下標k-1的元素  
這種解法雖然能通過Leetcode，但不是最佳解  
這裡我們用Binary Search的方式    
左右邊界分別為第一個和最大的元素  
那middle當然是他們中間的元素    
在迴圈中  
我們再用一次Binary Search  
去尋找小於middle元素的個數  
如果這個個數小於題目要求的k，代表middle太小  
左邊界就改為 middle+1
反之則右邊界改為 right-1  
直到左右邊界交會後，左右邊界的其中一個即為所求  
   
***  
  
### [394.Decode_String](../../SourceCode/Python/394.Decode_String.py) Level: Medium Tags: []


思路:給你一個特定符號要你解碼字串    
題意不難理解    
但是需要用一個由list組成的list做stack  
另一個num字串給掃到的數字用  
  
一開始從左至右掃過所有字元  
掃到數字時，我們先存到num字串中  
因為有可能下一個字元也是數字  
掃到"["時，代表累積前面的數字要和其後的字串相乘  
所以可以把["", int(num)] 加到stack中  
然後清空num準備下一輪的數字
掃到字母時，代表這字母將會和stack頂端的數字相乘  
我們可以寫成 stack[-1][0] += char  
把字母塞進stack頂端  
  
掃到"]"時，代表累積的字串和數字要相乘了  
把stack pop後讓他們相乘  
然後把運算後的字串加到pop後stack頂端的字串部分  
如 stack[-1][0] = chars * num  
  
全部掃過後我們會發現最後解碼的字串會位於stack最底部的List的第一個元素  
也就是stack[0][0] 即為所求  
   
   
***  
  
### [399.Evaluate_Division](../../SourceCode/Python/399.Evaluate_Division.py) Level: Medium Tags: [Graph]
  
Time: O(n^3)   
Space: O(n)  
  
思路: 給你幾個數學符號的除法計算式和結果  
要你求題目要求的數學式的答案  
因為有數學運算，很容易聯想成是數學相關的程式題  
但其實他是一題跟Graph有關的題目  
(當然你開提示或看related topic便能馬上發現)  
A->B的關係就是A/B，反過來B->A就是B/A    
所以這題的中心思想就是  
把所有能找到的關聯圖都加進去  
題目要求的queries便可迎刃而解  
  
以題目範例給的關係式為例  
他給的式子也只有區區兩個a / b = 2.0, b / c = 3.0  
光兩個方向的圖是無法解題的  
剩下的方向就要靠我們自己用數學來推導:  
1. A/A = 1.0  
2. A/B == x時，B/A == 1/x  
3. A/B == x且B/C == y時，A/C == x * y  
以上這些都是國中小程度的數學公式  
  
在建構圖的過程中，時間複雜度會卡在條件3  
因為他需要同時找出三個元素來比較  
這裡的時間複雜度可達O(n^3)  
  
另外，如果用內建的dictionary會有許多KeyError Exception和多餘的判斷式要寫  
用collection的detaultdict會讓程式碼簡潔很多  
  
        
***  
  
### [406.Queue_Reconstruction_by_Height](../../SourceCode/Python/406.Queue_Reconstruction_by_Height.py) Level: Medium Tags: []
  
Time: O(n)   
Space: O(1)
  
思路:題意一開始很難理解，直到我看懂k的定義才明白  
給你一個數列由(h, k)組成  
h代表高度，k代表之後排序，會有幾個h比你高的人在前面  
求重新排序後的數列  
如[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]  
經過排序後為  
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]  
其中[5,0]代表高度5而且排序後前面沒有人比他高  
[7,0]同理  
[5,2]代表高度5且他前面有兩個元素比他高  
[6,1]代表高度6且前面只有一個元素比他高  
兩個高度5的都沒他高，可以忽略，所以符合要求  
依此類推  

這題我們可以先以第一個h元素作升序排列  
如果兩個h相同時，則以k的大小做降序排列  
以上面序列為例子，排序後可得:  
[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]  
  
接著我們來考慮k，以[6,1]為例子  
他現在前面有兩個高度比他高的元素  
但他的k為1，前面只能有一個高度比他高的元素存在  
所以我們把它搬到index為1的位置，如下:  
[[7, 0], [6, 1], [7, 1], [5, 0], [5, 2], [4, 4]]  
這種先排序後搬移的作法  
因為比我們要搬的元素高的元素都在前面了  
我們搬到指定位置上時，完全可以滿足只能有k個比他高的元素高的需求
這部份我們可以用list的pop和insert來實現  
全部搬完就是答案了    
  
  
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
  
### [447.Number_of_Boomerangs](../../SourceCode/Python/447.Number_of_Boomerangs.py) Level: Medium Tags: [Math]
      
Time:  O(n^2)    
Space: O(n)    
思路: Boomerangs是迴力鏢的意思  
代表有一個點到另外兩點距離相等  
題目給你n個點的座標，求能形成迴力鏢的總數  
這題解法很多，這裡講最通俗的解法  
把每個點一次取出來  
以這個點為起點去求其他點的距離  
把這些點的距離存到一個dictionary中  
求點和點之間距離的公式國中有教過是math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  
但在實務上我們不一定需要import math 去呼叫sqrt  
因為我們聚焦的只在相同距離，有沒有取平方根不影響答案  
  
所有離取完後  
我們可以看到在dictionary裡會有value超過2的key  
例如範例給的  [[0,0],[1,0],[2,0]]  
我們可以求到這三點到其他點的距離分別為  
[0, 0] => {1: 1, 4: 1}  
[1, 0] => {1: 2}  
[2, 0] => {1: 1, 4: 1}    
(key為4就是沒開平方根的距離)  
我們可以看到在[1, 0]中  
距離為1的邊有2個  
因此代表[1, 0]存在到其他點距離相等的回力鏢  
  
就算知道該點有多個到其他點的距離相等  
我們還是得求出這回力鏢有幾種組合  
這是一個排列組合的問題  
假如以四個點abcd，a到其他bcd點的距離都相同   
說明有3個距離是相等的  
則這些點的排列組合為:  
abc, acb, acd, adc, adb, abd 共6個  
經過推導可得公式 n*(n-1) = 3*1 = 6 
所以我們也可以比照辦理
```python
for d in disDict:
    ans += disDict[d] * (disDict[d] - 1)
```
依次把每個點的排列組合都算出來進行加總  
即為題目要的答案  
  
  
***  
  
### [481.Magical_String](../../SourceCode/Python/481.Magical_String.py) Level: Medium Tags: [Tricky]
  
Time:  O(n)  
Space: O(logn)
      
思路: 題目非常難理解，這裡有必要解釋清楚  
給你一個魔術字串S = "1221121221221121122...."  
這個字串有個神奇的地方在於  
從最左邊看到最右邊  
每一個對應的'1'或'2'都代表這字串的'1'或'2'出現次數  
把這些'1'或'2'出現的次數寫成一個字串  
剛好就等於S字串  
用對應關係來解釋，就是如下: 
```
(S字串)
1   22   11   2  1   22  ......

1    2    2   1  1    2  ......
('1'或'2'出現的次數所組成的字串)
```
可以看到下面的字串雖然不長  
但完全和上面的S字串相同  
所以只要給你S字串的開頭  
這個字串是可以生生不息的  
    
我們取"122"當作字串的樣板  
然後每次照順序拿一個數字出來  
用這數字乘上他應該重複的字串  
再把他加總起來，就是S字串的一部分  
```python
num = int(pattern[i])
..
..
genString += num * char
```  
加上去後別忘記切換Flag來交替疊加'1'字串或'2'字串  
我是用1和-1交替切換  
```python
Flag = -Flag
```
我們不斷從樣板字串取數字出來，最後總會走到盡頭  
但別忘記我們新生的字串理論上應該要和樣板字串完全相同  
所以可以寫個try / except  
當取不到index時  
把新生的字串重新當樣板字串，就能繼續取值了  
```python
try:
    num = int(pattern[i])
except IndexError:
    pattern = genString
    num = int(pattern[i])
```
至於題目的n長度找幾個'1'的要求  
只要我們取的i和n相等時跳出迴圈  
計算新生的字串有多少個'1'就是答案了
  
   
***  
  
### [498.Diagonal_Traverse](../../SourceCode/Python/498.Diagonal_Traverse.py) Level: Medium Tags: []
    

思路:  要你照下圖的方式Traversal一個2維陣列的元素  
  
![](../Res/diagonal_traverse.png)  
  
  
按照提議去觀察每個元素的變化  
你會發現他們是有規律的 [1,-1] 和[-1,1] 在移動  
切換條件在邊界時，變化規則如下圖:  

![](../Res/Picture5.png) 

基本上就是:  
1. 任何一邊的index小於0時，扶正回0   
2. 任何一邊的index大於其最大index時，扶正回最大index  
且另一邊的index+2  
  
須注意此種寫法，判斷條件的順序會有差別  
條件二的判斷必須在條件一之前  
不然另一邊的index會受到影響  
  

***  
  
### [560.Subarray_Sum_Equals_K](../../SourceCode/Python/560.Subarray_Sum_Equals_K.py) Level: Medium Tags: []
  
Time:  O(n)    
Space: O(n)
  
思路: 給你一個整數組成的數列和一個數字k  
要你求出這個數列中連續元素的和為k的個數  
例如[1,1,1]和k=2，得到答案為2  
因為下標0和1的元素和、還有1和2的元素和均為2  
但是第下標0和2的元素和就不能算進去，因為沒有連續  
暴力算法可以用兩個迴圈  
分別為i從0~數列長度、j從i+1~數列長度  
然後再用一個for迴圈從i到j開始計算所有的和是否為k  
這暴力算法為 O(n^3)  
  
最佳解為O(n)，我們需要用一個dictionary來儲存元素和  
key為元素和，而value為出現過的次數  
例如prefixSum[1] == 1  
意思就是出現過連續元素和為1的情況有1次  
  
接著我們用for迴圈遍歷整個nums  
藉由加總目前的元素不斷更新sum  
然後去找sum-k 這個key有沒有在prefixSum這個dictionary出現過  
如果有的話，代表之前曾經有元素和為sum-k過  
這代表的意思就是:  
目前的元素和sum，扣掉之前的元素和sum-k，得到的另一段元素和即為k  
用上面的數列來表示的話，就是這樣:  
```
    i->j  (k: sum(i+1, j))
[1, 1, 1]
 0 --> j  (新sum: 3)
 i        (舊sum: 1)
 
sum(i)和sum(0, j)已知的話  
同等於知道sum(i+1, j) == k會在這裡出現  
```

所以我們可以看到新舊sum相減後就是一組sum為k  
出現次數+1  
  
因此，我們只要把所有的舊sum都存到prefixSum字典中  
新的sum出現時，拿sum-k當key去prefixSum裡找  
如果存在的話，代表有一組數列的加總會是k  
(至於位置在哪裡並不是題目要求的，不重要)    
因為他和sum-k出現的次數是一樣的  
所以sum-k出現多少次，加總為k的數列就會出現多少次  
為何這裡要強調出現多少次呢  
因為在元素可能為負數的情況下  
元素和sum-k可能會出現不止一次  
會有不同的連續元素和加總後一樣都是k  
所以當元素和sum有出現在prefix時  
我們要更新相對應的prefixSum[sum]的計數讓他加1  
把所有的出現次數加總即為答案  
  
***  
  
### [681.[Locked]Next_Closest_Time](../../SourceCode/Python/681.[Locked]Next_Closest_Time.py) Level: Medium Tags: [DFS]  
  
Time:  O(1440) (Worst case)  
Space: O(1)   
  
思路:給你一個24小時制的時間  
求下一個在這個時間的數字集合內的時刻  
例如 19:34 的下一個時刻是 19:39 而不是19:35  
因為5不在其數字集合內  
雖然此題可用DFS解  
但其實暴力解法也不算太慢，而且最差複雜度也為常數O(1440)  
  
我們寫一個計算當前時刻的下一分鐘的函式  
然後也對這下一分鐘取集合 (Set)  
如果此Set是原本時間Set的subset的話  
那就是題目要的答案了  
因為一天內的時間最長也不過1440分鐘  
所以此法既簡潔又快速  
  
  
***  
  
### [739.Daily_Temperatures](../../SourceCode/Python/739.Daily_Temperatures.py) Level: Medium Tags: [Stack]  
    
Time:  O(n)  
Space: O(n)  
    
思路: 給你一個數天的溫度列表  
要你找出以每一天的溫度為基準，再過幾天溫度會比當天溫暖  
是 [503.Next_Greater_Element_II](../../SourceCode/Python/503.Next_Greater_Element_II.py) 的類似題  
直觀的解法是用兩個for迴圈從第一天的溫度開始  
不斷地往後找第一個比當天大的溫度然後把index存到答案中  
然而O(n^2)的時間複雜度因為天數太多而會造成超時(Time Limit Exceed)  
所以我們不能用遍歷天數的方式  
因為題目有提示溫度不會超過100度，我們可以考慮採用遍歷溫度的作法  
從數列的最右邊開始讀取溫度  
每一次都把溫度當key，index當value 存到一個溫度dictionary裡
```python
for day in xrange(length - 1, -1, -1):
    warmer = []
    tMap[temperatures[day]] = day
```  
然後我們從比該天溫度高一度的溫度開始，遍歷整個當天溫度到最高溫度的區間  
目的在於從目前的溫度dictionary中找出比當天溫度還高的溫度  
如果有存在比當天溫度還大的溫度的話  
就把它和當天時間的差距(天)加到一個暫存list中  
因此這List就是所有溫度比當天溫度高的時間差距  
```python
for t in xrange(temperatures[day] + 1, 101):
    if t in tMap:
        warmer.append(tMap[t] - day)
```
這List的最小值，很明顯地為該天的下一個比他高溫度的最小天數  
如果這List為空，說明之後沒有任何一天的溫度比當天高了  
照題目要求需要填0進去  
因為我們是從最後一天開始看起  
所以加入答案的方式也必須相反  
有的人是用插入最前面的方式來做，這樣最後一次插入的元素就是第一天
```python
if warmer:
    ans.insert(0, min(warmer))
else:
    ans.insert(0, 0)
```  
也有人是照原本方式從最後一天增加起然後反轉答案List的
```python
    if warmer:
        ans.insert(min(warmer))
    else:
        ans.insert(0)
        
return ans[::-1]      
```   
端看個人需求
  
另一種解題思路是用stack的方式
先把答案要的陣列預備好，也就是全部初始化成0  
```python
length = len(temperatures)
ans = [0] * length
```
把該天的index塞到stack中
在這之前先檢查stack的最頂端的index指向的溫度是否大於該天溫度  
如果是的話，就把頂端的index pop出來  
並把這個index當作答案陣列的index(因為我們找到他的下一個較溫暖的時間了)  
然後把把答案陣列中指向的那一天填入該天溫度的index減去index
就是index那天溫度到現在這天溫度的差距天數  
```python
for i in xrange(length):
    while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
        temp = stack.pop()
        ans[temp] = i - temp

    stack.append(i)
```
  
這步驟需要反覆進行  
因為有可能stack裡最頂端元素指向那天的溫度都小於今天的溫度  
例如溫度(73, 72, 75)這種場合  
一開始stack裡塞了[0, 1]  
等走到75這天時，stack頂端元素 index 1 指向的那天溫度小於75
所以pop index 1 => ans[1] = 2 - 1   
=> ans[1] == 1  
繼續比較發現目前stack頂端的元素指向的溫度一樣小於75  
所以ans[0] == 2   
  
把每天的index遍歷完，ans即為所求    

  
***
  


 
  