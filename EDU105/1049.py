import heapq
def lastStoneWeightII(stones) -> int:
    stones = [-ele for ele in stones]
    heapq.heapify(stones)
    print(stones)
    while len(stones)>=2:
        bigger = heapq.heappop(stones)
        smaller = heapq.heappop(stones)
        heapq.heappush(stones,bigger-smaller)

    return -stones[0]

print(lastStoneWeightII([31,26,33,21,40]))
