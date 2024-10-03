
from def_ import *



def main():
    b = Bill()
    p = Product()
    c = Customer()

    while True:
        print("\n========== MENU ==========")
        print("1. Hóa đơn")
        print("2. Sản phẩm trong kho")
        print("3. Thông tin khách hàng")
        print("4. Thoát")
        ch1 = int(input("Nhập lựa chọn của bạn: "))

        if ch1 == 1:
            while True:
                print("\n========== HÓA ĐƠN ==========")
                print("1. Tạo hóa đơn")
                print("2. Hiển thị tất cả hóa đơn")
                print("3. Sửa thông tin hóa đơn")
                print("4. Xóa hóa đơn")
                print("5. Tìm kiếm hóa đơn")
                print("6. Thoát")
                ch2 = int(input("Nhập lựa chọn của bạn: "))

                if ch2 == 1:
                    createbill()
                elif ch2 == 2:
                    b.readfile()
                elif ch2 == 3:
                    b.modifile()
                elif ch2 == 4:
                    b.deletefile()
                elif ch2 == 5:
                    b.searchfile()
                elif ch2 == 6:
                    print("Đang thoát...")
                    break
                else:
                    print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

        elif ch1 == 2:
            while True:
                print("\n========== SẢN PHẨM ==========")
                print("1. Thêm sản phẩm")
                print("2. Hiển thị tất cả sản phẩm")
                print("3. Xóa sản phẩm")
                print("4. Tìm kiếm sản phẩm theo ID")
                print("5. Sắp xếp sản phẩm theo giá")
                print("6. Thay đổi thông tin sản phẩm")
                print("7. Thoát")
                ch3 = int(input("Nhập lựa chọn của bạn: "))

                if ch3 == 1:
                    p.writefile()
                elif ch3 == 2:
                    p.readfile()
                elif ch3 == 3:
                    p.deleteproduct()
                elif ch3 == 4:
                    p.search_by_id("productinfor.txt")
                elif ch3 == 5:
                    p.sortproduct()
                elif ch3 == 6:
                    p.edit_product()
                elif ch3 == 7:
                    print("Đang thoát...")
                    break
                else:
                    print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

        elif ch1 == 3:
            while True:
                print("\n========== KHÁCH HÀNG ==========")
                print("1. Thêm khách hàng")
                print("2. Hiển thị tất cả khách hàng")
                print("3. Sửa thông tin khách hàng")
                print("4. Xóa khách hàng")
                print("5. Tìm kiếm khách hàng")
                print("6. Thoát")
                ch4 = int(input("Nhập lựa chọn của bạn: "))

                if ch4 == 1:
                    c.writefile()
                elif ch4 == 2:
                    c.readfile()
                elif ch4 == 3:
                    c.modifile()
                elif ch4 == 4:
                    c.deletefile()
                elif ch4 == 5:
                    c.searchfile()
                elif ch4 == 6:
                    print("Đang thoát...")
                    break
                else:
                    print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

        elif ch1 == 4:
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

