#!/usr/bin/env python3

import operator
import logging 
import math

def calculate(arg):
	stack = list()
	mod=1
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			if token =='+':
				arg1 = stack.pop()
				arg2 = stack.pop()
				result = arg1 + arg2
				stack.append(result)
			elif token =='-':
				arg1 = stack.pop()
				arg2 = stack.pop()
				result = arg2 - arg1
				stack.append(result)
			elif token =='*':
				arg1 = stack.pop()
				arg2 = stack.pop()
				result = arg1 * arg2
				stack.append(result)
			elif token =='/':
				arg1 = stack.pop()
				arg2 = stack.pop()
				result = arg2 / arg1
				stack.append(result)
			elif token =='^':
				arg1 = stack.pop()
				arg2 = stack.pop()
				result = math.pow(arg2,arg1)
				stack.append(result)
			elif token =='sin':
				arg1 = stack.pop()
				if(mod==2):
					arg1=arg1*math.pi/180
				stack.append(math.sin(arg1))
			elif token =='cos':
				arg1 = stack.pop()
				if(mod==2):
					arg1=arg1*math.pi/180
				stack.append(math.cos(arg1))
			elif token =='rad':
				mod=1
			elif token =='deg':
				mod=2
			elif token =='cpy':
				arg1 = stack.pop()
				stack.append(arg1)
				stack.append(arg1)
			else:
				print('Not an operator')
		#print (stack)
	if len(stack) !=1:
		raise TypeError

	return stack.pop()
	
def main():
	while True:
		print(calculate(input("rpn calc> ")))

if __name__ == '__main__' :
	main()
