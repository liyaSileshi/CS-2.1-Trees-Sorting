#!python

from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    new_list = []
    items1_pointer = 0
    items2_pointer = 0
    #both should have items
    while (items1_pointer < len(items1) and items2_pointer < len(items2)):
        if (items1[items1_pointer] < items2[items2_pointer]):
            new_list.append(items1[items1_pointer])
            items1_pointer += 1
        else:
            new_list.append(items2[items2_pointer])
            items2_pointer += 1
    #check which pointer is greater(to know which has been copied fully)
    #then append the remaining items
    if items1_pointer < items2_pointer:
        while(items1_pointer < len(items1)):
            new_list.append(items1[items1_pointer])
            items1_pointer += 1
    else:
        while(items2_pointer < len(items2)):
            new_list.append(items2[items2_pointer])
            items2_pointer += 1

    return new_list

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order

    #the first half of the list
    items1 = items[:len(items)//2]
    #second half of the list
    items2 = items[len(items)//2: len(items)]
    #sort each lists individually
    items1 = insertion_sort(items1)
    items2 = insertion_sort(items2)
    #merge the two sorted lists back
    merged = merge(items1, items2)

    #copy everything from merged to items one by one
    for i in range(len(merged)):
        items[i] = merged[i]

    return items

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # TODO: Split items list into approximately equal halves
    #the first half of the list
    items1 = items[:len(items)//2]
    #second half of the list
    items2 = items[len(items)//2: len(items)]
    # TODO: Sort each half by recursively calling merge sort
    items1 = merge_sort(items1)
    items2 = merge_sort(items2)
    # TODO: Merge sorted halves into one list in sorted order
    merged = merge(items1, items2)
    #copy everything from merged to items one by one
    for i in range(len(merged)):
        items[i] = merged[i]

    return items
    
def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


if __name__ == '__main__':
    # print(merge([1,4,6],[2,3,7]))
    print(merge_sort([3,8,5,2,6,9]))