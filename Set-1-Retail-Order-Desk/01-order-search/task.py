import csv,time
from pathlib import Path
def linear(a,x):
 for r in a:
  if int(r["orderId"])==x:return r
def binary(a,x):
 lo,hi=0,len(a)-1
 while lo<=hi:
  m=(lo+hi)//2;v=int(a[m]["orderId"])
  if v==x:return a[m]
  if v<x:lo=m+1
  else:hi=m-1
if __name__=="__main__":
 p=Path("orders.csv")
 if p.exists():
  with p.open(newline="",encoding="utf-8") as f:a=list(csv.DictReader(f))
 else:a=[{"orderId":i,"customerId":i%7000,"amount":(i*37)%5000+100,"createdAt":f"2026-10-{i%28+1:02d}T10:{i%60:02d}:00"} for i in range(50000)]
 a.sort(key=lambda r:int(r["orderId"]));x=int(a[-1]["orderId"])
 for fn in (linear,binary):
  t=time.perf_counter();v=fn(a,x);print(fn.__name__,v is not None,"ms",round((time.perf_counter()-t)*1000,3))
 print("records",len(a),"binary search requires sorted IDs")
