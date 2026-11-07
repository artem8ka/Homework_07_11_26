class Stack:
    def __init__(self):
        self.lst=[]
    def push(self,num):
        if len(self.lst)>0:
            self.lst.append([num,min(num,self.lst[-1][1])])
        else:
            self.lst.append([num,num])
    def pop(self):
        if len(self.lst)>0:
            self.lst.pop()
    def top(self):
        if len(self.lst)>0:
            return self.lst[-1][0]
        else:
            return None
    def get_min(self):
        if len(self.lst)>0:
            return self.lst[-1][1]
        else:
            return None
stack = Stack()
stack.push(-2)
stack.push(0)
stack.push(-3)
assert stack.get_min() == -3
stack.pop()
assert stack.top() == 0
assert stack.get_min() == -2
print('проверки пройдены')