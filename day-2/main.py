
print("welcome to tip calculator")
bill=float(input("what is the total bill ? rupees"))
tip=float(input("what tip you want to give"))
split=float(input("how many persons"))
pay=(bill+tip)/split
print("each person have to pay",pay)