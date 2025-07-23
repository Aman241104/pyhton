class yourlist:
    def __init__(self,data):
        self.data = data

    def __iter__(self):
        return iter(self.data)
    
for item in yourlist([1,2,3]):
    print(item)