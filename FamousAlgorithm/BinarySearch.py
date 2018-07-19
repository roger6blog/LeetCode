
'''

'''


def BinarySearch(lst, item):
    '''
    :param lst: sorted list of integers
    :param item: integer you are searching for
    :return:
    '''

    if len(lst) == 0:
        print("No element in list")
        return False

    first = 0
    last = len(lst) - 1
    mid = (first + last) // 2

    if lst[mid] == item:
        return True
    elif lst[mid] < item:
        return BinarySearch(lst[mid + 1:], item)
    else:
        return BinarySearch(lst[:mid], item)


def BinarySearchIter(lst, item):
    left = 0
    right = len(lst)

    while left <= right:
        mid = (left + right) / 2
        if lst[mid] == item:
            return True
        elif lst[mid] > item:
            right = mid - 1
        elif lst[mid] < item:
            left = mid + 1

    return False

a = [1,2,3,5,7,9]
ans = BinarySearch(a, 2)
print ans
ans = BinarySearchIter(a, 4)
print ans
