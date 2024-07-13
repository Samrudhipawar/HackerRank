def flatland(n, m, space_stations):
    space_stations.sort()
    max_dist = 0
    
    # Distance to the nearest space station for the first city to the first space station
    max_dist = space_stations[0]
    
    # Check the distances between consecutive space stations
    for i in range(1, m):
        dist = (space_stations[i] - space_stations[i - 1]) // 2
        if dist > max_dist:
            max_dist = dist
    
    # Distance to the nearest space station for the last city to the last space station
    dist = n - 1 - space_stations[-1]
    if dist > max_dist:
        max_dist = dist
    
    print(max_dist)

n, m = map(int, input().split())
space_stations = list(map(int, input().split()))
flatland(n, m, space_stations)
