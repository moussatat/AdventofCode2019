import math

data = open("Day_01_input.txt", "r")
line_array = []
lines = data.read().splitlines()
 
for line in lines :
    line_array.append(int(line)) 
data.close()  

fuel = 0
for x in line_array :
    add = math.floor(x/3)-2
    fuel0=0
    while add >=0 :
        fuel0 = fuel0 + add
        add = math.floor(add/3)-2 
    fuel = fuel + fuel0
    
print(f"fuel needed : {fuel}") 