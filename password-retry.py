password = 'a123456'
i = 3
while i > 0:
	pwd = input('please enter the password: ')
	if pwd == password:
		print('login successful')
		break
	else:
		i = i - 1
		print('wrong password ! still have', i , 'more chance')