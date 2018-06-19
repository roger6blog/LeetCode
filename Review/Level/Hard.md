
  
  
  
  
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
  
  
  
***
  
  
### [158.\[Locked\]Read_N_Characters_Given_Read4_II_-_Call_multiple_times](../../SourceCode/Python/158.\[Locked\]Read_N_Characters_Given_Read4_II_-_Call_multiple_times.py) Level: Hard Tags: []
  
  
這題是157題: [157.Read_N_Characters_Given_Read4](../../SourceCode/Python/157.[Locked]Read_N_Characters_Given_Read4.py) 的延伸  
但多了多次讀取的部分
多次讀取的意義在於每次呼叫Read4所得到的資料量可能不同
所以需要準備一個buffer來存放讀取4字元後多餘的資料  
每次我們的read被呼叫時，先檢查buffer有無資料  
有的話就先從buffer拿資料出來  
還不夠的話繼續呼叫read4來存取檔案  
  
  
***
  
  
### [159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters](../../SourceCode/Python/159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters.py) Level: Hard Tags: [Sliding Window]
  
  
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
  
***
