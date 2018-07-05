
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
        return

    first = 0
    last = len(lst) - 1
    mid = (first + last) // 2

    if lst[mid] == item:
        return mid
    elif lst[mid] < item:
        return BinarySearch(lst[mid + 1:], item)
    else:
        return BinarySearch(lst[:mid], item)


a = [1,2,3,5,7,9]
ans = BinarySearch(a, 9)
print ans
