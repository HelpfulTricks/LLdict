class HTDictionary:

    #written by madi
    def __init__(self, arr, size):
        #sets the size of our hash table
        self._max_size = size
        #creates an array of a number of arrays equal to our max size, which is 20
        self._hash_table = [[] for _ in range(0, self._max_size)]
        #for each item in the input array, we run the key (i[0]) through the hash function, which assigns it to a certain slot in the hash table depending on its key value
        for i in arr:
            self._hash_table[self._hash_function(i[0])-1].append(i)
        #size will dictate how many actual objects are in the array, will be updated whenever we insert or pop an item from the array
        self._size = len(arr)

    #provided as part of the assignment
    def _hash_function(self, key):
        return key % self._max_size

    #provided as part of the assignment
    def __len__(self):
        return self._size

    #written by madi
    def _find(self, key):
        #we find which entry in the hash table it'd be in using the hash function, and loop through each item in that entry
        for i, j in enumerate(self._hash_table[self._hash_function(key)-1]):
            #we're looking for the key here
            if j[0] == key:
                #if we find it, we return an array containing the array we're looking in, and the entry in that array
                return [self._hash_function(key)-1, i]
        #if we never found it, we simply return -1.
        #we don't have to worry about this accidentally activating, as this only comes up if we haven't returned yet, which is what we want.
        return -1

    #provided as part of the assignment
    def __contains__(self, key):
        results = self._find(key)
        if results == -1:
            return False
        return True

    #written by madi
    def __getitem__(self, key):
        #first, we find the key value we're looking for
        item = self._find(key)
        #and raise an error if it doesn't exist
        if item == -1:
            raise KeyError("Item does not exist")
        #if it does exist, we return the item we're looking for. it looks a bit odd, but since each key-value pair is in an arrays of arrays, this is how we have to do it.
        return self._hash_table[item[0]][item[1]]

    #provided as part of the assignment
    def __setitem__(self, key, value):
        self._insert(key,value)

    #written by madi
    def _insert(self, key, value):
        #first, we try to find the key value to check if it exists already
        item = self._find(key)
        if item == -1:
            #if it does not, we add it into the hash table and increase the size
            self._hash_table[self._hash_function(key)-1].append([key, value])
            self._size += 1
        else:
            #otherwise, we change the value of the already-existing key
            self._hash_table[item[0]][item[1]] = [key, value]

    #written by madi
    def pop(self, key):
        #once again, we first find the key to make sure it exists
        item = self._find(key)
        if item == -1:
            #and raise an error if it doesn't
            raise KeyError("Item does not exist")
        else:
            #and remove it if it does
            self._hash_table[item[0]].pop(item[1])
            self._size -= 1

    #provided as part of the assignment
    def __str__(self):
        results = ""
        for entry in self._hash_table:
            if len(entry) != 0:
                for x in entry:
                    results+= "Key: " + str(x[0]) + " value: " + x[1]
                    results += "\n"
        results += "Length: " + str(self._size)
        return results

#all code below is testing code that was provided as part of the assignment
def main():
    arr = [[1,"John"],[3,"Jack"],[2, "Ann"], [21, "Amy"]]
    d = HTDictionary(arr, 20)
    # Printing original dictionary
    print(d)
    # Changing the entry at key 1 in the dictionary
    d[1] = "Ted"
    print(d)
    # Removing the entry at key in the dictionary
    d.pop(1)
    print(d)
    # Inserting a new entry in the dictionary
    d[23] = "Jade"
    print(d)

    '''
    How the output will look like for the above main:

    Key: 1 value: John
    Key: 21 value: Amy
    Key: 2 value: Ann
    Key: 3 value: Jack

    Key: 1 value: Ted
    Key: 21 value: Amy
    Key: 2 value: Ann
    Key: 3 value: Jack

    Key: 21 value: Amy
    Key: 2 value: Ann
    Key: 3 value: Jack

    Key: 21 value: Amy
    Key: 2 value: Ann
    Key: 3 value: Jack
    Key: 23 value: Jade
    '''

if __name__ == "__main__":
    main()
