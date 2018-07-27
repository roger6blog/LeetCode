
  
***

### [004.Median_of_Two_Sorted_Arrays](../../SourceCode/Python/004.Median_of_Two_Sorted_Arrays.py) Level: Hard Tags: [Math]
    

題意:找出兩個已排序的正整數陣列的中位數
乍看之下不難，但難點在於題目要求時間複雜度在O(nlogn)  
暴力解法的兩陣列合併，最少也需要O(m+n)  
要達到O(nlogn)的效率，最起碼也得用Binary Search的方式  
但要怎麼取得中間的K值成了最大問題  
其實這是有數學公式的    
如以下情況:兩個數列A和B，我們要找中位數所以取k=6，其中    
A1<A2<A3<A4<A5<A6  
B1<B2<B3<B4<B5<B6    
如果今天A3<=B3時  (即A[k/2]和B[k/2]比較)  
那麼最第6小的數絕對不會是A1、A2和A3 
因為B3>A3，所以B3 > B1,B2,A1,A2,A3 已經五個數了  
第六個數只可能在 A4,A5,A6,B1,B2,B3之中  
所以下一次的比較中我們就可以把A1,A2和A3剃除  
變成以下數列的相比:  
A4<A5
B1<B2<B3<B4<B5<B6  
k在這時是取原本k值的一半或是 A陣列長度 (看哪個比較小)  
這種比法需要A的陣列長度永遠比B陣列長度小  
所以我們判斷A陣列長度比較長時需要把兩個陣列交換來比較  

我們這裡用一個實際例子來描述細節幫助理解:  
A = [1, 3, 5, 7]
B = [2, 4, 6, 8, 9, 10]  
10個元素，第一個K取5  
第一次比較時把A用pa=min(k/2,lenA)分成兩堆:  
[1, 3] 和 [5, 7]
B則是k-pa來分成 [2, 4, 6] 和 [8, 9, 10]  
我們比較 A[pa-1]=3 和 B[pb-1]=6
因為3<6，所以1和3被捨棄  
接著要比較的是A=[5,7] 和 B = [2, 4, 6, 8, 9, 10] k為pb=3
  
第二次比較時  
pa=min(k/2,lenA)=1  
分成[5] 和[7]  
B則是k-pb=2  
分成[2, 4] 和 [6, 8, 9, 10]
因為 A[pa-1] = 5 大於 B[pb-1] = 4  
所以這次B被切開  
用 A=[5, 7] 和 B=[6, 8, 9, 10]來比，k為pa=1
  
第三次比較時，因為k=1  
所以答案就是 min(A[0]B[0]) = 5  
  
因為本例子的陣列和為偶數  
所以還要算一個A和B中取 k=5+1=6的數字出來  
最後結果是6  
所以中位數應為(5+6)/2.0 = 5.5

  
***

### [010.Regular_Expression_Matching](../../SourceCode/Python/010.Regular_Expression_Matching.py) Level: Hard Tags: [DP]
  
Time:  O(m * n)  
Space: O(m * n)  
  
思路:其實就是把正規表示式的"." 和 "\*"寫出來    
十分難的一題  
和 [044.Wildcard_Matching](../../SourceCode/Python/044.Wildcard_Matching.py)  很像  
但兩者間有微妙的差別，具體可以見44題的思路  
不過簡單來說，這題比44題難多了  
因為本題的"*"有太多狀況要考慮了  
  
這題我們用Dynamic Programming(DP)解題  
首先我們準備一個二元的DP陣列，大小為 (s+1)*(p+1)
裏頭的元素除最左上角為True外，其餘初始值均為False    
我們用它來做DP的matching  
其中心思想是dp[sp][pp]為 s[0:sp] 和p[0:pp]是否match  
其餘的規則，我們用範例來說明，例子如下    
```
s = "xaabyc"
p = "xa*b.c"
```
以上面的例子來說，我們需要一個7*7的DP陣列 
第一行和第一列代表沒有任何字元或沒有任何pattern  
所以 "" 一定match空pattern "" 
  
|s\p|   | x | a | * | b | . | c |
|---|---|---|---|---|---|---|---|
|   | T |   |   |   |   |   |   |
| x |   |   |   |   |   |   |   |
| a |   |   |   |   |   |   |   |
| a |   |   |   |   |   |   |   |
| b |   |   |   |   |   |   |   |
| y |   |   |   |   |   |   |   |
| c |   |   |   |   |   |   |   |
    
    
在開始match traversal之前，我們先檢查一個特殊的scenario  
也就是第一行，這裡先用另一個例子說明
```s = "", p = "c*"```
在正規表示式中，"\*"代表他前面的字元有可能出現多個，也有可能不出現  
所以當p[pp]為*且為第二個字元時，他必定符合空字串    
所以他的欄位應該填上True  
而我們一開始的例子裡並沒有這種情況  
所以第一行應該都填上False　　

