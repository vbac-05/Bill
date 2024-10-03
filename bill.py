from product import*

import os
import time
class Bill(Product):
    def __init__(self):
        self.b_id=""     #mã hóa đơn
        self.b_n=""      #số lượng sản phẩm đã mua
        self.product=[]   #các sản phẩm đã mua
        self.b_time=""   #ngày xuất hóa đơn
        self.b_value="0"  #tổng giá trị hóa đơn
    
    def inp(self):
        self.b_id=input("Nhập mã hóa đơn: ")
        self.b_n=input("Nhập số loại sản phẩm đã mua: ")
        print("Các sản phẩm bạn đã mua là:")
        print("--------------------------")
        for i in range(int(self.b_n)):
            self.product.append(Product())
            self.product[i].input()
            self.b_value = str(int(self.b_value) + int(self.product[i].cost) * int(self.product[i].quantity))
        print("--------------------------")
        self.b_time=time.strftime("%H:%M:%S %d/%m/%Y",time.localtime())
    
    def out(self):
        print("Mã hóa đơn:",self.b_id)
        print("Số loại sản phẩm đã mua:",self.b_n)
        print("Thông tin các sản phẩm đã mua là:")
        for i in range(int(self.b_n)):
            self.product[i].output()
        print("Thời gian mua hàng là:",self.b_time)
        print("Tổng giá trị đơn hàng: ",self.b_value)


    

            
    
    def readfile(self):
        try:
            with open("bill.txt",mode='r') as file:
                print("Thông tin hóa đơn: ")
                
                for line in file:
                    data=line.strip().split("|")
              
                    b=Bill()
                    b.b_id, b.b_n, product, b.b_time, b.b_value=data
                     # Tách dữ liệu sản phẩm
                    data_product = product.strip('*').split("*")
                    b.product = []  # Khởi tạo lại danh sách sản phẩm
                    for i in range(int(b.b_n)):
                       p = Product()  # Khởi tạo một đối tượng Product mới
                       p.id, p.quantity, p.name, p.cost = data_product[i].strip().split("/")
                       b.product.append(p)  # Thêm đối tượng Product vào danh sách sản phẩm
                    b.out()
        except FileNotFoundError:
            print("!!file không tồn tại!!")
    def modifile(self):
        f=0
        try:
            with open("bill.txt",mode="r") as file1,open("temp.txt",mode="w") as file2:
                x_id = input("Nhập mã hóa đơn muốn sửa: ")
                
                for line in file1:
                    data=line.strip().split('|')
                    if data[0]==x_id:
                        f=1
                        b=Bill()
                        print("Nhập thông tim mới cho hóa đơn: ")
                        b.inp()
                        file2.write(b.b_id+'|'+b.b_n+'|')
                        for i in range(int(b.b_n)):
                            file2.write(b.product[i].id+'/'+b.product[i].quantity+'/'+
                            b.product[i].name+ '/' +b.product[i].cost+'*')
                        file2.write('|'+b.b_time+'|'+b.b_value+'\n')
                    else:
                        file2.write(line)
            if f==1:
                os.remove("bill.txt")
                os.rename("temp.txt","bill.txt")
                print("Thông tin hóa đơn đã được cập nhật!!")
            else:
                print("!!Thông tin không tồn tại!!")
        except FileNotFoundError:
            print("!!file không tồn tại!!")

    def deletefile(self):
        f=0
        try:
            with open("bill.txt",mode="r") as file1,open("temp.txt",mode="w") as file2:
                x_id=input("Nhập mã hóa đơn muốn xóa: ")
                
                for line in file1:
                    data=line.strip().split('|')
                    if data[0]==x_id:
                        f=1
                    else:
                        file2.write(line)
            if f==1:
                os.remove("bill.txt")
                os.rename("temp.txt","bill.txt")
            else:
                print("!!Thông tin không tồn tại!!")
        except FileNotFoundError:
            print("!!file không tồn tại!!")

    def searchfile(self):
        f=0
        try:
            with open("bill.txt",mode="r") as file:
                x_id=input("Nhập mã hóa đơn muốn tìm: ")
                
                for line in file:
                    data=line.strip().split("|")
                    if data[0]==x_id:
                        b=Bill()
                        b.b_id, b.b_n, product_, b.b_time, b.b_value=data
                        product_data=product_.strip("*").split('*')
                        
                        for i in range(int(b.b_n)):
                            b.product.append(Product())
                            b.product[i].id, b.product[i].quantity, b.product[i].name,b.product[i].cost= product_data[i].strip().split("/")
                            
                        b.out()
                        f=1
            if f==0:
                print("!!Thông tin không tồn tại!!")
        except FileNotFoundError:
            print("!!file không tồn tại!!")