import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

menu_options = {
    1: 'run the password generator',
    2: 'Exit',
}

def print_between():
    print("------------------------------")


def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
        print_between()

def random_pass():
    try:
        password = ''.join(
            random.choice(characters) for i in range(int(input("Enter Enter the number of characters:"))))

        print("Random password is:", password)
        print_between()
    except:
        print('Wrong input. Please enter a number ...')
        print_between()

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            random_pass()
        elif option == 2:
            print('Thanks for using the password generator ')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 2.')
