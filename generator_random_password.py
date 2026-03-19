'''Привет, это программа для генерации случайных паролей. Что делает эта программа:
1) Вначале программа приветскувует тебя
2) Запускается первая функция которая спрашивает тебя какую длину пароля ты хочешь
3) После запускается второя функция которая будет спрашивать какой пароль ты хочешь
4) В конце запускается последняя функция которая создает твой пароль основываясь на твоих данных, по желаю ты можешь сохранить пароль в .txt файле
Что было использовано в коде: в коде использовались модули string, secrets, os. Модуль string используется для хранения всех букв, цифр и знаков препинания. 
Модуль secrets используется для генерации паролей. В отличии от random, модуль secret используется для генерации безопасных символов(букв, цифр, знаков) что безопасно для создания токенов, ссылок для сайтов и паролей.
Модуль os используется для управления папками.'''

'''Hello, this is a program for generating random passwords. What does this program do?
1) First, the program greets you.
2) The first function runs, asking you what password length you want.
3) Then, the second function runs, asking you what password you want.
4) Finally, the last function runs, creating your password based on your data. You can optionally save the password in a .txt file.
What was used in the code: The string, secrets, and os modules were used. The string module is used to store all letters, numbers, and punctuation marks.
The secrets module is used to generate passwords. Unlike random, the secret module is used to generate secure characters (letters, numbers, and symbols), making it safe for creating tokens, website links, and passwords.
The os module is used to manage folders.'''

import string
import secrets
import os


print('Hello, this is a program for creating random passwords!')
#The first function asks how long the password you want is.
def selecting_a_password_length():
    while True:
        password_length = int(input('Select a password length of at least 8 characters: '))
        if password_length < 8:
            print('The password must be at least 8 characters long!')
        else:
            return password_length
        
#The second function asks what password you want.      
def password_option():
    print('\nPassword options: ', '\n1. Latin letters', '\n2. Numbers', '\n3. Punctuation marks', '\n4. Latin letters + Numbers', '\n5. Latin letters + Punctuation marks', '\n6. Numbers + Punctuation marks', '\n7. Latin letters + Numbers + Punctuation marks')
    #We use the string module to store all types of characters in a variable.
    letters = string.ascii_letters #All letters(A-Z, a-z)
    numbers = string.digits #All digits (0-9)
    symbols = string.punctuation #All symbols !"#$%&'()*+,-./:;<=>?@[]^_`{|}~
    while True:
        choice = input('Select a number from (1-7): ')

        if choice == '1':
            print('\nWhat letters do you want?:', '\n1. Basic (Where there are uppercase and lowercase letters(A-Z, a-z))', '\n2. Lowercase letters only', '\n3. Capital letters only')
            while True:
                let = input('\nSelect a number from (1-3): ')
                if let == '1':
                    return letters 
                elif let == '2':
                    return letters.lower() 
                elif let == '3':
                    return letters.upper() 
                else:
                    print('There is no such option, please try again.')
                       

        elif choice == '2':
            return numbers 
        
        elif choice == '3':
            return symbols 
        
        elif choice == '4':
            print('\nWhat letters do you want?:', '\n1. Basic (Where there are uppercase and lowercase letters(A-Z, a-z))', '\n2. Lowercase letters only', '\n3. Capital letters only')
            while True:
                let = input('\nSelect a number from (1-3): ')
                if let == '1':
                    return letters+numbers
                elif let == '2':
                    return letters.lower()+numbers
                elif let == '3':
                    return letters.upper()+numbers
                else:
                    print('There is no such option, please try again.')
                       

        elif choice == '5':
            print('\nWhat letters do you want?:', '\n1. Basic (Where there are uppercase and lowercase letters(A-Z, a-z))', '\n2. Lowercase letters only', '\n3. Capital letters only')
            while True:
                let = input('\nSelect a number from (1-3): ')
                if let == '1':
                    return letters+symbols
                elif let == '2':
                    return letters.lower()+symbols
                elif let == '3':
                    return letters.upper()+symbols
                else:
                    print('There is no such option, please try again.')
                    

            
        elif choice == '6':
            return numbers+symbols 
        
        elif choice == '7':
            print('\nWhat letters do you want?:', '\n1. Basic (Where there are uppercase and lowercase letters(A-Z, a-z))', '\n2. Lowercase letters only', '\n3. Capital letters only')
            while True:
                let = input('\nSelect a number from (1-3): ')
                if let == '1':
                    return letters+numbers+symbols
                elif let == '2':
                    return letters.lower()+numbers+symbols
                elif let == '3':
                    return letters.upper()+numbers+symbols
                else:
                    print('There is no such option, please try again.')

        else:
            print('There is no such option, please try again.')

#This function creates a password                 
def creating_your_password():
    print('Create your password...')
    #Variables length and option contain your previous password information.
    length = selecting_a_password_length()
    option = password_option()
    #This variable creates your password.
    password = "".join(secrets.choice(option) for i in range(length))
    print('\nYour password: ', password, '\n')
    print('Do you want to save your password?', '\nYes', '\nNo')
    answer = input('\nWrite your answer: ')
    if answer == 'Yes' or 'yes':
        string = str(password)
        #Makes a path to the desktop
        desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        #Checking files for presence
        if not os.path.exists(desktop):
            #If there is no folder, then the path changes
            desktop = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
        #Saving a password to .txt file
        with open(os.path.join(desktop, "Password.txt"), "w") as f:
            f.write('Your password: ' + string)
            f.read
            f.close()
            print('The file with the password has been saved')
            print('Have a nice day')
    elif answer == 'No' or 'no':
        print('Have a nice day')
    else:
        print('There is no such answer option, please try again.')
    
print(creating_your_password())
        

        
    



        
