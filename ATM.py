data={'current_balance':46578,'history':[]}
def check_balance():
    print(f"Current Balance: {data['current_balance']}")
def deposit():
    amount=int(input("Enter the amount: "))
    data['current_balance']+=amount
    data['history'].append(f'Deposited - ${amount}')
    print(f'Deposited Successfully - ${amount}')
def withdraw():
    amount=int(input("Enter the amount: "))
    if data['current_balance']>=amount:
        data['current_balance']-=amount
        data['history'].append(f'withdraw - ${amount}')
        print(f'Withdraw Successfully - ${amount}')
    else:
        print("Ins blnc")
def history():
    print("Transactions")
    for i in data['history']:
        print(i)
while True:
    print('Welcome to ATM'.center(30,'*'))
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.History')
    print('0.Exit')

    op=int(input("Enter your choice: "))
    if op==0:
        print("======Thankyou======")
        break
    elif op==1:
        check_balance()
    elif op==2:
        deposit()
    elif op==3:
        withdraw()
    elif op==4:
        history()
    else:
        print("Invalid choice. Try Again")