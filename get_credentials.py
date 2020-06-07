import pickle

def get_creds():
	print('Please enter the following information:')
	credentials = {}


	print('Which browser is installed on your system? Chrome or Firefox (0 for Chrome, 1 for Firefox)')
	ans = input()
	if ans == '0':
		credentials['Browser'] = 'Chrome'
	else:
		credentials['Browser'] = 'Firefox'

	print('Please enter the path to geckodriver')
	credentials['EXECUTABLE_PATH'] = input()

	print("Please enter your LinkedIn Email/Phone No")
	credentials['Email_or_phone_no'] = input()

	print("Please enter your password")
	credentials['Password'] = input()

	with open('credentials.pickle','wb') as f:	
		pickle.dump(credentials,f)