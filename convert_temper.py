# submission: https://leetcode.com/problems/convert-the-temperature/submissions/1894057792

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15 , celsius * 1.80 + 32.00]