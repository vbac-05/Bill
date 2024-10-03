import os
import time
from bill import*



#class quản lý khách hàng
class Customer:
    def __init__(self):
        self.c_id = ""
        self.c_name = ""
        self.c_age = ""
        self.c_phnumber = ""
        self.c_address = ""
        self.bill_id = ""

    def inp(self):
        self.c_id = input("Nhập mã số khách hàng: ")
        self.c_name = input("Nhập tên khách hàng: ")
        self.c_age = input("Nhập tuổi khách hàng: ")
        self.c_phnumber = input("Nhập số điện thoại khách hàng: ")
        self.c_address = input("Nhập địa chỉ khách hàng: ")
        self.bill_id = input("Nhập mã hóa đơn khách hàng đã mua: ")

    def out(self):
        print("---------- Thông tin khách hàng -----------")
        print("Mã khách hàng:", self.c_id)
        print("Tên:", self.c_name)
        print("Tuổi:", self.c_age)
        print("Số điện thoại:", self.c_phnumber)
        print("Địa chỉ:", self.c_address)
        print("--- Hóa đơn khách hàng đã mua ---")
        a=self.bill_id.split()
        f=0
        for i in a:
            with open("bill.txt",mode="r") as file:
                
                for line in file:
                    data=line.strip().split("|")
                    if data[0]==i:
                        b=Bill()
                        b.b_id, b.b_n, product_, b.b_time, b.b_value=data
                        product_data=product_.strip("*").split('*')
                        
                        for i in range(int(b.b_n)):
                            b.product.append(Product())
                            b.product[i].id, b.product[i].quantity, b.product[i].name,b.product[i].cost= product_data[i].strip().split("/")
                        
                        b.out()
                        print("*****************************")
                        f=1
        if f==0:
            print("!!Khách chưa mua hàng")
        print("----------------------------")

    def writefile(self):
        with open("customer.txt", mode='a') as file:
            n = int(input("Số khách hàng cần nhập vào file: "))
            for i in range(n):
                c = Customer()
                c.inp()
                file.write(c.c_id + '|' + c.c_name + '|' + c.c_age + '|' +
                           c.c_phnumber + '|' + c.c_address + '|' + c.bill_id + "\n")
                print("Thông tin đã được nhập.")

    def readfile(self):
        try:
            with open("customer.txt", mode="r") as file:
                print("Thông tin khách hàng: ")
                for line in file:
                    data = line.strip().split("|")
                    c = Customer()
                    c.c_id, c.c_name, c.c_age, c.c_phnumber, c.c_address, c.bill_id = data
                    c.out()
        except FileNotFoundError:
            print("Không thể mở file để đọc!")

    
    def modifile(self):
        f = 0
        try:
            with open("customer.txt", mode="r") as file1, open("temp.txt", mode='w') as file2:
                x_id = input("Nhập mã khách hàng muốn sửa: ")
        
                for line in file1:
                    data = line.strip().split('|')
                    if data[0] == x_id:
                        f = 1
                        print("Thông tin khách hàng bạn muốn sửa: ")
                        c = Customer()
                        c.c_id, c.c_name, c.c_age, c.c_phnumber, c.c_address, c.bill_id = data
                        c.out()
                        
                        print("Nhập thông tin mới cho khách hàng: ")
                        c.inp()
                        file2.write(c.c_id + '|' + c.c_name + '|' + c.c_age + '|' +
                                    c.c_phnumber + '|' + c.c_address + '|' + c.bill_id + "\n")
                        print("Thông tin khách hàng đã được cập nhật.")
                    else:
                        file2.write(line)
            if f == 1:
                os.remove("customer.txt")
                os.rename("temp.txt", "customer.txt")
            else:
                print("!!Thông tin không tồn tại!!")
        except FileNotFoundError:
            print("Không thể mở file để đọc!")


    def deletefile(self):
        f = 0
        try:
            with open("customer.txt", mode="r") as file1, open("temp.txt", mode='w') as file2:
                x_id = input("Nhập mã khách hàng muốn xóa: ")
                
                for line in file1:
                    data = line.strip().split('|')
                    if data[0] == x_id:
                        f=1
                        c = Customer()
                        c.c_id, c.c_name, c.c_age, c.c_phnumber, c.c_address, c.bill_id = data
                        print("Thông tin khách hàng muốn xóa là: ")
                        c.out()
                        print("Đã xóa thông tin khách hàng có ID :",c.c_id)
                    else:
                        file2.write(line)
            if f == 1:
                os.remove("customer.txt")
                os.rename("temp.txt", "customer.txt")
            else:
                print("!!Thông tin không tồn tại!!")
        except FileNotFoundError:
            print("Không thể mở file để đọc!")


    def searchfile(self):
        f = 0
        try:
            with open("customer.txt", mode="r") as file1:
                x_id = input("Nhập mã khách hàng muốn tìm: ")
            
                for line in file1:
                    data = line.strip().split('|')
                    if data[0] == x_id:
                        c = Customer()
                        c.c_id, c.c_name, c.c_age, c.c_phnumber, c.c_address, c.bill_id = data
                        c.out()
                        f = 1
            if f == 0:
                print("!!Thông tin không tồn tại!!")
        except FileNotFoundError:
            print("Không thể mở file để đọc!")