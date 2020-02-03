password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('please enter the password: ')
	if pwd == password:
		print('login successful')
		break
	else:
		print('wrong password !')
		if i > 0:
			print('still have', i , 'more chance')