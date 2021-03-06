import os	
import getpass
import csv
import service.BussinessLogic as bssLogic
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR, filename="logs.log")


#greet the user
def greeting():
	while True:
		txt = input("Welcome to SmartBanking!!\nType 'r' to register an account, type 'l' to login, type 'e' to exit\n")
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
			logger.error("INPUT VALUE WAS INVALID IN GREETING")
			os.system('clear')	
			print("INPUT VALUE WAS INVALID")
			
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
			else:
				logger.error('THE USERNAME IS TAKEN IN INPUTREG')
				os.system("clear")
				print("THE USERNAME IS TAKEN")

#Handles Login for the user
def Login():
	with open('../../../resources/userdata.csv', 'r') as f:
		reader = csv.reader(f)
		mydict = dict(reader)
		while True:	
			name = input("username: ")
			password = getpass.getpass("password: ")
			if name not in mydict:
				logger.error("THE USERNAME DOES NOT EXIST")
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
			os.system("clear")
			greeting()
			break
			


