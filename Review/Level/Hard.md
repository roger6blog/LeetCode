
  
  
  
  
***
  
### [044.Wildcard_Matching](../SourceCode/Python/044.Wildcard_Matching.py) Level: Hard Tags: []
   
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

***
