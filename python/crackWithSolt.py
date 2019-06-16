#!/usr/bin/python

import colorama
import argparse
import hashlib
import sys
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
# Author Information
__author__='''

######################################################
  ____        _____  _____       ________  ________
 /_   |__ ___/ ____\/ ____\__.__.\______ \/   __   \\
  |   |  |  \    __\\\  __<   |  | |    |  \____    /
  |   |  |  /|  |   |  |  \___  | |    `   \ /    /
  |___|____/ |__|   |__|  / ____|/_______  //____/
                          \/             \/
######################################################

    [+] 1uffyD9
    [+] https://github.com/1uffyD9
    [+] https://twitter.com/1uffyD9

######################################################
'''
print (__author__)
####################################################################################
# argparse
# https://docs.python.org/3.3/library/argparse.html#module-argparse
def get_args():
	parser = argparse.ArgumentParser(description='crackWithSalt is just a simple script to crack hash value with a salt')
	# Add arguments
	parser.add_argument('-hs', '--hash', type=str, help='Add your hash value', required=True)
	parser.add_argument('-s', '--salt', type=str, help='Add your salt value', required=True)
	parser.add_argument('-w', '--wordlist', type=str, help='Path to your wordlist', required=True)
	parser.add_argument('-a', '--algo', type=str, help='Add your algorithm type. Ex: md5, sha1, sha224, sha256, sha384, sha512', required=True)
	# Array for all arguments passed to script
	args = parser.parse_args()

	# Assign args to variables
	hash = args.hash
	salt = args.salt
	wordlist = args.wordlist
	algo = args.algo

	return hash,salt,wordlist,algo

#####################################################################################
args = get_args()

def crackHash():
	found = False
	f = open(args[2], "r")
	maxLen = 0
	for x in f:
		curntLen = len(x)
		if maxLen < curntLen :
			maxLen = curntLen

		process(maxLen, x.rstrip())
		if args[3] == "md5" :
  			if hashlib.md5( x.rstrip() + args[1]).hexdigest() == args[0] :
				found = True
				print ( "\n" + success + "found! Password : {}".format(x))
				break
		elif args[3] == "sha1":
			if hashlib.sha1( x.rstrip() + args[1]).hexdigest() == args[0] :
				found = True
				print ( "\n" + success + "found! Password : {}".format(x))
				break
		elif args[3] == "sha224":
			if hashlib.sha224( x.rstrip() + args[1]).hexdigest() == args[0] :
                                found = True
                                print ( "\n" + success + "found! Password : {}".format(x))
                                break
		elif args[3] == "sha256":
			if hashlib.sha256( x.rstrip() + args[1]).hexdigest() == args[0] :
                                found = True
                                print ( "\n" + success + "found! Password : {}".format(x))
                                break
		elif args[3] == "sha384":
			if hashlib.sha384( x.rstrip() + args[1]).hexdigest() == args[0] :
                                found = True
                                print ( "\n" + success + "found! Password : {}".format(x))
                                break
		else:
			if hashlib.sha512( x.rstrip() + args[1]).hexdigest() == args[0] :
                                found = True
                                print ( "\n" + success + "found! Password : {}".format(x))
                                break

	if found == False :
		print ( "\n" + fail + "Nothing were found! Try a Different wordlist\n")


def process(maxLen, data):
	fill = maxLen - len(data)
	sys.stdout.write( notification + "{}".format(data) + " "*fill + "\r")
	sys.stdout.flush()

crackHash()
