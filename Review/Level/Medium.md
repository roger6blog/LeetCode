


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
  
***
  
### [200.Number_of_Islands](../SourceCode/Python/200.Number_of_Islands.py) Level: Medium Tags: []
  
思路: 本題是找出與周圍被0包圍的1  
可以使用DFS，利用四個方向去取得每個元素的周圍是否還有0  
已經走過 (visited) 的元素我們用0標示，如此便不會再去走它  
  
  
### [208.Implement_Trie_(Prefix_Tree)](../SourceCode/Python/208.Implement_Trie_(Prefix_Tree).py) Level: Medium Tags: []
  
Time:  O(n), per operation
Space: O(1)
思路:本題要求你實作一個字典樹(Trie)的insert, search和startWith  
在此之前你必須先了解字典樹是什麼  
  
![一個保存了8個鍵的trie結構，"A", "to", "tea", "ted", "ten", "i", "in", and "inn".](../Res/1200px-Trie_example.svg.png)
  
簡單來說就是一個方便搜尋同樣Prefix單字的樹  
有同樣prefix字的單字會被插到同一條Trie  
roo節點通常為空，底下有a~z 26個子Trie
好處是用空間換取時間  
搜尋速度比為最佳化的Hash快，只要O(n)    
壞處就是浪費空間和比不上最佳化的Hash  
  
  
