import mysql.connector
mydb=mysql.connector.connect(
 
    host="localhost",
    user="root",
    password="12345",
    database="atm_db" 

 )
 


#ADDDATA FUNCTION IS USE TO CREATE AN USER ACCOUNT 

def adddata(id,name,password,depositamt):
    mycursor=mydb.cursor()
    sql="insert into customers_data(id,name,password,depositamt) value(%s,%s,%s,%s)"
    users=(id,name,password,depositamt)
    mycursor.execute(sql,users)
    mydb.commit()

#UPDATE FUNCTION IS USE TO WHEN USER CHANGE SOME DETAIL IT WILL STORE WITH HELP OF UPDATE FUNCTION
def update(depositamt,id,password):
    mycursor=mydb.cursor()
    sql="update customers_data set depositamt=%s where id=%s and password=%s"
    users=(depositamt,id,password)
    mycursor.execute(sql,users)
    mydb.commit()

#DEPOSIT FUNCTION IS USE TO ADD AMOUNT TO THE BALANCE

def deposit(depositamt,id,password):
    mycursor=mydb.cursor()
    sql="update customers_data set balance=depositamt+%s where id=%s and password=%s"
    users=(depositamt,id,password)
    mycursor.execute(sql,users)
    mydb.commit()

#WITHDRAWAL FUNCTION IS USE TO WHEN THE USER WITHDRAW MONEY WILL UPDATED BY THE DATABASE

def withdrawal(depositamt,id,password):
    mycursor=mydb.cursor()
    sql="update customers_data set balance=depositamt-%s where id=%s and password=%s"
    users=(depositamt,id,password)
    mycursor.execute(sql,users)
    mydb.commit()

#CURRENT BALANCE FUNCTION IS USE TO SHOWN THE CURRENT BALANCE IN THE CUSTOMER ACCOUNT
def currentbalance(id,password):
    mycursor=mydb.cursor()
    sql="select balance from customers_data where id=%s and password=%s"
    users=(id,password)
    mycursor.execute(sql,users)
    r=mycursor.fetchall()
    print(r)
   
#CREATING ACCOUNT OR REGESTRATION
      
user=int(input("WELCOME TO CANARA BANK \n INSERT YOUR CARD \nIF YOU ARE NEW USER PRESS 1 OLD USER PRESS 2: "))

#CHECKING ID AND PASSWORD

if user==1:
    id=input("ENTER YOUR ID:")
    name=input("ENTER YOUR NAME:")
    password=input("ENTER YOUR PASSWORD: ")
    depositamt=input("ENTER YOUR DEPOSIT AMT:")    
    adddata(id,name,password,depositamt)

elif user==2:
    id=input("ENTER YOUR ID:")
    password=input("ENTER YOUR PASSWORD: ")
    
    #INFINITY LOOP
    while True:
        temp=int (input("DEPOSIT PRESS 1\n WITHDRAWAL PRESS 2\n VIEW BALANCE PRESS 3\n"))
    
        #HERE I CAN USE IF STATEMENT WITH 3 MAJOR CONDITIONS
        #DEPOSIT
        # WITHDRAWAL
        # CURRENT BALANCE

        # NO 1 IS WHEN USER WANT TO DEPOSIT THEY CAN PRESS ONE      
        if temp==1:
            print("you are select deposit")
            depositamt=(input("enter your amt to deposit: "))
            deposit(depositamt,id,password)
    
        #NO 2 IS WHEN USER WANT TO WITHDRAWAL THEY CAN PRESS TWO
        elif temp==2:
            print("you are select withdrawal")
            wamt=(input("enter your amt to withdrawal: "))
            withdrawal(wamt,id,password)

        #NO 3 IS WHEN USER WANT TO SHOW THERE BANK CURRENT THEY PRESS THREE    
        elif temp==3:

            print("YOUR CURRENT BALANCE IS")
            currentbalance(id,password)
    
        #NO 0 IS TO EXIT WHEN USER PRESS ZEOR THE INFINITY LOOP IS TERMINATED
        elif temp==0:
            break
        #INVALID INPUT
        else:
            print("Invalid Input")
