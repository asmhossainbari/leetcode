import random


'''
Time complexity: O(1) average for insert, remove, and getRandom
Space complexity: O(n)
'''
class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        self.num_map[val] = len(self.num_list)
        self.num_list.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False
        idx = self.num_map[val]
        last_val = self.num_list[-1]
        self.num_list[idx] = last_val
        self.num_map[last_val] = idx
        self.num_list.pop()
        del self.num_map[val]
        return True    

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
