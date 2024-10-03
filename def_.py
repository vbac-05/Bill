from customer import*


import os



def createbill():
        b=Bill()
        with open("bill.txt",mode='a') as file:
            
            b.inp()
            file.write(b.b_id+'|'+b.b_n+'|')
            for i in range(int(b.b_n)):
               
                file.write(b.product[i].id+'/'+b.product[i].quantity+'/'+
                b.product[i].name+ '/' +b.product[i].cost+'*')
                b.product[i].edit_product_quantity(b.product[i].id,b.product[i].quantity)
            file.write('|'+b.b_time+'|'+b.b_value+'\n')
            print("Thông tin đã được nhập!!")
        f = 0
        try:
            with open("customer.txt", mode="r") as file1, open("temp.txt", mode='w') as file2:
                x_id = input("Nhập mã khách mua hàng: ")
        
                for line in file1:
                    data = line.strip().split('|')
                    if data[0] == x_id:
                        f = 1
                        
                        c = Customer()
                        c.c_id, c.c_name, c.c_age, c.c_phnumber, c.c_address, c.bill_id = data
                        
                        
                        c.bill_id+=(f" {b.b_id}")
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