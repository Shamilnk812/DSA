
class HashMapWithCollision:
    def __init__(self) -> None:
        # Initialize the hash map with a fixed size and an array of empty lists to handle collisions
        self.size = 10
        self.arr = [[] for _ in range(self.size)]

    def get_hash_value(self, key):
        # Generate a hash value for the given key by summing the ASCII values of its characters
        h = 0
        for i in key:
            h += ord(i)
        return h % self.size


    def insert_items(self, key, val):
        # Insert a key-value pair into the hash map, handling collisions using chaining (lists)
        h = self.get_hash_value(key)
        for index, element in enumerate(self.arr[h]):
            # If the key already exists, update its value
            if element and element[0] == key:
                self.arr[h][index] = (key, val)
                break
        else:
            # If the key does not exist, append the new key-value pair to the list
            self.arr[h].append((key, val))


    def get_items(self, key):
        # Retrieve the value associated with the given key from the hash map
        h = self.get_hash_value(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None  # Return None if the key is not found


    def delete_items(self, key):
        # Delete the key-value pair associated with the given key from the hash map
        h = self.get_hash_value(key)
        for index, element in enumerate(self.arr[h]):
            if element and element[0] == key:
                del self.arr[h][index]
                break  



h1 = HashMapWithCollision()
