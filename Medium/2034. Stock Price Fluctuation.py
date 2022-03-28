import heapq
class StockPrice:

    def __init__(self):
        from collections import defaultdict
        self.max_hq = []
        self.min_hq = []
        
        self.dic = {}
        self.cur_time = 0
        
    def update(self, timestamp: int, price: int) -> None:
        self.dic[timestamp] = price
        heapq.heappush(self.max_hq, (-price, timestamp))
        heapq.heappush(self.min_hq, (price, timestamp))
        
        if timestamp >= self.cur_time:
            self.cur_time = timestamp
    
    def current(self) -> int:
        return self.dic[self.cur_time]

    def maximum(self) -> int:

        price, timestamp = heapq.heappop(self.max_hq)
        while self.dic[timestamp] != -price:
            price, timestamp = heapq.heappop(self.max_hq)
        heapq.heappush(self.max_hq, (price, timestamp))
        return -price

    def minimum(self) -> int:
        price, timestamp = heapq.heappop(self.min_hq)
        
        while self.dic[timestamp] != price:
            price, timestamp = heapq.heappop(self.min_hq)
        heapq.heappush(self.min_hq, (price, timestamp))
        
        return price
        
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

#Runtime: 856 ms, faster than 89.05% of Python3 online submissions for Stock Price Fluctuation .
#Memory Usage: 61.6 MB, less than 20.65% of Python3 online submissions for Stock Price Fluctuation .
#Fu-Ti, Hsu 
#shifty049@gmail.com
