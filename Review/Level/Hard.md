
  
***

### [057.Insert_Interval](../../SourceCode/Python/057.Insert_Interval.py) Level: Hard Tags: [List]
  
思路: 是[056.Merge_Interval](../../SourceCode/Python/056.Merge_Interval.py) 的延伸  
做法也極為類似  
只要把要插入的Interval插入原本的List  
剩下的就跟056.Merge_Interval一樣了
  
***
  
### [044.Wildcard_Matching](../../SourceCode/Python/044.Wildcard_Matching.py) Level: Hard Tags: []
   
用三個指針來代表string，pattern和星號(star)指向的位置  
一個變數代表星號所涵蓋的string長度  
然後用不同條件來traversal兩個指針  
有2種match或不match的情況:  
1. string指針還沒走完，pattern指針卻走完了: 不match  
2. 兩個指針都走完: match  
  
在Traversal兩個指針時
比較特別的是發現pattern指向的位置有星號  
此時要做的動作就是紀錄string在何處開始符合星號pattern  
和開始累積starString coverage的起始範圍  
  
此情況觸發後，接下來的step是在下一個字串符合pattern指針的所指向的下一個(當前是星號)字元前    
starString coverage和string指針都不斷往前進
  
  
英文分析  
Analysis:

For each element in s  
If *s==*p or \*p == ? which means this is a match, then goes to next element s++ p++.  
If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
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

Note that in char array, the last is NOT NULL, to check the end, use  "*p"  or "*p=='\0'".  

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
