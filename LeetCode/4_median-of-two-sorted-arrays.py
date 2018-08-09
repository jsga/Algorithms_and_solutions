"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


def findMin(nums1, nums2):
    #  here we keep the prev item (we just need 2 items to calculate median)
    # Remember that one of the lists can be empty
    if len(nums1) > 0 and len(nums2) > 0:
        prev = min(nums1[0], nums2[0])
        # Take out first element
        if prev == nums1[0]:
            nums1.pop(0)
        else:
            nums2.pop(0)

    elif len(nums1) == 0 and len(nums2) > 0:
        prev = nums2.pop(0)

    elif len(nums1) > 0 and len(nums2) == 0:
        prev = nums1.pop(0)

    else:
        print('Not possible')

    return prev, nums1, nums2


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # If some list is length zero?


    # find the indexes of the max
    n1 = len(nums1)
    n2 = len(nums2)
    N = n1 + n2
    imax = N // 2 # we just need to sort half of the items

    if N % 2 == 0: # do we take the avg of two items or not?
        avg2 = True
    else:
        avg2 = False

    # Start the sorting
    last, nums1, nums2 = findMin(nums1,nums2)

    i = 1
    while i <= imax:
        prev = last
        last, nums1,nums2 = findMin(nums1, nums2)
        i += 1

    # Calculate median
    if avg2 == True:
        median = (float(prev) + float(last))/2
    else:
        median = last

    # END
    return median




nums1 = [1,2,3]
nums2 = [2,4,5]

findMin(nums1,nums2)

nums1 = []
findMin(nums1,nums2)

findMedianSortedArrays(nums1,nums2)

nums1 = [1]
nums2 = [2,3]
findMedianSortedArrays(nums1,nums2)




