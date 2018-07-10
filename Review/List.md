
***

[056.Merge_Interval](../../SourceCode/Python/056.Merge_Interval.py) Level: Medium Tags: [List]  
  
思路: 對Python來說不難，因為Python就有內建List排序  
把題目給的List照start值得順序排好後  
用以下的方式來判斷兩個Interal:
1. 如果新的List裡面沒Interval，直接加入新List
2. 如果有的話，比較新List最後一個Interval和要加入的Interval是否有重疊
  重疊的規則: 新Interval的start值落在最後一個Interval的區間裡(相同值也算)
  如此不斷iterate所有元素
  新List即為答案
  
***

[057.Insert_Interval](../../SourceCode/Python/057.Insert_Interval.py) Level: Hard Tags: [List]
  
思路: 是[056.Merge_Interval](../../SourceCode/Python/056.Merge_Interval.py) 的延伸  
做法也極為類似  
只要把要插入的Interval插入原本的List
剩下的就跟056.Merge_Interval一樣了
  
***
  
### [289.Game_of_Life](../SourceCode/Python/289.Game_of_Life.py) Level: Medium Tags: [List, Bit manipulation]
  
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