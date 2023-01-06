#Cashier_Task_14

print('=== Parfume Store Nota ===')

item_name= input('Input Item Name   : ')
price= float(input('Input Price Item  : '))
quantity= float(input('Input quantity of the  Item  : '))
total_money= float(input('Input total money you pay  : '))
re_money= total_money - quantity * price

#nota coy
text=f'''
============================
     Nota of the shop:3
============================
- Your Item Name        : {item_name}
- Your Item Price       : {price}
- Your Item Quantity    : {quantity}
- Your Total of Money   : {total_money}
- Your Total of Change  : IDR{re_money}
============================
'''
#open and make new file txt

file= open('nota.txt','w')
#writing ito file
file.write(text)