接著我們正式開始填DP陣列  
以正規表示式來說，我們可以找到下面的規則  

1. 如果當前p的欄位是"\*"的話，分成以下三種情況  
a) 考慮 "xa" match "xa*"的場合:  
p往前退一個時，"xa"一樣能match "xa"  
所以只要dp[sp][pp-1]的欄位為True，當前欄位就為True  
  
b) 考慮 "x" match "xa*" 的場合:
p往前退兩個時，"x"一樣能match "x"  
所以只要dp[sp][pp-2]的欄位為True，當前欄位就為True  
  
c) 考慮 "xaa" match "xa*" 的場合:  
只要s退一步，就能走到和上面a)一樣的 "xa" match "xa*"  
這時我們除了要確認之前match的結果 (dp[sp-1][pp])是否為True外  
還要確認s和p的前一個字元是否相同  (s[sp-1] == p[pp-2])  
或者p的前一個字元是否為'.' (p[pp-2] == '.')  
以"xaa" match "xa*"來說，他符合 s[sp-1] -> "a" == p[pp-2] -> a
所以 "xaa" match "xa*" 的欄位為 True

2. 如果當前p的欄位為"."的話，代表符合任意一個字元  
因此我們可以比較他的前一個比較結果 (dp[sp-1][pp-1]) 是否為True  
是的話當前欄位就為True  

3. 如果s的當前字元 (s[sp-1]) 等於當前p字元的話
那當然也是可以參考他的前一個結果 (dp[sp-1][pp-1])
  
情況2和3可以寫在一起以節省行數  
  
知道規則後我們從第二列開始填起  
注意*號的欄位可以參考前一個的True或前二個的True  
所以他為True

|s\p|   | x | a | * | b | . | c |
|---|---|---|---|---|---|---|---|
|   | T |   |   |   |   |   |   |
| x |   | T |   | T |   |   |   |
| a |   |   |   |   |   |   |   |
| a |   |   |   |   |   |   |   |
| b |   |   |   |   |   |   |   |
| y |   |   |   |   |   |   |   |
| c |   |   |   |   |   |   |   |
  
  
接著第三列  
比較令人注意的是 "xa" == "xa*"  

|s\p|   | x | a | * | b | . | c |
|---|---|---|---|---|---|---|---|
|   | T |   |   |   |   |   |   |
| x |   | T |   | T |   |   |   |
| a |   |   | T | T |   |   |   |
| a |   |   |   |   |   |   |   |
| b |   |   |   |   |   |   |   |
| y |   |   |   |   |   |   |   |
| c |   |   |   |   |   |   |   |


接著第四列  

|s\p|   | x | a | * | b | . | c |
|---|---|---|---|---|---|---|---|
|   | T |   |   |   |   |   |   |
| x |   | T |   | T |   |   |   |
| a |   |   | T | T |   |   |   |
| a |   |   |   | T |   |   |   |
| b |   |   |   |   |   |   |   |
| y |   |   |   |   |   |   |   |
| c |   |   |   |   |   |   |   |
  
  
全部填完後可得  

|s\p|   | x | a | * | b | . | c |
|---|---|---|---|---|---|---|---|
|   | T |   |   |   |   |   |   |
| x |   | T |   | T |   |   |   |
| a |   |   | T | T |   |   |   |
| a |   |   |   | T |   |   |   |
| b |   |   |   |   | T |   |   |
| y |   |   |   |   |   | T |   |
| c |   |   |   |   |   |   | T |

最右下角的欄位就是我們要的答案
這裡為True，所以 "xaabyc" macth "xa*b.c" 為True    


***
  
### [044.Wildcard_Matching](../../SourceCode/Python/044.Wildcard_Matching.py) Level: Hard Tags: [DP]
   
