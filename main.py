import User

user = User.search(3)

if user:
    print(user.first_name)
else:
    print('user not found')
