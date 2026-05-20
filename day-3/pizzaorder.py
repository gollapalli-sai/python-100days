print("welcome to pizza order")
n=input("size of pizza s,m,l")
pepproni=input("want it or not y or n")
cheese=input("want it or not y or n")
bill=0
if(n=="s"):
    bill=bill+30
if(n=="m"):
    bill+=50
if(n=="l"):
    bill+=70
if(pepproni=="y"):
    bill=bill+10
else:
    bill=bill
if(cheese=="y"):
    bill=bill+10
else:
    bill=bill
print(bill)
