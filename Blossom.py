class HashMap:
    def __init__(self, size) -> None:
        self.array_size = size
        self.array = [None] * size #list of none objects of length size 


    def hash(self, key):
       return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size 

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        self.array[array_index] = [key, value]

    def retrieve(self, key):
        array_index = self.compress((self.hash(key)))
        payload = self.array[array_index]
        if payload != None:
            if payload[0] == key:
                return payload[1]
        elif payload == None or payload[0] != key:
            return None


