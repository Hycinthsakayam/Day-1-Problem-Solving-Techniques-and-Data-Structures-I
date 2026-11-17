"""Task 5 - minimum notes/coins for a refund: greedy, a case where greedy fails, and dynamic programming."""


def greedy_change(amount, denominations):
    result = []
    for d in sorted(denominations, reverse=True):
        while amount >= d:
            amount -= d
            result.append(d)
    return result if amount == 0 else None


def dp_change(amount, denominations):
    INF = float("inf")
    best = [0] + [INF] * amount          # best[x] = fewest coins for x
    last = [0] * (amount + 1)
    for x in range(1, amount + 1):
        for d in denominations:
            if d <= x and best[x - d] + 1 < best[x]:
                best[x] = best[x - d] + 1
                last[x] = d
    if best[amount] == INF:
        return None
    coins = []
    while amount:
        coins.append(last[amount])
        amount -= last[amount]
    return coins


INR = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
print("Indian notes/coins:", INR)
for refund in [2749, 3888, 576]:
    g = greedy_change(refund, INR)
    d = dp_change(refund, INR)
    print(f"  refund Rs.{refund}: greedy {len(g)} pieces {g}")
    print(f"  {'':12} dp     {len(d)} pieces")

print("\nA set where greedy fails: [1, 7, 10]")
odd = [1, 7, 10]
for refund in [14, 15, 21]:
    g = greedy_change(refund, odd)
    d = dp_change(refund, odd)
    flag = "  <- greedy is not optimal" if len(g) > len(d) else ""
    print(f"  refund {refund}: greedy {len(g)} {g}   dp {len(d)} {sorted(d, reverse=True)}{flag}")

print("\nGreedy: O(k + number of coins) time, O(1) extra space - works for 'canonical' sets like INR.")
print("DP    : O(amount x k) time, O(amount) space - always gives the minimum.")
