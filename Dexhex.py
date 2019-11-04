# dechex.py CWC BK kenny
def hexcon(num):
	key = "0123456789abcdef"
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = str(h16)+str(h1)
	return h
	
def main():
	hs = ""
	for i in range(127, 150):
		hs = hexcon(i)
		print(i,hs)

main()
