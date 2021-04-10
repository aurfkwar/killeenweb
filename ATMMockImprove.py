#use Functions,  Include register, and login, Generate Account Number
import sys
import random
import datetime
x = datetime.datetime.now()
currentBalance = 0

# allowedUsersDict = {
#     'Seyi':'passwordSeyi',
database_user = {
    'Seyi':'passwordSeyi',
    'Mike':'passwordMike', 
    'Love':'passwordLove'  }
database ={}

def init():

     print("Welcome to BankATM MOCK Improve")

     haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
     if(haveAccount == 1):
        
        login()
     elif(haveAccount == 2):
        
        register()
def login():

     print("********* Login ********** ")
     name = input("Enter your name? \n")
     password = input("Your password? \n")
     for name in database_user:
          
      if(name in database_user and password == database_user[name]):       
          print('Welcome %s' % name)
          print('Login time: %s' % x)
          print('These are the available options: ')
          print('1 Withdrawal')
          print('2. Cash Deposit')
          print('3. Complaint')
          print('4. Logout')
          
          isValidOptionSelected = False
          while isValidOptionSelected  == False:
            selectedOption = int(input('Please select an option: 1 (Withdrawal) 2 (Cash Deposit) 3 (Complaint) 4 (Logout) \n'))
        #    for selectedOption in range(0, 4):
            if(selectedOption == 1):
                isValidOptionSelected  == True
                withdrawalOperations()   
              
            elif(selectedOption == 2):
                isValidOptionSelected  == True
                cashDepositOption()
                                 
            elif(selectedOption == 3):
                isValidOptionSelected  == True
                complaintOption()
                
            
            elif(selectedOption == 4):
                isValidOptionSelected == True
                Logout()
                
            
            
            else:
                print('Invalid Option selected, please try again')   
 
      else:
             print('Name or password incorrect, please try again') 
             login()  
        
   # else:
    # print('Password incorrect, please try again')    

# else:
#     print('Name not found, please try again')

def register():
    print("****** Register ******")
    
    name = (input("What is your name? \n"))
    password = (input("Create a password \n")) 

    accountNumber = generationAccountNumber()
    #database[accountNumber] = [name, password]
    database[name] = password
    
    database_user.update(database)
    

    print("Your Account has been created")
    print("== === ==== ==== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe") 
    print("== === ==== ==== ===")
     

    # if (name not in database_user):
    #  database_user.update({name: password})
    
    login()
       

def withdrawalOperations():
    print('you selected option 1: Withdrawal \n')
    amount = float(input("\nHow much would you like to withdraw: "))
    Confirm = input("Is this the correct amount, Yes or No ? " + str(amount) + " \n")
    if Confirm == "Y":            
             print('take your cash')
             nextAction()

def cashDepositOption():
     print('you selected option 2: Deposit \n')           
     depositAmount = float(input("How much would you like to deposit? "))           
     currentBalance = depositAmount
     print("Your current balance is: %s cash" % currentBalance) 
     nextAction()
               

def complaintOption():
    print('you selected 3: Complaint \n')
    print(input("\nWhat issue will you like to report? "))
    print("Thanks for contacting us")
    nextAction()


def generationAccountNumber():
    #print("Generating Account Number")
    return random.randrange(1111111111, 9999999999)

def Logout():
    login()

def nextAction():
    EndTransaction = int(input("What will you like to do next? 1 (End) 2 (selectAnotherOption) \n" ))
    if(EndTransaction == 1):
        
        Exit()
    elif(EndTransaction == 2):
        
        login()
   

def Exit():
    print("Thanks for Banking with us")
    exit()
init()            
                
            
           
       
    
       
   
        
        

 