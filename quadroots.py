def root(a,b,c):
		d = (b*b - 4*a*c)
		print()
		print("D = " + str(D))
		if (D >= 0):  #check for postive D
				print ("REAL ROOTS")
				D = D**0.5 # Calculate aquare root of D
				x1 = (-b + D) / (2*a)
				x2 = (-b - D)/ (2*a)
				print ("x1 = "+str(x1)+" x2 = "+str(x2))
				
		elif(D < 0):  #check for negtive D
				D= (D * -1)**0.5;  #Change D to a postive.
				# Take square root of D then represent with "i"
				print("IMAGINARY ROOTS")
				print ("x1 = -"+str(b/(2*a))+" - "+str(D/(2*a))+"i")
				#print ("x1 = -"+str(b/(2*a))+" + "+str(D/(2*a))+"i")
#The following has two underscores__ before and after name and main
if __name__ == '__main__':
		print("Input a,b and c for the quadratic (ax^2 + bx = c)")
		a = input("Enter a: ")
		b = input("Enter b: ")
		c = input("Enter c: ")
		roots(float(a), float(b), float(c))
'''
Output for 5x^2 + 4x + 2
$ python quadroots.py
Input a,b and c for the quadratic (ax^2 + bx + c)
Enter a: 5
Enter b: 4
Enter c: 2
D = -24.0
IMAGINARY ROOTS
x1 = -0.4 - 0.489897948557i
x1 = -0.4 + 0.489897948557i

quadroots.py CWC BK
Quadratic calulator
D is the discriminant of a quadratic equation . D = b^2 - 4ac
Try the following equations
y = x^2 + 2x + 1 (1,2,1)
y = x^2 + 9   (1,0,9)
y =  (5x^2 + 4x +2)
y =  (5x^2 + 4x +2)
'''
