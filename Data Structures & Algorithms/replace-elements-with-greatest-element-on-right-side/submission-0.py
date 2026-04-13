class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_val = -1
            for n in range(i+1,len(arr)):
                if max_val < arr[n]:
                    max_val = arr[n]
            arr[i] = max_val
        return arr