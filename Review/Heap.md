


# 堆
通常所說的堆(Heap)是指二叉堆，從結構上說是完全二叉樹，從實現上說一般用數組。  
以數組的下標建立父子節點關係：  
對於下標為i的節點，其父節點為(int)i/2，其左子節點為2i，右子節點為2i+1。  
堆最重要的性質是，它滿足部分有序(partial order)：  
最大(小)堆的父節點一定大於等於(小於等於)當前節點，  
且堆頂元素一定是當前所有元素的最大(小)值。

堆算法的核心在於插入，刪除算法如何保持堆的性質(以下討論均以最大堆為例):

下移(shift-down)操作：下移是堆算法的核心。  
對於最大值堆而言，對於某個節點的下移操作相當於比較當前節點與其左右子節點的相對大小。  
如果當前節點小於其子節點，則將當前節點與其左右子節點中較大的子節點對換，  
直至操作無法進行(即當前節點大於其左右子節點)。

建堆：假設堆數組長度為n，建堆過程如下，註意這裏數組的下標是從 1 開始的：
```
for i, n/2 downto 1
    do shift-down(A,i)
```    
插入：將新元素插入堆的末尾，並且與父節點進行比較，  
如果新節點的值大於父節點，則與之交換，即上移(shift-up)，直至操作無法進行。

彈出堆頂元素：彈出堆頂元素(假設記為A[1]，堆尾元素記為A[n])並維護堆性質的過程如下：
```
output = A[1]
exchange A[1] <-> A[n]
heap size -= 1
shift-down(A,1)
return output
```
值得注意的是，堆的插入操作逐層上移，耗時O(log(n))，與二叉搜索樹的插入相同。  
但建堆通過下移所有非葉子節點(下標n/2至1)實現，耗時O(n)，小於BST的O(nlog(n))。

通過上述描述，不難發現堆其實就是一個優先隊列。


  
***
  
### [00295.Find_Median_from_Data_Stream](../../SourceCode/Python/Problem/00295.Find_Median_from_Data_Stream.py) Level: Hard Tags: [Heap]
  
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
