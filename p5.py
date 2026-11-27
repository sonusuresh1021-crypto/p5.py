name = input("Enter customer name: ")
balance = float(input("Enter initial balance: ")) 
deposit = float(input("Enter deposit amount: "))
balance = balance + deposit 
withdraw = float(input("Enter withdrawal amount: ")) 
  if  balance - withdraw >= 2000:    
    balance = balance - withdraw 
 else:    
    print("Minimum balance of Rs 2000 required ") 
    print("Customer Name:", name) 
    print("Updated Balance:", balance)