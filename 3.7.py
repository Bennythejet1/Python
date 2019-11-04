'''
import random
iterations = 100
count = 0
count_mn = 0
count_mx = 0
count_md = 0
rv = 0
done = False
'''
Explain what this algorithm does along with
describing the variable names.
'''
while(done==False):
 mn = int(input("Input a minimum integer value: "))
 mx = int(input("Input a maximum integer value: "))
 iterations = int(input("Input an iteration value: "))
 if(mn<mx):
  done=True
md = int((mx - mn)/2)
while(count < iterations):
 rv = random.randint(mn,mx)
 if (count % 10 == 0 and count != 0):
  print()
 print (str(rv)+str(" "),end="")
 count = count+1
 if(rv == mn):
  count_mn = count_mn + 1
 if(rv == mx):
  count_mn = count_mx + 1
 if(rv == md):
  count_md = count_md + 1
'''
print("\n\nmn , count_mn , md, count_md, mx, count_mx")
print(mn,count_mn,md,count_md,mx,count_mx
