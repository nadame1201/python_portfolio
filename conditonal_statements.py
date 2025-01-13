#initializations
#functions
#16 years of or older
#passed your driver's exam
def drive_check():
    #collect some input
    age= int(input ("please enter your age: ")) #input by default collects a string
    exam = input("did you pass your exam(yes,no):")
    #process that data
    if age > 15 and exam == "yes" : #evaluates TRUE or FALSE
        print("you are eligble for a Drivers license")
    else:
        print("you are NOT eligble for a Drivers license`")

#main
drive_check()

#main
# == equal to
# > greater than
# < less than
# >= greater or equal to
# <= less or equal to
# != not equal to

# logiacal operators
# and if both statements are true
# or if one statment is true
