name = input("Enter customer name: ")
balance = float(input("Enter initial balance: ")) 
deposit = float(input("Enter deposit amount: "))
balance = balance + deposit 
withdraw = float(input("Enter withdrawal amount: ")) 
  if withdraw <= balance:    
    balance = balance - withdraw 
 else:    
    print("Insufficient balance") 
    print("Customer Name:", name) 
    print("Updated Balance:", balance)