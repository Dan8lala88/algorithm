class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        #result = [0 for x in range(100)]
        result = 0
        n_2 = 0
        n_1 = 0
        for i in range(n):
            if i <= 1:
                result = i
            else:
                #result[i] = result[i-2] + result[i-1]
                #result = self.fibonacci(n-2) + self.fibonacci(n-1)
                n_2 = n_1
                n_1 = result
                result = n_2 + n_1
       return result 
