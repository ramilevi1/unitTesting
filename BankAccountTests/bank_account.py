# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions. 
# Create an bankFees() method to apply the bank fees:
#   if withdraw is within the balance 5% fee will be included
#   if withdraw is with insufficient funds but still less than double the balance 10% fee will be included. 
# Create a display() method to display account details.
# Give the complete code for the  BankAccount class.


class BankAccount:
    # create the constuctor with parameters: accountNumber, name and balance 
    def __init__(self,accountNumber, name, initialAmmount):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = initialAmmount
        
    # create Deposit() method
    def Deposit(self , d ):
        self.balance = self.balance + d


    def returnValue():
        return 2500

    # create Withdrawal method
    def Withdrawal(self , w):
        if(self.balance > w):
            self.balance = self.balance- w
            BankAccount.bankFees(self, self.balance)
        elif (self.balance < w) and (self.balance < w*2):
             print( "insuficient funds, operation is not possible")
        else:
               self.balance = self.balance - w
               BankAccount.bankFees(self, self.balance)
   
    # create bankFees() method
    def bankFees(self, balance ):
        if balance < 0:
            self.balance = balance * 1.1
            print("Insufficient balance, fees of 10'%' apply!")

        else:    
            self.balance = balance * 0.95
            print("Withdraw operation includes 5'%' bank fee")

   
    # create display() method
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")

class BankForiengAccount(BankAccount):
    def __init__(self,accountNumber, name, balance, currency):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        self.currency = currency

    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance, "\u20ac")    
        print("currecny is : " , self.currency) 

    def combinedAccountInfo(self,nfa,na):
        if nfa.currency == 'Euro':
           nfa.balance = nfa.balance*1.04 + na.balance
        return nfa.balance

#  Display account informations
newAccount = BankAccount(2178514584, "Albert" , 3200)
newAccount.display()  
newAccount.Withdrawal(3300) 
newAccount.display()
newAccount.Withdrawal(400)
newAccount.display()
newForiengAccount = BankForiengAccount(2178514584,"Albert", 2300, "Euro")
newForiengAccount.display()
if newForiengAccount.accountNumber == newAccount.accountNumber:
      newAccount.balance = newForiengAccount.combinedAccountInfo(newForiengAccount,newAccount )
newAccount.display()
