def minmax(a):
 if not a:raise ValueError("empty")
 if len(a)==1:return a[0],a[0]
 if len(a)==2:return min(a),max(a)
 m=len(a)//2;x,y=minmax(a[:m]);u,v=minmax(a[m:])
 return min(x,u),max(y,v)
if __name__=="__main__":
 a=[1200.5,99,450.25,9999,18.75,2300,650]
 print("divide/conquer",minmax(a));print("brute force",(min(a),max(a)))
