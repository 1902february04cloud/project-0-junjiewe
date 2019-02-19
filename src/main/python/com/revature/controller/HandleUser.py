import os	
import getpass
import csv
import service.BussinessLogic as bssLogic
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('../error/logging.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


#greet the user
def greeting():
	while True:
		os.system("clear")
		txt = input("Welcome to SmartBanking!!\nType 'r' to register an account, type 'l' to login, type 'e' to exit\n")
		if txt == 'r' or txt == 'l' or txt == 'e':
			if txt == 'r':
				InputReg()
				greeting()
				break
			elif txt == 'l':
				Login()
				break
			elif txt == 'e':
				break	
		else:
			os.system("clear")
			logger.error('YOUR INPUT WAS INVALID!!!')	


#Handles the Register input from a user
def InputReg():
	#read to the database
	with open('../../../resources/userdata.csv', 'r') as f:
		reader = csv.reader(f)
		mydict = dict(reader)
		while True:
			name = input("Enter the name: \n")
			password = getpass.getpass("Enter the password: \n")
			if name not in mydict:
				# save the new user into the database
				with open('../../../resources/userdata.csv', 'a+') as f:
					balance = 0.0
					identities = [password, balance]
					writer = csv.writer(f)
					writer.writerow([name,identities])
				
				with open('../../../resources/usertrans.csv', 'a+') as f2:
					transaction = ''
					writer = csv.writer(f2)
					writer.writerow([name,transaction])
				break
			
			else:
				os.system("clear")
				print('THE USERNAME IS TAKEN')

#Handles Login for the user
def Login():
	with open('../../../resources/userdata.csv', 'r') as f:
		reader = csv.reader(f)
		mydict = dict(reader)
		while True:	
			name = input("username: ")
			password = getpass.getpass("password: ")
			if name not in mydict:
				os.system("clear")
				print("THE USERNAME DOES NOT EXIST")
				getinput = input("Do you want to register as an new user? Type 'y' for yes, Type 'n' for no\n")
				if getinput == 'y':
					greeting()
					break
				else:
					continue
			else:	
				Asking(name)
				break

#After Successful login
def Asking(user):
	os.system('clear')
	print("Hello " + user + "," + " How can I help you?\n")
	print("-----------------------------------")
	while True:
		request = input("'v' to check remaining balance\n'w' to withdraw money\n'd' to deposit money\n'h' to view your transactions history\n'e' to logout\n\n:")
		if request == 'v':
			bssLogic.BalanceCheck(user)
		elif request == 'd':
			bssLogic.Deposit(user)
		elif request == 'w':
			bssLogic.Withdraw(user)
		elif request == 'h':
			bssLogic.checkHistory(user)
		elif request == 'e':
			greeting()
			break
			














