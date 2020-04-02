#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #Check that all adjacent items are in order, return early if so
    if len(items) < 2: #if there is only 1 item or none
        return True

    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False #not sorted
    return True #sorted

def swap(items, i, j): 
    '''Helper function to swap items'''
    # temp = items[j]
    # items[j] = items[j+1]
    # items[j+1] = temp
    items[i], items[j] = items[j], items[i] 

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: Worst case: O(n^2) - we'll have O(n-1) passes
                                        and checking to swap each element with
                                        the rest of the elements O(n)
                  Best case: O(n) - when the items are sorted. 
    TODO: Memory usage: ??? Why and under what conditions?"""
    #Repeat until all items are in sorted order
    #Swap adjacent items that are out of order

    steps = 0 #to track the range of items we want to compare
    looks = len(items) - steps #the range of item we'll compare
    swapped = False #to keep track if any swaps are being made in one round loop
    for _ in range(looks):
        for j in range(looks - 1): #-1 for index not to be out of range
            if items[j] > items[j+1]:
                swap(items, j, j+1) #call the swap function
                swapped = True #we made a swap
                
        steps -= 1 #decrements because each iteration, the last item will be sorted
        if swapped == False: #no swaps were made; everything is sorted
            return items #exit early
    return items
    
def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    pointer = 0
    minimum = items[pointer]
    for i in items:
        tracker_minimum = i 


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


if __name__ == '__main__':
    # print(is_sorted(['a', 'b', 'c', 'd']))
    print(bubble_sort([5,3]))
