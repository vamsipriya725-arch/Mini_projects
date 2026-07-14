balance = 5000
try:
    amount = int(input("Enter Amount: "))
    if amount>0:
         if amount > balance:
             raise Exception("Insufficient Balance")
         balance -= amount
         print("Withdraw Successful")
         print("Avaliable Balance: ",balance)
except Exception as e:
          print(e)
