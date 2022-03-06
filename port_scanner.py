from socket import *
import time

start = time.time()

if __name__ == '__main__':
	target = input("Enter the ip address to be scanned: ")
	n = int(input("Enter the first port number: "))
	k = int(input("Enter the last port number: "))
	if n < 0:
		print("First port number can't be less than 0")
		n = 0
	if k > 65536:
		print("Last port number can't be more than 65536")
		k = 65536
	targetip = gethostbyname(target)
	print("Starting scan: " + targetip)

	for i in range(n,k+1):
		s = socket(AF_INET,SOCK_STREAM)

		conn = s.connect_ex((targetip, i))
		if conn == 0:
			print("Open Port Discovered: {}".format(i))
		s.close()
print("Time Elapsed: "  + time.time() - startTime)
