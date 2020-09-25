def numeric_compare(x, y):
    return int(str(x) + str(y)) - int(str(y) + str(x))

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

class Solution:
    def largestNumber(self, nums):
        result = sorted(nums, key=cmp_to_key(numeric_compare), reverse = True)
        string = ''.join(str(integer) for integer in result)
        string = string.lstrip('0')
        if string == '':
            return '0'
        else:
            return string
