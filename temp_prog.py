import os
import sys
import psutil
import shutil


def copy_files():
	file_list = os.listdir()
	for i in file_list:
		new_file = i + '.copy'
		shutil.copy(i, new_file)
		print('File: ' + new_file + 'created!')

def print_files():
	file_list = os.listdir()
	for i in file_list:
		print(i)

def del_files():
	count = 0
	file_list = os.listdir()
	for i in file_list:
		if i.endswith('.copy'):
			os.remove(i)
			print(i + ' deleted!')
			count += 1
		else:
			print(i)
	return(count)


print("Hi! This is my first Python program")
print("Current working path is:" + os.getcwd())

answer = ''
while answer != 'Q':
	answer = input("Want to change? (Y/N/Q) :")
	if answer == 'N':
		print("Current working path is: " + os.getcwd())
	elif answer == 'Y':
		new_path = input("Please, enter new path :")
		os.chdir(new_path)
		print("Current working path is: " + os.getcwd())
		print("Copy procedure")
		copy_files()
		print_files()
		print("Delete duplicates procedure")
		print('Files deleted count: ' + str(del_files()))
		print_files()			
	else:
		print("wrong input")
