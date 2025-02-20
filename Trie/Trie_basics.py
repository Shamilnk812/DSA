class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False



class Trie:
    def __init__(self):
        self.root = TrieNode()

    
    def insert_values(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end  = True


    def search_word(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end


    def delete_word(self,word):
        if not self.search_word(word) :
            print('given word not found')
            return         
        
        current_node = self.root
        stack = []

        for char in word:
            stack.append(current_node)
            current_node = current_node.children[char]

        while stack:
            node = stack.pop()
            char = word[len(stack)]

            if not node.children[char].is_end and not node.children[char].children  :
                del node.children[char] 
            else :
                break

        print('word removed') 
    


    def starts_with(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True    

   



words = ['apple','shamil','jack','app','application']
t1 = Trie()
for w in words:
    t1.insert_values(w)

print(t1.search_word('shamil'))




