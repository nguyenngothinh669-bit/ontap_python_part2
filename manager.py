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
            val = input(prompt).strip()
            if not val and check_emty: 
                print("Lỗi: Bắt buộc phải nhập không được dể trống!")
            else: 
                return val 
        
    def _input_positive_number(self,prompt,is_float= True): 
        while True: 
            try: 
                val_str = input(prompt).strip()
                if not val_str: 
                    print("Lỗi: Bắt buộc phải nhập không được dể trống!")
                    continue 
                
                val = float(val_str) if is_float else int(val_str) 
                if val < 0 : 
                    print("Lỗi: Dữ liệu nhập vào khôgn được âm")
                else: 
                    return val 
                  
            except ValueError: 
                print("Lỗi: Vui long nhập đúng định dạng số!!")
    def _input_open_days(self):
        while True: 
            days = self._input_positive_number("Nhập vào ngày (0-31): ",is_float= False)
        
            if 0 <= days <= 31: 
                return days 
            print("Lỗi: Số phải nằm trong ngày từ 0 đến 31")
        
    def _find_store_index_by_id(self,store_id): 
        for i , store in enumerate(self.stores): 
            if store.id == store_id.upper(): 
                return i 
        return -1 
    
    def add_store(self): 
        print("\n=== THÊM MỚI CỬA HÀNG ===")
        store_id = self._input_string("Nhập mã Cửa hàng: ")
        if self._find_store_index_by_id(store_id) != -1: 
            print("Mã cửa hàng này đẫ tồn tại trong hệ thống")
            return 
        
        name = self._input_string("Nhập tên cửa hàng: ")
        revenue_day = self._input_positive_number("Nhập doanh thu trong 1 ngày: ")
        open_days = self._input_open_days() 
        bonus = self._input_positive_number("Nhập doanh thu thưởng: ")
        
        new_store = Store(store_id.upper(),name.capitalize(),revenue_day,open_days,bonus) 
        self.stores.append(new_store)
        print("\n Thêm cửa hàng thành công")
            
            
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
            print(f"| {s.id:<10} | {s.name:<25} | {s.revenue_day:<15,.0f} | {s.open_days:<10,.0f} | {s.bonus:<15,.0f} | {s.net_revenue:<20,.0f} | {s.performance_type:<15} |") 
        print("-"*len(header)) 
        
    def update_store(self): 
        print("\n=== SỬA THÔNG TIN CỬA HÀNG ===")
        if not self.stores: 
            print("Danh sách hiện đang trống khồn thể sửa!")
            return 
        
        store_id = self._input_string("Nhập mã Cửa hàng muốn cập nhật: ")
        index = self._find_store_index_by_id(store_id) 
        
        if index == -1 : 
            print("Mã này không tồn tại trong cửa hàng")
            return 
        print(f"Đang cập nhật cho cửa hàng {self.stores[index].name}")
        self.stores[index].revenue_day = self._input_positive_number("Nhập doanh thu mới trong 1 ngày: ")
        self.stores[index].open_days = self._input_open_days() 
        self.stores[index].bonus = self._input_positive_number("Nhập tiền thưởng mới: ") 
        
        self.stores[index].calculate_net_revenue() 
        self.stores[index].classify_performance() 
        print("\n Cập nhật thành công thông tin cửa hàng")  
        
    def delete_store(self): 
        if not self.stores: 
            print("Danh sách hiện đang trống không thể xóa!")
            return 
        
        store_id = self._input_string("Nhập mã cửa hàng muốn xóa: ") 
        index = self._find_store_index_by_id(store_id) 
        if index == -1 : 
            print("Mã này không tồn tại trong cửa hàng")
            return  
        
        confirm = input("Bạn có chắc chắn muốn xóa sản phẩm này ra khỏi danh sách khôgn (Y/N): ").strip().upper()
        if confirm == "Y": 
            del self.stores[index]
            print("bạn đã xóa thành công")
        else: 
            print("Hủy thao tác") 
        
    def search_store(self): 
        print("\n=== TÌM KIẾM CỬA HÀNG ===")
        if not self.stores: 
            print("Danh sách hiện đang trống không thể tìm kiếm!")
            return 
        
        keyword = self._input_string("Nhập từ khóa muốn tìm kiếm theo tên cửa hàng: ").lower()
        found_stores = [s for s in self.stores if keyword in s.name.lower()] 
        
        if not found_stores: 
            print("Không tìm thấy cửa hàng nào trong danh sách")
        else: 
            print(f"\nTìm thấy {len(found_stores)} kết quả: ") 
            header = f"| {'Mã CH':<10} | {'Tên cửa hàng':<25} | {'DT trong ngày':<15} | {'Ngày mở':<10} | {'Thưởng':<15} | {'Tổng doanh thu':<20} | {'Hiệu năng':<15} |" 
            print("-"*len(header))
            print(header) 
            print("-"*len(header)) 
            
            for s in found_stores: 
                print(f"| {s.id:<10} | {s.name:<25} | {s.revenue_day:<15,.0f} | {s.open_days:<10,.0f} | {s.bonus:<15,.0f} | {s.net_revenue:<20,.0f} | {s.performance_type:<15} |") 
            print("-"*len(header)) 
            
    def statistic(self): 
        print("\n=== THỐNG KÊ HIỆU NĂNG ===")
        
        if not self.stores: 
            print("Danh sách hiện đang trống không thể thống kê!")
            return 
        
        stats = {"Thấp": 0 , "Trung bình": 0 ,"Khá": 0, "Cao": 0 } 
        for store in self.stores: 
            
            if not store.performance_type: 
                store.classify_performance() 
                
            p_type = store.performance_type 
            if p_type not in stats: 
                stats[p_type] = 0 
            stats[p_type] += 1 
            
        print(f"| {'Hiệu năng': <10} | {'Số lượng':<10} |")
        print("-"*25)
        for p_type , count in stats.items(): 
            print(f"| {p_type:<10} | {count:<10} |")
        print("-"*25)
        