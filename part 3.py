#I declare that my work contains no examples of misconduct ,such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student Id - W1867661, 20210545

#Date - 2021/12/02

#Part 1 - Main Version
#reference -  Telusko (2019)vedio tutorials, user define functions .Available at:https://www.youtube.com/watch?v=aequTxAvQq4(Accessed: 18/11/2021).

answer = str("y")
progress= 0
moduletrailer = 0
exclude  = 0
moduleretriever = 0
progression_outcome = []

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

'''function 3 to seperate output using a dashline.'''
def seperate(dashline):
  print(dashline*70)
  
 
while answer == "y":# used to continue and predict progression outcome for multiple student.if user inputs 'q' program will quit.
    try:
        #prompot for number of credit at pass, defer and fail.
         
        credit_pass = int(input("Please enter your credit at pass:"))
        if credit_pass not in range(0, 121, 20):
            incorrect("out of range" ) #call  function 1
            continue
        credit_defer = int(input("Please enter your credit at defer:"))
        if credit_defer not in range(0, 121, 20):
            incorrect("out of range" ) #call  function 1
            continue
        credit_fail = int(input("Please enter your credit at fail:"))
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
            progression_outcome.append(f"progress - {credit_pass},{credit_defer},{credit_fail}")
            progression1()#call a function  
        elif credit_pass == 100:
            progression_outcome.append(f"Progress (module trailer) - {credit_pass},{credit_defer},{credit_fail}")
            progression2()#call a function  
        elif credit_fail >= 80:
            progression_outcome.append(f"Exclude - {credit_pass},{credit_defer},{credit_fail}")
            progression3()#call a function 
        else:
            progression_outcome.append(f"module retriever - {credit_pass},{credit_defer},{credit_fail}")
            progression4()#call a function
            
        

        answer = str(input("would you like to enter another set of data?\nEnter 'y' for yes or 'q' for quit:"))

        #Display appropriate progression outcome for an individual student.
        if credit_pass == 120:
            progress += 1
        elif credit_pass == 100:
            moduletrailer += 1
        elif credit_fail >= 80:
            exclude += 1
        else:
            moduleretriever += 1 
        
            
        total_2 = progress +  moduletrailer + exclude + moduleretriever #total count of the progression outcomes 

    except ValueError:
     incorrect("integer required") # call function 1
      


 
seperate("-")# called function 3  
print ("Horizontal Histogram")
# count of the progress,moduletrailer,exclude,moduleretrever saved in the below lists(w,x,y,z). 
w = [progress] 
x = [moduletrailer] 
y = [exclude] 
z = [moduleretriever]
#Above lists stores count of progression data 
#below for loop used to print the horizontal histogram using w,x,y,z lists.
for i in w:
    for j in x:
        for k in y:
            for l in z:
                print("Progress",progress,"      :",i*"*")
                print("moduletrailer",moduletrailer," :",j*"*")
                print("exclude",exclude,"      :",k*"*")
                print("moduleretriever",moduleretriever,":",l*"*")
print(total_2,"outcomes in total")
seperate("-")#called function 3

#part 2
#reference - Stack Exchange Inc; user contributions (2021) print vertically in python loops .Available at: https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops (Accessed: ....... 2021).
#I used a string formatting to stucture the vertical histogram.
header = ["progress  ","moduletrailer  ","exclude  ","moduleretriever  " ]
print(''.join(header))
for s in range(max(i,j,k,l)):
    print(" {0}             {1}           {2}          {3}".format(
        '*' if s < i else ' ',
        '*' if s < j else ' ',
        '*' if s < k else ' ',
        '*' if s < l else ' '
    ))

print(total_2,"outcomes in total")
seperate("-")#called function 3

#part 3
#reference - w3schools (2021) lists . Available at: https://www.w3schools.com/python/python_lists.asp (Accessed: 2 december 2021).
for progress in progression_outcome:   
 print(progress)
               
              
   





 
             
                
             



             

            

             
 
 
              
         
     
          
                
                
                
                 

            
          






 
 


