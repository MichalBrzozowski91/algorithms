class Solution:
    def sequentialDigits(self, low, high):
        res = [] # List of results
        first_digit = int(str(low)[0]) # Take a first digit of low
        length = len(str(low)) # Get a number of digits of low
        while True:
            if first_digit + length - 1 <= 9: # We check if there exists a number with sequential digits starting with first_digit with number of digits == length
                # Try a number with sequential digits starting with first_digit with number of digits == length
                candidate = ''.join([str(first_digit + i) for i in range(length)])
                candidate = int(candidate)
                if candidate < low:
                    pass
                elif candidate <= high: # A candidate is between low and high, we add it to a result list
                    res.append(candidate)                     
                else: #candidate > high # A candidate is larger than high, hence we have already found all the numbers
                    return res
            elif first_digit == 1: # Candidates are bigger than 123456789 
                return res
            
            # Increment the first digit or a number of digits
            if first_digit != 9:
                first_digit += 1
            else:
                first_digit = 1
                length += 1    
