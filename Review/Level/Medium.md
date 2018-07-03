


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

### [179.Largest_Number](../SourceCode/Python/179.Largest_Number.py) Level: Medium Tags: [Sort]

  
  
***
  
  
### [133.Clone_Graph](../SourceCode/Python/133.Clone_Graph.py) Level: Medium Tags: [Graph, DFS]
  
  
  
***
  
### [163.Missing_Range](../SourceCode/Python/163.Missing_Range.py) Level: Medium Tags: []
  
思路:我們可以使用雙指標
pre指標指向前一個元素、curr指標指向後面一個元素  
不斷的比較前一個元素和後一個元素是否有大於2的差距  
如果有的話代表有Missing range  
把這兩個元素的區間逐個印出來就大功告成  
需注意判斷lower和upper的區間
  
***
  
### [166.Fraction_to_Recurring_Decimal](../SourceCode/Python/166.Fraction_to_Recurring_Decimal.py) Level: Medium Tags: []
  
思路: 題目要求你找出不同數字相除後的小數，如果有循環則在循環的數字中括號
除了最基本的兩數相除取模和找商之外  
我們需要一個dictionary來記錄該小數點數字出現的位置  
不能直接把小數點數字加入list再去搜尋該list  
否則會無法處理小數點數字重複的情況如: 1/333=0.(003) 
