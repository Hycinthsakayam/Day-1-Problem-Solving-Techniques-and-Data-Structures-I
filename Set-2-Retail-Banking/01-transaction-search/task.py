def linear(a,x):
 c=0
 for v in a:
  c+=1
  if v==x:return c
 return c
def binary(a,x):
 l,h=0,len(a)-1;c=0
 while l<=h:
  m=(l+h)//2;c+=1
  if a[m]==x:return c
  if a[m]<x:l=m+1
  else:h=m-1
 return c
if __name__=="__main__":
 a=list(range(100000))
 for name,x in [("best",0),("middle",50000),("last",99999),("absent",100001)]:
  print(name,"linear",linear(a,x),"binary",binary(a,x))
