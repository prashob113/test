cherry = 20
mango = 40
orange = 50
Wrap_Cherry =0
Wrap_mango =0
Wrap_orange =0
def gift_wrap():
    gift_wrap = input("Do you want this product wrapped as a gift (yes/no)")
    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']
    if gift_wrap.lower() in yes_choices:
        return 1
    elif gift_wrap.lower() in no_choices:
        return 0
cherry_amount = int(input("How much    cherry do you want ?"))
if cherry_amount > 0:
    wrap_cherry = gift_wrap()
mango_amount = int(input("How much    mango do you want ?"))
if mango_amount > 0:
    wrap_mango = gift_wrap()
orange_amount = int(input("How much orange do you want ?"))
if orange_amount > 0:
    wrap_orange = gift_wrap()
if cherry_amount > 0:
    print("You have  orderd",cherry_amount,"cherry for :$", cherry*cherry_amount)
if mango_amount > 0:
    print("You have orderd",mango_amount,"mango for :$", mango*mango_amount)
if orange_amount > 0:
    print("You have orderd",orange_amount,"orange for : $", orange*orange_amount)
total_amount = cherry_amount + mango_amount + orange_amount
subtotal = cherry*cherry_amount+mango*mango_amount+orange*orange_amount
print("subtotal for this purchase is : $",subtotal)
flat_10_discount = 0
bulk_5_discount = 0
bulk_10_discount = 0
tiered_50_discount = 0
discount_1 = 0
discount_2 = 0
discount_3 = 0
discount_4 = 0
if subtotal > 200:
    discount_1 = 10
    flat_10_discount = subtotal - discount_1
if cherry_amount >10 or orange_amount > 10 or mango_amount > 10:
    if cherry_amount > 10:
        discount_2 = (cherry_amount*cherry*5)/100
    elif mango_amount > 10:
        discount_2 = (mango_amount*mango*5)/100
    elif orange_amount > 10:
        discount_2 = (orange_amount*orange*5)/100
bulk_5_discount = subtotal - discount_2
if cherry_amount + mango_amount + orange_amount > 20:
    discount_3 = (subtotal * 10) / 100
    bulk_10_discount = subtotal - discount_3

if (cherry_amount + mango_amount + orange_amount > 30) and ( cherry_amount > 15 or mango_amount > 15 or orange > 15 ):
    if cherry_amount > 15 :
        discount_4 = ( cherry_amount * cherry * 50 ) / 100
    elif mango_amount > 15 :
        discount_4 = ( mango_amount * mango * 50 ) / 100
    elif orange_amount > 15 :
        discount_4 = ( orange_amount * orange * 50 ) / 100
    tiered_50_discount = subtotal - discount_4
final_discount = [ discount_1 , discount_2 , discount_3 , discount_4 ]
final_discount.sort()
discount_flag=0
if final_discount[3] == discount_1:
    discount_flag=1
    print("flat_10_discount is applied. The discount amount is : $", discount_1)
elif final_discount[3] == discount_2:
    discount_flag=2
    print("bulk_5_discount is applied. The discount amount is : $", discount_2)
elif final_discount[3] == discount_3:
    discount_flag=3
    print("bulk_10_discount is applied. The discount amount is : $", discount_3)
elif final_discount[3] == discount_4:
    discount_flag=4
    print("50_discount is applied. The discount amount is : $", discount_4)
if discount_flag == 1:
    total = flat_10_discount 
elif discount_flag == 2:
    total = bulk_5_discount 
elif discount_flag == 3:
    total = bulk_10_discount 
elif discount_flag == 4:
    total = tiered_50_discount 
else: 
    total = subtotal
total_gift_wrap_fee = 0
if wrap_cherry == 1:
    total=total + cherry_amount
    total_gift_wrap_fee = total_gift_wrap_fee + cherry_amount
    print("Gift wrap fee for cherry : $", cherry_amount)
if wrap_mango == 1:
    total=total + mango_amount
    total_gift_wrap_fee = total_gift_wrap_fee + mango_amount
    print("Gift wrap fee for mango : $", mango_amount)
if wrap_orange == 1:
    total=total + orange_amount
    total_gift_wrap_fee = total_gift_wrap_fee + orange_amount
    print("Gift wrap fee for orange : $", orange_amount)
if wrap_orange == 1 or wrap_mango == 1 or wrap_cherry == 1:
    print("total gift wrap fee is : $", total_gift_wrap_fee)
if total_amount%10 == 0:
    package_quantity = int( ( total_amount / 10 ))
    print("The shipping fee for your purchase : $", package_quantity * 5) 
else:
    package_quantity = int( ( total_amount / 10 ) +1)
    print("The shipping fee for your purchase is : $", package_quantity * 5)
shipping_fee = package_quantity * 5
total = total + shipping_fee
print("Your total amount for this purchase is :", total)