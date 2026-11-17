from bisect import bisect_right
def dp(jobs):
 a=sorted(jobs,key=lambda x:x[1]);ends=[x[1] for x in a];p=[]
 for i,(s,e,n) in enumerate(a):p.append(bisect_right(ends,s,0,i)-1)
 d=[0]*(len(a)+1)
 for i in range(1,len(a)+1):d[i]=max(d[i-1],1+d[p[i-1]+1])
 out=[];i=len(a)
 while i:
  if 1+d[p[i-1]+1]>d[i-1]:out.append(a[i-1][2]);i=p[i-1]+1
  else:i-=1
 return d[-1],out[::-1]
def greedy(jobs):
 out=[]
 for x in sorted(jobs,key=lambda z:z[1]):
  if not out or x[0]>=out[-1][1]:out.append(x)
 return len(out),[x[2] for x in out]
if __name__=="__main__":
 a=[(0,4,"A"),(1,2,"B"),(2,5,"C"),(4,7,"D"),(5,9,"E"),(7,8,"F")]
 print("DP",dp(a));print("greedy",greedy(a))
