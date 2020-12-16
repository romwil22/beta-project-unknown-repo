admin_dict = {'Rom': '1101', 'Patrick': '1115'}

print('Admin Log-in:')
print()
while True:

    # user input admin and passcode
    user_admin = input('admin: ')
    user_admin = user_admin.title()
    passcode = input('passcode: ')
    print()

    # admit message
    if user_admin in list(admin_dict.keys()) and passcode in list(admin_dict.values()):
        print('beta test project admit by', user_admin)
        break

    # error message log-in
    print('Inavalid user or passcode, try again')
    print('meann')
