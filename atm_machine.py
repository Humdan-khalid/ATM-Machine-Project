def atm_machine(total_balance , pin : int):
    try:
        user_pin : int = int(input("enter user pin: "))
        while True:

            if user_pin == pin:
                print("\n1. Cash withdraw")
                print("2. Check balance")
                print("3. Deposit money")
                print("4. Exit\n")
 
                user_choice = input("Enter your choice(1 2 3 or 4): ")
                
                if user_choice == '1':
                    try:
                        withdraw_amount : int = int(input("\nEnter your withdraw amount: "))
                        
                        if (withdraw_amount < 500):
                            print("Withdraw amount is start to 500")

                        elif withdraw_amount <= 0:
                            print("Enter a valid amount")

                        elif withdraw_amount <= total_balance:
                            print(f"\nTake cash your {withdraw_amount} withdraw amount.")
                            total_balance -= withdraw_amount
                        
                        else:
                                print("Insufficient Balance")

                    except ValueError:
                        print("Please enter a digits value.")
                    
                elif user_choice == '2':
                    print(f"Total balance is: {total_balance}")
                
                elif user_choice == '3':

                    try:
                        deposit_money : int = int(input("enter deposit amount: "))
                        print("Successfully deposit")
                        total_balance += deposit_money
                    except ValueError:
                        print("Please enter a digits")
               
                elif user_choice == '4':
                    print("Thanks for using this atm")
               
                else:
                    print("You have a only choice is (1 2 3 or 4)")

                atm_choice = input("\nare you want to agin using this atm: ").lower()

                if atm_choice == 'yes':
                    print("Ok")
                else:
                    print("Thankyou for using this ATM.")
                    break
        else:
            print("Please enter a correct pin")

    except ValueError:
        print("Please enter a digits")

atm_machine(20000 , 1234)



        