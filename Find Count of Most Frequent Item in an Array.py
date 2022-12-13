# DESCRIPTION:
# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
#
# Example
# input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# ouptut: 5
# The most frequent number in the array is -1 and it occurs 5 times.

def most_frequent_item_count(collection):
    # Do your magic. :)
    dict_ = ({i:collection.count(i) for i in collection})
    if collection ==[]:
        return 0
    return max(dict_.values())