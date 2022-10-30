class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.food_hq = defaultdict(list)
        self.food_cui = defaultdict(str)
        self.food_rate = defaultdict(int)
        
        for food,cui,rate in zip(foods, cuisines, ratings):
            tmp_list = self.food_hq[cui]
            heapq.heappush(tmp_list, (-rate, food))
            self.food_hq[cui] = tmp_list
            self.food_cui[food] = cui
            self.food_rate[food] = rate
            
    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rate[food] = newRating
        cui = self.food_cui[food]
        tmp_list = self.food_hq[cui]
        heapq.heappush(tmp_list, (-newRating, food))
        self.food_hq[cui] = tmp_list
        
    def highestRated(self, cuisine: str) -> str:
        
        while self.food_rate[self.food_hq[cuisine][0][1]] != -self.food_hq[cuisine][0][0]:
            tmp_list = self.food_hq[cuisine]
            heapq.heappop(tmp_list)
            self.food_hq[cuisine] = tmp_list
        res = self.food_hq[cuisine][0][1]
        rate = self.food_hq[cuisine][0][0]
        for i in range(1, len(self.food_hq[cuisine])):
            if self.food_hq[cuisine][i][0] != rate:
                return res
            else:
                res = min(res, self.food_hq[cuisine][i][1])
        return res
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)