# this prompts user to name and
# if name is Jake or Jackie the program prints hello Jake and jackie
# and if it is any other name the program prints hello friend
# if none of the above requirements are met the program ends
name=input("Please Enter your Name:")
if name==name:
    print("Hello Friend!!!")
elif name==('Jake' or 'Jackie'):
   print("Hello Jake and Jackie")
else:
   print("Thank you for using the program.Goodbye")
   
#     in this case we have different groups and their different 
# job statuses according to age 
age = int(input("How old are you please? "))
if age < 18:
    print("Your are below the age of working.")
elif age > 18 and age < 25:
    print("You are in a job-seeking age.")
elif age > 25 and age < 30:
    print("You should a job already.")
elif age > 30 and age < 60:
    print("You should retire.")
else:
    print("Goodbye,", name)
    print("You are" , age , "years old.")
    print("Goodbye, thanks for using our program.")





