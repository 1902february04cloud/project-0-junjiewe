#!/usr/bin/env python3

'''
This is your main script, this should call several other scripts within your packages.
'''

import controller.HandleUser as contrl
import service.BussinessLogic as bssLogic


def main():
	contrl.greeting()
	

if __name__ == '__main__':
	main()
