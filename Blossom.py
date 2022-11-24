from linkedlist import Node, LinkedList
class HashMap:
    def __init__(self, size) -> None:
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)] #list of none objects of length size 


    def hash(self, key):
       return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size 

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key,value])
        list_at_array = self.array[array_index]
        for i in list_at_array:
            if i[0] == key:
                i[1] = value
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress((self.hash(key)))
        list_at_index = self.array[array_index]
        for i in list_at_index:
            if i[0] == key:
                return i[1]
        return None
