import sys
import csv
import json
import argparse
from util.login import login_insta
from util.without_acc import without_account


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# to analyze data with logged in account 
ap.add_argument('-l', type = str)
# to analyze data without account for more than one profile
ap.add_argument('-wo', type = str, nargs = '*')
# to gather data using csv 
ap.add_argument('-csv', type = str)

args = ap.parse_args()

acnt_username = []

if args.l:
	acc_username = args.l
	login_insta(acc_username)

elif args.wo:
	acc_username = []
	acc_username = args.wo
	without_account(acc_username)

elif args.csv:
	# open CSV file and read usernames to extract data about followers
	with open(args.csv) as csv_file_r:
		csv_reader = csv.reader(csv_file_r, delimiter=',')
		your_list = list(csv_reader)

	
	for i in range(len(your_list)):
		acnt_username.append(str(your_list[i])[2:-2])
		#acnt_username = str(your_list[i])[2:-2] 
	
	#print(acnt_username)
	without_account(acnt_username)


