purchase_amount=int(input("enter purchase_amount:$"))
if purchase_amount>=5000:
  print("discount:",20)
  print(purchase_amount-20)
elif purchase_amount>=3000:
  print("discount:",10)
  print(purchase_amount-10)
elif purchase_amount>=1000:
  print("discount:",5)
  print(purchase_amount-5)
else:
  print(purchase_amount-0)
