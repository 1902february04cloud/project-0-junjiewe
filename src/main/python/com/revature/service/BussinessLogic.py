import csv
import os
import ast


def Openfile(user):
	with open('../../../resources/userdata.csv', 'r+') as f:
		reader = csv.reader(f)
		mydict = dict(reader)
		new = mydict[user][1:-1]
		balance = new.split(',')
	return balance

#Handles check balance
def BalanceCheck(user):
	os.system('clear')	
	print('====================View Balance=================\n')
	data = Openfile(user)			
	print("The current balance you have is:" + data[1]+ "\n")

#Handles deposit balance
def Deposit(user):
	os.system("clear")
	print("======================Deposit====================\n")
	data = Openfile(user)
	while True:
		message = print('You currently have ' + data[1] + ' on your account, how much do you want to deposit?\n')
		amountdepo = input("amount deposit: ")
		
		try:
			val = float(amountdepo)
		except ValueError:
			print("INVALID INPUT")	
			Deposit(user)
			break
		if(float(amountdepo) < 1):
			os.system("clear")
			print("INVALID INPUT, MUST BE GREATER THAN 1")
		else:   
			userdata_list = []
			val = float(data[1]) + float(amountdepo)	
			with open('../../../resources/userdata.csv', 'r') as f:
				userdata = csv.reader(f)
				userdata_list.extend(userdata)
				for i in range(0,len(userdata_list)):
					if userdata_list[i][0] == user:
						newstr = userdata_list[i][1][1:-1]
						arr = newstr.split(',')
						arr[1] = str(val)
						backtostring = (',').join(arr)
						updatenewstr = '['+ backtostring + ']'
						userdata_list[i][1] = updatenewstr
						with open('../../../resources/userdata.csv', 'w') as f:
							writer = csv.writer(f)
							for i in userdata_list:
								writer.writerow(i)
			write_to_trans_depo(user, amountdepo)	
			break
			

def write_to_trans_depo(user, amount):
	tranMsg = "You have deposit " + amount + " dollar,"
	msg_list = []
	with open('../../../resources/usertrans.csv', 'r') as f:
		transdata = csv.reader(f)
		msg_list.extend(transdata)
		for i in range(0,len(msg_list)):
			if msg_list[i][0] == user:
				msg_list[i][1] += tranMsg
				break
			
		with open('../../../resources/usertrans.csv', 'w') as f:
			writer = csv.writer(f)
			for i in msg_list:
				writer.writerow(i)

def write_to_trans_withdraw(user,amount):
	tranMsg = "You have withdraw " + amount + " dollar,"
	msg_list = []
	with open('../../../resources/usertrans.csv', 'r') as f:
		transdata = csv.reader(f)
		msg_list.extend(transdata)
		for i in range(0,len(msg_list)):
			if msg_list[i][0] == user:
				msg_list[i][1] += tranMsg
				break
			
		with open('../../../resources/usertrans.csv', 'w') as f:
			writer = csv.writer(f)
			for i in msg_list:
				writer.writerow(i)	

#Handles Withdraw
def Withdraw(user):
	os.system('clear')
	print("==================Withdraw=====================\n")
	data = Openfile(user)
	while True:
		message = print("You currently have " + data[1] + " remaining in your account, how much do you want to withdraw?")
		amount = input("Withdraw amount: ")
		
		try:
			val = float(amount)
		except ValueError:
			print("INVALID INPUT")
			Withdraw(user)	
			break
		if(float(amount) < 1):
			print("INVALID INPUT, MUST BE GREATER THAN 1")
		else:
			userdata_list = []
			val = float(data[1]) - float(amount)
			with open('../../../resources/userdata.csv', 'r') as f:
				userdata = csv.reader(f)
				userdata_list.extend(userdata)
				for i in range(0, len(userdata_list)):
					if userdata_list[i][0] == user:
						newstr = userdata_list[i][1][1:-1]
						arr = newstr.split(',')
						if float(arr[1]) - float(amount) < 0:
							print("YOU DONT HAVE ENOUGH MONEY IN YOUR BANK!!")	
							Withdraw(user)
							break
						else:
							arr[1] = str(val)
							backtostr = (',').join(arr)
							updatenewstr = '['+backtostr+']'
							userdata_list[i][1] = updatenewstr
							with open('../../../resources/userdata.csv', 'w') as f:
								writer = csv.writer(f)
								for i in userdata_list:
									writer.writerow(i)
			write_to_trans_withdraw(user,amount)
		break	

def checkHistory(user):
	os.system('clear')
	print("==================Transaction History======================\n")	
	with open('../../../resources/usertrans.csv', 'r') as f:
		reader = csv.reader(f)
		msg_list = []
		msg_list.extend(reader)
		for i in range(0, len(msg_list)):
			if msg_list[i][0] == user:
				arr = msg_list[i][1].split(',')
				for i in range(0, len(arr)):
					print(arr[i])
				break
						
