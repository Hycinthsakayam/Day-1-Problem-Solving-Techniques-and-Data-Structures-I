import random,time
def linear(a,x):
 for r in a:
  if r["id"]==x:return r
def binary(a,x):
 l,h=0,len(a)-1
 while l<=h:
  m=(l+h)//2
  if a[m]["id"]==x:return a[m]
  if a[m]["id"]<x:l=m+1
  else:h=m-1
if __name__=="__main__":
 a=[{"id":i,"name":f"Patient-{i}"} for i in range(20000)]
 targets=[random.Random(7+i).randrange(20000) for i in range(1000)]
 for name,f in [("linear",linear),("binary",binary)]:
  t=time.perf_counter()
  for x in targets:f(a,x)
  print(name,"1000 lookups ms",round((time.perf_counter()-t)*1000,3))
