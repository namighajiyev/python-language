class Solution:
    
    def getPermutations(self,array):
        permutations = []
        self.permutationsHelper(array,[], permutations)
        return permutations

    def permutationsHelper(self, array, currentPermutation, permutations):
        if not len(array) and len(currentPermutation):
            permutations.append(currentPermutation)
            return
        
        for i in range(len(array)):
            newPermutation = currentPermutation+[array[i]]
            newArray = array[:i]+array[i+1:]
            self.permutationsHelper(newArray, newPermutation, permutations)
sol = Solution()
print(sol.getPermutations([1,2,3]))
print(sol.getPermutations([1,2,3,4]))
        
        
    