class Store: 
    def __init__(self,store_id,name,revenue_day,open_days,bonus):
        self.id = store_id 
        self.name = name 
        self.revenue_day = revenue_day
        self.open_days = open_days
        self.bonus = bonus
        self.net_revenue = 0.0 
        self.performance_type = ""
        
        self.calculate_net_revenue()
        self.classify_performance()
        
        def calculate_net_revenue(self):
            self.net_revenue = (self.revenue_day * self.open_days) + self.bonus 
            
        def classify_performance(self): 
            if self.net_revenue < 9000000: 
                self.performance_type = "Thấp"
            elif 9000000 <= self.net_revenue < 15000000: 
                self.performance_type = "Trung bình"
            elif 15000000 <= self.net_revenue < 30000000: 
                self.performance_type = "Khá"
            else: 
                self.performance_type = "Cao" 
                
                
        