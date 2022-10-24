class TrieNode:
    def __init__(self):
        self.children = dict()
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            node.count += 1
    def search(self, word):
        count = 0
        node = self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            count += node.count
        return count
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tree = Trie()
        for word in words:
            tree.insert(word)
        node = tree.root
        
        res = []
        for word in words:
            res.append(tree.search(word))
        return res