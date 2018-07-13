

  
  
  
***
  
### [295.Find_Median_from_Data_Stream](../../SourceCode/Python/295.Find_Median_from_Data_Stream.py) Level: Hard Tags: [Heap]
  
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