思路: 題目要求用?代表一個字元，*代表所有字元    
來比對該字串是否符合特定的pattern  
乍看之下和 [010.Regular_Expression_Matching](../../SourceCode/Python/010.Regular_Expression_Matching.py) 很像  
但兩者間有微妙的差別  
不過這裡的 "\*"和第10題的"." 幾乎一樣就是了  
這裡有兩種解法，第一種是暴力算法  
用三個指針來代表string，pattern和星號(star)指向的位置    
一個變數代表星號所涵蓋的string長度  
然後用不同條件來traversal兩個指針  
有2種match或不match的情況:  
1. string指針還沒走完，pattern指針卻走完了=> 不match  
2. 兩個指針都走完: match  
  
在Traversal兩個指針時  
比較特別的是發現pattern指向的位置有星號  
此時要做的動作就是紀錄string在何處開始符合星號pattern  
和開始累積starString coverage的起始範圍  
  
此情況觸發後  
接下來的step是在下一個字串符合pattern指針的所指向的下一個(當前是星號)字元前    
starString coverage和string指針都不斷往前進  
  
  
英文分析  
Analysis:

For each element in s  
If *s==*p or \*p == ? which means this is a match, 
then goes to next element s++ p++.  

If p=='*', this is also a match, 
but one or many chars may be available, 
so let us save this *'s position and the matched s position.

If not match, then we check if there is a * previously showed up,  
       if there is no *,  return false;  
       if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.  

e.g.  

abed  
?b*d**  

a=?, go on, b=b, go on,  
e=*, save * position star=3, save s position ss = 3, p++  
e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1  
d=d, go on, meet the end.  
check the rest element in p, if all are *, true, else false;  

Note that in char array, 
the last is NOT NULL, 
to check the end, use  "*p"  or "*p=='\0'".  

第二種解法是動態規劃  
我們以題目給的其中一個例子來說明  
```
s = "acdcb"  
p = "a*c?b"  
```  
  
首先我們宣告一個len(s)+1 x len(p)+1 的表格  
表格內的內容除了最左上角是True外，其他全為False  
如下表

|s\p|   | a | * | c | ? | b |
|---|---|---|---|---|---|---|
|   | T |   |   |   |   |   |
| a |   |   |   |   |   |   |
| c |   |   |   |   |   |   |
| d |   |   |   |   |   |   |
| c |   |   |   |   |   |   |
| b |   |   |   |   |   |   |

這是DP的表格，我們用sp和pp來iterate這個表格  
他們的初始值都是0，而dp[0][0]永遠為True  
一般情況下d[sp][pp]表示s[0:sp-1]和p[0:pp-1]是否有match    
所以我們可以不斷的參考前面的結果來得到目前的結果  

在正式填表之前，我們需要對星號做特別處理  
因為有可能p的開頭就有星號  
做法是看第一列dp[0]，如果某個元素有星號的話  
他後面的元素就會遵從這星號對應的結果  
以上表來說就是這樣  

|s\p|   | a | * | c | ? | b |
|---|---|---|---|---|---|---|
|   | T |   | F | F | F | F |
| a |   |   |   |   |   |   |
| c |   |   |   |   |   |   |
| d |   |   |   |   |   |   |
| c |   |   |   |   |   |   |
| b |   |   |   |   |   |   |

這基本上是針對第一個元素是星號程式碼  
如s = "aa", p ="*"時  
第一列都會變為True  

現在我們要正式填表了
填表格的規則如下:  

1. 如果當前p的欄位是"\*"  
那可以直接參考他上方或他左方的結果  
其中一個是True，該欄位就能寫成True 
因為*可以表示任何字元  
這是match s = "a", p = "a*" (dp[sp][pp-1])  
和 s = "ab", p = "a*" (dp[sp-1][pp]) 的情況  

2. 如果當前p的欄位是"?"或者s[sp] match p[pp]  
那當前的欄位就可以參考前一個match的結果  
即dp[sp][pp] = dp[sp-1][pp-1]  
因為 "?" 為任意一個字元  
所以我們可以參考他前面一個比較的結果  
 
  
  
我們先看sp=1的情況  
sp和pp都為1的時候，"a" match "a" 所以表格為   

|s\p|   | a | * | c | ? | b |
|---|---|---|---|---|---|---|
|   | T |   | F | F | F | F |
| a |   | T |   |   |   |   |
| c |   |   |   |   |   |   |
| d |   |   |   |   |   |   |
| c |   |   |   |   |   |   |
| b |   |   |   |   |   |   |

接著走到星號時  
"a" match "a*"所以為True
  
|s\p|   | a | * | c | ? | b |
|---|---|---|---|---|---|---|
|   | T |   | F | F | F | F |
| a |   | T | T |   |   |   |
| c |   |   |   |   |   |   |
| d |   |   |   |   |   |   |
| c |   |   |   |   |   |   |
| b |   |   |   |   |   |   |  
  
