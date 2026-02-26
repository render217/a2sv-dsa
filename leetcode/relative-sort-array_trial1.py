class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr1)
        order = {v: i for i, v in enumerate(arr2)}
        def key(x):
            return (order.get(x, float('inf')), x)

        # selection sort
        # for i in range(n):
        #     min_idx = i
        #     for j in range(i+1,n):
        #         if key(arr1[j]) < key(arr1[min_idx]):
        #             min_idx  = j
        #     arr1[min_idx],arr1[i] = arr1[i],arr1[min_idx]

        #bubble sort
        #  for i in range(n):
        #     for j in range(n-1-i):
        #         a = arr1[j]
        #         b = arr1[j+1]

        #         key_a = (order.get(a,float("inf")),a)
        #         key_b = (order.get(b,float("inf")),b)

        #         if key_a > key_b:
        #             arr1[j] , arr1[j+1] = arr1[j+1], arr1[j]

        # insertion sort
        # for i in range(1,n):
        #     current = arr1[i]
        #     j = i - 1
        #     while j >= 0 and key(arr1[j]) >  key(current):
        #         arr1[j+1] = arr1[j]
        #         j-=1
        #     arr1[j+1] = current

      
        # return arr1
        return sorted(arr1, key=lambda x: key(x))