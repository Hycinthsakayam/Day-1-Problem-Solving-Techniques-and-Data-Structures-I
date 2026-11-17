from collections import deque
class Stack:
 def __init__(s):s.a=[]
 def push(s,x):s.a.append(x)
 def pop(s):return s.a.pop()
class Queue:
 def __init__(s):s.a=[]
 def enqueue(s,x):s.a.append(x)
 def dequeue(s):return s.a.pop(0)
if __name__=="__main__":
 s=Stack()
 for x in ["address edit","quantity edit","coupon edit"]:s.push(x)
 print("undo",s.pop())
 q=Queue()
 for x in ["O1","O2","O3"]:q.enqueue(x)
 print("dispatch",q.dequeue(),q.dequeue(),q.dequeue())
 d=deque(["O1","O2"]);print("deque popleft",d.popleft())