同理，第三行的元素為  

|s\p|   | a | * | c | ? | b |
|---|---|---|---|---|---|---|
|   | T |   | F | F | F | F |
| a |   | T | T |   |   |   |
| c |   |   | T | T |   |   |
| d |   |   |   |   |   |   |
| c |   |   |   |   |   |   |
| b |   |   |   |   |   |   |
  
  
中間過程省略，我們看最後一行的結果(False省略)    

|s\p|   | a | * | c | ? | b |
|---|---|---|---|---|---|---|
|   | T |   |   |   |   |   |
| a |   | T | T |   |   |   |
| c |   |   | T | T |   |   |
| d |   |   | T |   | T |   |
| c |   |   | T | T |   |   |
| b |   |   | T |   | T |   |
  
最右下角的元素便代表全部的match結果    
所以這個match的結果為False  
"acdcb" 不match "a*c?b"  
  
  
***

### [057.Insert_Interval](../../SourceCode/Python/057.Insert_Interval.py) Level: Hard Tags: [List]
  
思路: 是[056.Merge_Interval](../../SourceCode/Python/056.Merge_Interval.py) 的延伸  
做法也極為類似  
只要把要插入的Interval插入原本的List  
剩下的就跟056.Merge_Interval一樣了
  
***
  
### [123.Best_Time_to_Buy_and_Sell_Stock_III](../../SourceCode/Python/123.Best_Time_to_Buy_and_Sell_Stock_III.py) Level: Hard Tags: [DP]
  
Time:  O(n)  
Space: O(n)  
  
思路: 是[122.Best_Time_to_Buy_and_Sell_Stock_II](../../SourceCode/Python/122.Best_Time_to_Buy_and_Sell_Stock_II.py)   
     和[121.Best_Time_to_Buy_and_Sell_Stock_II](../../SourceCode/Python/121.Best_Time_to_Buy_and_Sell_Stock.py) 的延伸  
但本題因為只能用DP解題，屬於高難度  
同樣是買低賣高，這題限制只能做兩次交易  
我們用一維的雙動態規劃來解題  
使用兩組DP陣列 DP1和DP2   
DP1代表在遍歷prices數列時，在prices[x]之前所能達到的最大利潤  
DP2代表在逆向遍歷prices數列時，在prices[x]之後所能達到的最大利潤  
則DP1[x]的利潤加上DP2[x]的利潤  
就是代表在x時間點前後的兩次交易所能達到的利潤  
所以取兩者和的最大值即為所求  
  
另一種特別的解法是  
其實我們並不需要每個時間點買賣第一第二筆股票收益的所有利潤  
我們只要知道前一個時間點買賣第一第二筆股票的最大利潤  
就能得到當前最大的最大利潤了  
我們在遍歷prices數列的時候  
使用四個變數:  
buy1: 在該價格買入第一筆股票後手裡剩的錢  
sell1: 在該價格賣出第一筆股票後手裡剩的錢  
也就是說第一筆買進賣出後得到的利潤  
或者是上一輪賣出第一筆股票後的利潤，兩者取其大  
buy2: 在該價格買入第二筆股票後手裡剩的錢  
同等於上一輪賣出第一筆股票後的利潤減去當前股票價格  
sell2: 在該價格賣出第二筆股票後手裡剩的錢，即最後利潤  
或者是上一輪賣出第二筆股票後的利潤，兩者取其大  
我們能做的就是儘可能的低價買入後高價出售(廢話)  
要注意的是第二筆交易裡我們是把第一筆交易的利潤考慮進去的  
所以能達到題目要求  
此法時間複雜度為O(n)，空間複雜度為O(1)
  
***
  
### [146.LRU_Cache](../../SourceCode/Python/146.LRU_Cache.py) Level: Hard Tags: []
  
