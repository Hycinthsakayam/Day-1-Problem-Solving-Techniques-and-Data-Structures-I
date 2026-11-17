import random
def bubble(a):
 a=a[:];tr=[]
 for i in range(len(a)-1):
  changed=False
  for j in range(len(a)-1-i):
   if a[j]<a[j+1]:a[j],a[j+1]=a[j+1],a[j];changed=True
  if i<3:tr.append(a[:])
  if not changed:break
 return a,tr
def merge(a):
 if len(a)<=1:return a[:]
 m=len(a)//2;l=merge(a[:m]);r=merge(a[m:]);o=[];i=j=0
 while i<len(l) and j<len(r):
  if l[i]>=r[j]:o.append(l[i]);i+=1
  else:o.append(r[j]);j+=1
 return o+l[i:]+r[j:]
if __name__=="__main__":
 a=[120,450,80,300,200,510,150];b,t=bubble(a)
 print("input",a)
 for i,p in enumerate(t,1):print("pass",i,p)
 print("bubble",b,"merge",merge(a))
 x=random.Random(42).sample(range(100000),10000)
 print("merge matches built-in",merge(x)==sorted(x,reverse=True))
