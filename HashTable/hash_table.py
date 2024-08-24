class HashMap:
    def __init__(self) -> None:
        # Initialize the hash map with a fixed size of 10 and an array filled with None
        self.size = 10
        self.arr = [None for _ in range(self.size)]


    # Generate a hash value for the given key by summing the ASCII values of its characters
    def get_hash_value(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.size


    # Insert a key-value pair into the hash map. Overwrites any existing value at the same hash index
    def insert_item(self, key, val):
        h = self.get_hash_value(key)
        self.arr[h] = val


    # Retrieve the value associated with the given key from the hash map
    def get_item(self, key):
        h = self.get_hash_value(key)
        return self.arr[h]


    # Delete the key-value pair associated with the given key from the hash map by setting it to None
    def delete_item(self, key):
        h = self.get_hash_value(key)
        self.arr[h] = None



h1 = HashMap()
