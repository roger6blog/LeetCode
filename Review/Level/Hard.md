
  
  
  
  
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
  
  
  
  
***
  
  
