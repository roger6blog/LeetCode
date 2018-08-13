

https://wdxtub.com/interview/14520595848890.html


位操作
對於網路、操作系統、嵌入式系統等職位的面試，位運算也是常見的題目類型之一。  
所謂的位運算，是指按二進制進行的運算。  
常見運算包括求反，與運算，或運算，異或運算及位移。  


在Python中，基本的位運算符總結如下，其中運算符優先級為從上到下遞減，且<<，>>優先級相同：


|操作符|功能|用法|
|---|---|---|
|~  |位求反|~var|
|<< |左移(乘法)|var << position|
|>> |右移(除法)|var >> position|
|&  |位與(AND)|var1 & var2|
|^  |位異或(XOR)|var1 ^ var2|
|一條豎線|位或(OR)|var1 豎線 var2|
		
		
		
複雜的位運算建議都用括號強制計算順序，而不是依賴於優先級，  
這樣做可以增加可讀性並避免錯誤。

用十六進制(hex)定義一個變量如下所示：
```python
value = 0xFFFF
```

等價於二進制(binary)定義：
```python
value = 0b1111111111111111
```

等價於十進制定義：
```python
value = 65535
```

## 解題策略
### 基本的位運算
最基本的操作包括獲取位、設置位和清除位。  
獲取位可以利用&1：&(0x1 << pos) ；  
設置位可以利用|1: | (0x1 << pos) ；  
清除位可以利用&0: &(~(0x1 << pos))。  
判斷某位是否相同用：(A & (0x1 << pos)) ^ (B & (0x1 << pos))。  

### 位掩碼
選擇合適的位掩碼(bit mask)，然後與給定的二進制數進行基本位操作。  
而掩碼，通常可以通過對\~0，1 進行基本操作和加減法得到。  
例如，我們要構造一個第i到第j位為0，其他位為1的位掩碼，  
則可以對~0進行左移操作獲得形如111…0000的mask，再對\~0進行右移操作，  
獲得形如000…111的mask，最後通過位或(此處相當於相加)得到最終的位掩碼。

在尋求得到一個特定的掩碼時，還是利用最基本的獲取位、設置位或清除位得到所需掩碼的形態。  
另外，應當盡可能避免直接出現常數，  
比如使用32-i這樣的情況(這裏默認想要操作一個32bit的整型)，  

### XOR 異或
異或：相同為0，不同為1。也可用「不進位加法」來理解。

異或操作的一些特點：
```python
x ^ 0 = x
x ^ 1s = ~x # 1s = ~0
x ^ (~x) = 1s
x ^ x = 0 # interesting and important!
a ^ b = c => a ^ c = b, b ^ c = a # swap
a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c # associative
```

### 移位操作
移位操作可近似為乘以/除以2的冪。0b0010 * 0b0110等價於0b0110 << 2.   
下面是一些常見的移位組合操作。

1. 將x最右邊的n位清零 ```x & (~0 << n)```
2. 獲取x的第n位值(0或者1) ```x & (1 << n)```
3. 獲取x的第n位的冪值 ```(x >> n) & 1```
4. 僅將第n位置為```1 x | (1 << n)```
5. 僅將第n位置為```0 x & (~(1 << n))```
6. 將x最高位至第n位(含)清零 ```x & ((1 << n) - 1)```
7. 將第n位至第0位(含)清零 ```x & (~((1 << (n + 1)) - 1))```
8. 僅更新第n位，寫入值為v; v為1則更新為1，  
否則為0 ```mask = ~(1 << n); x = (x & mask) | (v << i)```  
***
* Two's Complement - 負數可以看作是最高位的 1 為負，  
其他位為正，相加得到最後的值
    * 例如 -1 = (1111) 最高位的 1 表示 -8， 剩下三位等於 7，相加後等於 -1
* logical right shift - put a 0 in the most significant bit - ```>>>```
* arithmetic right shift - put a 1 in the most significant bit - ```>>```
### Get Bit
Shifts 1 over by i bits, creating a value that looks like 00010000.   
AND operation
```
boolean getBit(int num, int i){
    return ((num & (1 << i)) != 0);
}
```
### Set Bit
Shifts 1 over by i bits, creating a value like 00010000.   
OR operation
```
int setBit(int num, int i){
    return num | (1 << i);
}
```
### Clear Bit
Create a number like 11101111 by creating the reverse of it (00010000).   
AND operation.
```
int clearBit(int num, int i){
    int mask = ~(1 << i);
    return num & mask;
}
```
To clear all bits from the most significant bit through i (inclusive), we create a mask with a 1 at the ith bit(1 << i). Then we subtract 1 from it, giving us a sequence of 0s followed by i 1s. AND operation.

int clearBitsMSBthroughI(int num, int i){
    int mask = (1 << i) - 1;
    return num & mask;
}
To clear bits from i through 0 (inclusive),   
we take a sequence of 1s (which is -1) and shift it over by 31 - i bits.
```
int clearBitsIthrough0(int num, int i){
    int mask = ~(-1 >>> (31 - i));
    return num & mask;
}
```
#### Update Bit
Set the ith bit to a value v
```
int updateBit(int num, int i, boolean bitIs1){
    int value = bitIs1 ? 1 : 0;
    int mask = ~(1 << i);
    return (num & mask) | (value << i);
}
```

*** 