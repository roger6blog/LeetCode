
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