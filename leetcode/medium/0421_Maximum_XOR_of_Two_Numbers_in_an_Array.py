class Solution:
    def findMaximumXOR(self, nums):
        result = ''
        # Edge cases
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return nums[0] ^ nums[1]
        # Create a list of binary representations
        binary = list(nums)
        for i in range(len(nums)):
            binary[i] = str(bin(nums[i]))[2:]
            binary[i] = '0' * (31 - len(binary[i])) + binary[i]
        # Create a first container
        i = 0
        while i < 31:
            bag_0 = {j for j in range(len(nums)) if binary[j][i] == '0'}
            bag_1 = {j for j in range(len(nums)) if binary[j][i] == '1'}
            i += 1
            if bag_0 and bag_1: # Both bags are nonempty
                result += '1'
                container = [[bag_0,bag_1]]
                break
        #print(container, result + '?'*(31-i))
        while i < 31:
            new_container = []
            for pair in container:
                bag_00 = {j for j in pair[0] if binary[j][i] == '0'}
                bag_11 = {j for j in pair[1] if binary[j][i] == '1'}
                if bag_00 and bag_11: # Both bags are nonempty
                    new_container.append([bag_00,bag_11])
                bag_01 = {j for j in pair[0] if binary[j][i] == '1'}
                bag_10 = {j for j in pair[1] if binary[j][i] == '0'}
                if bag_01 and bag_10: # Both bags are nonempty
                    new_container.append([bag_01,bag_10])
            if new_container:
                result += '1'
                container = new_container
            else:
                result += '0'
            i += 1
            #print(container, result + '?'*(31-i))
        return int(result,2)
