#!python

from sorting_iterative import insertion_sort, swap
import random
import time
from random import randint
 
def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(m+n): it's going to go through each item in the array and check
    Memory usage: O(m+n): new list is made with size of item1+item2"""
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
    Running time: Best case : same as insertion sort O(n)
                  Worst case: same as insertion sort O(n^2) 
    Memory usage: O(n): we make a new array to merge it back"""
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
    Running time: O(nlogn): wether it's sorted or unsorted it will keep on
                        breaking into a smaller list until it's of size 1.
                        which is logn and it will do that for n items. so O(nlogn)
    Memory usage: O(nlogn): we're making new list memory each time merge_sort
                        is recursively called"""
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

def time_merge_quick():
    '''
    Time test for merge sort and quick sort
    '''
    #for small lists, merge sort is better than quick sort
    start_time = time.time()
    merge_sort([5,3,4,7,8])
    end_time = time.time()
    print('merge sort', end_time - start_time)
    start_time = time.time()
    quick_sort([5,3,4,7,8])
    end_time = time.time()
    print('quick sort', end_time - start_time)
    print()

    start_time2 = time.time()
    merge_sort([random.randint(1, 20) for _ in range(20)])
    end_time2 = time.time()
    print('merge sort', end_time2 - start_time2)
    start_time2 = time.time()
    quick_sort([random.randint(1, 20) for _ in range(20)])
    end_time2 = time.time()
    print('quick sort', end_time2 - start_time2)
    print()

    start_time3 = time.time()
    merge_sort([random.randint(1, 100) for _ in range(40)])
    end_time3 = time.time()
    print('merge sort', end_time3 - start_time3)
    start_time3 = time.time()
    quick_sort([random.randint(1, 100) for _ in range(40)])
    end_time3 = time.time()
    print('quick sort', end_time3 - start_time3)
    print()

    #Merge sort is much faster when compared to iterative sorts when the list gets larger
    #as the list grows larger, merge sort and quick sort have similar run time
    start_time4 = time.time()
    merge_sort([random.randint(1, 100000) for _ in range(1000)])
    end_time4 = time.time()
    print('merge sort', end_time4 - start_time4)
    start_time4 = time.time()
    quick_sort([random.randint(1, 100000) for _ in range(1000)])
    end_time4 = time.time()
    print('quick sort', end_time4 - start_time4)

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (randomly selecting an item and swapping with high) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    if len(items) == 0: #no items to partition
        return #return None

    #use random item as pivot
    pivot_index = randint(low, high)
    #swap it with high(pivot)
    items[pivot_index], items[high] = items[high], items[pivot_index]
    pivot = high #the last elt
    high = pivot - 1

    while low <= high:
        #check items in low index and high index with pivot
        #if low is greater than pivot, and high is less than pivot, swap
        if items[low] > items[pivot] and items[high] < items[pivot]:
            items[low], items[high] = items[high], items[low]
        #elt at low is on the right place
        if items[low] <= items[pivot]: 
            low += 1 #increment low
        #elt at high is at its right place
        if items[high] >= items[pivot]:
            high -=1 #decrement high
        
    #low passes high; swap low with pivot
    items[low], items[pivot] = items[pivot], items[low]

    #return index of old pivot
    return low

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(nlogn) Why and under what conditions?
    Worst case running time: O(n^2): if the list is sorted
    Memory usage: O(logn) since we're calling it recursively, the call stack will
                    keep on saving variables O(logn) times."""
    
    # TODO: Check if list or range is so small it's already sorted (base case)
    
    
    #Check if high and low range bounds have default values (not given)
    if low is None or high is None:
        low = 0
        high = len(items) - 1

    #Sort each sublist range by recursively calling quick sort
    if low < high:
        #Partition items in-place around a pivot and get index of pivot
        pivot = partition(items, low, high)
        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot+1, high)

if __name__ == '__main__':
    # time_merge_quick()
    items = [2,4,1,3]
    # print(partition(items,0,len(items)-1))
    quick_sort(items)
    print(items)
