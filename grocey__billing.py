item1=int(input("Item 1 price: $"))#taking price of item 1 
item2=int(input("Item 2 price: $"))#taking price of item 2 
item3=int(input("Item 3 price: $"))#taking price of item 3 
total=item1+item2+item3 #calculating total 
if total>50: #setting conditions for a discount 
    discount= total/10 
    final_total= total-discount 
else:  
    discount=0 
    final_total=total 
print(f"Total= ${total}\nDiscount= ${discount}\nFinal Amount= 
${final_total}\n")