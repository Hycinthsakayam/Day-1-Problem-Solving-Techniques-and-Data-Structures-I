def insertion(a):
 a=a[:]
 for i in range(1,len(a)):
  x=a[i];j=i-1
  while j>=0 and a[j]["date"]>x["date"]:a[j+1]=a[j];j-=1
  a[j+1]=x
 return a
def merge(a):
 if len(a)<=1:return a[:]
 m=len(a)//2;l=merge(a[:m]);r=merge(a[m:]);o=[];i=j=0
 while i<len(l) and j<len(r):
  if l[i]["date"]<=r[j]["date"]:o.append(l[i]);i+=1
  else:o.append(r[j]);j+=1
 return o+l[i:]+r[j:]
if __name__=="__main__":
 a=[{"id":"T1","date":"09:00"},{"id":"T2","date":"08:30"},{"id":"T3","date":"09:00"}]
 for f in (insertion,merge):print([(x["id"],x["date"]) for x in f(a)])
