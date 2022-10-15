import random
#an empty list for storing all characters that the user would want in the password
empty = []
length = int(input('How many characters do you want in your password: '))
low = input('Do you want lowercase in your password: ').lower()
if low == 'yes' or low == 'y':
    empty += ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up = input('Do you want uppercase in your password: ').lower()
if up == 'yes' or up == 'y':
    empty += ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','U','V','W','X','Ý','Z']
num = input('Do you want numbers in your password: ').lower()
if num == 'yes' or num == 'y':
    empty += ['0','1','2','3','4','5','6','7','8','9']
spec = input('Do you want special characters in your password (@, _, ., etc): ').lower()
if spec == 'yes' or spec == 'y':
    empty += ['!','@','#','$','%','^','&','*','(',')','-','_','+','=']
no_of_pas = int(input('How many passwords do you want: '))


def gen_password(length,no_of_pas):

    for i in range(no_of_pas):
        while True:
            ''' because the passwords are generated randomly, i realized that it is possible for the password to not contain all characters
             that the user wanted. Hence, I created a condition to check if the password generated contains the characters the user wants.
             If not, it should generate the password again.'''
            generate_pass = ''.join([random.choice(empty) for n in range(length)])
            if generate_pass in empty:
                generate_pass = ''.join([random.choice(empty) for n in range(length)])
            else:
                print(generate_pass)
                break
                                       
        
        

gen_password(length,no_of_pas)
