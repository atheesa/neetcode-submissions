class MinStack:

    def __init__(self):
        self.stack_val = []
        self.stack_min = []
        
    
    def push(self, val: int) -> None:
        self.stack_val.append(val)
        if self.stack_min:
            min_val = min(self.stack_min[-1],val)
            self.stack_min.append(min_val)
        else:
            self.stack_min.append(val)

    def pop(self) -> None:
        self.stack_min.pop()
        self.stack_val.pop()

    def top(self) -> int:
       return self.stack_val[-1] 

    def getMin(self) -> int:
        return self.stack_min[-1]   


