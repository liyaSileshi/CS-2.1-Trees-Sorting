#!python

from sorting_iterative import insertion_sort, swap
def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #Repeat until one list is empty
    #Find minimum item in both lists and append it to new list
    #Append remaining items in non-empty list to new list
    new_list = []
    items1_pointer = 0
    items2_pointer = 0
    #both should have items
    while (items1_pointer < len(items1) and items2_pointer < len(items2)):
        if (items1[items1_pointer] < items2[items2_pointer]): #check for stable
            new_list.append(items1[items1_pointer])
            items1_pointer += 1
        else:
            new_list.append(items2[items2_pointer])
            items2_pointer += 1
    #check which pointer is greater(to know which has been copied fully)
    #then append the remaining items
    # if items1_pointer < items2_pointer:
        # while(items1_pointer < len(items1)):
    new_list.extend(items1[items1_pointer:])
            # new_list.append(items1[items1_pointer])
            # items1_pointer += 1
    # else:
        # while(items2_pointer < len(items2)):
    new_list.extend(items2[items2_pointer:])
            # items2_pointer += 1

    return new_list

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #Split items list into approximately equal halves
    # Sort each half using any other sorting algorithm
    # Merge sorted halves into one list in sorted order

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
    # for i in range(len(merged)):
    #     items[i] = merged[i]
    items[:] = merged

    return items

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    #Split items list into approximately equal halves
    #the first half of the list
    items1 = items[:len(items)//2]
    #second half of the list
    items2 = items[len(items)//2: len(items)]
    #Sort each half by recursively calling merge sort
    items1 = merge_sort(items1)
    items2 = merge_sort(items2)
    #Merge sorted halves into one list in sorted order
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
    #Choose a pivot any way and document your method in docstring above
    pivot = high #the last elt
    high = pivot - 1
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]

    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    while low <= high:
        #check items in low index and high index with pivot
        #if low is greater than pivot, and high is less than pivot, swap
        if items[low] > items[pivot] and items[high] < items[pivot]:
            # swap(items, low, high)
            items[low], items[high] = items[high], items[low]
        #elt at low is on the right place
        if items[low] <= items[pivot]: 
            low += 1 #increment low
        #elt at high is at its right place
        if items[high] >= items[pivot]:
            high -=1 #decrement high
        
    #low passes high; swap low with pivot
    items[low], items[pivot] = items[pivot], items[low]
    # swap(items, low, pivot)
    # print(items)
    #return index of old pivot
    return low


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
    if low is None or high is None:
        low = 0
        high = len(items) - 1

    # if len(items) <= 1: #already sorted
    #     return items

    # if (high - low) <= 1: 
    #     return
    #sort based on the pivot and save the pivot inside a variable
    
    if low < high:
        pivot = partition(items, low, high)
        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot+1, high)

if __name__ == '__main__':
    # print(merge([1,4,6],[2,3,7]))
    # print(merge_sort([3,8,5,2,6,9]))
    items = [9,5,2,6,1,11,3]
    items2 = [1]
    items3 = [6,9,11,5]
    # print(partition(items,0,len(items)-1))
    quick_sort(items)
    print(items)