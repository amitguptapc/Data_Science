if __name__=='__main__':
	# what to do when this module is run directly
	print("Name of M1 is %s"%(__name__))
else:
	# what to do when this module is imported
	print("I am in M1's else block")
