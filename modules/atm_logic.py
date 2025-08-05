data ={
    12345:{'pin':123,'balance':12345,'history':[]},
    12346:{'pin':124,'balance':12345,'history':[]},
    12347:{'pin':125,'balance':12345,'history':[]},
    12348:{'pin':126,'balance':12345,'history':[]}
}
acc_num=None
login_status=None
def Welcome():
    print("Welcome".center(50,'*'))
def Menu():
    print('\n[C]heck balance')
    print('\n[D]eposit')
    print('\n[W]ith draw')
    print('\n[V]iew Tranctions')
    print('\n[E]xit')
def Login():
    acc_number=int(input("Enter the account number:"))
    pin=int(input("Enter the pin number:"))
    global acc_num
    global login_status
    if acc_number in data:
        if data[acc_number]['pin']==pin:
            print("Login Successfully.")
            acc_number =acc_num
            login_status = True
            return True
        else:
            print("Invalid pin number.")
            login_status = True
            return False
    else:
        print("Invalid account number.")
        login_status = True
        return False

def Check_balance():
    if acc_num and login_status:
        print(f"\nCurrent Balance: {data[acc_num]['balance']}")
    else:
        print("You need to login again")

def Deposit():
    if acc_num and login_status:
        amount=int(input("Enter the amount to deposit."))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'deposited. - ${amount}')
        print(f'${amount} is successfully desposited')
    else:
        print("You need to login again")

def Withdraw():
    if acc_num and login_status:
        amount=int(input("Enter the amount to withdraw."))
        if data[acc_num]['balance']>=amount:
           data[acc_num]['balance']-=amount
           data[acc_num]['history'].append(f'wihdraw. - ${amount}')
           print(f'${amount} is successfully withdraw')
        else:
            print("Insufficient Balance")
    else:
        print("You need to login again")
        
def View_transaction():
    if login_status and acc_num:
        if data[acc_num]['history']:
            print("Transactions History".center(50,'-'))
            for i in data[acc_num]['history']:
                print(i)
            else:
                print("End of the history".center(50,'-'))

        else:
            print("No Transactions")
    else:
        print("You need to login again")