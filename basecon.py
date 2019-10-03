#basecon.py bk,cwc

def bincon(num,addSpace):
	n = num
	s = addSpace
	#print(n,s);
	d = 128
	binstring ="" #create a string called binString
	for i in range(0,8)
			q = int(n / d)
			r = int(n % d)
			#print (d,q,r)# debug line
			n = r
			d = int(d / 2)
			bingstring = binString+str(q)
	#print(binString)
	return binString
		
def main():
	bs = ""
	for i in range(0,256)
	bs = bincon(i,i)
	print(i,bs)

main()
	
