class MyHashMap(object):

    def __init__(self):
        self.Dict={}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.Dict[key]=value        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.Dict:
            return self.Dict[key]
        return -1 
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.Dict:
            del(self.Dict[key]) 

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)