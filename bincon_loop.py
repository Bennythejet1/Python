# bincon_loop.py CWC bk
# Convert a base 10 number to binary
# use 191 base 10 equal to 1011 1111 base 2
# q(quotient) d(divisor) r(remainder) n(interger input)
# div 128 * * * * * * *
n = int (input ("Input and integer less than 256 : "))
n_orginal = n
d = 128
binstring ="" #create a string called binstring
for i in range(0,8):
		q = int (n / d)
		r = int (n % d)
		print (d,q,r)# debug line
		n = r
		d = int(d / 2)
		binsString = binString+str (q)
print ("\n*********\t")
print
print (str (str(n_orginal)+" base 10 = "+binString+" base 2")
print ("\n*********\t")
		
