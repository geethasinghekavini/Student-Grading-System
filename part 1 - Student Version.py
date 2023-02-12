#I declare that my work contains no examples of misconduct ,such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student Id - W1867661  , 20210545

#Date - 2021/11/18

#Part 1 - Main Version
#STUDENTS VERSION
#reference -  Telusko (2019)vedio tutorials, user define functions .Available at:https://www.youtube.com/watch?v=aequTxAvQq4(Accessed: 18/11/2021).

 
progress= 0
moduletrailer = 0
exclude  = 0
moduleretriever = 0
 
'''function1 used to define if user inputs are wrong.
   if user  inputs wrong number of credit at pass , fail , defer or if total is incorrect this will print the appropriate message for it.'''
def incorrect (argument_1):#function 1
    print(argument_1)

'''These set of function  will display  the appropriate progression outcome for an individual student.'''
def progression1(): 
    print("progress")
def progression2(): 
    print("Progress (module trailer)")
def progression3(): 
    print("Exclude")
def progression4(): 
    print("Do not Progress - module retriever")

 
 
while True: 
  try:
   
        #prompot for number of credit at pass, defer and fail.
         
        credit_pass = int(input("Enter your total PASS credits:")) 
        if credit_pass not in range(0, 121, 20):
            incorrect("out of range" ) #call  function 1
            continue
        credit_defer = int(input("Enter your total DEFER credits:"))
        if credit_defer not in range(0, 121, 20):
            incorrect("out of range" ) #call  function 1
            continue
        credit_fail = int(input("Enter your total FAIL credits:"))
        if credit_fail not in range(0, 121, 20):
            incorrect("out of range" )#call  function 1
            continue
            
        total_1 =  credit_pass + credit_defer + credit_fail
        if total_1 == 120:
            print("Total",total_1)
        else:
            incorrect("Total incorrect")#call function 1
            continue
        
        
        #This will display appropriate progression outcome for an individual student using   conditional statments and update the progression_outcome list.
        if credit_pass == 120:
            progression1()#call a function  
        elif credit_pass == 100:
            progression2()#call a function  
        elif credit_fail >= 80:
            progression3()#call a function 
        else:
            progression4()#call a function
        break     
        

  except ValueError:
     incorrect("integer required")        
  


 
 

