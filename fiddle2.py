def minRefuelStops(target, startFuel, stations):
    dp = [startFuel] + [0] * len(stations)
    for i, (location, capacity) in enumerate(stations):
        for t in range(i, -1, -1):
            if dp[t] >= location:#if we can reach the location
                #max capacity/distance is eather if we refill or  refill next
                dp[t+1] = max(dp[t+1], dp[t] + capacity)

    for i, d in enumerate(dp):
        if d >= target: return i
    return -1

print(minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]] ))