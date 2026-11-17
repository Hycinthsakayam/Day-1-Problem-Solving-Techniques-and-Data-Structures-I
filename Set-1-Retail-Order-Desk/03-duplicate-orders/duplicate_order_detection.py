from collections import defaultdict
def find(rows):
 d=defaultdict(list);out=[]
 for r in rows:
  k=(r["customerId"],round(float(r["amount"]),2),r["createdAt"][:16])
  for old in d[k]:out.append((old["orderId"],r["orderId"]))
  d[k].append(r)
 return out
if __name__=="__main__":
 a=[{"orderId":"O1","customerId":"C7","amount":250,"createdAt":"2026-10-14T10:31:05"},{"orderId":"O2","customerId":"C7","amount":250,"createdAt":"2026-10-14T10:31:48"},{"orderId":"O3","customerId":"C7","amount":250,"createdAt":"2026-10-14T10:32:01"}]
 print("duplicate pairs",find(a))
