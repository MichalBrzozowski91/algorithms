from collections import deque
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        rev1 = deque(version1.split('.'))
        rev2 = deque(version2.split('.'))
        num1 = None
        num2 = None
        stop1 = False
        stop2 = False
        while True:
            if not rev1:
                num1 = 0
                stop1 = True
            else:
                num1 = int(rev1.popleft())
            if not rev2:
                num2 = 0
                stop2 = True
            else:
                num2 = int(rev2.popleft())
            if stop1 and stop2:
                return 0
            # Comparision
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        return 0
