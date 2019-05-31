#!/usr/bin/python

import colorama
import argparse
import os

#####################################################################################
# Adds colourised notifications to text
# Colourama is not neccesary for ANSI compliant terminals; however, it will make it work in windows.
colorama.init()
error = '\033[31m[!] \033[0m'       # [!] Red
fail = '\033[31m[-] \033[0m'        # [-] Red
success = '\033[32m[+] \033[0m'     # [+] Green
event = '\033[34m[*] \033[0m'       # [*] Blue
debug = '\033[35m[%] \033[0m'       # [%] Magenta
notification = '[-] '               # [-]

#####################################################################################

# argparse
# https://docs.python.org/3.3/library/argparse.html#module-argparse
def get_args():
	parser = argparse.ArgumentParser(description='createGitRepo: This simple scirpt will create a repo with ')
	# Add arguments
	parser.add_argument('-r', '--repo', type=str, help='Add repo for current directory', required=True)

	# Array for all arguments passed to script
	args = parser.parse_args()

	# Assign args to variables
	repo = args.repo

	return repo

#####################################################################################
repo = get_args()

def createRepo():
	# Get current working directory
	cwd = os.getcwd()
	# Set new directory path
	path = cwd + "/{}".format(repo)
	try:
    		os.mkdir(path)
		file1 = open(path + "/README.md","w")
		file1.write("# {} \n".format(repo.split("/")[-1]))
		file1.close()
	except OSError:
		print (fail + "Error. Directory already exist!")
		# print (fail + "Creation of the directory %s failed" % path)
	else:
		print (success + "\"{}\" Succssfully created at {}".format(repo,cwd))


createRepo()

