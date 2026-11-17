class Queue:
 def __init__(s):s.a=[]
 def enqueue(s,x):s.a.append(x)
 def dequeue(s):return s.a.pop(0)
class Stack:
 def __init__(s):s.a=[]
 def push(s,x):s.a.append(x)
 def pop(s):return s.a.pop()
if __name__=="__main__":
 q=Queue()
 for x in ["TX100","TX101","TX102"]:q.enqueue(x)
 print("FIFO",q.dequeue(),q.dequeue(),q.dequeue())
 s=Stack()
 for x in ["fee +10","interest -5","correction +2"]:s.push(x)
 print("undo",s.pop())
