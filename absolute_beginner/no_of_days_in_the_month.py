#To print the no.of.days in given month num

month=int(input())  #Enter the month number

if month== "2":
	print("28")
elif month in (4, 6, 9, 11):
	print("30")
elif month in (1,3,5,7,8,10,12):
	print("31")
else:
	print("Error")    #print error if month is invalid
