# dechex.py CWC BK
def hexcon(num):
	print(num," in dechex function ",end="")
	h = ""
	h16 = int(num/16)
	if(h16 > 9):
		print("h16 is greater than 9")
	h1 = num % 16
	h = str(h16)+str(h1)
	return "ff"
	
def main():
	hs = ""
	for i in range(127, 150):
		hs = hexcon(i)
		print(i,hs)

main()
