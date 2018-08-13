
https://wdxtub.com/interview/14520597162931.html
  
# 搜索解題策略
##動態數據結構的維護
維護動態數據(data stream)的最大值、最小值或中位數，可以考慮使用堆。  
如果是動態數據求最大的k個元素，因為元素總數量不確定，不能使用quick select，  
這種情況下也應該用堆解決。

如果需要一個動態插入/刪除的有序數據結構，那麽可以使用二叉搜索樹，  
因為它天生就是一個動態的有序數組，並且支持檢索。

### 對於有序／部分有序容器的搜索
用二分查找(binary search)。

### 數據範圍有限、離散
數據範圍有限、離散(或存在大量重覆數據，即密集數據)的排序問題，一般可以使用桶排序。  
對於有限位數的數據(如string, vector<int>, int)，  
可以利用基數排序進行數值序或詞典序排序。

### Scalability & Memory Limits 問題
對這類問題一般采用Divide & Conquer策略，即對問題進行預處理，  
將問題的輸入進行分割、歸類(sorting)，放入相應的桶(單機上的某一塊Chunk，  
或者分布式系統中的一台單機)，再對每個桶進行後期處理，最後合併結果。

整個過程中應該用到哈希函數:   
對於Memory Limits問題，一般可以直接利用哈希函數建立對象到索引的直接映射；  
對Scalability問題，一般可以用哈希表來記錄對象與存儲該對象的機器之間的映射，  
在該機器上進一步做映射以獲得索引。
  
  
***
  
### [162.Find_Peak_Element](../SourceCode/Python/Find_Peak_Element.py) Level: Medium Tags: [Binary Search]

Basic Idea: Binary search

Elaboration: 
 if an element(not the right-most one) is smaller than its right neighbor, then there must be a peak element on its right, because the elements on its right is either 
   1. always increasing  -> the right-most element is the peak
   2. always decreasing  -> the left-most element is the peak
   3. first increasing then decreasing -> the pivot point is the peak
   4. first decreasing then increasing -> the left-most element is the peak  

   Therefore, we can find the peak only on its right elements( cut the array to half)

   The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.



Conditions:
     1. array length is 1  -> return the only index 
     2. array length is 2  -> return the bigger number's index 
     3. array length is bigger than 2 -> 
           (1) find mid, compare it with its left and right neighbors  
           (2) return mid if nums[mid] greater than both neighbors
           (3) take the right half array if nums[mid] smaller than right neighbor
           (4) otherwise, take the left half

Run time: O(logn)
Memory: constant
  
  
  
***
