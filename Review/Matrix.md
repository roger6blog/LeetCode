

  
  
***
  
### [054.Spiral_Matrix](../SourceCode/Python/054.Spiral_Matrix.py) Level: Medium Tags: [Matrix]
   
思路: 定義四種方向，如
+ 0 表示向右邊讀取
+ 1 表示向下讀取
+ 2 表示向左讀取
+ 3 表示向上讀取
用狀態還不夠，因為我們是從最外圈向內讀取，所以還需要四個指針標示目前所讀取的位置
+ upRow 表示外圈的上行位置
+ downRow 表示外圈的下行位置
+ leftCol 表示外圈的左列位置
+ rightCol 表示外圈的右列位置
  
每次加完該列(或行)的元素後，指針都需要有相對應的增減
  
***
