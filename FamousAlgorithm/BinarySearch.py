
'''

'''


def binarySearch(lst, item):
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
    i = (first + last) // 2

    if lst[i] == item:
        return i
    elif lst[i] < item:
        return binarySearch(lst[i+1:], item)
    else:
        return binarySearch(lst[:i], item)


a = [1,2,3,5,7,9]
ans = binarySearch(a, 9)
print ans
