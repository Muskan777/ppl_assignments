ub = int(input("Input the upper bound\n"))
lb = int(input("Input the lower bound\n"))
for i in range(lb,ub):
	num= i
	sum = 0 
	temp = num  
  
	while temp > 0:  
   		digit = temp % 10  
   		sum += digit ** 3  
   		temp //= 10  
  
	if num == sum:  
   		print(num)    

