class Solution:
    def average(self, salary: List[int]) -> float:
        minsalary = min(salary)
        maxsalary = max(salary)
        return (sum(salary) - minsalary - maxsalary)/(len(salary) - 2)