import sys

def printData():
	print(sys.argv)
def sum():
	print(int(sys.argv[1])+int(sys.argv[2]))
# sum()

print(sys.version)

# interpreter will search for packages in these paths
print(sys.path)
print(type(sys.stdin))
print(sys.stdout)
print(sys.maxsize)
print(type(sys.stdout))
