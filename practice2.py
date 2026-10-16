
order_amount=int(input("enter order_amount:$"))
if order_amount>=2000:
  print("free delivery")
#   print("order_amount:150)
elif order_amount>=1000:
  print("delivery charge:50")
  print(order_amount+50)
else:
  print(order_amount+100)