思路: 實作一個 Least Recently Used (LRU) cache.  
最簡單的作法是使用Python內建的dictionary來存放資料和索引  
用List來存放Cache容量滿的時候要移出去的index  
這種做法的時間複雜度為 O(n)  
如果需要O(1)的複雜度  
則需要用Dobule LinkList來取代原本的List
  
  
***
  
  
### [158.[Locked]Read_N_Characters_Given_Read4_II_-_Call_multiple_times](../../SourceCode/Python/158.\[Locked\]Read_N_Characters_Given_Read4_II_-_Call_multiple_times.py) Level: Hard Tags: []
  
  
這題是157題: [157.Read_N_Characters_Given_Read4](../../SourceCode/Python/157.[Locked]Read_N_Characters_Given_Read4.py) 的延伸    
但多了多次讀取的部分  
多次讀取的意義在於每次呼叫Read4所得到的資料量可能不同  
所以需要準備一個buffer來存放讀取4字元後多餘的資料  
每次我們的read被呼叫時，先檢查buffer有無資料  
有的話就先從buffer拿資料出來  
還不夠的話繼續呼叫read4來存取檔案  
  
  
***
  
  
### [159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters](../../SourceCode/Python/159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters.py) Level: Hard Tags: [Sliding Window]
  
Time:  O(n)  
Space: O(1)  
思路: 用Slinding Window來計算最長的兩個兩個不相同字元組成的字串長度  
另外用一個Hashmap來記錄目前在Slinding Window的字元  
1. 一開始先用Window 的右側bar來累加所有不同的字元並存入Hashmap  
每掃到一個新字元，Hashmap相對應的字元就累加1  
2. 右側bar前進的同時也檢查目前Hashmap裡的不同字元有沒有超過2個  
有的話則滑動Window的左側bar，並將左側bar原本指向的字元在Hashmap裡的數量減1  
減到0之後，Hashpmap裡不同字元的數量便少了1  
如此重複直到Hashmap裡的不同字元少於2個為止  
3. 取當前Window右側的bar(通常是for迴圈裡的i) 和Window左側bar相減的長度、和當前最長不同字元字串的長度的最大值  
接著繼續讓Window右側bar前進來讀取整個字串  
4. 等Traverse完整個字串，即得到最大不同字元的字串長度
  
  
***
  
  
### [253.[Locked]Meeting_Rooms_II](../../SourceCode/Python/253.[Locked]Meeting_Rooms_II.py) Level: Hard Tags: [List]
  
思路: 直觀可以看出就是找出所有List重疊的部分，重疊代表要多準備會議室  
可以把Meeting room所有的起始和結束時間按順序排好  
並從左掃到右，每遇到Start，需要會議室就+1，遇到end，需要會議室就-1  
同時記錄在這iterate中的最大會議室數  
此即為答案
  
  
  
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
  
### [218.The_Skyline_Problem](../../SourceCode/Python/218.The_Skyline_Problem.py) Level: Hard Tags: [Heap]
  
Time:  O(nlogn)  
Space: O(n)  
    
思路:堪稱是Leetcode最知名的經典難題之一  
我們必須從圖A的建築物圖形中找出他剪影圖的特定點  
![](../Res/skyline1.jpg)![](../Res/skyline2.jpg)  
題目有提示這些點的特性固定的，可以參考圖B    
具體的描述是"水平線段的左邊端點，就是所謂的關鍵點"  
另外一個重點是"同一條天際線裡只能取一個關鍵點"  
解題的核心思路是從左到右掃描每一個建築物  
用Max heap來儲存目前最高天際線的右端點  
如果目前天際線上左端點的天際線高度不等於Max heap中的最大高度的話    
就是我們要的關鍵點  
  
如果目前的建築物左端點範圍落在Max heap擁有最高天際線的建築右端點外面的話  
說明當前建物已經不屬於這個建築群，我們需要逐步移除Max heap裡的建築  
在移除之前別忘記從天際線落地時也有一個關鍵點  
  
Python heapq提供的heap的是Min heap  
所以我們要用Max heap的話，每個元素都要乘上-1才能達到Max heap的效果  
   
   
***
  
### [336.Palindrome_Pairs](../../SourceCode/Python/336.Palindrome_Pairs.py) Level: Hard Tags: []
     
Time:  O(n * k^2),   
n is the number of the words, k is the max length of the words.  
Space: O(n * k)   
  
思路: 給你一個字串組成的陣列　　
要你判斷哪些字串的組合可以形成回文(Palindrom)  
用暴力法來做的話就是用兩個指標各挑一個字串來組合  
看能不能形成回文  
但此法的時間複雜度為O(n^2)在Leetcode會超時  
另一種可以被接受的方法為減少比對次數    
用以下三種判斷方式:  
先做一個字串對應編號的字典已加速查詢，然後依次挑一個字串出來:    
1. 如果此字串是空字串，那麼只要剩下的字串自己就能形成回文  
那就能達成要求  
  
