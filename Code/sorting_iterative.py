#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: Best case: O(1) - if no items or 1 item
                  Worst case:  O(n) - if everything is sorted except the last two items
    Memory usage: O(1) - we're not creating new memory"""
    #Check that all adjacent items are in order, return early if so
    if len(items) < 2: #if there is only 1 item or none
        return True

    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False #not sorted
    return True #sorted

def swap(items, i, j): 
    '''Helper function to swap items'''
    items[i], items[j] = items[j], items[i] 

def bubble_sort(items, ascending=True):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: Worst case: O(n^2) - we'll have O(n-1) passes
                                        and checking to swap each element with
                                        the rest of the elements O(n)
                  Best case: O(n) - when the items are sorted. 
    Memory usage: O(1) When we're swapping we're not making new memory, we're just ch
                   changing reference"""
    #Repeat until all items are in sorted order
    #Swap adjacent items that are out of order

    steps = 0 #to track the range of items we want to compare
    looks = len(items) - steps #the range of item we'll compare
    swapped = False #to keep track if any swaps are being made in one round loop
    for _ in range(looks):
        for j in range(looks - 1): #-1 for index not to be out of range
            if ascending == True: #ascending order
                if items[j] > items[j+1]:
                    swap(items, j, j+1) #call the swap function
                    swapped = True #we made a swap
            else: #decreasing order
                if items[j] < items[j+1]:
                    swap(items, j, j+1) #call the swap function
                    swapped = True #we made a swap 
        steps -= 1 #decrements because each iteration, the last item will be sorted
        if swapped == False: #no swaps were made; everything is sorted
            return items #exit early

    return items
def selection_sort(items, ascending=True):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) even if all items are sorted we would have to loop 
                    through the entire array to check if there's minimum than
                    current...

    Memory usage: O(1)- in the for loop we're changing reference not making
                        new memory"""
    # Repeat until all items are in sorted order
    # Find minimum item in unsorted items
    # Swap it with first unsorted item
    
    for i in range(len(items)): 
        curr = items[i] #should hold the min/max elt from the given range (updates to find the 'real' min/max)
        curr_index = i #the index of the min/max
        for j in range(i+1, len(items)): #the items in the right of the curr
            if ascending == True: #increasing order
                if items[j] < curr: #compare the cur to each item
                    curr = items[j] #if lesser is found, update curr
                    curr_index = j #update the index as well
            else: #decreasing order
                if items[j] > curr: #compare the curr_min to each item
                    curr = items[j] #if lesser is found, update curr_min
                    curr_index = j #update the index as well

        if curr_index != i: #to make sure curr min was actually updated
            swap(items, curr_index, i) #swap the new min with old min(i)
    return items 

def insertion_sort(items, ascending=True):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Best case: O(n) - if all items are sorted, yet it has to check if they are
                  Worst case: O(n^2) - if sorted in decreasing order
    Memory usage: O(1) no new memory allocated"""
    #Repeat until all items are in sorted order
    #Take first unsorted item
    #Insert it in sorted order in front of items
    for i in range(1, len(items)):
        pulled = items[i] #the item we pulled
        hole = i #the 'hole' we need to fill by shifting/inserting

        #while hole is greater than the first index
        #and items before the pulled element is greater
        # than the pulled element
        if ascending == True: #increasing order
            while (hole > 0 and items[hole - 1] > pulled):
                items[hole] = items[hole-1] #hole gets filled by shifting items to the right
                hole -= 1 #adjust where the new hole is (adjusted to left)
        else: #decreasing order
             while (hole > 0 and items[hole - 1] < pulled):
                items[hole] = items[hole-1] #hole gets filled by shifting items to the right
                hole -= 1 #adjust where the new hole is (adjusted to left)

        items[hole] = pulled #insert the pulled item into the hole
    return items

def cocktail_shaker_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order. both backwards and forward
    Running time: Worst case: O(n^2) 
                  Best case: O(n) - when the items are sorted. 
    Memory usage: O(1) """
    steps = 0 #to track the range of items we want to compare
    looks = len(items) - steps #the range of item we'll compare
    swapped = False #to keep track if any swaps are being made in one round loop
    start = 1 #start pointer; increases each time revese bubble sort loop runs

    for _ in range(looks):
        for j in range(looks - 1): #-1 for index not to be out of range
                if items[j] > items[j+1]:
                    swap(items, j, j+1) #call the swap function
                    swapped = True #we made a swap
            
        steps -= 1 #decrements because each iteration, the last item will be sorted
        if swapped == False: #no swaps were made; everything is sorted
            return items #exit early

        swapped = False #start with swap being false for reverse bubble sort
        for k in reversed(range(start, looks-1)):
            if items[k] < items[k-1]:
                items[k], items[k-1] = items[k-1], items[k]
                swapped = True
        start += 1 #increment start 
        if swapped == False: #no swaps were made; everything is sorted
            return items #exit early

    return items

if __name__ == '__main__':
    # print(is_sorted(['a', 'b', 'c', 'd']))
    # print(bubble_sort([5,3,4,7,8],False))
    # print(selection_sort([5,3,3,9,0,8], False))
    # print(insertion_sort([5,3,7], False))
    print(cocktail_shaker_sort([2,4,6,2,1,3]))
    # for i in reversed( range(1, 10)):
    #     print(i)
