def greedy(n,coins):
 out=[]
 for c in sorted(coins,reverse=True):
  q,n=divmod(n,c);out += [c]*q
 return out if n==0 else None
def dp(n,coins):
 d=[n+1]*(n+1);pick=[0]*(n+1);d[0]=0
 for v in range(1,n+1):
  for c in coins:
   if c<=v and d[v-c]+1<d[v]:d[v]=d[v-c]+1;pick[v]=c
 if d[n]>n:return None
 out=[]
 while n:out.append(pick[n]);n-=pick[n]
 return out
if __name__=="__main__":
 print("greedy 63",greedy(63,[25,10,5,1]))
 print("greedy 6",greedy(6,[4,3,1]))
 print("DP 6",dp(6,[4,3,1]))
