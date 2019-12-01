import math

data = open("Day_01_input.txt", "r")
list = []
line = data.read().splitlines()
 
for x in line :
    list.append(int(x)) 
data.close()  

fuel = 0
for x in list :
    add = math.floor(x/3)-2
    fuel0=0
    while add >=0 :
        fuel0 = fuel0 + add
        add = math.floor(add/3)-2 
    fuel = fuel + fuel0
    
print(f"fuel needed : {fuel}") 