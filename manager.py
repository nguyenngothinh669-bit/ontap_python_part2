from store import Store 

class StoreManager: 
    def __init__(self): 
        self.stores = []
        self._load_sample_data() 
        
    def _load_sample_data(self): 
        self.stores.append(Store("CH01","Cửa hàng quận 1",1000000,31,200000))
        self.stores.append(Store("CH02","Cửa hàng quận 2",200000000,11,200000))
        self.stores.append(Store("CH03","Cửa hàng quận 3",5000000000,3,200000)) 
        
    def _input_string(self,prompt,check_emty =True): 
        while True: 
            val = input(prompt)
            if not val and check_emty: 
                print("Lỗi: Bắt buộc phải nhập không được dể trống!")
            else: 
                return val 
        
    def _input_positive_number(self,prompt,is_float = True): 
        
    
        
    def show_data(self): 
        print("\n=== DANH SÁCH CỬA HÀNG ===")
        if not self.stores: 
            print("Danh sách hiện đang trống!")
            return 
        
        header = f"| {'Mã CH':<10} | {'Tên cửa hàng':<25} | {'DT trong ngày':<15} | {'Ngày mở':<10} | {'Thưởng':<15} | {'Tổng doanh thu':<20} | {'Hiệu năng':<15} |" 
        print("-"*len(header))
        print(header) 
        print("-"*len(header)) 
        
        for s in self.stores: 
            print(f"| {s.id:<10} | {s.name:<25} | {s.revenue_day:<15} | {s.open_days:<10} | {s.bonus:<15} | {s.net_revenue:<20} | {s.performance_type:<15} |") 
        print("-"*len(header)) 
        
        