import random
from datetime import datetime
customersRecord={}
def init():
    haveAccount=int(input('Welcome! Do you have an account with us: (1) Yes, (2) No\n'))
    if(haveAccount==1):
        login()
    elif(haveAccount==2):
        register()
    else:
        print('Invalid option selected')
        init() 
def register():
    print('Register please')
    account_FirstName=input("Please enter your first name:\n")
    account_LastName= input("Please enter your last name:\n")
    emailAdress= input("Please enter your email address here: \n")
    password=input('Please create a password:\n')
    accountNumber =generateAccountNumber()
    customersRecord[accountNumber]=[account_FirstName, account_LastName, emailAdress, password]
    print("Welcome %s %s %i is your account number" %(account_FirstName, account_LastName, accountNumber))
    print("Please keep safe")
    loginOption=int(input("You may now proceed to login, Select (1)Login, (2) Exit \n"))
    if(loginOption==1):
        login()
    elif(loginOption==2):
        exit()
    else:
        print('Invalid option selected') 

def login():
    print("******* Login *******")
    print(datetime.now())
    customerAccount=int(input("Please enter your account number: \n"))
    customerPassword=input("Please enter your password:\n")
    for accountNumber, userDetails in customersRecord.items():
        if (accountNumber==customerAccount):
            if(userDetails[3]==customerPassword):
                print("Login successful\n")
                bankOperation(userDetails) 

            else:
                print('Invalid account number or password')
                login()
    
def bankOperation(user):
    print('Welcome %s %s' %(user[0], user[1]))
    selectedOpt=int(input("What will you like to do? (1) Withdraw, (2) Deposit, (3) Logout, (4) Exit\n"))
    if(selectedOpt==1):
        withdrawalOps()
    elif(selectedOpt==2):
        depositOps()
    elif(selectedOpt==3):
        login()
    elif(selectedOpt==4):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)
def depositOps():
    print('Deposit some cash')
def withdrawalOps():
    print('Please take your cash')
def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)
init()