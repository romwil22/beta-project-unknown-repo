admin_dict = {'Rom': '1101', 'Patrick': '1115'}

print('Admin Log-in:')
print()
while True:

    user_admin = input('admin: ')
    user_admin = user_admin.title()
    passcode = input('passcode: ')
    print()

    if user_admin in list(admin_dict.keys()) and passcode in list(admin_dict.values()):
        print('beta test project admit by', user_admin)
        break

    print('Inavalid user or passcode, try again')
