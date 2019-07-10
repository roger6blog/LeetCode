

  
  
***

### [00003.Longest_Substring_Without_Repeating_Characters](../../SourceCode/Python/Problem/00003.Longest_Substring_Without_Repeating_Characters.py) Level: Medium Tags: [String, Sliding Window]  
  
Time:  O(n)  
Space: O(1)    
  
思路:給你一個字串  
要你求最大長度的不重複字元子字串的長度  
解題的核心觀念就是題目告訴你的:  
不重複字元子字串，代表這個字串不能存在兩個相同的字元  
所以我們可以用一個Sliding Window來計算這字串的長度  
加上一個dictoionary來儲存目前字串擁有的字元和位置  
一開始這Window的左右邊界都在最左邊  
然後我們讓右邊界的值不斷增加  
在他們兩個中間的字串就是當前最長的不重複子字串  
在右邊界增加的同時，我們把右邊界指向的新字元和dictionary裡的內容比較  
如果dictionary裡不存在這個新字元  
就把他加入裡面並賦值為當前位置
```python
wordDict[char] = index
```
反之如果能在dictionary裡找到這個字元  
說明這個字串已經有字元重複了  
我們應該把左邊界移動到這個重複字元位置的右邊一位  
然後把該字元的位置更新成當前字元所在位置  
```python
if char in wordDict and wordDict[char] >= begin:
    begin = wordDict[char] + 1
```
這裡有一個額外的判斷是wordDict[char] >= begin  
他是為了避免begin會因為某個重複字元出現在begin的前面過  
造成begin往回指的狀況
  
每一次的新增字元都能判斷一次當前最長不重複子字串是否為最大  
整個字元都掃描完後這個當前最長子字串就是答案了    

***
  
  
### [00159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters](../../SourceCode/Python/Problem/00159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters.py) Level: Hard Tags: [Sliding Window]
  
Time:  O(n)  
Space: O(1)  
思路: 用Slinding Window來計算最長的兩個兩個不相同字元組成的字串長度  
另外用一個Hashmap來記錄目前在Slinding Window的字元  
1. 一開始先用Window 的右側bar來累加所有不同的字元並存入Hashmap  
每掃到一個新字元，Hashmap相對應的字元就累加1  
2. 右側bar前進的同時也檢查目前Hashmap裡的不同字元有沒有超過2個  
有的話則滑動Window的左側bar，並將左側bar原本指向的字元在Hashmap裡的數量減1  
減到0之後，Hashpmap裡不同字元的數量便少了1  
如此重複直到Hashmap裡的不同字元少於2個為止  
3. 取當前Window右側的bar(通常是for迴圈裡的i) 和Window左側bar相減的長度、和當前最長不同字元字串的長度的最大值  
接著繼續讓Window右側bar前進來讀取整個字串  
4. 等Traverse完整個字串，即得到最大不同字元的字串長度
  
  
***
  
### [00340.[Locked]Longest_Substring_with_At_Most_K_Distinct_Characters](../../SourceCode/Python/Problem/00340.[Locked]Longest_Substring_with_At_Most_K_Distinct_Characters.py) Level: Hard Tags: [Sliding Window]
    
Time:  O(n)  
Space: O(1)  
思路:和 [00159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters](../../SourceCode/Python/Problem/00159.[Locked]Longest_Substring_with_At_Most_Two_Distinct_Characters.py) 幾乎完全一樣  
差別只在於159只要你找出最長的2個字母組成的字串長度  
這題要K個而已  
完全可以用159題的解法解答  
  
***
  
### [00643.Maximum_Average_Subarray_I](../../SourceCode/Python/Problem/00643.Maximum_Average_Subarray_I.py) Level: Easy Tags: [List, Sliding window]

Time:  O(n)  
Space: O(1)    
  
題意: 給你一個List和區間k  
要你求出長度為k的連續子List的最大平均值  
用slice的方式會造成超時(Time Limit Exceed)  
我們可以用Sliding winodws的方法  
從左到右開始不斷的加總k個元素    
為了保持每次都是K個元素的加總  
每從右邊加一個新元素，左邊的元素就要被減去  
```python
for i in xrange(len(nums)):
    sums += nums[i]
    if i+1 > k:
        sums -= nums[i-k]
```
接著只要計算最大元素和即為所求  

  
***