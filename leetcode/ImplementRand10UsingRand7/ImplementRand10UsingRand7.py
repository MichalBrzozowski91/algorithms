class Solution:
    # Three helper functions
    
    def rand49(self):
        '''
        Returns a random number from 0 to 48
        Expected value of rand7() calls equal to 2 (It is deterministic) 
        '''
        multiple = rand7() - 1
        remainder = rand7() - 1
        return 7*multiple + remainder
    
    def rand2(self):
        '''
        Returns a random number from 0 to 1
        Expected value of rand7() calls equal to 1 + 1/6 = 7/6 
        '''
        x = rand7()
        while x == 7:
            x = rand7()
        return x % 2

    def rand5(self):
        '''
        Returns a random number from 0 to 4
        Expected value of rand7() calls equal to 1 + 2/5 = 7/5 
        '''
        x = rand7()
        while x in [6,7]:
            x = rand7()
        return x % 5
        
    # Three solutions
    
    def rand10_method_1(self):
        '''
        Returns a random number from 1 to 10
        Expected value of rand7() calls equal to 1 + 2 * (9/40) = 2.45 
        '''
        x = self.rand49()
        while x in range(40,49): # [40,41,42,43,44,45,46,47,48]
            x = self.rand49()
        return 1 + x % 10
    
    def rand10_method_2(self):
        '''
        Returns a random number from 1 to 10
        Expected value of rand7() calls equal to 1 + 2/7(7/5) + (5/7)(7/6) = 2.2(3) 
        '''
        x = rand7()
        if x in [1,2]:
            y = self.rand5()
            return 5*(x-1) + y + 1 
        if x in [3,4,5,6,7]:
            y = self.rand2()
            return 5*y + (x-3) + 1

    def rand10_method_3(self):
        '''
        Returns a random number from 1 to 10
        Expected value of rand7() calls equal to 2.19(3) 
        '''
        while True:
            x = rand7() - 1 #  Uniform Distribution (UD) on 0,...,6
            y = rand7() - 1 # UD on 0,...,6
            result = (x)*7 + y # UD on 0,1,...,48
            if result not in range(40,49): # [40,41,42,43,44,45,46,47,48]
                # result conditionally uniformly distributed on 0,...,49
                return result % 10 + 1 # result % 10 UD on 0,...,9 
            else:
                x = result - 40 # UD on 0,...,8
                y = rand7() - 1 # UD on 0,...,6
                result = x * 7 + y # UD on 0,...,62
                if result not in range(60,63): #[60,61,62]
                    # result conditionally uniformly distributed on 0,...,59
                    return result % 10 + 1 # result % 10 UD on 0,...,9
                else:
                    x = result - 60 # UD on 0,...,2
                    y = rand7() - 1# UD on 0,...,6
                    result = (x)*7 + y # UD on 0,1,...,20
                    if result != 20:
                        # conditionally uniformly distributed on 0,...,19
                        return result % 10 + 1 # result % 10 has uniform distribution on 0,...,9
                    else: continue
