from manager import StoreManager 

def main(): 
    manager = StoreManager()
    while True: 
        print("\n=================== MENU ===================")
        print("1.Hiển thị danh sách cửa hàng")
        print("2.Thêm cửa hàng mới")
        print("3.Cập nhật thông tin cửa hàng")
        print("4.Xóa cửa hàng")
        print("5.Tìm kiếm cửa hàng")
        print("6.Thống kê hiệu năng")
        print("7.Thoát chương trình") 
        print("==============================================") 
        
        choice = input("Nhập lựa chọn của bạn (1-7): ").strip() 
        
        if not choice: 
            print("Dữ liệu nhập vào không được không trống!!")
            continue 
        
        match choice:
            case "1":
                manager.show_data() 
            case "7": 
                break  
            case _: 
                print("Lựa chọn cửa bạn không hợp lệ , Vui long nhập lại từ 1 - 7") 
                
                
if __name__ == "__main__":
    main() 