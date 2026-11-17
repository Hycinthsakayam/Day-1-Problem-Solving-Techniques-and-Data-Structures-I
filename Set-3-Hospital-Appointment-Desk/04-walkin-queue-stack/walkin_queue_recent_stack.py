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
 for x in ["W01","W02","W03"]:q.enqueue(x)
 print("walk-in FIFO",q.dequeue(),q.dequeue(),q.dequeue())
 s=Stack()
 for x in ["P10","P20","P30"]:s.push(x)
 print("most recent",s.pop())
