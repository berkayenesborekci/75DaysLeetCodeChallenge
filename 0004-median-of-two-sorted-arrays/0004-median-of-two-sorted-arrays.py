class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        arr = len(num1) + len(num2)
        sortedarray = sorted(num1 + num2)
        if arr % 2 == 0 :
            arr /= 2
            median = (sortedarray[int(arr)-1] + sortedarray[int(arr)])/2
        else :
            arr/= 2
            arr= int(arr)
            median = sortedarray[int(arr)]
        return median