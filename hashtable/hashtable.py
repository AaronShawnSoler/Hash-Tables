class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.key}, {self.value}"


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.items = 0
        self.slots = len(self.storage)
        self.load = 0
        self.resizing = False

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        hash = 14695981039346656037

        key_bytes = str(key).encode()

        for byte in key_bytes:
            hash *= 1099511628211
            hash ^= byte

        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # print(key, self.fnv1(key) % self.capacity)
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        new_hash = HashTableEntry(key, value)
        print(new_hash)
        index = self.hash_index(key)
        if self.storage[index] == None:
            self.storage[index] = new_hash
            self.items = len(self.storage) - self.storage.count(None)
            self.slots = len(self.storage)
            self.load = round(self.items / self.slots, 2)
            print("LOAD: ", self.load)
            if self.resizing == False:
                if self.load < 0.2 or self.load > 0.7:
                    self.resize()
        else:
            if self.storage[index].key == key:
                self.storage[index].value = value
                return
            curr_entry = self.storage[index]
            while curr_entry.next != None:
                curr_entry = curr_entry.next
                if curr_entry.key == key:
                    curr_entry.value = value
                    return

            curr_entry.next = new_hash
            print("CURR: ", curr_entry)
            print("NEXT: ", curr_entry.next)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index].key == key:
            self.storage[index] = None
            self.items = len(self.storage) - self.storage.count(None)
            self.slots = len(self.storage)
            self.load = round(self.items / self.slots, 2)
            print("LOAD: ", self.load)
            if self.resizing == False:
                if self.load < 0.2 or self.load > 0.7:
                    self.resize()
        else:
            last_entry = None
            curr_entry = self.storage[index]
            while curr_entry.key != key:
                last_entry = curr_entry
                curr_entry = curr_entry.next
            print("DELETE: ", curr_entry)
            if curr_entry.next == None:
                print(last_entry)
                print("NONE")
                last_entry.next = None
            else:
                print(last_entry)
                print(curr_entry.next)
                last_entry.next = curr_entry.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        # if entry != None:
        #     curr_entry = entry
        #     while curr_entry.next != None:
        #         curr_entry = curr_entry.next
        #         print(curr_entry)
        if self.storage[index] != None:
            if self.storage[index].key == key:
                return self.storage[index].value

            curr_entry = self.storage[index]
            while curr_entry.next != None:
                curr_entry = curr_entry.next
                if curr_entry.key == key:
                    return curr_entry.value
            return None
        else:
            return self.storage[index]

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.resizing = True

        if self.load < 0.2:
            print("**** HALF ****", self.load, self.slots)
            self.capacity //= 2
        elif self.load > 0.7:
            print("**** DOUBLE ****", self.load, self.slots)
            self.capacity *= 2
        old_storage = self.storage.copy()
        self.storage = [None] * self.capacity

        entries = []

        for entry in old_storage:
            if entry != None:
                entries.append(entry)
                curr_entry = entry
                while curr_entry.next != None:
                    curr_entry = curr_entry.next
                    entries.append(curr_entry)

        for entry in entries:
            self.put(entry.key, entry.value)

        self.resizing = False


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    ht.put("line_4", "I'm overflowing")
    ht.put("line_5", "There's way too much")

    print("")

    ht.delete("line_5")
    ht.delete('line_3')
    ht.delete('line_4')
    # ht.delete('line_2')

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))
    print(ht.get("line_4"))
    print(ht.get("line_5"))

    print(ht.storage)
    print("LOAD: ", ht.load)

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))
    print(ht.get("line_4"))
    print(ht.get("line_5"))

    print(ht.storage)
    print("LOAD: ", ht.load)

    print("====================================")
    for index, entry in enumerate(ht.storage):
        print(f"Entry {index}:")
        print(entry)
        if entry != None:
            curr_entry = entry
            while curr_entry.next != None:
                curr_entry = curr_entry.next
                print(curr_entry)
        print("")