2. 把該字串反轉，看反轉的字串有沒有在設好的字典中  
有的話就是兩種組合  
不過因為挑中的字串也許本身就是回文  
所以要注意在字典中找到的字串是不是和原本的同一個  
  
3. 第三種是把挑中的字串取每個字母累加的方式來切割  
例如挑中的字串是 "sssll"   
我們就能把它分成左右兩邊
```
"s"   <-> "ssll"
"ss"  <-> "sll"
"sss" <-> "ll"
...
```
然後我們可以發現  
左邊為回文的話，只要剩餘的右邊部分反轉後能在字典裡找到  
那這個字串的組合和反轉後的字就必定是回文  
右邊為回文的話也是同理  
例如給一個字串陣列 
```
words = ["abcd","dcba","lls","s","sssll"]
```
我們可以發現在"sssll"切成 "ss" <-> "sll"時
"ss"為回文，我們又能在陣列中找到 "sll" 的回文 "lls"
所以他們可以組合成 "llssssll" 這個回文  
  
用上面三種比對方式  
就能有效地降低時間複雜度從O(n*n)降低成O(n*k*k)  
k是所有字串中最大的字串長度  
  
另外要注意一點  
用這三種比對方式會找到重複的pair  
所以python可以用set來消除重複的pair
   
***
  
### [340.[Locked]Longest_Substring_with_At_Most_K_Distinct_Characters](../../SourceCode/Python/340.[Locked]Longest_Substring_with_At_Most_K_Distinct_Characters.py) Level: Hard Tags: [Sliding Window]
    
Time:  O(n)  
Space: O(1)  
思路:和 [159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters](../../SourceCode/Python/159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters.py) 幾乎完全一樣  
差別只在於159只要你找出最長的2個字母組成的字串長度  
這題要K個而已  
完全可以用159題的解法解答  
  
***
  
### [295.Find_Median_from_Data_Stream](../../SourceCode/Python/295.Find_Median_from_Data_Stream.py) Level: Hard Tags: [Heap]
  
Time:  O(nlogn) for total n addNums,    
O(logn) per addNum,   
O(1) per findMedian.   
Space: O(n), total space  
  
思路:題目要求你在不斷輸入的數字之中找出其中位數  
在一個List中找出中位數的方法並不難  
不考慮執行時間的情況下  
準備一個List，每次新加入一個數字後便排序然後找出中位數是很容易想到的方法    
但本題藏著TLE(Time Limit Exceed)陷阱    
雖然Python的list sort時間複雜度已經是O(nlogn)
但一旦輸入的資料是大量數字還是很容易超時  
有效率的解法是準備兩個heap，一個是minHeap另一個是maxHeap  
用這兩個heap的頂端元素找出中位數  
為了達到這樣的效果，他們必須滿足兩個條件:  
1. minHeap內的元素都需要大於maxHeap內的元素    
如此一來minHeap和maxHeap的頂端一定是中間附近的元素

2. minHeap和maxHeap的size要接近對分，才有中位數的效果    
所以每加入一個新元素後都要平衡  
  
當maxHeap > minHeap的時候，maxHeap的頂端就是中位數
如果兩者相等，那就是兩個heap頂端的元素相加除二  
maxHeap < minHeap理論上可以透過平衡來避免    
確保maxHeap的大小永遠大於或等於minHeap  

以Python來說，內建的heapq module就有提供min heap的方法  
可以直接套用  
而maxheap沒有直接支援  
我們可以用heapq開一個min heap叫做maxHeap  
然後把要放到maxHeap裡的元素全部加上負號  
如此一來就能達到max heap的效果了  
當然平衡時頂端元素的轉移別忘記處理負號  

最後尋找中位數時，別忘記題目要求回傳浮點數  
相除或相乘的常數加上小數點便可達到題目要求  
  
***
  
### [297.Serialize_and_Deserialize_Binary_Tree](../../SourceCode/Python/297.Serialize_and_Deserialize_Binary_Tree.py) Level: Hard Tags: [DFS, Tree]
  
Time:  O(n)  
Space: O(h)  
  
思路:看起來題目很長又很難，但中心觀念只在於Traversal整個Tree而已  
deserialize則是把資料加回Tree的過程  
這裡我們用Preorder來traversal整個tree  
因為題目很freestyle，沒有完全標準的答案  
我們另外附上能被accept的版本  

[297.Serialize_and_Deserialize_Binary_Tree_accept](../../SourceCode/Python/297.Serialize_and_Deserialize_Binary_Tree_accept.py)  

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
