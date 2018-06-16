

  
  
  
***

## [042.Trapping_Rain_Water](../SourceCode/Python/042.Trapping_Rain_Water.py) Level: Hard Tags: []
   
思路: 
he following idea is in fact from the last answer in this link, which leads to a clean code. I just reorganize it and add some explanations. I hope it is Ok.

The following are four solutions in C/C++/Java/Python respectively.  
The basic idea is that we set two pointers l and r to the left and right end of height.  
Then we get the minimum height (minHeight) of these pointers  
(similar to Container with Most Water due to the Leaking Bucket Effect) since the level of the water cannot be higher than it.  
Then we move the two pointers towards the center.  
If the coming level is less than minHeight, then it will hold some water.  
Fill the water until we meet some "barrier"  
(with height larger than minHeight) and update left and right to repeat this process in a new interval
  
  
***
