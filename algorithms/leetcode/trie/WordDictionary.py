class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for x in word:
            if not x in curr:
                curr[x] = {}
                curr = curr[x]
            else:
                curr=curr[x]
        curr["*"] = True

    def search(self, word: str) -> bool:
        return self.searchRecursive(word, self.root, 0)
    
    def searchRecursive(self, word: str, root, startIndex) -> bool: 
            curr = root
            if root == True:
                return startIndex == len(word)
            for i in range(startIndex, len(word)):
                x = word[i]
                if x == "." : 
                    if i == len(word) -1 and "*" in curr:
                        return True
                    for key in curr:
                        if key == "*":
                            continue
                        if self.searchRecursive(word, curr[key], startIndex+1):
                            return True
                    return False
                else:
                    if x not in curr:
                        return False
                    curr = curr[x]
            return curr == True or "*" in curr
                

def run(ops, words):
    dict = WordDictionary()
    res = []
    for i, op in enumerate(ops):
        match op:
            case "WordDictionary":
                res.append(None)
            case "addWord" :
                dict.addWord(words[i][0])
                res.append(None)
            case "search" :
                res.append(dict.search(words[i][0]))
    print(res)
    return (dict, res)

def isEqual(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

# example 1
_ , res =run(["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]])   
print(isEqual(res, [None,None,None,None,False,True,True,True] ))  

            
# example 2
_ , res =run(["WordDictionary","addWord","addWord","search","search","search","search","search","search"],
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]])   
print(isEqual(res, [None,None,None,True,True,False,True,False,False]))  

# example 3
dict , res =run(["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"],
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]])   
print(isEqual(res, [None,None,None,None,None,False,False,None,True,True,False,False,True,False])) 


# dict = WordDictionary()
# dict.addWord("and")
# print(dict.search("an."))