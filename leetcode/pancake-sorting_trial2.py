class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        last = len(arr) - 1
        k_ = []

        def search(end):
            idx = 0
            for i in range(1, end + 1):
                if arr[i] > arr[idx]:
                    idx = i
            return idx

        while last > 0:
            i = search(last)

            arr[:i + 1] = reversed(arr[:i + 1])
            k_.append(i + 1)

            arr[:last + 1] = reversed(arr[:last + 1])
            k_.append(last + 1)

            last -= 1
        return k_