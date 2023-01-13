class Solution:
    
    def getPermutations(self,array):
        permutations = []
        self.permutationsHelper(0,array, permutations)
        return permutations

    def permutationsHelper(self, i, array, permutations):
        if i == len(array) -1:
            permutations.append(array[:])
            return
        
        for j in range(i,len(array)):
            self.swap(array, i, j)
            self.permutationsHelper(i+1, array, permutations)
            self.swap(array, i, j)
            
    def swap(self, array, i, j):
        array[i], array[j] = array[j] , array[i]
        

sol = Solution()
print(sol.getPermutations([1,2,3]))
print(sol.getPermutations([1,2,3,4]))
        
        
    