cents = int(input())
pennie = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200
ntoonies = cents // toonie
remainder1 = cents - (ntoonies * toonie)
nloonies = remainder1 // loonie
remainder2 = remainder1 - (nloonies * loonie)
nquarters = remainder2 // quarter
remainder3 = remainder2 - (nquarters * quarter)
ndimes = remainder3 // dime
remainder4 = remainder3 - (ndimes * dime)
nnickels = remainder4 // nickel
remainder5 = remainder4 - (nnickels * nickel)
npennies = remainder5 // pennie
print ("Your change is",cents,"cents.")
print (ntoonies,"toonie(s)")
print (nloonies,"loonie(s)")
print (nquarters,"quarter(s)")
print (ndimes,"dime(s)")
print (nnickels,"nickel(s)")
print (npennies,"pennie(s)")