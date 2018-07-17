'''

In selection sort we start by finding the minimum value in a given list and move it to a sorted list.

Then we repeat the process for each of the remaining elements in the unsorted list.

The next element entering the sorted list is compared with the existing elements and placed at its correct position.

So at the end all the elements from the unsorted list are sorted.

'''

def selectionSort(list):
    for i in xrange(len(list)):
        minIndex = i
        for j in xrange(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j

        # Swap the minimum value with the compared value
        list[i], list[minIndex] = list[minIndex], list[i]

nums = [19,2,31,45,30,11,121,27]
print nums
selectionSort(nums)
print "----------"
print nums