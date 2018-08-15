
https://wdxtub.com/interview/14520597162931.html

### 內排序演算法
所謂的內排序是指所有的數據已經讀入記憶體，在記憶體中進行排序的算法。  
排序過程中不需要對磁碟進行讀寫。  
同時，內排序也一般假定所有用到的輔助空間也可以直接存在於記憶體中。  
與之對應地，另一類排序稱作外排序，  
即記憶體中無法保存全部數據，需要進行磁碟訪問，每次讀入部分數據到記憶體進行排序。
常見的內排序演算法:
* Merge Sort
* Quick Sort (快速排序)
* Heap Sort(堆排序)  
* Bucket Sort (桶排序) 和 Radix Sort (基数排序)  


### 外排序演算法
外排序算法的核心思路在於把文件分塊讀到記憶體，  
在記憶體中對每塊文件依次進行排序，  
最後合併排序後的各塊數據，依次按順序寫回文件。  
相比於內排序，外排序需要進行多次磁碟讀寫，因此執行效率往往低於內排序，  
時間主要花費於磁碟讀寫上。我們給出外排序的算法步驟如下：

假設文件需要分成k塊讀入，需要從小到大進行排序

1. 依次讀入每個文件塊(Chunk)，在記憶體中對當前文件塊進行排序(應用恰當的內排序算法)。  
此時，每塊文件相當於一個由小到大排列的有序隊列
2. 在記憶體中建立一個最小值堆，讀入每塊文件的隊列頭
3. 彈出堆頂元素，如果元素來自第i塊，則從第i塊文件中補充一個元素到最小值堆。  
彈出的元素暫存至臨時數組
4. 當臨時數組存滿時，將數組寫至磁碟，並清空數組內容。
5. 重覆過程3)，4)，直至所有文件塊讀取完畢  

常見的外排序演算法:  
* Quick selection algorithm
* Binary search  


## 排序法效率對比  

|排序方法|平均情況|最好情況|最壞情況|輔助空間|穩定性|
|------|-------|------|-------|------|-----|
|冒泡排序|O(n^2)|O(n)   |O(n^2)|O(1)   |穩定 |
|選擇排序|O(n^2)|O(n^2)|O(n^2) |O(1)   |不穩定|
|插入排序|O(n^2)|O(n)  |O(n^2) |O(1)   |穩定 | 
|希爾排序|O(nlogn)~O(n^2)|O(n1.3)|O(n^2)|O(1)|不穩定| 
|堆排序  |O(nlogn)|O(nlogn)|O(nlogn)|O(1)|不穩定| 
|歸並排序|O(nlogn)|O(nlogn)|O(nlogn)|O(n)|穩定| 
|快速排序|O(nlogn)|O(nlogn)|O(n^2)|O(logn)~O(n)|不穩定| 

(希爾排序: Shell Sort)  

***

