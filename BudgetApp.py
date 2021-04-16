class BudgetApp:
    food=2500
    clothing=2000
    entertainment=1500
    def __init__(self, amount, category, operation):
        self.amount=amount
        self.category=category
        self.operation=operation    
    def deposit_fund_food(self):
        self.food+=self.amount
        print(f'Your deposit was successful and your new balance is: {self.food}')
    def deposit_fund_cloth(self):
        self.clothing+=self.amount
        print(f'Your deposit was successful and your new balance is: {self.clothing}')
    def deposit_fund_ent(self):
        self.entertainment+=amount
        print(f'Your deposit was successful and your new balance is: {self.entertainment}')
    def withdraw_food(self):
        self.food-=self.amount
        print(f'Please take your cash. Your new balance is: {self.food}')
    def withdraw_clothing(self):
        self.clothing-=self.amount
        print(f'Please take your cash. Your new balance is: {self.clothing}')
    def withdraw_ent(self):
        self.entertainment-=self.amount
        print(f'Please take your cash. Your new balance is: {self.entertainment}')
    def transfer_food_cloth(self):
        self.food-=self.amount
        self.clothing+=self.amount
        print('Transfer successful')
        print(self.clothing)
    def transfer_food_ent(self):
        self.food-=self.amount
        self.entertainment+=self.amount
        print(self.entertainment)
    def transfer_cloth_food(self):
        self.clothing-=self.amount
        self.food+=self.amount
        print(self.food)
    def transfer_cloth_ent(self):
        self.clothing-=self.amount
        self.entertainment+=self.amount
        print(self.entertainment)
    def transfer_ent_food(self):
        self.entertainment-=self.amount
        self.food+=self.amount
        print(self.food)
    def transfer_ent_cloth(self):
        self.entertainment-=self.amount
        self.clothing+=self.amount
        print(self.clothing)
amount=int(input("Please enter an amount: \n"))
category=input("Please enter account category: \n")
operation=input("Please select an operation type: 1. deposit, 2. withdraw, 3. transfer \n")
test=BudgetApp(amount,category, operation)
if(category=='food'):
    if(operation=='deposit'):
        test.deposit_fund_food()
    elif(category=='food'):
        if(operation=='withdraw'):
            test.withdraw_food()    
        elif(category=='food'):
            if(operation=='transfer'):
                transfer_to=input('Please select category to transfer to: \n')
                if(transfer_to=='clothing'):
                    test.transfer_food_cloth()
                elif(category=='entertainment'):
                    test.transfer_food_ent()
elif(category=='clothing'):
    if(operation=='deposit'):
        test.deposit_fund_cloth()
    elif(operation=='withdraw'):
        test.withdraw_clothing()
    elif(operation=='transfer'):
        transfer_to=input('Please select category to transfer to:\n')
        if(transfer_to=='food'):
            test.transfer_cloth_food()
        elif(transfer_to=='entertainment'):
            test.transfer_cloth_ent()  
elif(category=='entertainment'):
    if(operation=='deposit'):
        test.deposit_fund_ent()
    elif(operation=='withdraw'):
        test.withdraw_ent()
    elif(operation=='transfer'):
        transfer_to=input('Please select category to transfer to:\n')
        if(transfer_to=='food'):
            test.transfer_ent_food()
        elif(transfer_to=='clothing'):
            test.transfer_ent_cloth()

