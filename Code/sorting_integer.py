#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    minimum = min(numbers)
    # print('min',minimum)
    maximum = max(numbers)
    # print('max', maximum)
    hist_num = [0 for i in range(maximum - minimum + 1)]
    
    #make the histogram array
    for i in numbers:
        hist_num[i - minimum] += 1

    #create a pointer
    pointer = 0
    for index, frequency in enumerate(hist_num): #loop over your 'histogram'
        for i in range(frequency):
            numbers[pointer] = index + minimum    #overwrite the orignal list
            pointer += 1 #increment pointer

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    pass


numbers = [10, 10, 11, 10]
counting_sort(numbers)
print(numbers)