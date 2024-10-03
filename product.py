import os
import time


#class quản lý sản phẩm
class Product:
    def __init__(self):
        self.id = ""
        self.quantity = ""
        self.name = ""
        self.cost = ""

    def input(self):
        self.id = input("Nhập ID sản phẩm: ")
        self.quantity = input("Nhập số lượng sản phẩm: ")
        self.name = input("Nhập tên sản phẩm: ")
        self.cost = input("Nhập giá bán: ")

    def output(self):
        print(f"--- Thông tin sản phẩm ---")
        print(f"ID sản phẩm: {self.id}")
        print(f"Số lượng sản phẩm: {self.quantity}")
        print(f"Tên sản phẩm: {self.name}")
        print(f"Giá bán: {self.cost}")
        print("----------------------------")
    def writefile(self):
        n = int(input("Nhập số sản phẩm muốn thêm: "))
        products = [Product() for _ in range(n)]  #tạo n đối tượng product
        with open("productinfor.txt", "a") as outfile:
            for product in products:
                product.input()
                outfile.write(f"{product.id}|{product.quantity}|{product.name}|{product.cost}\n")
                print("Sản phẩm đã được nhập.")
    def readfile(self):
     try:
        with open("productinfor.txt", "r") as infile:
            for line in infile:
                data=list(line.strip().split("|"))
                p=Product()
                p.id,p.quantity,p.name,p.cost=data
                p.output()
     except FileNotFoundError:
        print("Không thể mở file để đọc!")
    def search_by_id(self, filename):
        # Tìm kiếm sản phẩm theo id trong file
        target_id = input("Nhập ID sản phẩm cần tìm: ")
        found = False
        with open(filename, "r") as file:
            for line in file:
                data = list(line.strip().split("|"))
                if target_id ==data[0]:
         
                    p=Product()
                    p.id,p.quantity,p.name,p.cost=data
                    print("Sản phẩm bạn cần tìm là:")
                    p.output()
                    found=True
                    break
            
        if not found:
            print("Sản phẩm không được tìm thấy.")
    def deleteproduct(self):
        # Xóa sản phẩm theo ID
        target_id = input("Nhập ID sản phẩm cần xóa: ")
        found = False

        try:
            with open("productinfor.txt", "r") as infile, open("temp.txt", "w") as outfile:
                for line in infile:
                 data = list(line.strip().split("|"))
                 if target_id == data[0]:
                    found = True
                    
                    p = Product()
                    p.id, p.quantity, p.name, p.cost = data
                    print("Sản phẩm được xóa là:")
                    p.output()
                 else:
                    outfile.write(line)  # Ghi lại dòng không chứa ID cần xóa

            # Thay thế file cũ bằng file tạm thời nếu sản phẩm được tìm thấy
            if found:
                os.remove("productinfor.txt")
                os.rename("temp.txt", "productinfor.txt")
            else:
                os.remove("temp.txt")
                print("Sản phẩm không được tìm thấy.")
        except FileNotFoundError:
            print("Không thể mở file để đọc!")
    def sortproduct(self):
        # Sắp xếp sản phẩm theo giá
        products = []
        try:
            with open("productinfor.txt", "r") as infile:
                for line in infile:
                    id, quantity,name, cost = line.strip().split("|")
                    products.append((id,quantity,name, float(cost)))  # Lưu thông tin sản phẩm

            # Sắp xếp theo giá tăng dần
            products.sort(key=lambda x: x[3])

            # Ghi lại vào file
            with open("productinfor.txt", "w") as outfile:
                for product in products:
                    outfile.write(f"{product[0]} {product[1]} {product[2]} {str(product[3])}\n")

            print("Đã sắp xếp kho hàng theo giá tăng dần.")
        except FileNotFoundError:
            print("Không thể mở file để đọc!")
    def edit_product_quantity(self,target_id,n):
        
        found = False
        try:
            with open("productinfor.txt", "r") as infile, open("temp.txt", "w") as outfile:
             for line in infile:
                data = list(line.strip().split("|"))
                if target_id == data[0]:
                    found = True
                    
                    p = Product()
                    p.id, p.quantity, p.name, p.cost = data
         
                    #giảm số lượng sản phẩm còn lại trong kho
                    p.quantity=int(p.quantity)-int(n)
                    # Ghi lại thông tin mới vào file tạm
                    outfile.write(f"{p.id}|{str(p.quantity)}|{p.name}|{p.cost}\n")
           
                else:
                    outfile.write(line)  # Ghi lại dòng không chứa ID cần sửa

           #  Thay thế file cũ bằng file tạm thời nếu sản phẩm được tìm thấy
            if found:
              os.remove("productinfor.txt")
              os.rename("temp.txt", "productinfor.txt")
        except FileNotFoundError:
            print("Không thể mở file để đọc!")
    def edit_product(self):
    # Sửa thông tin sản phẩm theo ID
        target_id = input("Nhập ID sản phẩm cần sửa: ")
        found = False
        try:
            with open("productinfor.txt", "r") as infile, open("temp.txt", "w") as outfile:
             for line in infile:
                data = list(line.strip().split("|"))
                if target_id == data[0]:
                    found = True
                    
                    p = Product()
                    p.id, p.quantity, p.name, p.cost = data
                    
        
                    print("Thông tin sản phẩm bạn muốn sửa là:")
                    p.output()
                    
                    # Nhập thông tin mới
                    print("Nhập thông tin mới cho sản phẩm:")
                    p.input()  # Sử dụng phương thức input để nhập thông tin mới
                    
                    # Ghi lại thông tin mới vào file tạm
                    outfile.write(f"{p.id} {p.quantity} {p.name} {p.cost}\n")
                    print("Thông tin sản phẩm đã được cập nhật.")
                else:
                    outfile.write(line)  # Ghi lại dòng không chứa ID cần sửa

           #  Thay thế file cũ bằng file tạm thời nếu sản phẩm được tìm thấy
            if found:
              os.remove("productinfor.txt")
              os.rename("temp.txt", "productinfor.txt")
        except FileNotFoundError:
            print("Không thể mở file để đọc!")