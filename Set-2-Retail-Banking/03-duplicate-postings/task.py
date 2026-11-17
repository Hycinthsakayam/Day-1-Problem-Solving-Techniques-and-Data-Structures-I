from collections import defaultdict
from datetime import datetime
def find(rows):
 d=defaultdict(list);out=[]
 for r in rows:
  k=(r["account"],float(r["amount"]),r["merchant"]);t=datetime.fromisoformat(r["time"])
  for old,ot in d[k]:
   if abs((t-ot).total_seconds())<=60:out.append((old["id"],r["id"]))
  d[k].append((r,t))
 return out
if __name__=="__main__":
 a=[{"id":"P1","account":"A1","amount":499,"merchant":"Cafe","time":"2026-10-14T10:00:00"},{"id":"P2","account":"A1","amount":499,"merchant":"Cafe","time":"2026-10-14T10:00:45"},{"id":"P3","account":"A1","amount":499,"merchant":"Cafe","time":"2026-10-14T10:02:00"}]
 print("duplicate pairs",find(a))
