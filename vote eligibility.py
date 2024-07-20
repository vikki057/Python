print("check eligibility to vote ")
decide = input("yes or no : ")

if decide == 'yes':   # using if or else
    age = int(input('enter your age : '))
    vote = ('you are eligible to vote ', 'you are not eligible to vote ') [age<18] #using clever if/ternery operator
    print(vote)
    print('thanks for using my program')

else :
    print('thanks for using our program')