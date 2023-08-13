class MinStack:

    def __init__(self):
        self.min_st = [] 
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not len(self.min_st) :
            self.min_st.append(val)
        else:
            if self.min_st[-1] >= val :
                self.min_st.append(val)

    def pop(self) -> None:
        ele = self.st.pop()
        if len(self.min_st) > 0 and self.min_st[-1] == ele:
            self.min_st.pop()

    def top(self) -> int:
        if len(self.st) > 0:
            return self.st[-1]

    def getMin(self) -> int:
        if len(self.min_st) > 0 :
            return self.min_st[-1]
