def key(x):return (x["urgency"],x["arrival"])
def selection(a):
 a=a[:];sw=0
 for i in range(len(a)-1):
  m=min(range(i,len(a)),key=lambda j:key(a[j]))
  if m!=i:a[i],a[m]=a[m],a[i];sw+=1
 return a,sw
def quick(a):
 a=a[:];sw=0
 def part(l,h):
  nonlocal sw
  p=key(a[h]);i=l-1
  for j in range(l,h):
   if key(a[j])<=p:
    i+=1
    if i!=j:a[i],a[j]=a[j],a[i];sw+=1
  if i+1!=h:a[i+1],a[h]=a[h],a[i+1];sw+=1
  return i+1
 def sort(l,h):
  if l<h:
   p=part(l,h);sort(l,p-1);sort(p+1,h)
 sort(0,len(a)-1);return a,sw
if __name__=="__main__":
 a=[{"patient":"A","urgency":2,"arrival":3},{"patient":"B","urgency":1,"arrival":5},{"patient":"C","urgency":1,"arrival":2},{"patient":"D","urgency":3,"arrival":1}]
 for n,f in [("selection",selection),("quick",quick)]:
  x,s=f(a);print(n,[(z["patient"],key(z)) for z in x],"swaps",s)
