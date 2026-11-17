def find(a):
 seen=set();out=[]
 for r in a:
  k=(r["patient_id"],r["slot"])
  if k in seen:out.append(k)
  else:seen.add(k)
 return out
if __name__=="__main__":
 a=[{"patient_id":"P10","slot":"10:00"},{"patient_id":"P11","slot":"10:00"},{"patient_id":"P10","slot":"10:00"},{"patient_id":"P10","slot":"10:30"}]
 print("double bookings",find(a))
