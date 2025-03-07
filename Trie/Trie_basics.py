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
    
    
    def get_words_starts_with_prefix(self,prefix):
        def dfs(node,prefix,result):
            if node.is_end:
                result.append(prefix)
            for char in node.children:
                dfs(node.children[char],prefix+char,result)


        node = self.root
        result = []

        for char in prefix:
            if char not in node.children:
                return result
            node = node.children[char]

        dfs(node,prefix,result)

        return result    

    
    def find_logest_word(self):
        longest = [""]
        def dfs(node,word):
            if node.is_end:
                if len(word) > len(longest[0]):
                    longest[0] = word
            for char in node.children:
                dfs(node.children[char],word+char)       

        node = self.root 
        dfs(node,"")
        return longest[0]
    
    def find_smallest_word(self):
        queue = [(self.root, "")]  # Initialize a queue with the root node and an empty word.
    
        while queue:  # Loop until queue is empty
            node, word = queue.pop(0)  # Dequeue the first element
            
            if node.is_end:  # If we reached a complete word
                return word  # Return the first found word (shortest)
            
            for char in node.children:  # Sort keys for lexicographical order
                queue.append((node.children[char], word + char))  # Add child nodes to queue
        
        # return None  # Return None if no words are found

       
       
words = ['apple','shamil','jack','app','application']
t1 = Trie()
for w in words:
    t1.insert_values(w)

print(t1.search_word('shamil'))

print(t1.get_words_starts_with_prefix(''))
print(t1.find_logest_prefix())
print('-------------------')
# print(t1.find_smallest_prefix())
