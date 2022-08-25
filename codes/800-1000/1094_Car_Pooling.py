class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # greedy problem
        # treat "from" as taking positive passenger, "to" as taking negative passenger
        # during the trip, if the number of capacity is larger than required, return False
        
        trip_list = []
        for i in range(len(trips)):
            trip = trips[i]
            trip_list.append([trip[1], trip[0]])
            trip_list.append([trip[2], -trip[0]])
        
        trip_list = sorted(trip_list)
        capa = 0
        for i in range(len(trip_list)):
            capa += trip_list[i][1]
            if capa > capacity:
                return False
        return True