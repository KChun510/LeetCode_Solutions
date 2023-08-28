class MyStack:
    def __init__(self):
        self.arr = []
        
    def push(self, x: int) -> None:
        self.arr += [x]
    
    def pop(self) -> int:
        max_len = len(self.arr) - 1
        last_val = self.arr[max_len]
        self.arr = self.arr[0:max_len]
        return last_val
        
    def top(self) -> int:
        max_len = len(self.arr) - 1
        return self.arr[max_len] 
        

    def empty(self) -> bool:
        max_len = len(self.arr)
        if max_len <= 0:
            return True 
        else:
            return False
