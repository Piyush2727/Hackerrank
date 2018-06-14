def fuzzy(h,m):
	ones={0:'twelve',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'ninteen',20:'twenty'}		
	if m==0:
		print (ones[h] + " o'clock")
	elif m==15:
		print("quarter past " + ones[h])
	elif m==30:
		print("half past " + ones[h])
	elif m==45:
		print("quarter to "+ones[(h+1)%12])
	elif 0<m<15 or 15<m<=20:
		print(ones[m] + " past " + ones[h])
	elif 20<m<30:
		print("twenty "+ones[m-20] +" past "+ones[h])
	elif 30<m<40:
		print("twenty "+ones[40-m] +" to "+ ones[(h+1)%12])
	elif 40<=m<45 or 45<m<=59 :
		print(ones[60-m] + " to "+ ones[(h+1)%12])
	else:
		print("'null'")	

time=raw_input("enter the time in HH:MM format ")
h=int(time[0:2])
m=int(time[3:5])
k= time[2:3]
if h<=12 and 0<=m<=60 and k==':':
	fuzzy(h,m)
elif 12<h<24 and 0<=m<=60 and k==':':
	fuzzy(h-12,m)
else :
	print("'null'")
