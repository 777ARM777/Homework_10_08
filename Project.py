def Email():
    mail = input("Input an email: ").strip()
    if mail.endswith('@gmail.com') and mail.isascii():
        print('The Email is valid')
    else:
        print('The Email is not valid')


def URL():
    url = input("Input an url: ").strip()
    if url.startswith(('http://www.', 'https://www.')) and len(url) < 2270 and '.am/' in url and url.isascii():
        print('The url is valid')
    else:
        print('The url is not valid')


def Date():
    date = input("Input the date: ").strip()
    if date[2] == date[5] in (' ', '-', '.', '/'):
        print('Date is valid')
    else:
        print('Date is not valid')


def Number():
    num = input("Input the number: ")
    if num.isdigit():
        print("The number is valid")
    else:
        print("The number is not valid")


def CardNumber():
    cardNum = input("Input the credit card number: ").strip()
    if (len(cardNum) == 19 and cardNum[4] == cardNum[9] == cardNum[14] in ('-', ' ')
            and cardNum.replace(' ', '').replace('-', '').isdigit()) or len(cardNum) == 16 and cardNum.isdigit():
        print("The credit card number is valid")
    else:
        print("The credit card number is not valid")


def PhoneNumber():
    phoneNum = input("Input the mobile phone number: ").strip()
    if ((phoneNum.startswith('+374') and len(phoneNum) == 12 and phoneNum[1:].isdigit()) or
            phoneNum.startswith('0') and len(phoneNum) == 9 and phoneNum.isdigit()):
        print('Mobile phone number is valid')
    else:
        print('Mobile phone number is not valid')


try:
    option = int(input("Input an option: "))
except:
    print("The option must be an integer from 1 to 6")


if option == 1:
    Email()
elif option == 2:
    URL()
elif option == 3:
    Date()
elif option == 4:
    Number()
elif option == 5:
    CardNumber()
elif option == 6:
    PhoneNumber()
else:
    print("The option must be an integer from 1 to 6")
